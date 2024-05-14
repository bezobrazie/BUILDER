

class CoffeeBuilder:

    def __init__(self):
        self.reset()

    def reset(self) -> None:
        self._coffee = Coffee()

    def create_coffee(self):
        coffee = self._coffee
        self.reset()
        return coffee

    def choose_sort(self, sort: str):
        self._coffee.add(key='sort', value=sort)
        return self

    def sugar(self, sugar: int):
        self._coffee.add(key='sugar', value=sugar)
        return self

    def syrup(self, syrup: list):
        self._coffee.add(key='syrup', value=syrup)
        return self

    def milk(self, milk: list):
        self._coffee.add(key='milk', value=milk)
        return self


class Coffee:

    def __init__(self) -> None:
        self.parts = {}

    def add(self, key, value) -> None:
        if key in self.parts:
            self.parts[key] = self.parts[key] + value
            return
        self.parts[key] = value

    def list_parts(self) -> None:
        # TODO: сюда нужно запихнуть превращение self.parts в Coffee dataclass
        print(self.parts)


if __name__ == "__main__":
    # coffee 1
    builder = CoffeeBuilder()
    builder.choose_sort('ЛАТТЭ').sugar(1).sugar(5).milk([1.1]).milk([0.0]).syrup(['vkus penisa']).syrup(['kokos']).create_coffee().list_parts()
    # coffee 2
    builder.choose_sort('КАПУЧИНО')
    builder.milk([100.1])
    coffee2 = builder.create_coffee()
    coffee2.list_parts()



