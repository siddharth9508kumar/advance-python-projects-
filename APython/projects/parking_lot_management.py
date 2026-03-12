class parking_lot:
    def __init__(self, total_slots):
        self.total_slots = total_slots
        self.occupied_slots = 0

    def vehicle_entry_exit(self, action):
        if action == "entry":
            if self.occupied_slots < self.total_slots:
                self.occupied_slots += 1
                print("Vehicle entered. Occupied slots:", self.occupied_slots)
            else:
                print("Parking lot is full. Cannot accommodate more vehicles.")
        elif action == "exit":
            if self.occupied_slots > 0:
                self.occupied_slots -= 1
                print("Vehicle exited. Occupied slots:", self.occupied_slots)
            else:
                print("Parking lot is empty. No vehicles to exit.")
        else:
            print("Invalid action. Please use 'entry' or 'exit'.")
    def available_slots(self):
        available = self.total_slots - self.occupied_slots
        print("Available slots:", available)
    def comute_parking_fee(self, hours):
        fee_per_hour = 10  #let's assume a flat fee of $10 per hour
        total_fee = hours * fee_per_hour
        print("Total parking fee for", hours, "hours is:", total_fee)



parking_lot = parking_lot(100)  # Initialize parking lot with 100 slots
action = input("Enter '1' for vehicle entry or '2' for vehicle exit or '3' to check available slots or '4' to compute parking fee: ")
if action == "1":
    parking_lot.vehicle_entry_exit("entry")
    parking_lot.available_slots()  
elif action == "2":
    parking_lot.vehicle_entry_exit("exit")
    parking_lot.available_slots()  
elif action == "3":
    parking_lot.available_slots()
elif action == "4":
    hours = int(input("Enter the number of hours parked to compute the parking fee: ")) 
    parking_lot.comute_parking_fee(hours) 
else:
    print("Invalid action. Please use '1', '2', '3', or '4 '.")