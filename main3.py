def hotel_cost(nights):
    return 140*nights
def plane_ride_cost(city):
    if city == "Charlotte":
        return 183
    elif city == "Tampa":
        return 220
    elif city == "Pittsburgh":
        return 222
    elif city == "Los Angeles":
        return 475
def rental_car_cost(days):
    if days >= 7:
        return days*40 - 50
    elif days >= 3:
        return days*40 - 20
    else:
        return days*40
def trip_cost(city, days, spending_money):
    return hotel_cost(days) + plane_ride_cost(city) + rental_car_cost(days) + spending_money
print("Cost of car rental:", rental_car_cost(5))
print("Cost of plane ride to Los Angeles:", plane_ride_cost("Los Angeles"))
print("cost of hotel room", hotel_cost(7))
print("Total trip cost:", trip_cost("Los Angeles", 7,5000))
print(trip_cost("Tampa",6,5000))