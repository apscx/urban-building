class Buiding:
    def __init__(self,floors,type):
        self.numberOfFloors = floors
        self.buildingType = type

    def __eq__(self,other):
        return (self.numberOfFloors == other.numberOfFloors) and \
               (self.buildingType == other.buildingType)

b1 = Buiding(5,'office')
b2 = Buiding(4,'office')
b3 = Buiding(5,'office')

print(b1 == b2)
print(b1 == b3)
