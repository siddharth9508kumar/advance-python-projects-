#.Flight Booking System A system to search, book, and cancel flight tickets. 
#Handle exceptions such as seat not available, invalid passenger details, payment failure.
class FlightBookingSystem:
    def __init__(self):
        self.flights = {"FL123": {"seats": 5, "price": 100}}
        self.bookings = {}

    def search_flight(self, flight_number):
        return self.flights.get(flight_number, None)

    def book_ticket(self, flight_number, passenger_name):
        flight = self.search_flight(flight_number)
        if not flight:
            raise ValueError("Flight not found")
        if flight["seats"] <= 0:
            raise ValueError("No seats available")
        if not passenger_name:
            raise ValueError("Passenger name cannot be empty")
        booking_id = f"{flight_number}_{passenger_name}"
        self.bookings[booking_id] = {"flight_number": flight_number, "passenger_name": passenger_name}
        flight["seats"] -= 1
        return booking_id

    def cancel_ticket(self, booking_id):
        booking = self.bookings.get(booking_id, None)
        if not booking:
            raise ValueError("Booking not found")
        flight_number = booking["flight_number"]
        self.flights[flight_number]["seats"] += 1
        del self.bookings[booking_id]
# test the flight booking system
if __name__ == "__main__":
    flight_booking_system = FlightBookingSystem()
    try:
        print("Searching for flight...")
        print("Enter flight number: ")
        flight_number = input()
        flight = flight_booking_system.search_flight(flight_number)
        if flight:
            print(f"Flight found: {flight_number}, Seats available: {flight['seats']}, Price: {flight['price']}")
            print("Booking ticket...")
            print("Enter passenger name: ")
            passenger_name = input()
            booking_id = flight_booking_system.book_ticket(flight_number, passenger_name)
            print(f"Ticket booked successfully. Booking ID: {booking_id}")
            print("Canceling ticket...")
            flight_booking_system.cancel_ticket(booking_id)
            print("Ticket canceled successfully.")
        else:
            print("Flight not found.")
    except ValueError as e:
        print(e)    