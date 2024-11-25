# TASK 4

# Import packages - Netmiko needs to be installed with PIP
# Error handling for when packages aren't installed
try:
    from netmiko import ConnectHandler
except Exception as e:
    print("**ERROR**: There was an error with the python packages")
    print(f"**ERROR INFORMATION**: {e}")

# Function to split the ssh connection from the rest of the program
def remoteConnection():
    # Try, exception for error handling unsuccessful connection
    try:
        connectLinuxVM_RemoteBack = ConnectHandler(
            device_type = "linux",
            ip = "",
            username = "",
            password = "",
            secret = "",
            port = ""
        )
    except Exception as e:
        print("**ERROR**: There was an error while trying to establish a connection to the remote host")
        print(f"**ERROR Information**: {e}")
        quit()

    # Set boolean flag to True to allow for initial while exeuction
    # While loop to ensure that the path is correct.
    boolFlag = True
    while(boolFlag == True):
        try:
            connectLinuxVM_RemoteBack.enable()
            userInputPath = input("\nPlease specify the full path for the file that needs to be backed up: ")

            # Pass Null through userOutput function to initiate the while true
            if(userInputPath[0] != '/'):
                print("\nThere needs to be a '/'.")
                userOutput(None, None, True, None)
                continue

            # Line to backup the file using the send command pre defined function
            fileBackup = connectLinuxVM_RemoteBack.send_command(f"cp {userInputPath} {userInputPath}.old")

            # Splits input directory where there are / and places them into an array
            UserInputArray = userInputPath.split("/")
            # This line gets the last value within that array to get the filename so that .old can be added as the extension
            userInputFile = str(UserInputArray[-1:]).replace("[", "").replace("'", "").replace("'", "").replace("]", "")

            boolFlag = False

            # Call userOutput function, where exception is null - there is no error
            userOutput(userInputFile, userInputPath, boolFlag, None)
        except Exception as e:
            userOutput(None, None, boolFlag, e)
            boolFlag = True

def userOutput(userInputFile, userInputPath, boolFlag, e):
    """
    Function:
    This function provides the user output based on the arguments that are passed as parameters
    from the function caller.

    Parameters:
    userInputFile : string
    userInputPath : string
    boolFlag : boolean
    e : string

    Returns:
    Void
    """
    if(boolFlag):
        userOutput = f"\nUnsuccessful! Please Retry."
        if(e != None):
            print(f"**ERROR** {e}")
    else:
        userOutput = f"\nSuccess! You created a backup of {userInputFile} in the {userInputPath} directory called {userInputFile}.old\n"

    # Function provides a printed output to the user as opposed to a return value
    print(userOutput)

# Main function for function calling organisation and debugging
def Main():
    print("\n=================== REMOTE FILE BACKUP ==================")
    remoteConnection()