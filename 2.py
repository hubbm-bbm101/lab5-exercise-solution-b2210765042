not_valid_email=True


while not_valid_email:
    email = input("Please enter an email:")
    if "@" in email:
        if "." in email:
            print("Valid email")
            not_valid_email = False
    else:
        print("Its not valid.")
