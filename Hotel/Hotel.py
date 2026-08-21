class Hotel:

    def __init__(self):

        self.filename = "hotel.txt"

        self.rooms = {
            101: {
                "type": "Single",
                "price": 1500,
                "status": "Available",
                "name": "",
                "days": 0
            },

            102: {
                "type": "Double",
                "price": 2500,
                "status": "Available",
                "name": "",
                "days": 0
            },

            103: {
                "type": "Deluxe",
                "price": 3500,
                "status": "Available",
                "name": "",
                "days": 0
            },

            104: {
                "type": "Suite",
                "price": 5000,
                "status": "Available",
                "name": "",
                "days": 0
            },

            105: {
                "type": "Luxury",
                "price": 9000,
                "status": "Available",
                "name": "",
                "days": 0
            }
        }

    # ==============================
    # SHOW ROOMS
    # ==============================

    def show_rooms(self):

        print("\n==============================================")
        print("              HOTEL ROOMS")
        print("==============================================")

        for room_id in self.rooms:

            room = self.rooms[room_id]

            print(
                "Room:", room_id,
                "| Type:", room["type"],
                "| Price: Rs", room["price"],
                "| Status:", room["status"]
            )

        print("==============================================")

    # ==============================
    # BOOK ROOM
    # ==============================

    def book_room(self):

        print("\n==============================================")
        print("                 BOOK ROOM")
        print("==============================================")

        room_no = int(input("Enter Room Number: "))

        if room_no in self.rooms:

            if self.rooms[room_no]["status"] == "Available":

                name = input("Enter Customer Name: ")

                days = int(input("Enter Number of Days: "))

                self.rooms[room_no]["status"] = "Booked"
                self.rooms[room_no]["name"] = name
                self.rooms[room_no]["days"] = days

                print("\nRoom Booked Successfully!")
                print("Customer:", name)
                print("Room Number:", room_no)
                print("Days:", days)

            else:

                print("Room is already booked.")

        else:

            print("Invalid Room Number.")

    # ==============================
    # CHECKOUT
    # ==============================

    def checkout(self):

        print("\n==============================================")
        print("                 CHECKOUT")
        print("==============================================")

        room_no = int(input("Enter Room Number: "))

        if room_no in self.rooms:

            if self.rooms[room_no]["status"] == "Booked":

                name = self.rooms[room_no]["name"]
                room_type = self.rooms[room_no]["type"]
                price = self.rooms[room_no]["price"]
                days = self.rooms[room_no]["days"]

                amount = price * days

                self.save_bill(
                    name,
                    room_no,
                    room_type,
                    price,
                    days,
                    amount
                )

                print("\n==============================================")
                print("                 HOTEL BILL")
                print("==============================================")

                print("Customer Name :", name)
                print("Room Number   :", room_no)
                print("Room Type     :", room_type)
                print("Price Per Day :", price)
                print("Number of Days:", days)

                print("----------------------------------------------")

                print("Total Amount  : Rs", amount)

                print("==============================================")

                self.rooms[room_no]["status"] = "Available"
                self.rooms[room_no]["name"] = ""
                self.rooms[room_no]["days"] = 0

                print("Checkout Successful!")

            else:

                print("Room is not booked.")

        else:

            print("Invalid Room Number.")

    # ==============================
    # SAVE BILL
    # ==============================

    def save_bill(
        self,
        name,
        room_no,
        room_type,
        price,
        days,
        amount
    ):

        file = open(self.filename, "a")

        file.write(
            f"Customer Name : {name}\n"
            f"Room Number   : {room_no}\n"
            f"Room Type     : {room_type}\n"
            f"Price Per Day : {price}\n"
            f"Number of Days: {days}\n"
            f"Total Amount  : Rs {amount}\n"
            f"----------------------------------\n"
        )

        file.close()

        print("Bill saved successfully!")

    # ==============================
    # VIEW BILL HISTORY
    # ==============================

    def view_bills(self):

        print("\n==============================================")
        print("              BILL HISTORY")
        print("==============================================")

        try:

            file = open(self.filename, "r")

            for line in file:

                print(line.strip())

            file.close()

        except FileNotFoundError:

            print("No bill history found.")

    # ==============================
    # MENU
    # ==============================

    def menu(self):

        while True:

            print("\n")
            print("==============================================")
            print("          HOTEL MANAGEMENT SYSTEM")
            print("==============================================")

            print("1. Show Rooms")
            print("2. Book Room")
            print("3. Checkout")
            print("4. View Bill History")
            print("5. Exit")

            print("==============================================")

            choice = input("Enter Your Choice: ")

            if choice == "1":

                self.show_rooms()

            elif choice == "2":

                self.book_room()

            elif choice == "3":

                self.checkout()

            elif choice == "4":

                self.view_bills()

            elif choice == "5":

                print("\nThank You for using Hotel Management System!")
                break

            else:

                print("Invalid Choice. Please try again.")


# ==============================
# MAIN PROGRAM
# ==============================

hotel = Hotel()
hotel.menu()