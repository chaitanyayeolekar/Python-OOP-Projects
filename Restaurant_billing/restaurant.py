class restaurant:

    GST_RATE = 18

    def __init__(self):
        self.filename = "restaurant.txt"


        self.menu = {
            1:("Noodles",150),
            2:("Manchurian",200),
            3:("Masala Does",120),
            4:("Samosa",20),
            5:("Cold Coffee",120)
        }

    #Show Menu

    def show_menu(self):
        print("\n========MENU==========")
        for food_id in self.menu:

            name , price = self.menu[food_id]

            print(food_id, ":", name, "RS", price)

    #ORDER Food

    def order_food(self, food_id, quantity):

        if food_id not in self.menu:
            print("invalid Food Id")
            return
        name, price = self.menu[food_id]

        amount = price * quantity

        file = open(self.filename,"a")

        file.write(
            f"{name},{price},{quantity},{amount}\n"
        )

        file.close()

        print(name, "ordered successfully")
        print("Amount :",amount)

    #GENERATE BILL

    def generate_bill(self):

        file = open(self.filename,"r")

        total = 0

        print("\n=======BILL========")

        for line in file:

            data = line.strip().split(",")

            name = data[0]
            price = int(data[1])
            quantity = int(data[2])
            amount = int(data[3])

            print(
                name,
                "x",
                quantity,
                "=",
                amount
            )

            total = total + amount

        file.close()

        gst = total * self.GST_RATE / 100

        final_amount = total + gst

        print("------------------------------")
        print("Subtotal :", total)
        print("GST 18%  :",gst)
        print("Total    :",final_amount)


#MAIN Program

r1 = restaurant()

while True:

    print("\n=============RESTAURANT===========")

    print("1.Show Menu")
    print("2. Order Food")
    print("3. Generate Bill")
    print("4. EXit")

    choice = int(input("Enter your choice"))

    if choice == 1:
        r1.show_menu()

    elif choice == 2:
        r1.show_menu()

        food_id = int(input("Enter Food ID :  "))
        quantity = int(input("Enter Quantity :  "))

        r1.order_food(food_id, quantity)

    elif choice == 3:

        r1.generate_bill()

    elif choice == 4:

        print("thank you ")

        break
    else:
        print("Invalid Choice")