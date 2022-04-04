import json

import pandas as pd

from budget import Budget
from enums import TransactionType

# read bank statement
g = {'date': ['2022-02-01', '2022-01-02'], 'amount': [200.00, -350.00], 'title': ['biedronka', 'Mexicana'],
         'bank_name': ['MBank', 'Santander']}
jan_transactions = pd.DataFrame(data=g)

# upload mapping file
f = open('categories.json')
category_mapping = json.load(f)

# create Budget() object and run methods
b = Budget(5000.0)
b.bank_statement_compile(jan_transactions)
b.sum_transactions(TransactionType.INCOME, 1)
b.show_balance(1)
b.create_category(category_mapping)
b.assign_category(b.income)
b.assign_category(b.expense)

a = 1
