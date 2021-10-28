import sys

class contact:
    def __init__(self, name, phone_num, address, dob):
        self.name = name
        self.phone_num = phone_num
        self.address = address
        self.dob = dob

if __name__=="__main__":

    answer = input("Do you want to add another contact Yes/No ")
    while answer == 'Yes':
        con1 = contact(input("Enter your first name "), input("Enter your phone number "), input("Enter your address "),
                       input("Enter your dob "))
        print("Age: " + con1.name)
        print("Phone Number: " + con1.phone_num)
        print("Address: " + con1.address)
        print("Date of Birth: " + con1.dob)
        answer = input("Do you want to add another contact Yes/No ")
    else:
        print("No more contacts will be added")



    file = open('contactinfo.txt','a')
    file.write('\n' + str(contact))
    file.close()
    






















