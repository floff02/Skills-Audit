import random

def generate_pin():
    return random.randint(100, 999)

def find_pin(pin_attempt):
    if pin_attempt == pin:
        print("Correct PIN!")
        return True
    else:
        print("Incorrect PIN. Please try again.")
        return False



pin = generate_pin()
print("Your PIN is:", pin)

def forgot_pin():
    
    print("Your PIN is: ", pin)

pin_correct = False
while not pin_correct:
  
    pin_attempt = input("Enter your PIN or type 'forgot' to retrieve your PIN: ")
  
    if pin_attempt == "forgot":
        forgot_pin()
    else:
        pin_correct = find_pin(int(pin_attempt))

print("Access granted.")