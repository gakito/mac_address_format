
# Code to format a MAC address according to team standards

# get the original mac address and exclude all . in it. 
# TODO later: delete any special character
def mac_modifier(mac_input):
    mac_input = mac_input.replace(".","")
    output_mac = ""
    for i, char in enumerate(mac_input):
        output_mac += char
        #check if it is a pair character so it can include : after it. it also checks if it's not the last digit.
        if (i+1) % 2 == 0 and i != len(mac_input) - 1:
            output_mac += ":"
    return output_mac


if __name__ == "__main__":
    mac_input = input("What is you MAC Address? ")
    output_mac = mac_modifier(mac_input)
    print("Original MAC Address: ", mac_input)
    print("Corrected MAC Address: ", output_mac)
