class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory
    @property
    def cpu(self):
        return self.__cpu
    @cpu.setter
    def cpu(self, cpu1):
        self.cpu == cpu1
    @property
    def memory(self):
        return self.__memory 
    @memory.setter
    def memory(self, memory1):
        self.memory == memory1
    def __make_computations(self):
        print(f'Резултат сложения {self.cpu + self.memory}') 
        print(f'Резултат вычитания {self.cpu - self.memory}')  
        print(f'Резултат умножения {self.cpu * self.memory}') 
        print(f'Резултат деления {self.cpu / self.memory}') 
    @property
    def make_computations(self):
        return self.__make_computations

class Laptop(Computer):
    def __init__(self, cpu, memory, memory_card):
        super().__init__(cpu, memory)
        self.__memory_card = memory_card
    @property
    def memory_card(self):
        return self.__memory_card 
    def info(self):
        print(f'{self.cpu} ядер, {self.memory} - память, {self.memory_card} - карта памяти')

laptop = Laptop(200, 100, 100) 
laptop.info()   
laptop.make_computations()