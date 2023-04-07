import json
import os.path

seating = {}

# available seat
available_seat = '.'
occupied_seat = 'X'
empty_covid = 'e'


# Define the number of rows and columns in the seating chart
NUM_R = 20
NUM_C = 26


def print_seating():
    """
    Print the current seating chart.
    """
    print("\n            Stage    \n")
    print("   " + " ".join([chr(i)
          for i in range(ord('A'), ord('A')+NUM_C)]))

    if os.path.isfile('seating.json'):
        # si el archivo existe, cargar el contenido del archivo JSON y asignarlo a seating
        seating = load_seating_data()
    else:
        seating = {}

    for i in range(1, NUM_R+1):
        row_str = str(i).zfill(2) + " "
        for j in range(1, NUM_C+1):
            if (i, j) in seating:
                row_str += occupied_seat + " "
            else:
                row_str += available_seat + " "
        print(row_str)


def save_seating_data():
    json_seating = json.dumps(
        {str(k): v for k, v in seating.items()}, default=lambda x: list(x))
    with open("seating.json", 'w') as file:
        file.write(json_seating)


def load_seating_data():
    try:
        with open("seating.json", "r") as f:
            seating = json.load(f)

        # Convertir las claves del diccionario a tuplas
        seating = {eval(k): v for k, v in seating.items()}

        return seating

    except FileNotFoundError:
        return {}


def buy_ticket():
    """
    Buy a ticket by selecting a seat.
    """

    print_seating()

    while True:
        seat = input("Enter seat (e.g. 10A): ").upper()
        if len(seat) < 2 or len(seat) > 3:
            print("Invalid seat. Please try again.")
            continue
        row_str, col_str = seat[:-1], seat[-1]
        if not row_str.isdigit():
            print("Invalid seat. Please try again.")
            continue
        row, col = int(row_str), ord(col_str) - ord('A') + 1
        if row < 1 or row > NUM_R or col < 1 or col > NUM_C:
            print("Invalid seat. Please try again.")
            continue
        if os.path.isfile('seating.json'):
            # si el archivo existe, cargar el contenido del archivo JSON y asignarlo a seating
            seating = load_seating_data()
        else:
            seating = {}

        if (row, col) in seating:
            print("Seat already taken. Please try again.")
            continue

        break

    # Add the seat to the seating dictionary
    # seating[(row, col)] = {"Name": name, "E-mail", email}
    seating[(row, col)] = occupied_seat

    print_seating()


def menu():

    # Print the initial seating chart
    """
    Boddy of the app / Menu / Switches cases
    """
    # loop until user types q
    user_quit = False
    # While userQuit not True still printing the Menu
    while not user_quit:

        line = f"\n    -----------------------------------------"

        print(line)
        print("-+-| Welcome to the Outdoor Park Concert App |-+-")
        print("\n[B]uy")
        print("[V]iew Seating")
        print("[S]earch for a Customer")
        print("[D]isplay all the Purchases")
        print("[Q]uit\n")

        # get first character of input for the menu
        user_input = input("Enter an option: ")
        lower_input = user_input.lower()
        first_char = lower_input[0:1]

        if first_char == 'q':
            user_quit = True

        elif first_char == 'b':

            buy_ticket()
            save_seating_data()

            print("\nSuccesced purchased!")

            print("Seating data saved")

        elif first_char == 'v':

            print_seating()

        elif first_char == 's':
            print("SEARCH")

        elif first_char == 'd':
            print("DISPLAY")

        else:
            print(first_char + " is not a valid option, please try again. ")

    print("\n")
    print("Thank you for using the Outdoor Park Concert App version 1.0 ")
    print("\n")


menu()