# You are provided with a list (or array) of integer arrays (or tuples). 
# Each integer array has two items which represent number of people get into bus 
# (The first item) and number of people get off the bus (The second item) in a bus stop.
# Your task is to return number of people who are still in the bus after the last bus station (after the last array). 


def number(bus_stops):
    total = 0
    for i in range (len(bus_stops)):
        total += (bus_stops[i][0]) - (bus_stops[i][1])
    return total
    
    
def main():
    bus_stops = [[10,0],[3,5],[5,8]]
    number(bus_stops)
    result = number(bus_stops)
    print("The number of people who are still in the bus after the last bus station:", result)

main()
print ("The End. Press Enter")