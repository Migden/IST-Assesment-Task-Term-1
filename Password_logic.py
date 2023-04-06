import math

def symbol_check(password): ### Get ratio of number of symbols to length and compares to the average password average and returns the difference -5 out of 5
    number_of_symbols = 0
    symbols = "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
    for symbol in password:
        if symbol in symbols:
            number_of_symbols += 1
    average_ratio_of_symbols = 0.1875
    ratio =  float((number_of_symbols / len(password)))
    if number_of_symbols == 0:
        return 0
    if ratio <= average_ratio_of_symbols:
        difference = average_ratio_of_symbols - ratio
        if difference == 0:
            return 5
        else:
            result = (5 - (5 * difference))
            return result
    else:
        result = ratio - average_ratio_of_symbols
        return (5 - (5 * result))

def length_check(length): ## If length is over 16 return 5 else return length compared to standard length
    pass_standard = 16
    if length > pass_standard:
        return 5
    return float((5 * (length / pass_standard)))


def upper_case_to_lower_case_check(password): ## gets average ratio of uppercase to lowercase and rates out of 5
    number_of_symbols = 0
    for symbol in password:
        if symbol.isupper() == False and symbol.islower() == False:
            number_of_symbols += 1
    length = (len(password) - number_of_symbols)
    upper_case = 0
    lower_case = 0
    for item in password:
        if item.isupper():
            upper_case += 1
        elif item.islower():
            lower_case += 1
    if (upper_case + lower_case) == 0:
        return 0
    if upper_case > lower_case:
        numb = upper_case - lower_case
        result = 5 - ((5 * float(upper_case / (length))) * (numb / upper_case))
        return result
    return ((5 * float(upper_case / (length)))) * 2

def password_rating(password): ## acessed by main function, it returns value out of 15 from supplied password
    if len(password) > 200:
        return 15
    elif len(password) > 0:
        return math.trunc((upper_case_to_lower_case_check(password) + length_check(len(password)) + symbol_check(password)))
    else:
        return 0
    
