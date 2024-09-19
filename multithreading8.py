from threading import Thread,Lock,current_thread
from time import sleep

class BusTicket():
    def __init__(self,name,available_seats,lock) -> None:
        self.name = name
        self.available_seats = available_seats
        self.lock = lock

    def reserveSeats(self,name,seats_required):
        self.lock.acquire()
        print(f"Welcome to {self.name}! Seats available are {self.available_seats}")
        ct = current_thread().name
        if(self.available_seats >= seats_required):
            print(f"{seats_required} are booked by {name} from thread {ct}...")
            self.available_seats-=seats_required
            sleep(1)
        else:
            print(f"Sorry, {name} from thread {ct}! Required seats are not available.")
        self.lock.release()

if __name__ == "__main__":
    lock = Lock()
    btobj1 = BusTicket("IRCTC Bus Ticketing Service",8,lock)
    t1 = Thread(target=btobj1.reserveSeats,args=("Ramesh",3),name="Ramesh")
    t2 = Thread(target=btobj1.reserveSeats,args=("Suresh",5),name="Suresh")
    t3 = Thread(target=btobj1.reserveSeats,args=("Dinesh",1),name="Dinesh")

    t1.start()
    t2.start()
    t3.start()