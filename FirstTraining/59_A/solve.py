data = input()
#sum just the data tha is lowercase
lower = sum(map(str.islower, data))
upper = abs(len(data)-lower)
print(data.upper() if (upper>lower) else data.lower() if (upper == lower) else data.lower() )