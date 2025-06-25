# Train Ticket Booking System

class Train:
    def __init__(self, train_number, name, source, destination, seats):
        self.train_number = train_number
        self.name = name
        self.source = source
        self.destination = destination
        self.seats = seats  # total available seats

    def display_train_info(self):
        print(f"Train No: {self.train_number}, Name: {self.name}, From: {self.source}, To: {self.destination}, Seats Available: {self.seats}")


class Passenger:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def display_passenger_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}")


class Ticket:
    ticket_counter = 1

    def __init__(self, passenger, train):
        self.ticket_id = Ticket.ticket_counter
        Ticket.ticket_counter += 1
        self.passenger = passenger
        self.train = train

    def display_ticket(self):
        print("\n--- TICKET DETAILS ---")
        print(f"Ticket ID: {self.ticket_id}")
        self.passenger.display_passenger_info()
        self.train.display_train_info()
        print("----------------------\n")


class Account:
    def __init__(self):
        self.trains = []
        self.tickets = []

    def add_train(self, train):
        self.trains.append(train)

    def show_trains(self):
        print("\nAvailable Trains:")
        for train in self.trains:
            train.display_train_info()

    def book_ticket(self, train_number, passenger):
        for train in self.trains:
            if train.train_number == train_number:
                if train.seats > 0:
                    train.seats -= 1
                    ticket = Ticket(passenger, train)
                    self.tickets.append(ticket)
                    print("Ticket booked successfully!")
                    ticket.display_ticket()
                    return
                else:
                    print("Sorry, no seats available on this train.")
                    return
        print("Train not found.")

    def show_all_tickets(self):
        if not self.tickets:
            print("No tickets booked yet.")
        else:
            for ticket in self.tickets:
                ticket.display_ticket()


# -------------------------------
# Main Application
# -------------------------------

def main():
    account = Account()

    # Add some trains
    account.add_train(Train(101, "Express Line", "Hyderabad", "Delhi", 3))
    account.add_train(Train(202, "Southern Rail", "Chennai", "Bangalore", 2))

    while True:
        print("\n========= Train Booking Menu =========")
        print("1. Show Available Trains")
        print("2. Book Ticket")
        print("3. Show Booked Tickets")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            account.show_trains()
        elif choice == '2':
            name = input("Enter Passenger Name: ")
            age = int(input("Enter Age: "))
            gender = input("Enter Gender: ")
            passenger = Passenger(name, age, gender)

            account.show_trains()
            train_number = int(input("Enter Train Number to Book: "))
            account.book_ticket(train_number, passenger)
        elif choice == '3':
            account.show_all_tickets()
        elif choice == '4':
            print("Exiting system. Thank you!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
