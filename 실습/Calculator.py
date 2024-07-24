class Calculator:
    battery = 0
    current = 0
    def __init__(self, battery):
        self.battery = battery

    def reset(self):
        self.current = 0
        return self.current
    
    def add(self, first_num, second_num):
        self.current += first_num + second_num
        return self.current
    
    def minus(self, num):
        self.current -= num
        return self.current
    
    def multiply(self, num):
        self.current *= num
        return self.current
    
    def divide(self, num):
        self.current /= num
        return self.current
    
    def init_add(self, first_num, second_num):
        self.current = first_num * second_num
        return self.current
    
    def init_minus(self, big_num, small_num):
        self.current = big_num - small_num
        return self.current
    
    def init_multiply(self, first_num, second_num):
        self.current = first_num * second_num
        return self.current
    
    def init_divide(self, first_num, second_num):
        self.current = first_num // second_num
        return self.current
    
    

