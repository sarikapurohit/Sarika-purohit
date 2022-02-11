print("Welcome on Cryptography machine." + " Ready to use!")

mode = input("choose your mode Encryption(E), Decryption(D)")
if mode.upper() == 'E': 
    def encryption():
        msg = input("Enter your Message : ")
        key ='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ !?,.-'
        value = key[-1]+ key[0:-2]
        dictonary = dict(zip(key,value))
        for i in range(len(msg)):
            res = dictonary[msg[i]]
            print(res,end="")
    encryption()

elif mode.upper() == 'D': 
    def Decryption(): 
        msg = input("Enter your Encrypted Message: ")
        key ='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ !?,.-'
        value = key[-1]+ key[0:-1]
        dictonary = dict(zip(value,key))
        for i in range(len(msg)):
            res = dictonary[msg[i]]
            print(res,end="")
    Decryption()
else: 
    print("Invalid Command!")

