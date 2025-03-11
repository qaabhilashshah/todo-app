# filenames = ['1.Raw Data.txt','2.Reports.txt','3.Presentations.txt']

# for filename in filenames:
#     filename = filename.replace('.','-',1)
#     print(filename)
# List of products
# products = ["table", "chair", "door"]

# # Iterate over the list and print each product
# for product in products:
#     print(f"Product: {product}")

# filenames = ['document', 'report', 'presentation']
# for index, filename in enumerate(filenames):
#     row = f"{index}-{filename.title()}.txt"
#     print(row)

# mylist = ['a', 'b', 'c', 'd']

# for item in mylist:
#     print(len(mylist))

# measurements = [177.8, 175.8, 166.9, 182.5]
# measurements.sort()
# for m in measurements:
#     print(m)

# for i, j in enumerate("abcd"):
#     print(i.capitalize())

# for i, j in enumerate("abcd"):
#     print(f"Printing {j * 5}")

# countries = ["Albania", "Belgium", "Canada", "Denmark", "Ethiopia", "France"]

# for country in countries:
#     # Create a filename with .txt extension
#     filename = f"{country}.txt"
    
#     # Write the country name into the file
#     file = open(filename, "w")
#     file.write(country)

member = input("Add a new member: ")

file = open("members.txt", 'r')
existing_members = file.readlines()
file.close()

existing_members.append(member + "\n")

file = open("members.txt", 'w')
existing_members = file.writelines(existing_members)
file.close()