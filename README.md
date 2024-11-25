PythonIP


Introduction
- This is part of my Project for my System Architecture and Automation module.
- The idea of this program is to remotely connect to a linux virtual machine (ubuntu) and complete a set of commands for the user.


Dependencies
- This program requires 3 dependencies. These include the netmiko library, public-ip library and the requests library.
- However, you can install these dependencies within your local environment with the following commands:
    - 'pip install public-ip'
    - 'pip install netmiko'
    - 'pip install requests'


Additional Notes
- The public IPv4 address functionality is dependent on your ISP's DHCP functionality - sometimes it works, others it won't.
