from item import Item

class Phone(Item):

    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        # call super function / access attributes and methods
        super().__init__(
            name, price, quantity
        )

        # validation
        assert broken_phones >= 0, f'Broken phones value {broken_phones} is not greater than 0'

        # assignment
        self.broken_phones = broken_phones
