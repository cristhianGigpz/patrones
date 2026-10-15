from decimal import Decimal


class FareCalculator:
    def calculate(self, trip, driver):

        base_fare = Decimal("5.00")

        price_per_km = Decimal("2.00")

        if driver.category == "premium":
            price_per_km = Decimal("3.00")

        distance_cost = trip.distance * price_per_km

        duration_cost = trip.duration * Decimal("0.50")

        return base_fare + distance_cost + duration_cost


class Driver:
    def __init__(self, driver_id, category):
        self.id = driver_id
        self.category = category


class Trip:
    def __init__(self, trip_id, distance, duration):
        self.id = trip_id
        self.distance = Decimal(str(distance))
        self.duration = Decimal(str(duration))


driver = Driver(1, "premium")

trip = Trip(trip_id=101, distance=10, duration=20)

calculator = FareCalculator()

total = calculator.calculate(trip, driver)

print(total)
