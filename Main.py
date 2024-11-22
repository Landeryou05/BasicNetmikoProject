# Menu
from Tasks import DateAndTime
from Tasks import ipAddress
from Tasks import RemoteHomeDir
from Tasks import BackupRemoteFile
from Tasks import WebPageBackup

def choice():
    """
    Function:
    This function deals with the output and user input of the choices.
    This function also calls the script that corresponds to the selection made.

    Parameters:
    None

    Returns:
    Void
    """
    loop = True
    while(loop == True):
        print("\n======================= MAIN MENU =======================\n" + "\n" + "Please select an option:\n")

        userOutput = input(
            "1: Print the local date and time\n" 
            "2: Print the public and private IP address of this computer\n"
            "3: Print out the listing of the \'home\' directory on the remote computer\n"
            "4: Backup a file with input of the relative path\n"
            "5: Backup a webpage\n"
            "6: Exit\n\n"
        )

        # Try, catch for error handling
        try:
            # Convert userOutput to int from str
            userOutput = int(userOutput)

            match userOutput:
                case 1:
                    DateAndTime.Main()
                    loop = (loopProgram())
                case 2:
                    ipAddress.Main()
                    loop = (loopProgram())
                case 3:
                    RemoteHomeDir.Main()
                    loop = (loopProgram())
                case 4:
                    BackupRemoteFile.Main()
                    loop = (loopProgram())
                case 5:
                    WebPageBackup.Main()
                    loop = (loopProgram())
                case 6:
                    print("Goodbye!")
                    quit()
                case _:
                    print("\nInvalid Option")
                    continue
        except Exception as e:
            print("\nInvalid Option")
            continue

def loopProgram():
    """
    Function:
    This function deals with the loop of the program.
    This is for when the user wants to make another choice.

    Parameters:
    None

    Returns:
    Void
    """
    programIteration = True
    while(programIteration):
        userLoopProgram = input("\nDo you want to pick another function? (y/n)\n\n").lower()
        try:
            if userLoopProgram == 'y':
                loop = True
            elif userLoopProgram == 'n':
                loop = False
                print("Goodbye!\n")
            return loop
        except Exception as e:
            print("\nInvalid Option, please input y / n")
            continue

def Main():
    choice()

Main()
