import convert 
import invert 

inches = int(input("Inches to convert "))
print(convert.inches_to_feet(inches), " ft")
ounces = int(input("ounces to pounds "))
print(convert.ounces_to_pounds(ounces), " lb")



# The following are not working because functions are not in the name variable.
# We need to create if __name__ == '__main__':
# and put inside the functions.
#print(invert.feet_to_inches(1))
#print(invert.pounds_to_ounces(1))

print("\n")
print("\t\t The value and type of the global name")
print("\t\t", __name__, type(__name__))
print("\t\tThe value of __name__ is Python String")
print("\n")
