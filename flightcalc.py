import webview
import csv
import tkinter as tk

Cessna_182 = {
    "prange" : 1053,
    "gph" : 14,
    "fuel_type" : "avgas",
    "cruise_speed" : 167,
    "fuel_price" : 7.87
}

Pilatus_PC12 = {
    "prange" : 1742,
    "gph" : 63,
    "fuel_type" : "jetfuel",
    "cruise_speed" : 270,
    "fuel_price" : 3.2
}

fuel_price = 3.5

def printstats(plane):
    prange = plane["prange"]
    gph = plane["gph"]
    fueltype = plane["fuel_type"]
    print(f"Range (Miles)= {prange}")
    print(f"Efficiency (GPH) = {gph}")
    print(f"Fuel type = {fueltype}")

def addplane():
    print("Feature not yet implemented. Come back later!")

main = input("Hello! This is my flight calculator tool. \nPress Enter to begin, <a> to add a plane, and <s> to open distance calculator.")
if main == "a":
    addplane()
elif main == "s":
    webview.create_window("Distance Calculator", "https://www.airmilescalculator.com")
    webview.start()
else:
    pass

while True:
    plane = input("What plane would you like to use? (Cessna 182, Pilatus PC-12) c, p to choose! >> ")
    if plane == "c":
        print("Cessna 182")
        printstats(Cessna_182)
        break
    elif plane == "p":
        print("Pilatus PC-12")
        printstats(Pilatus_PC12)
        break
    else:
        print("Invalid plane, please try again!")
while True:
    try:
        dist = int(input("Now, how long is your trip? (use miles, not nautical miles)>> "))
    except ValueError:
        print("Use a valid number!")
    if plane == "p" and dist < Pilatus_PC12["prange"]:
        print("Ok, calculating...")
        break
    elif plane == "c" and dist < Cessna_182["prange"]:
        print("Ok, calculating...")
        break
    else:
        print("That is too far for your plane!")

if plane == "c":
    flight_time = dist/Cessna_182["cruise_speed"]
    fuel_burn = flight_time * Cessna_182["gph"]
    fuel_cost = fuel_burn * Cessna_182["fuel_price"]
    print(f"Here are your details! \n Warning: Everything shown is based off of 2023 prices and stats. \nNo values are guaranteed to be exact.")
    print(f"Your total flight time will be {flight_time} hours.")
    print(f"Your total fuel needed will be {fuel_burn} gallons.")
    print(f"Your total fuel cost will be ${fuel_cost}.")
if plane == "p":
    flight_time = dist/Pilatus_PC12["cruise_speed"]
    fuel_burn = flight_time * Pilatus_PC12["gph"]
    fuel_cost = fuel_burn * Pilatus_PC12["fuel_price"]
    print(f"Here are your details! \n Warning: Everything shown is based off of 2023 prices and stats. \nNo values are guaranteed to be exact.")
    print(f"Your total flight time will be {flight_time} hours.")
    print(f"Your total fuel needed will be {fuel_burn} gallons.")
    print(f"Your total fuel cost will be ${fuel_cost}.")
