# TASK 1

# Import packages
# No need to error handle as datetime is a pre-installed package
from datetime import datetime

def Date():
    """
    Function:
    This function provides the user with the date. This function also
    provides string manipulation techniques to ensure the output is
    in the correct format.

    Parameters:
    None

    Returns:
    Void
    """
    date = str(datetime.now().strftime('%d/%m/%Y'))
    date = date[:10]
    print("\n========= DATE =========")
    print("The date: " + date)

def Time():
    """
    Function:
    This function provides the user with the time. This function also
    provides string manipulation techniques to ensure the output is
    in the correct format.

    Parameters:
    None

    Returns:
    Void
    """
    time = str(datetime.now().replace(microsecond = 0))
    time = time[11:]
    print("\n========= TIME =========")
    print("The local time: " + time + "\n")

# Main function for function calling organisation and debugging
def Main():
    print("\n====================== DATE AND TIME ====================")
    Date()
    Time()