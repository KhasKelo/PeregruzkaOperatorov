class Building:

    def __init__(self, numberOfFloors : int, buildingType : str):
        self.numberOfFloors = numberOfFloors
        self.buildingType = buildingType


    def __eq__(self, other):
        return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType


building_1 = Building(4, 'Home')
building_2 = Building(4, 'Home')

print(building_1 == building_2)