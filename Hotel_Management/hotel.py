
class Hotel:

    def __init__(self):
        self.filename = "hotel.txt"

    def book_room(self, name, room_no, price, days):
        file = open(self.filename, "r")

        for line in file:

            data = line.strip().split(",")

            if data[0] == str(room_no):
                print("room Already Booked")
                file.close()
                return
        file.close()

        file = open(self.filename,"a")
        file.write(f"{name},{room_no},{price},{days}")
        file.close()

        print("Room Booked Successfully")

    def search_room(self, room_no):

        file = open(self.filename,"r")

        found = False

        for line in file:
            data = line.strip().split(",")

            if data[0] == str(room_no):

                print("\nRoom Found")
                print("Room No :", data[0])
                print("Customer :",data[1])
                print("price :",data[2])
                print("Days :",data[3])

                found = True
                break

        if found == False:
            print("Room Not Found")

        file.close()


    def generate_bill(self, room_no):

        file = open(self.filename,"r")

        found = False

        for line in file:

            data = line.strip().split(",")

            if data[0] == str(room_no):

                total = int(data[2]) * int(data[3])

                print("\n-----Bill------")
                print("Customer :", data[1])
                print("Room No :", data[0])
                print("Total Bill :", total)

                found = True
                break

            if found == False:
                print("Room Not Found")

            file.close()


    def checkout(self,room_no):

        file = open(self.filename,"r")

        record = []

        found = False

        for line in file:

            data = line.strip().split(",")

            if data[0] == str(room_no):
                found = True

            else:
                record.append(line)

        file.close()

        file = open(self.filename,"w")

        file.writelines(record)

        file.close()

        if found:
            print("Checkout Successfull")
        else:
            print("Room Not found")



h1 = Hotel()

while True:

    print("\n=====HOTEL MANAGEMENT=====")
    print("1. Book Room")
    print("2. Search Room")
    print("3. Generate Bill")
    print("4. checkout")
    print("5. Exit")

    choice = int(input("Enter Choice :"))

    if choice == 1:

        room = int(input("Enter Room Number:"))
        name = input("enter Customer name :")
        price = int(input("Enter Price per Day :"))
        days = int(input("Enter Days :"))

        h1.book_room(room, name, price , days)

    elif choice == 2:
        room = int(input("Enter Room Number: "))
        h1.search_room(room)

    elif choice == 3:
        room = int(input("Enter Room Number : "))
        h1.generate_bill(room)

    elif choice == 4:
        room = int(input("Enter Room Number : "))
        h1.checkout(room)

    elif choice == 5:

        print("Thank you")
        break
    else:
        print("Invalid Choice")

