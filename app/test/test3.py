def weather(temperature):
    if temperature > 25:
        return "Hot"
    elif temperature >= 15 and temperature <= 25:
        return "Warm"
    else:                       
        return "Cold"
    
result = weather(10)
print(result)
       