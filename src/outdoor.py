import login
import json
import os.path

# ITEMS


def load_seating_data():
    try:
        with open("seating.json", "r") as f:
            data = json.load(f)
            seating = {}
            for k, v in data.items():
                k_tuple = tuple(map(int, k.strip("()").split(",")))
                seating[k_tuple] = v
            return seating
    except FileNotFoundError:
        return {}


# Check if the JSON file exists
if os.path.exists("seating.json"):
    # Load the contents of the file into a dictionary
    seating = load_seating_data()
else:
    # If the file doesn't exist, create an empty dictionary
    seating = {}

# available seat
available_seat = '.'
occupied_seat = 'X'
empty_covid = 'e'


# Define the number of rows and columns in the seating chart
NUM_R = 20
NUM_C = 26


def print_seating(seating):
    """
    Print the current seating chart.
    """
    print("\n            Stage    \n")
    print("   " + " ".join([chr(i)
          for i in range(ord('A'), ord('A')+NUM_C)]))
    for i in range(1, NUM_R+1):
        row_str = str(i).zfill(2) + " "
        for j in range(1, NUM_C+1):

            if os.path.exists("seating.json"):
                seating = load_seating_data()
            else:
                seating = {}

            if (i, j) in seating:
                row_str += occupied_seat + " "
            else:
                row_str += available_seat + " "
        print(row_str)


def buy_ticket():
    """
    Buy a ticket by selecting a seat.
    """

    print_seating(seating)

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
        if (row, col) in seating:
            print("Seat already taken. Please try again.")
            continue

        break

    # Add the seat to the seating dictionary
    # seating[(row, col)] = {"Name": name, "E-mail", email}
    seating[(row, col)] = occupied_seat

    login.receipt()

    save_seating_data(seating)

    print_seating(seating)


def save_seating_data(seating):

    seating_str = {}
    for k, v in seating.items():
        seating_str[str(k)] = v
    with open("seating.json", 'w') as file:
        json.dump(seating_str, file)


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

            print("\nSuccesced purchased!")

        elif first_char == 'v':

            seating = load_seating_data()
            print_seating(seating)

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
