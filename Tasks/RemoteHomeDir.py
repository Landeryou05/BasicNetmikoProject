# TASK 3

# Import packages - Netmiko needs to be installed with PIP
# Error handling for when packages aren't installed
try:
    from netmiko import ConnectHandler
except Exception as e:
    print("**ERROR**: There was an error with the python packages")
    print(f"**ERROR INFORMATION**: {e}")

def remoteConnection():
    """
    Function:
    This function is to connect to the remote computer and then output
    the home directory using the send_command function with Netmiko.

    Parameters:
    None

    Returns:
    Void
    """
    # Connect to the VM
    try:
        connectLinuxVM_HomeDir = ConnectHandler(
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

    # Execute the command to print the contents of the home directory
    # Includes error handling for problems with the command.
    try:
        connectLinuxVM_HomeDir.enable()
        commandExecution = connectLinuxVM_HomeDir.send_command(f"ls -l /home/")
        userOutput(commandExecution)
    except Exception as e:
        print("**ERROR**: There was an error while trying to execute the command. Ensure that you are connecting to a linux-based OS")
        print(f"**ERROR Information**: {e}")

# Function to handle user output
# Takes the output of the command as the parameter
def userOutput(commandExecution):
    print(commandExecution + "\n")

# Main function for function calling organisation and debugging
def Main():
    print("\n================== REMOTE HOME DIRECTORY ================")
    remoteConnection()