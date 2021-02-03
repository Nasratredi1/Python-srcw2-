# for more detail click on this link: https://micropyramid.com/blog/understand-self-and-__init__-method-in-python-class/#:~:text=%22__init__%22%20is%20a%20reseved,the%20attributes%20of%20a%20class.
class point():
    def __init__(self,input1, input2):# You can write x and y self represents the instance of the class. By using the "self" keyword we can access the attributes and methods of the class in python.
        self.x = input1
        self.y = input2
        
p = point(2, 8)
print(p.x)
print(p.y)

#"__init__" is a reseved method in python classes. It is known as a constructor in object oriented concepts. This method called when an object is created from the class and it allow the class to initialize the attributes of a class.