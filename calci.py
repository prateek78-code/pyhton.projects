import math

class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def division(self, x, y):
        try:
            return x / y
        except ZeroDivisionError:
            return "Error: Division by zero is not allowed."

    def power(self, x, y):
        return math.pow(x, y)
    
    def modulus(self,x,y):
        return x%y

    def sqroot(self, x):
        return math.sqrt(x)

    def log(self, x):
        if x <= 0:
            return "Error: Natural log undefined for zero or negative numbers."
        return math.log(x)

    def sine(self, x):
        return math.sin(math.radians(x))

    def cos(self, x):
        return math.cos(math.radians(x))

    def tan(self, x):
        return math.tan(math.radians(x))
    
    def factorial(self, x):
        return math.factorial(int(x))
    
    def exponential(self, x):
        return math.exp(x)
    
    def cuberoot(self,x):
        return math.cbrt(x)
    
    def multiplicationtable(self,x):
        table=[{int(x)*i} for i in range(1,11)]  
        return table  
    
    def floor(self,x):
        return math.floor(x)
    
    def ceil(self,x):
        return math.ceil(x)
    
    def combination(self, n, r): 
        try: return math.comb(int(n), int(r))
        except: return "Error"
   
    def permutation(self, n, r): 
        try: return math.perm(int(n), int(r))
        except: return "Error"

    def HCF(self, x, y): 
        return math.gcd(int(x), int(y))    

    

    def printing(self):
        print("\nSelect operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Power (x^y)")
        print("6. modulus")
        print("7. sqroot")
        print("8. log")
        print("9. sine")
        print("10. cosine")
        print("11.tan")
        print("12.factorial of a number")
        print("13.exponential of a number")
        print("14.cuberoot")
        print("15.multiplication table")
        print("16.floor of a number")
        print("17.ceil of a number")
        print("18.combination")
        print("19.permutation")
        print("20.HCF")




calc = Calculator()
degree_sign = u"\u00B0"
calc.printing()

    
try:
        choice = int(input("Enter operation number: "))

        if choice == 0:
            print("Invalid choice. Please select a number between 0 and 10.")
            

        elif choice in range(1, 7):
            x = float(input("Enter first number: "))
            y = float(input("Enter second number: "))

            if choice == 1:
                print(f"Sum of {x} and {y}  = {calc.add(x, y)}")
            elif choice == 2:
                print(f"Difference of {x} and {y}  = {calc.subtract(x, y)}")
            elif choice == 3:
                print(f"Product of {x} and {y}  = {calc.multiply(x, y)}")
            elif choice == 4:
                print(f"Division of {x} by {y} = {calc.division(x, y)}")
            elif choice == 5:
                print(f"{x} raised to the power {y} = {calc.power(x, y)}")
            elif choice==6:
                print(f"the modulus of {x} with {y} = {calc.modulus(x)}")    

        elif choice in range(7,18):
            x = float(input("Enter the number: "))

            if choice == 7:
                print(f"Square root of {x} = {calc.sqroot(x)}")
            elif choice == 8:
                print(f"Log base 10 of {x} = {calc.log(x)}")
            elif choice == 9:
                print(f" value of Sin({x}{degree_sign}) = {calc.sine(x)}")
            elif choice == 10:
                print(f" value of Cos({x}{degree_sign}) = {calc.cos(x)}")
            elif choice == 11:
                print(f" value of Tan({x}{degree_sign}) = {calc.tan(x)}")
            elif choice==12:
                print(f"the factorial of {x} = {calc.factorial(x)}") 
            elif choice==13:
                print(f"the exponential of {x} = {calc.exponential(x)}")   
            elif choice==14:
                print(f"the cuberoot of {x} = {calc.cuberoot(x)}")  
            elif choice==15:
                print(f"the multiplication table for {x} = {calc.multiplicationtable(x)}")  
            elif choice==16:
                print(f"the floor for {x} = {calc.floor(x)}") 
            elif choice==17:
                print(f"the ceil for {x} = {calc.ceil(x)}")   

        elif choice in range(18,20):
            n=int(input("enter a number:"))
            r=int(input("enter a number:"))
            if choice==18:
                print(f"the combinatio {n}C{r} is {calc.combination(n,r)}") 
            elif choice==19:
                print(f"the permutation {n}C{r} {calc.permutation(n,r)}")     
        elif choice==20:
            x=int(input("enter a number:"))
            y=int(input("enter a number:"))
            print(f"the HCF of number {x} and {y} = {calc.HCF(x,y)}")       

except ValueError:
        print("Error: Please enter numeric input only.")