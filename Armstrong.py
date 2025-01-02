# Check if a number is an Armstrong number
def is_armstrong(num):
    digits = [int(d) for d in str(num)]
    power = len(digits)
    return num == sum(d**power for d in digits)

number = int(input("Enter a number: "))
if is_armstrong(number):
    print(f"{number} is an Armstrong number!")
else:
    print(f"{number} is not an Armstrong number.")
