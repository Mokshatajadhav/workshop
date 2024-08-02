class Vehicle:
    def __init__(self, vehicle_id, make, model, year, category):
        self.vehicle_id = vehicle_id
        self.make = make
        self.model = model
        self.year = year
        self.category = category

    def __str__(self):
        return f"{self.vehicle_id}: {self.year} {self.make} {self.model} ({self.category})"


class RentalSystem:
    def __init__(self):
        self.vehicles = []
        self.vehicle_set = set()

    def add_vehicle(self, vehicle):
        if vehicle not in self.vehicle_set:
            self.vehicles.append(vehicle)
            self.vehicle_set.add(vehicle)
            print(f"Vehicle {vehicle.vehicle_id} added successfully.")
        else:
            print(f"Vehicle {vehicle.vehicle_id} is already in the system.")

    def remove_vehicle(self, vehicle_id):
        vehicle_to_remove = next((v for v in self.vehicles if v.vehicle_id == vehicle_id), None)
        if vehicle_to_remove:
            self.vehicles.remove(vehicle_to_remove)
            self.vehicle_set.remove(vehicle_to_remove)
            print(f"Vehicle {vehicle_id} removed successfully.")
        else:
            print(f"Vehicle {vehicle_id} not found in the system.")

    def search_vehicles(self, search_term):
        return [v for v in self.vehicles if search_term.lower() in v.make.lower() or search_term.lower() in v.model.lower()]

    def list_vehicles(self):
        for vehicle in self.vehicles:
            print(vehicle)

    def categorize_vehicles(self):
        vehicle_categories = {}
        for vehicle in self.vehicles:
            vehicle_categories.setdefault(vehicle.category, []).append(vehicle)

        for category, vehicles in vehicle_categories.items():
            print(f"{category}:")
            for vehicle in vehicles:
                print(f"  - {vehicle}")


rental_system = RentalSystem()


rental_system.add_vehicle(Vehicle(1, "Toyota", "Camry", 2020, "Sedan"))
rental_system.add_vehicle(Vehicle(2, "Honda", "Civic", 2019, "Sedan"))
rental_system.add_vehicle(Vehicle(3, "Ford", "F-150", 2018, "Truck"))
rental_system.add_vehicle(Vehicle(4, "Tesla", "Model 3", 2021, "Electric"))


rental_system.add_vehicle(Vehicle(1, "Toyota", "Camry", 2020, "Sedan"))


print("\nAll vehicles:")
rental_system.list_vehicles()


print("\nSearch results for 'Camry':")
for vehicle in rental_system.search_vehicles("Camry"):
    print(vehicle)


rental_system.remove_vehicle(3)


print("\nAll vehicles after removal:")
rental_system.list_vehicles()


print("\nCategorized vehicles:")
rental_system.categorize_vehicles()
