#David Sebastian
password = []
encodedPasswordList=[]



def encode(password):
    for i in range (0, len(password)):
        encodedPasswordList.append(int(password[i])+3)
        encodedPasswordList[i]= str(encodedPasswordList[i])
    return ''.join(encodedPasswordList)




def main():
        x=1
        while x == 1:
            print("Menu")
            print("-------------")
            print("1. Encode")
            print("2. Decode")
            print("3. Quit")
            userChoice = input("Please enter an option:")
            if userChoice == "1":
                passwordStr = input("Please enter your password to encode:")
                password = list(passwordStr)
                encodedPassword = encode(password)
                print ("Your password has been encoded and stored!")
                print(encodedPassword)
           # if userChoice == "2":
             #   decode()
            if userChoice == "3":
                x=2









if __name__ == '__main__':
    main()
