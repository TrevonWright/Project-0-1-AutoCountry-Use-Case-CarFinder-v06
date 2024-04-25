import os

class CarFinder:

    def __init__(self):
        self.allowed_vehicle_file = "allowed_vehicles.txt"
        self.load_vehicles()

    def load_vehicles(self):
        if os.path.exists(self.allowed_vehicle_file):
            with open(self.allowed_vehicle_file, "r") as file:
                self.allowed_vehicle_list = file.read().splitlines()
        else:
            self.allowed_vehicle_list = ["Ford F-150",
                                         "Chevrolet Silverado",
                                         "Tesla CyberTruck",
                                         "Toyota Tundra",
                                         "Rivian R1T",
                                         "Ram 1500"]

    def save_vehicles(self):
        with open(self.allowed_vehicle_file, "w") as file:
            for vehicle in self.allowed_vehicle_list:
                file.write(vehicle + "\n")

    def print_allowed_vehicles(self):
        print("The AutoCountry sales manager has allowed these vehicles to be sold:")
        for vehicle in self.allowed_vehicle_list:
            print(vehicle)

    def search_vehicle(self):
        search_input = input("Please Enter the full Vehicle Name: ")
        if search_input in self.allowed_vehicle_list:
            print(f"{search_input} is an authorized vehicle")
        else:
            print(f"{search_input} is not an authorized vehicle, if you received this \
            in error please check the spelling and try again")

    def add_vehicle(self):
        new_vehicle = input("Please Enter the full Vehicle name you would like to \
        add: ")
        if new_vehicle not in self.allowed_vehicle_list:
            self.allowed_vehicle_list.append(new_vehicle)
            self.save_vehicles()
            print(f'You have added "{new_vehicle}" as an authorized vehicle')
        else:
            print(f'"{new_vehicle}" is already in the list of authorized vehicles')

    def delete_vehicle(self):
        delete_input = input("Please Enter the full Vehicle name you would like to \
        REMOVE: ")
        if delete_input in self.allowed_vehicle_list:
            confirm_delete = input(f'Are you sure you want to remove "{delete_input}" \
            from the Authorized Vehicles List?\n').lower()
            if confirm_delete == 'yes':
                self.allowed_vehicle_list.remove(delete_input)
                self.save_vehicles()
                print(f'You have REMOVED "{delete_input}" as an authorized vehicle')
        else:
            print(f"{delete_input} is not found in the list of authorized vehicles.")

    def display_menu(self):
        print("********************************")
        print("AutoCountry Vehicle Finder v0.6")
        print("********************************")
        print("Please Enter the following number below from the following menu:\n")
        print("1. PRINT all Authorized Vehicles")
        print("2. SEARCH for Authorized Vehicle")
        print("3. ADD Authorized Vehicle")
        print("4. DELETE Authorized Vehicle")
        print("5. Exit")

    def print_all_vehicles(self):
        self.print_allowed_vehicles()

    def search_authorized_vehicle(self):
        self.search_vehicle()

    def add_authorized_vehicle(self):
        self.add_vehicle()

    def delete_authorized_vehicle(self):
        self.delete_vehicle()

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")

            if choice == '1':
                self.print_all_vehicles()
            elif choice == '2':
                self.search_authorized_vehicle()
            elif choice == '3':
                self.add_authorized_vehicle()
            elif choice == '4':
                self.delete_authorized_vehicle()
            elif choice == '5':
                print("Thank you for using the AutoCountry Vehicle Finder. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    finder = CarFinder()
    finder.run()



