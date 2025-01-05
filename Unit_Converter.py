# Convert units of length
def unit_converter():
    print("Length Conversion Options:")
    print("1. Kilometers to Miles")
    print("2. Miles to Kilometers")

    choice = int(input("Choose an option (1/2): "))
    if choice == 1:
        kilometers = float(input("Enter length in kilometers: "))
        print(f"{kilometers} km = {kilometers * 0.621371} miles")
    elif choice == 2:
        miles = float(input("Enter length in miles: "))
        print(f"{miles} miles = {miles * 1.60934} km")
    else:
        print("Invalid option.")


unit_converter()
