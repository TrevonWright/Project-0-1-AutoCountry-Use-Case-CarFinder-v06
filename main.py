class CarFinder:
  def __init__(self):
      self.allowed_vehicle_list = ['Ford F-150', 'Chevrolet Silverado',
    'Tesla CyberTruck', 'Toyota Tundra',
    'Nissan Titan']

  def print_allowed_vehicles(self):
      print("The AutoCountry sales manager has allowed the following vehicles \
      to be sold:")
      for vehicle in self.allowed_vehicle_list:
          print(vehicle)

  def search_vehicle(self):
      search_input = input("Please Enter the full Vehicle Name: ")
      if search_input in self.allowed_vehicle_list:
          print(f"{search_input} is an authorized vehicle")
      else:
          print(f"{search_input} is not an authorized vehicle, if you received this in \
          error please check the spelling and try again")

  def display_menu(self):
      print("Welcome to the AutoCountry Car Finder!")
      print("Please select an option:")
      print("1. View allowed vehicles")
      print("2. Search for Authorized Vehicle")
      print("3. Exit")

  def run(self):
      while True:
          self.display_menu()
          choice = input("Enter your choice: ")

          if choice == '1':
              self.print_allowed_vehicles()
          elif choice == '2':
              self.search_vehicle()
          elif choice == '3':
              print("Thank you for using the AutoCountry Car Finder. Goodbye!")
              break
          else:
              print("Invalid choice. Please try again.")

if __name__ == "__main__":
  finder = CarFinder()
  finder.run()

