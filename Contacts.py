import sys

class contact:
    def __init__(self, name, phone_num, address):
        self.name = name
        self.phone_num = phone_num
        self.address = address

if __name__=="__main__":
    con1 = contact(input("Enter your first name "), input("Enter your phone number "), input("Enter your address "))
    print("Age: " + con1.name)
    print("Phone Number: " + con1.phone_num)
    print("Address: " + con1.address)









