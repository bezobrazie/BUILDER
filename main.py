# В кафетерии есть 3 рецепта:
# 1. Черный кофе
# 2. Кубинский кофе
# 3. Американо
#
# Также гость может запросить дополнительно:
#
# Сахар x кубиков
# Сироп "x"
# Молоко x% жирности
# Например:
#
# Черный кофе + Молоко 3.2% + кубик Сахара
# Кубинский кофе + Молоко 0% + кубик Сахара + кубик Сахара
# Американо +  Молоко 3.2% +  Молоко 0% +  сироп "Малиновый"
# Есть следующие модели:
# Необходимо реализовать класс, умеющий варить кофе всех 3-х рецептов с любыми добавками. (класс должен уметь создавать модель Coffee)


from dataclasses import dataclass, field
from typing import Iterable


@dataclass
class Milk:
    fat: float


@dataclass
class Syrop:
    taste: str


@dataclass
class Coffee:
    sort: str
    sugar: int = 0
    milk: Iterable[Milk] = field(default_factory=list)
    syrup: Iterable[Syrop] = field(default_factory=list)


