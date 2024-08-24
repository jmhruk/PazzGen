import random
import string

def gen(l, upper, num, nnum, snum, sym):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    
    normal = int(l - (nnum+snum))
    password = ""
    for x in range(nnum):
        password += random.choice(numbers)

    for x in range(snum):
        password += random.choice(symbols)
    
    for x in range(normal):
        if upper.lower() == "yes":
            if random.randint(1,2) == 2:
                password += random.choice(letters).upper()
            else:
                password += random.choice(letters).lower()

    
    stri = list(password)
    random.shuffle(stri)
    result = ''.join(stri)
    return result
        
nnum = 0
nsymbols = 0

print("Welcome to the Password Generator!")
length = int(input("Please enter the length of password you would like to generate: "))
uppercase = str(input("Would you like to include uppercase letters?: "))
numbers = str(input("Would you like to include numbers?: "))
if numbers.lower() == "yes":
    nnum = int(input("How many numbers would you like to include?"))
symbols = str(input("Would you like to include symbols?: "))
if symbols.lower() == "yes":
    nsymbols = int(input("How many symbols would you like to include?"))

print(gen(length, uppercase,numbers, nnum, nsymbols, symbols))

