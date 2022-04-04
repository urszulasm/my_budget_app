from enum import Enum


class TransactionType(Enum):
    INCOME = 'Income'
    EXPENSE = 'Expense'


class CategoryType(Enum):
    CATEGORY = 'Category'
    SUBCATEGORY = 'Subcategory'

