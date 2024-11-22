# TASK 5

# Import packages - requests needs to be installed with PIP
# Error handling for when packages aren't installed
try:
    import requests
except Exception as e:
    print("**ERROR**: There was an error with the python packages")
    print(f"**ERROR INFORMATION**: {e}")

def websiteURL():
    # Try, except for error handling
    try:
        # This gets the website URL from the user
        websiteURL = input("Please enter a URL:\n")
        httpRequest = requests.get(websiteURL)
        # This line converts the response from the websiteURL to text
        formatWebsite = httpRequest.text

        # This line get the user to enter the name of the file
        fileName = input("\nWhat do you want the file to be called?\n")

        # Loop initiation for error handling and unexpected inputs
        loop = True
        while(loop):
            # Getting the input from the user to get the file extension
            fileExtension = input("\nWhat file extension do want on the file?\n")

            # Making sure file extension is seperated from the file name
            # This does NOT check the validity of the file extension
            if ("." in fileExtension):
                fullFileName = (fileName + fileExtension)
                with open(f"{fullFileName}", "w") as fullFileName:
                    fullFileName.write(formatWebsite)
                print(f"\nSuccess! \'{websiteURL}\' has been backed up within this project's directory, under the name: {fileName}{fileExtension}!\n")
                break

            else:
                print("\n**ERROR**: Incorrect File Extension - must start with a \'.\'.")
                continue

    except Exception as e:
        print("**ERROR**: There was an error while trying to retrieve the HTML for the given URL")
        print(f"**ERROR Information**: {e}")

# Main function for function calling organisation and debugging
def Main():
    print("\n================== WEB PAGE FILE BACKUP =================\n")
    websiteURL()