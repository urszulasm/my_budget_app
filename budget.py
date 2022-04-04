import json
from datetime import datetime
from typing import List, Optional

import pandas as pd
from pandas import DataFrame

from category import Category
from enums import TransactionType, CategoryType
from transactions import Transaction


class Budget:

    def __init__(self, beginning_balance):
        self.income: Optional[List] = None
        self.expense: Optional[List] = None
        self.beginning_balance: float = beginning_balance
        self.list_of_categories: Optional[List] = None

    def bank_statement_compile(self, bank_statement: DataFrame) -> None:

        # for each transaction in bank statement creates an object and adds it to the list
        for index, transaction in bank_statement.iterrows():
            if transaction[1] > 0:
                t = Transaction(
                    _id=index, date=datetime.strptime(transaction[0], '%Y-%m-%d'), amount=transaction[1],
                    title=transaction[2],
                    bank_name=transaction[3], transaction_type=TransactionType.INCOME
                )
                if self.income is not None:
                    self.income.append(t)
                else:
                    self.income = [t]

            else:
                t = Transaction(
                    _id=index, date=datetime.strptime(transaction[0], '%Y-%m-%d'), amount=transaction[1],
                    title=transaction[2],
                    bank_name=transaction[3], transaction_type=TransactionType.EXPENSE
                )
                if self.expense is not None:
                    self.expense.append(t)
                else:
                    self.expense = [t]

    def group_by_month(self, transaction_type: TransactionType, month: int) -> List[Transaction]:

        monthly_transactions = []
        if transaction_type == TransactionType.INCOME:
            transactions: List[Transaction] = self.income
        else:
            transactions: List[Transaction] = self.expense

        for transaction in transactions:
            if transaction.date.month == month:
                monthly_transactions.append(transaction)
        return monthly_transactions

    def sum_transactions(self, transaction_type: TransactionType, month: int) -> float:

        # sum all transactions for Income and Expense types
        try:
            balance = 0
            for i in self.group_by_month(transaction_type, month):
                balance += i.amount
            return balance
        except TypeError:
            return 0

    def show_balance(self, month: int) -> float:

        # sum all transactions and beginning_balance to get ending_balance
        ending_balance = self.beginning_balance + self.sum_transactions(TransactionType.INCOME, month) \
                         + self.sum_transactions(TransactionType.EXPENSE, month)
        return ending_balance

    def create_category(self, mapping: json) -> None:

        # reads json file with category-subcategory mapping and for each creates Category() class object
        for k, v in mapping.items():

            c = Category(name=k, cat_type=CategoryType.CATEGORY)
            c.add_tags(v['list_of_tags'])

            for k1, v1 in v['subcategory'].items():
                s = Category(name=k1, cat_type=CategoryType.SUBCATEGORY)
                s.add_tags(v1['list_of_tags'])
                c.add_subcategory(s)

            if self.list_of_categories is not None:
                self.list_of_categories.append(c)
            else:
                self.list_of_categories = [c]

    def assign_category(self, transactions_list: List[Transaction]) -> None:

        for cat in self.list_of_categories:
            for subcategory in cat.subcategories:
                for transaction in transactions_list:
                    for tag in cat.list_of_tags:
                        if tag in transaction.title:
                            transaction.category = cat
                            transaction.subcategory = subcategory


