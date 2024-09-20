from threading import Thread,Semaphore,current_thread
from time import sleep
from random import randint

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
            print(f"{seats_required} seat(s) booked by {name} from thread {ct}...")
            self.available_seats-=seats_required
            sleep(1)
        else:
            print(f"Sorry, {name} from thread {ct}! {seats_required} seats not available.")
        self.lock.release()

if __name__ == "__main__":
    lock = Semaphore(3)
    btobj1 = BusTicket("IRCTC Bus Ticketing Service",20,lock)
    threads = []
    for i in range(1,10):
        threads.append(Thread(target=btobj1.reserveSeats,args=(f"User-{i}",randint(1,3))))
    [thread.start() for thread in threads]
    threads[-1].join()

    print(f"\nAvailable seats post all reservations is {btobj1.available_seats}")