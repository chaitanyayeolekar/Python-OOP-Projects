class Movie:
    def __init__(self,movie_name, total_seats):
        self.movie_name = movie_name
        self.total_seats = total_seats

class Booking:

    def book_ticket(self,movie,seats):

        if movie.total_seats >= seats:
            movie.total_seats -= seats
            print("ticket confirm")
        else:
            print("sold out")
        

    def cancel_ticket(self, movie, seats):
        movie.total_seats += seats
        print(seats,"Ticket cancelled Successfully")

    def show_seat(self, movie):
        print("moive :",movie.movie_name)
        print("Available Seats :", movie.total_seats)


m1 = Movie("intersteller",100)

b1 = Booking()
b1.book_ticket(m1,10)
b1.cancel_ticket(m1,20)
b1.show_seat(m1)
