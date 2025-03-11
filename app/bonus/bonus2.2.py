# file = open('logs.txt', 'w')
# file.write('101.102.103.222 GET 01.988')
# file.close()
 
# file = open('logs.txt', 'w')
# file.write('171.131.104.108 POST 2.143')
# file.close()

# filenames = ["1.doc","1.report","1.presentation"]

# filenames = [filename.replace('.','-') + '.txt' for filename in filenames]
# print(filenames)

user_entries = ['10', '19.1', '20']

# Convert the strings to floats and calculate the sum
total_sum = sum(float(number) for number in user_entries)

# Print the sum
print(total_sum)
