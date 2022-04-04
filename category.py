import json
from typing import Optional, List

from enums import CategoryType


class Category:
    def __init__(self, name: str, cat_type: CategoryType):
        self.name = name
        self.cat_type = cat_type
        self.subcategories: Optional[List['Category']] = None
        self.list_of_tags: Optional[List[str]] = None

    def add_subcategory(self, s: 'Category') -> None:
        if self.subcategories is not None:
            self.subcategories.append(s)
        else:
            self.subcategories = [s]

    def add_tags(self, t: List[str]) -> None:
        self.list_of_tags = t
