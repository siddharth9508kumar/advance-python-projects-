class book_ticket:
    def __init__(self, movie_name, show_time, seat_number):
        self.movie_name = movie_name
        self.show_time = show_time
        self.seat_number = seat_number

    def display_ticket_details(self):
        print(f"Movie: {self.movie_name}")
        print(f"Show Time: {self.show_time}")
        print(f"Seat Number: {self.seat_number}")
    def compute_ticket_price(self):
        base_price = 10 
        if self.show_time in ["12:00 PM", "3:00 PM"]:
            price = base_price * 0.8  
        else:
            price = base_price
        print(f"Ticket Price: ${price:.2f}")
    def check_seat_availability(self):
        print(f"Seat {self.seat_number} is available for booking.")
    def cancel_ticket(self):
        print(f"Ticket for {self.movie_name} at {self.show_time} with seat {self.seat_number} has been canceled.")

while True:
    movie_name = input("Enter the movie name: ")
    show_time = input("Enter the show time (e.g., 12:00 PM, 3:00 PM, 6:00 PM): ")
    seat_number = input("Enter the seat number: ")
    ticket = book_ticket(movie_name, show_time, seat_number)
    ticket.display_ticket_details()
    ticket.compute_ticket_price()
    ticket.check_seat_availability()
    cancel = input("Do you want to cancel the ticket? (yes/no): ")
    if cancel.lower() == "yes":
        ticket.cancel_ticket()
    continue_booking = input("Do you want to book another ticket? (yes/no): ")
    if continue_booking.lower() != "yes":
        print("Thank you for hooking with us! Enjoy your movie!")
        break

