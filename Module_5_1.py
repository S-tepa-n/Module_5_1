class House:
    def __init__(self, name, number):
        self.name = name
        self.number = int(number)


    def go_to(self,new_floor):
        int(new_floor)
        if new_floor > self.number or new_floor <1:
            print(f'Такого этажа в "{self.name}" не существует!')
        else:
            for i in range(1, new_floor + 1):
                print(i)




home_1 = House('ЖК Горский', 18)
home_2 = House('Домик в деревне', 2)
home_1.go_to(5)
home_2.go_to(10)