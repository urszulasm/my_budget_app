from datetime import datetime
from typing import Hashable

from category import Category
from enums import TransactionType, CategoryType


class Transaction:
    def __init__(self, _id: Hashable, date: datetime, amount: float, title: str, bank_name: str,
                 transaction_type: TransactionType) -> None:
        self.id = _id
        self.date = date
        self.amount = amount
        self.title = title
        self.bank_name = bank_name
        self.type = transaction_type
        self.category: Category = Category(name='unknown_category', cat_type=CategoryType.CATEGORY)
        self.subcategory: Category = Category(name='unknown_subcategory', cat_type=CategoryType.SUBCATEGORY)
        self.month = date.strftime('%B')

    def __str__(self) -> str:
        return f'Transaction(id: {self.id}, date: {self.date}, amount: {self.amount}, title: {self.title}, ' \
               f'bank name: {self.bank_name}, transaction type: {self.type})'


