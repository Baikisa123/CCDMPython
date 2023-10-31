try:
    #create class Triangle

    class Triangle:

    #create constructor
        def __init__(self,base,height):
            self.base = base
            self.height = height

        def TriArea(self):
            print("Area is: ",((self.base * self.height)/2), " cm2")

        def TriPeri(self):
            print("Perimeter is: ",(self.base + self.base + self.base), " cm")

    userbase = int(input("Enter base (cm): "))
    userheight = int(input("Enter height(cm): "))


#object instantiation . Attach to class only with parameters
    triObj = Triangle(userbase,userheight)
#use the object created. Call function here
    #triObj.TriArea()
    triObj.Myfunction()

except SyntaxError:
    print("Please check for missing colon or possible syntax error")

except AttributeError:
    print("Used available functions and methods")




 