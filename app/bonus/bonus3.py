# meals = ['pasta','pizza','salad']

# for meal in meals:
#     print(meal.capitalize())

# for i in range(1,10,2):
#     print(i)

waiting_list = ["sen","ben","john"]
waiting_list.sort()
for index, item in enumerate(waiting_list):
    result = f"{index+1}.{item.capitalize()}"
    print(result)