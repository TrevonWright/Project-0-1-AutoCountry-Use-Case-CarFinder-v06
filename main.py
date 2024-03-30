class CarFinder:
  def __init__(self):
    self.allowed_vehicle_list = ['Ford F-150', 'Chevrolet Silverado',
     'Tesla CyberTruck', 'Toyota Tundra',
     'Nissan Titan']

  def print_allowed_vehicles(self):
    print("The AutoCountry sales manager has allowed the following vehicles "
      "to be sold:")
    for vehicle in self.allowed_vehicle_list:
          print(vehicle)

  def display_menu(self):
      print("Welcome to the AutoCountry Car Finder!")
      print("Please select an option:")
      print("1. View allowed vehicles")
      print("2. Exit")

  def run(self):
      while True:
          self.display_menu()
          choice = input("Enter your choice: ")

          if choice == '1':
              self.print_allowed_vehicles()
          elif choice == '2':
              print("Thank you for using the AutoCountry Car Finder. Goodbye!")
              break
          else:
              print("Invalid choice. Please try again.")

if __name__ == "__main__":
  finder = CarFinder()
  finder.run()
