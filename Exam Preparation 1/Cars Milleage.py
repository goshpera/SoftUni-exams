cars_count = int(input())

fuel_by_car = {}
mileage_by_car = {}

for _ in range(cars_count):
    cars_arguments = input().split("|")
    car = cars_arguments[0]
    mileage = int(cars_arguments[1])
    fuel = int(cars_arguments[2])

    fuel_by_car[car] = fuel
    mileage_by_car[car] = mileage

while True:
    line = input()
    if line == "Stop":
        break
    command_args = line.split(" : ")
    command = command_args[0]
    car = command_args[1]

    if command == "Drive":
        distance = command_args[2]
        fuel_used = int(command_args[3])
        if fuel_used > fuel_by_car[car]:
            print("Not enough fuel to make that ride")
            continue

        mileage_by_car[car] += distance
        fuel_by_car[car] -= fuel_used

        print(f"{car} driven for {distance} kilometers. {fuel_used} litres of fuel consumed.")

        if mileage_by_car[car] >= 100000:
            fuel_by_car.pop(car)
            mileage_by_car.pop(car)
            print(f"Time to sell the {car}")

    elif command == "Refuel":
        fuel_refilled = int(command_args[2])
        fuel_by_car[car] = min(fuel_by_car[car] + fuel_refilled, 75)
        print(f"{car} refueled with {fuel_refilled} liters")

    else:
        reverted_km = int(command_args[2])
        mileage_by_car[car] -= reverted_km
        if mileage_by_car[car] > 10000:
            print(f"{car} mileage decreased by {reverted_km} kilometeres")
        else:
            mileage_by_car[car] = 10000

for car in fuel_by_car.keys():
    fuel = fuel_by_car[car]
    mileage = mileage_by_car[car]
    print(f"{car} -> Mileage: {mileage} kms, Fuel in the tank: {fuel} lt.")
