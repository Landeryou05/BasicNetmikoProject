# TASK 2

# Importing packages
# Error handling for handling uninstalled pockages
try:
    import socket
    import public_ip
    from netmiko import ConnectHandler
except Exception as e:
    print("**ERROR**: There was an error with the python packages")
    print(f"**ERROR INFORMATION**: {e}")

def localIP():
    """
    Function:
    This function provides the logic to find the public and private IPv4 address for the user.
    This also provides error handling for the possibility of the 'public_ip' not working as expected.
    This function will then call the 'userOutput' function with the public and private IP as arguements.

    Parameters:
    None

    Returns:
    Void
    """

    errorFlag = True
    # This line gets the hostname to then retrieve the private IP address of the local machine
    hostName = socket.gethostname()
    privateIpAddress = socket.gethostbyname(hostName)

    try:
        publicIpAddress = public_ip.get()
    # Store Exception object as a variable named 'e'.
    except Exception as e:
        errorFlag = False
        publicIpAddress = None

    # Calls localIPOutput within the UserOutput class with the following arguments
    UserOutput.localIPOutput(privateIpAddress, publicIpAddress, errorFlag)

def remoteIP():
    """
    Function:
    This function gets the private IP address of the remote computer.
    The localhost IP address is used to establish a connection with the remote
    computer and is NOT the private IP address.

    Parameters:
    None

    Returns:
    Void
    """
    try:
        connectLinuxVM_IP = ConnectHandler(
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

    try:    
        connectLinuxVM_IP.enable()
        command = "hostname -I"
        commandExecute = connectLinuxVM_IP.send_command(command)
        ipAddressArray = commandExecute.split()
        remoteIP = ipAddressArray[1]
        UserOutput.remoteIPOutput(remoteIP)
    except Exception as e:
        print("**ERROR**: There was an error while trying to execute the command. Ensure that you are connecting to a linux-based OS")
        print(f"**ERROR Information**: {e}")

# Class is used because there is more than one type of user output - based on the function caller
class UserOutput:
    def remoteIPOutput(remoteIP):
        print("\n======================= REMOTE IPv4 ======================" + f"\nYour remote computer's private IPv4 address is: {remoteIP} \n")
        
    def localIPOutput(privateIpAddress, publicIpAddress, errorFlag):
        """
        Function:
        This function provides the output for the program.

        Parameters:
        privateIpAddress : string
        publicIpAddress : string
        errorFlag : boolean

        Returns:
        Void
        """

        if(errorFlag and publicIpAddress != None):
            print("\n======================= PRIVATE IPv4 =====================" + f"\nYour local computer's private IPv4 address is: {privateIpAddress} \n")
            print("======================== PUBLIC IPv4 =====================" + "\nYour local computer's public IPv4 address is: " + str(publicIpAddress))
        else:
            print("\n======================= PRIVATE IPv4 =====================" + f"\nYour local computer's private IPv4 address is: {privateIpAddress}")

# Main function for function calling organisation and debugging
def Main():
    print("\n====================== IP ADDRESS =======================")
    localIP()
    remoteIP()