class TaxiRide:
    def __init__(self, rate_per_km):
        self.rate_per_km = rate_per_km # value in € (e.g. €2)
        self.distance = 0
        self.fare = 0

    def calculate_fare(self, distance):
        self.distance = distance
        self.fare = self.distance * self.rate_per_km

    def print_receipt(self):
        print(f"Ride distance: {self.distance},\nRate per kilometer: {self.rate_per_km},\nRide fare: {self.fare}")


def main():
    taxi1 = TaxiRide(2)
    taxi2 = TaxiRide(3)
    taxi1.calculate_fare(12)
    taxi2.calculate_fare(33)
    taxi1.print_receipt()
    taxi2.print_receipt()


if __name__ == "__main__":
    main()
