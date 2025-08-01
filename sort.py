def generate_numeric(prompt):
    "Validate the input prompt "

    while True:
        value = input(prompt).strip()
        try:
            return float(value)
        except ValueError:
            print("Please enter valid numeric dimension, please try again")


def isbulky(vol, width, height, length):
    "Check if the package is buly"

    if vol >= 1000000 or width >= 150 or height >= 150 or length >= 150:
        return True
    return False


def classify_package(width, height, length, mass):

    vol = width * height * length

    bulky = isbulky(vol, width, height, length)

    if bulky and mass >= 20:
        return 'Rejeåcted'
    elif bulky or mass >= 20:
        return "Special"
    else:
        return "Standard"


if __name__ == "__main__":
    width = generate_numeric("Width of the package in cm: ")
    height = generate_numeric("Height of the package in cm: ")
    length = generate_numeric("Length of the package in cm: ")
    mass = generate_numeric("Mass/Weight of the package in kg: ")
    result = classify_package(width, height, length, mass)

    if result == 'Rejected':
        print("Package is rejected as is it is bulky and heavy")
    elif result == 'Special':
        print("Package is special as it is either bulky or heavy")
    else:
        print("Package is standard")
