def Register(i:list,p:list)->any:
    """
    i=login
    p=parol
    
    """
    i=input("Create a Login:")
    p=input("Create a Password:")
    p2=input("Repeat your Password:")
    x=0
    while p2!=p:
        x+=1
        print("Looks like you forgot your password\nTry again:")
        p2=input("Repeat your Password:")
        if x==2:
            print("Your password confirmation attempts have ended")
            break
    l1=input("What do you like?\n(This word will be needed for account recovery)")
    print("Thanks for Creating your Account!")
    print("Welcome!",i+"!")
    return i,p,l1

def change(i,l1):
    l2=input("Input your Word of Recovery: ")
    if l2!=l1:
        i=input("Enter new login: ")
        print("Login successfully changed.")
    else:
        print("Recover word Not the same as when you signed up ")
    return i

def password(p,code):
    
    p=input("Enter new password: ")
    print("Password successfully changed.")
    return p


    