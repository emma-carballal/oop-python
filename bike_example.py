from enum import Enum

class MethodNotAllowed(Exception):
    pass

class Condition(Enum):
    NEW = 0
    GOOD = 1
    OKAY = 2
    BAD = 3

class Bike:
    num_wheels = 2
    counter = 0

    def __init__(self, description: str, condition: Condition, sale_price:int, cost: int = 0):
        self.description = description
        self.condition = condition
        self.sale_price = sale_price
        self.cost = cost
        self.sold = False
        type(self).counter += 1

    def update_sale_price(self, sale_price):
        if sale_price < 0:
            raise ValueError("Sale price cannot be negative")
        if self.sold:
            raise MethodNotAllowed("Cannot update sale price on a sold bike")            
        self.sale_price = sale_price

    def sell(self):
        self.sold = True
        profit = self.sale_price - self.cost
        return profit

    def service(self, cost, new_sale_price=None, new_condition=None):
        self.cost += cost
        if new_sale_price is not None:
            self.update_sale_price(new_sale_price)
        if new_condition is not None:
            self.condition = new_condition
    
    @property
    def profit(self):
        if self.sold:
            return self.sale_price - self.cost
        else:
            return None
    
    # @staticmethod
    # def get_test_bike():
    #     return Bike(
    #         description=f"Bike {Bike.counter + 1}",
    #         condition=Condition.GOOD,
    #         sale_price=(Bike.counter + 1)*100,
    #    )
    
    @classmethod
    def get_test_object(cls):
        return cls(
            description=f"{cls.__name__} {cls.counter + 1}",
            condition=Condition.GOOD,
            sale_price=(cls.counter + 1)*100,
        )
    
    def __str__(self) -> str:
        if self.sold:
            return self.description + " (sold)"
        else:
            return self.description + " (in stock)"
    
    def __repr__(self) -> str:
        return f"{type(self).__name__}({repr(self.description)}, {self.condition}, {self.sale_price}, {self.cost})"

    def __del__(self):
        Bike.counter -= 1

class Tricycle(Bike):
    num_wheels = 3
    counter = 0
    
if __name__ == '__main__':
    # my_bike = Bike("Orange Univega", Condition.OKAY, sale_price=200, cost=20)
    # bike_2 = Bike("Orange Univega", Condition.OKAY, sale_price=200, cost=20)
    # bike_3 = Bike("Orange Univega", Condition.OKAY, sale_price=200, cost=20)

    bike_1 = Bike.get_test_object()
    trike_1 = Tricycle.get_test_object()
    bike_2 = Bike.get_test_object()
    trike_2 = Tricycle.get_test_object()


    bikes = [bike_1, bike_2, trike_1, trike_2]
    print(bikes)
    print(bike_1.num_wheels)
    print(trike_1.num_wheels)
