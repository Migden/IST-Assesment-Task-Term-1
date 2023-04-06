import pwnedpasswords
import math

def check_number_of_leaked_passwords(password):
    ## Parse in string, integer number of passwords found in known password database is returned
    try:
        result = pwnedpasswords.check(password, plain_text=True)
    except:
        return 0
    return int(result)  

def check_blacklist(password):
    ## Takes in password, returns Boolean of True when password found in blacklist, and False if password not in Blacklist
    file = open("rockyou.txt","r",encoding='utf-8',errors='ignore')
    found = False

    for items in file:  ### Loops through file and tests for blacklisted password
        if str(items.strip()) == password:
            found = True
            file.close()
            return found
    
    file.close()
    return found


def check_password_sample_space(password):
    if len(password) > 150:
        return "Number to Big"
    ## Parse in a string, the result is returned as a float of days to crack password

    length = len(password)
    cps = 300000 ## average password guesses per second by a PC with average specs

    ## Measure complexity using S = C ^ N, where S is number of possible attempt, C is number of characters in the character pool, and N is the length of the password
    
    c = 0
    symbol_c = True
    digits_c = True
    upper_c = True
    lower_c = True
    symbols = "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
    digits = "1234567890"
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    ### Filters through password and add value of any symbol, digit, and letter
    for item in password:
        if item in symbols and symbol_c == True:
            c += len(symbols)
            symbol_c = False
        elif str(item) in str(digits) and digits_c == True:
            c += len(digits)
            digits_c = False
        elif item in alphabet and upper_c == True:
            c += len(alphabet)
            upper_c = False
        elif item in alphabet.lower() and lower_c == True:
            c += len(alphabet)
            lower_c = False

    cracks_in_days = float((float((pow(c, len(password)) / cps))) / 86400)  ## Returns amount of days to crack the password in exponetional notation
    return "{:e}".format(math.trunc(cracks_in_days))