def isPhoneNumber(text):
    if len(text)!=12:
        return False
    for i in range(0,3):
        if not text[i].isdecimal():
            return False
        if text[3]!='-':
            return False
        for i in range(4,7):
            if not text[i].isdecimal():
                return False
        if text[7]!='-':
            return False
        for i in range(8,12):
            if not text[i].isdecimal():
                return False
        return True

text=input("Please Enter a 12-digit phone number:")
if isPhoneNumber(text):
    print("Valid Phone Number")
else:
    print("Not a valid Phone number")

         
        
            
