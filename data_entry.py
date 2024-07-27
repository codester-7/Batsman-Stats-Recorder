def get_name():
    try:
        name = input("Enter name of player: ")
        return name
    except TypeError:
        print(f"{name} is not a string. Please enter valid input.")
        return get_name()


def get_matches():
    try:
        matches = int(input("Enter number of matches played: "))
        if matches <= 0:
            raise ValueError("Player must have played at least one match.")
        return matches
    except TypeError:
        print("Invalid data type. Please enter number of matches played as integer.")  
        return get_matches()


def get_runs_scored():
    try:
        runs_scored = int(input("Enter number of runs scored by batsman: "))
        if runs_scored <= 0:
            raise ValueError("Runs scored must be above 0.")
        return runs_scored
    except TypeError:
        print("Invalid data type. Please enter number of runs scored as integer.")
        return get_runs_scored()


def get_strike_rate():
    try:
        strike_rate = float(input("Enter strike rate of batsman: "))
        if strike_rate <= 0:
            raise ValueError("Strike rate must be above 0.")
        return strike_rate
    except TypeError:
        print("Invalid data type. Please enter strike rate as a decimal value.")
        return get_strike_rate()


def get_average():
    try:
        average = float(input("Enter average of batsman: "))
        if average <= 0:
            raise ValueError("Average must be above 0.")
        return average
    except TypeError:
        print("Invalid data type. Please enter average as a decimal value.")
        return get_average()
            
