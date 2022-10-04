class math:
    def __init__(self,x,y,z):
        self.num1 = x+y+z
        self.num2 = x-y +10
        self.num3 = x/2 +y*z
    def xinchao(self):
        return "result is  " + str(self.num1)


calculator = math(10,30,30)

print(calculator.num1)
print(calculator.num2)
print(calculator.num3)
print(calculator.xinchao())
