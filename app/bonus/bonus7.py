feet_inches = input("Enter feet and inches: ")

def parse(feetinches):
    parts = feetinches.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])
    return feet, inches

def convert(feet,inches):  
    total_inches = (feet * 0.3048) + inches * 0.0254
    return total_inches

f, i = parse(feet_inches)
print("f:",f , "i:",i)
result = convert(f,i)

if result < 1:
    print("Kid is too Small.")

else:
    print("Kid can use the slide.")

