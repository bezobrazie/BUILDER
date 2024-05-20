from main import Coffee


class CoffeeBuilder:

    def __init__(self):
        self.reset()

    def reset(self) -> None:
        self._coffee = {}

    def create_coffee(self):
        coffee = self._coffee
        self.reset()
        return Coffee(**coffee)

    def choose_sort(self, sort: str):
        self.add(key='sort', value=sort)
        return self

    def add_sugar(self, sugar: int):
        self.add(key='sugar', value=sugar)
        return self

    def add_syrup(self, syrup: list):
        self.add(key='syrup', value=syrup)
        return self

    def add_milk(self, milk: list):
        self.add(key='milk', value=milk)
        return self

    def add(self, key, value) -> None:
        if key in self._coffee:
            self._coffee[key] = self._coffee[key] + value
            return
        self._coffee[key] = value


if __name__ == "__main__":
    # coffee 1
    builder = CoffeeBuilder()
    print(builder.choose_sort('ЛАТТЭ').add_sugar(1).add_sugar(5).add_milk([1.1]).add_milk([0.0]).add_syrup(['vkus penisa']).add_syrup(['kokos']).create_coffee())

    # coffee 2
    builder.choose_sort('КАПУЧИНО')
    builder.add_milk([100.1])
    builder.add_syrup(['cocount'])
    coffee2 = builder.create_coffee()
    print(coffee2)
