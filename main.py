# object oriented programming
from pyscript import display 


class section:
    def __init__(self, numstudents, name, level, adviser) :
        self.numstudents = numstudents
        self.name = name
        self.level = level
        self.adviser = adviser


# instantiating an object 
section1 = section(24, "Topaz", "Mr. De Guzman")
section2 = section(25, "sapphire", "Mr. De Guzman")

display(f'{section1.level}- {section1.name} is part of Red Bulldogs', target='output')
display(f'{section2.level}- {section2.name} is part of Green Hornets', target='output')

display(f)

