class House:

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floors):
        self.new_floors = new_floors
        if self.number_of_floors >= 1:

            if self.new_floors > self.number_of_floors:
                print('this isn,t floors')
            else:
                for i in range(1, self.new_floors):
                    print(i)



h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(6)
h2.go_to(10)
