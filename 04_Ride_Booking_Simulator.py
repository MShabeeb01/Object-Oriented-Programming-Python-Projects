# Base Class
class Ride:
    def book(self, distance):
        pass

# Derived Classes
class CarRide(Ride):
    def book(self, distance):
        fare = distance * 15  # ₹15 per km
        return f"Car Ride booked for {distance} km. Fare: ₹{fare}"

class BikeRide(Ride):
    def book(self, distance):
        fare = distance * 8  # ₹8 per km
        return f"Bike Ride booked for {distance} km. Fare: ₹{fare}"

class AutoRide(Ride):
    def book(self, distance):
        fare = distance * 10  # ₹10 per km
        return f"Auto Ride booked for {distance} km. Fare: ₹{fare}"

# Polymorphism in action
def confirm_booking(ride, distance):
    print(ride.book(distance))

# User Interaction
while True:
    print("\n--- Welcome to Python Ride Booking ---")
    print("1. Car Ride")
    print("2. Bike Ride")
    print("3. Auto Ride")
    print("4. Exit")

    choice = input("Choose your ride: ")

    if choice == "4":
        print("Thank you for using Python Rides!")
        break

    distance = int(input("Enter distance in km: "))

    if choice == "1":
        confirm_booking(CarRide(), distance)
    elif choice == "2":
        confirm_booking(BikeRide(), distance)
    elif choice == "3":
        confirm_booking(AutoRide(), distance)
    else:
        print("Invalid choice! Try again.")
