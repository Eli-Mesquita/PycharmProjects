import csv


class Item:
    pay_rate = 0.8  # 20% discount
    all = []

    def __init__(self, name: str, price: float, quantity=0):
        # validation
        assert price >= 0, f'The price {price} is not greater than 0'
        assert quantity >= 0, f'The Quantity {quantity} is not greater than 0'

        # assignment
        self.__name = name
        self.__price = price
        self.quantity = quantity

        # execute action
        Item.all.append(self)

    @property
    def price(self):
        return self.__price

    @property
    # property decorator = read only attribute
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) > 10:
            raise Exception('The name is too long')
        else:
            print(f'você alterou o item {self.__name} para: ', end='')
            self.__name = value

    # method creation
    def calculate_total_price(self):
        return self.__price * self.quantity

    def apply_discount(self):
        self.__price = self.__price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        with open('Items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity'))
            )

    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f" {self.__class__.__name__}('{self.name}',  {self.__price}, {self.quantity}) \n"
