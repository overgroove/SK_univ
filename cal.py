class Calculator: # 클래스 선언
    
    def __init__(self, x, y): # 초기화함수
        self.x = x
        self.y = y
        
    def my_sum(self):
        z = self.x + self.y
        return z

    def my_minus(self):
        z = self.x - self.y
        return z

    def my_multiply(self):
        z = self.x * self.y
        return z

    def my_division(self):
        z = self.x / self.y
        return z