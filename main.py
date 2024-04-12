class CarFinder:
    def __init__(self):
        self.allowed_vehicle_list = ['Ford F-150', 'Chevrolet Silverado', 'Tesla \
        CyberTruck', 'Toyota Tundra', 'Nissan Titan']

    def print_allowed_vehicles(self):
        print("The AutoCountry sales manager has allowed the following vehicles to be \
        sold:")
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
        new_vehicle = input("Please Enter the full Vehicle name you would like to add:")
        self.allowed_vehicle_list.append(new_vehicle)
        print(f'You have added "{new_vehicle}" as an authorized vehicle')

    def display_menu(self):
        print("********************************")
        print("AutoCountry Vehicle Finder v0.3")
        print("********************************")
        print("Please Enter the following number below from the following menu:\n")
        print("1. PRINT all Authorized Vehicles")
        print("2. SEARCH for Authorized Vehicle")
        print("3. ADD Authorized Vehicle")
        print("4. Exit")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")

            if choice == '1':
                self.print_allowed_vehicles()
            elif choice == '2':
                self.search_vehicle()
            elif choice == '3':
                self.add_vehicle()
            elif choice == '4':
                print("Thank you for using the AutoCountry Vehicle Finder. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    finder = CarFinder()
    finder.run()


