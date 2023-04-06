import string
import random
import pyperclip

def copy_to_clipboard(text): ### Copies to user clipboar
    pyperclip.copy(text)  

def generate_password(length, numbers, symbols, uppercase): ### Takes in supplied options and generates password with selected options
    password = ""
    unselected = {"numb": numbers, "symb": symbols, "upprcs": uppercase}
    values = {"numb": string.digits, "symb": string.punctuation, "upprcs": string.ascii_uppercase, "lwrcs": string.ascii_lowercase}
    selected = []
    for i in unselected:
        if unselected[i] == True:
            selected.append(i)
    for i in selected:
        password += values[i]
    password += values["lwrcs"]
    password = ''.join(random.choice(password) for i in range(0, length))
    return password


