def run_app():
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
            print("BUY")

        elif first_char == 'v':
            print("VIEW")

        elif first_char == 's':
            print("SEARCH")

        elif first_char == 'd':
            print("DISPLAY")

        else:
            print(first_char + " is not a valid option, please try again. ")

    print("\n")
    print("Thank you for using the Outdoor Park Concert App version 1.0 ")
    print("\n")


run_app()
