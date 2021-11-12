#!/usr/bin/env python3

#print(random.choice(a,a=user_input))
#b=random.choices(list(a),k=user_input))
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print('''  ██████ ▓█████  ▄████▄   █    ██  ██▀███  ▓█████  ██▓███   ▄▄▄        ██████   ██████  ██▓███ ▓██   ██▓
▒██    ▒ ▓█   ▀ ▒██▀ ▀█   ██  ▓██▒▓██ ▒ ██▒▓█   ▀ ▓██░  ██▒▒████▄    ▒██    ▒ ▒██    ▒ ▓██░  ██▒▒██  ██▒
░ ▓██▄   ▒███   ▒▓█    ▄ ▓██  ▒██░▓██ ░▄█ ▒▒███   ▓██░ ██▓▒▒██  ▀█▄  ░ ▓██▄   ░ ▓██▄   ▓██░ ██▓▒ ▒██ ██░
  ▒   ██▒▒▓█  ▄ ▒▓▓▄ ▄██▒▓▓█  ░██░▒██▀▀█▄  ▒▓█  ▄ ▒██▄█▓▒ ▒░██▄▄▄▄██   ▒   ██▒  ▒   ██▒▒██▄█▓▒ ▒ ░ ▐██▓░
▒██████▒▒░▒████▒▒ ▓███▀ ░▒▒█████▓ ░██▓ ▒██▒░▒████▒▒██▒ ░  ░ ▓█   ▓██▒▒██████▒▒▒██████▒▒▒██▒ ░  ░ ░ ██▒▓░
▒ ▒▓▒ ▒ ░░░ ▒░ ░░ ░▒ ▒  ░░▒▓▒ ▒ ▒ ░ ▒▓ ░▒▓░░░ ▒░ ░▒▓▒░ ░  ░ ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░▒ ▒▓▒ ▒ ░▒▓▒░ ░  ░  ██▒▒▒ 
░ ░▒  ░ ░ ░ ░  ░  ░  ▒   ░░▒░ ░ ░   ░▒ ░ ▒░ ░ ░  ░░▒ ░       ▒   ▒▒ ░░ ░▒  ░ ░░ ░▒  ░ ░░▒ ░     ▓██ ░▒░ 
░  ░  ░     ░   ░         ░░░ ░ ░   ░░   ░    ░   ░░         ░   ▒   ░  ░  ░  ░  ░  ░  ░░       ▒ ▒ ░░  
      ░     ░  ░░ ░         ░        ░        ░  ░               ░  ░      ░        ░           ░ ░     
                ░                                                                               ░ ░  ''')


print("Welcome to the SecurePassPy Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
#this is probably secured way because no one guess which will come first
password=[]
for passwd in range(1,nr_letters+1):
    password+=random.choice(letters)
    
for passwd in range(1,nr_symbols+1):
    password+=random.choice(numbers)
    
for passwd in range(1,nr_numbers+1):
    password+=random.choice(symbols)
    
random.shuffle(password)
#print(password)
final = ""

for passwd in password:
    final+=passwd
print(f"Your super secure passwd is {final}")

#this is insecure way to genrate password because we have predectable output that first will be letter then sybmbol then number
#password=""
#for passwd in range(1,nr_letters+1):
 #   random_char=random.choice(letters)
  #  password=password+random_char
#print(password)
#for passwd in range(1,nr_symbols+1):
 #   random_char=random.choice(numbers)
 #   password+=random_char
#print(password)
#for passwd in range(1,nr_numbers+1):
 #   random_char=random.choice(symbols)
 #   password+=random_char
#print(password)
 

