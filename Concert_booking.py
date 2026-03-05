class Concert:
    def __init__(self, name, date, total_tickets, price_per_ticket):
        self.name = name
        self.date = date
        self.total_tickets = total_tickets
        self.tickets_sold = 0
        self.price_per_ticket = price_per_ticket

    def tickets_available(self):
        return self.total_tickets - self.tickets_sold

    def sell_tickets(self, quantity):
        if quantity > self.tickets_available():
            raise ValueError(f"Only {self.tickets_available()} tickets available for {self.name}.")
        self.tickets_sold += quantity
        return quantity * self.price_per_ticket

class TicketSystem:
    def __init__(self):
        self.concerts = {}
        self.purchased_tickets = {}  # User -> list of (concert_name, quantity)

    def add_concert(self, name, date, total_tickets, price_per_ticket):
        if name in self.concerts:
            raise ValueError(f"Concert '{name}' already exists.")
        self.concerts[name] = Concert(name, date, total_tickets, price_per_ticket)

    def view_concerts(self):
        if not self.concerts:
            return "No concerts available."
        result = "Available Concerts:\n"
        for concert in self.concerts.values():
            result += f"{concert.name} on {concert.date} - Tickets available: {concert.tickets_available()} - Price: ${concert.price_per_ticket}\n"
        return result

    def buy_tickets(self, user, concert_name, quantity):
        if concert_name not in self.concerts:
            raise ValueError(f"Concert '{concert_name}' not found.")
        concert = self.concerts[concert_name]
        total_cost = concert.sell_tickets(quantity)
        
        if user not in self.purchased_tickets:
            self.purchased_tickets[user] = []
        self.purchased_tickets[user].append((concert_name, quantity))
        
        return f"Purchased {quantity} tickets for {concert_name}. Total cost: ${total_cost}"

    def view_purchases(self, user):
        if user not in self.purchased_tickets or not self.purchased_tickets[user]:
            return f"No purchases for user '{user}'."
        result = f"Purchases for {user}:\n"
        for concert_name, quantity in self.purchased_tickets[user]:
            result += f"{quantity} tickets for {concert_name}\n"
        return result

def main():
    system = TicketSystem()
    
    # Sample data
    system.add_concert("Captain Lu 2026", "2026-12-15", 90, 980)
    system.add_concert("Jay Chou All the Way North 2026", "2026-11-20", 50, 1280)
    
    while True:
        print("\nConcert Ticket System Menu:")
        print("1. View available concerts")
        print("2. Buy tickets")
        print("3. View my purchases")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == '1':
            print(system.view_concerts())
        
        elif choice == '2':
            user = input("Enter your username: ").strip()
            concert_name = input("Enter concert name: ").strip()
            try:
                quantity = int(input("Enter number of tickets: ").strip())
                print(system.buy_tickets(user, concert_name, quantity))
            except ValueError as e:
                print(f"Error: {e}")
        
        elif choice == '3':
            user = input("Enter your username: ").strip()
            print(system.view_purchases(user))
        
        elif choice == '4':
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
