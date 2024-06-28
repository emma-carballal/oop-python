"""
Scratch file for testing concepts
"""
from bike_example import Bike, Condition

bike_1 = Bike('bike 1', Condition.NEW, 100)
bike_2 = Bike('bike 2', Condition.BAD, 200)

bikes = [bike_1.num_wheels, bike_2.num_wheels]
print(bikes)
