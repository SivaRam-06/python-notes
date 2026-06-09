import random

# Nested dictionary to store user data
users = {}


# ---------------------- FUNCTIONS ----------------------

def generate_otp():
    """Generate a 4-digit OTP"""
    return str(random.randint(1000, 9999))


def signup():
    username = input("Enter Username: ")

    if username in users:
        print("Username already exists. Please login.")
        return None

    name = input("Enter Your Name: ")

    # Creating nested dictionary for user
    users[username] = {
        "name": name,
        "wins": 0,
        "losses": 0,
        "score": 0
    }

    print("Signup Successful!")
    return username


def login():
    username = input("Enter Username: ")

    if username not in users:
        print("User not found. Please signup first.")
        return None

    otp = generate_otp()
    print("Generated OTP:", otp)

    entered_otp = input("Enter OTP: ")

    if entered_otp == otp:
        print("Login Successful!")
        return username
    else:
        print("Invalid OTP!")
        return None


def roll_dice():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    return die1, die2


def play_game(username):
    while True:
        print("\n------ Lucky 7 Game ------")
        print("Bet Options: +7  |  -7  |  ==7")
        print("Type 'exit' to logout")

        bet = input("Enter your bet: ")

        if bet == "exit":
            print("Logging out...")
            break

        if bet not in ["+7", "-7", "==7"]:
            print("Invalid Bet! Try again.")
            continue

        die1, die2 = roll_dice()
        total = die1 + die2

        print(f"Dice Rolled: {die1} and {die2}")
        print("Total:", total)

        # Conditional Statements
        if bet == "+7":
            if total > 7:
                print("You Won! +10 Points")
                users[username]["wins"] += 1
                users[username]["score"] += 10
            else:
                print("You Lost! -5 Points")
                users[username]["losses"] += 1
                users[username]["score"] -= 5

        elif bet == "-7":
            if total < 7:
                print("You Won! +10 Points")
                users[username]["wins"] += 1
                users[username]["score"] += 10
            else:
                print("You Lost! -5 Points")
                users[username]["losses"] += 1
                users[username]["score"] -= 5

        elif bet == "==7":
            if total == 7:
                print("You Won! +20 Points")
                users[username]["wins"] += 1
                users[username]["score"] += 20
            else:
                print("You Lost! -5 Points")
                users[username]["losses"] += 1
                users[username]["score"] -= 5

                # Display Updated Data
        print("\nUpdated User Data:", users[username])

        choice = input("\nPress any key to play again | Press 0 to stop game: ")

        if choice == "0":
            print("Game Stopped.")
            break

        # ---------------------- MAIN PROGRAM ----------------------


while True:
    print("\n===== Welcome to Lucky 7 Application =====")
    print("1. Signup")
    print("2. Login")
    print("3. Exit")

    option = input("Choose an option: ")

    if option == "1":
        user = signup()
        if user:
            play_game(user)

    elif option == "2":
        user = login()
        if user:
            play_game(user)

    elif option == "3":
        print("Exiting Application...")
        break

    else:
        print("Invalid Choice! Try Again.")