import re

"""
	Student: Edgar Nunez
	Module: user_login
	Description: This module requires an email in order to start to save the info of the client.
    If the adress is an invalid one, the app doesn't start.
"""

regex = re.compile(r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+")


def is_valid_email(lower_email):
    """Function to valid if a email is correct. Using regular expressios for get the possible ch in
    the correct position, the function also works to validate if there is a "@" and a dot (.) //
    Args:
        lowerEmail: _email input already passed to lower case_
    Returns:
        Boolean: - True is the email is valid
                 - False for incorrect email adress"""
    if re.fullmatch(regex, lower_email):
        return True
    else:
        return False


def login():
    """Function which convert the input email in lower case /
       If the email is correct, then it asks for the password /
    Returns:
        userName
    """

    while not (is_valid_email == True):
        email_address = input(
            "\nPlease enter an e-mail to continue with your reservation: "
        )
        lower_email = email_address.lower()

        if is_valid_email(lower_email) == True:
            return lower_email  # = user_name

        else:
            print("\nInvalid email adress, try again please.")


def receipt():
    name = input("Please emter your name: ")
    email = login()
    # seats =
    ticket_cost = 80
    tax = ticket_cost * 0.0725
    mask_fee = 5
    total = ticket_cost + tax + mask_fee

    receipts = {
        "name": name,
        "email": email,
        # seats =
        "ticket_cost": ticket_cost,
        "tax": tax,
        "mask_fee": mask_fee,
        "total": total,
    }

    return receipts
