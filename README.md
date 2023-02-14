# MAC Address Formatter
A code to format a MAC address according to team standards (XX:XX:XX:XX:XX:XX)

## Functionality
The `mac_modifier` function takes in an input MAC address as a string, removes all dots from the string, and formats it as a string of hexadecimal pairs separated by colons. 


## Usage
If you want to run the code, you can do so by including the following code:

if name == "main":
mac_input = input("What is your MAC Address? ")
output_mac = mac_modifier(mac_input)
print("Original MAC Address: ", mac_input)
print("Corrected MAC Address: ", output_mac)

This will prompt the user to input a MAC address, which will then be processed by the `mac_modifier` function and returned as a formatted string of hexadecimal pairs separated by colons
