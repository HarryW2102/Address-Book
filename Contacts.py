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
        con1 = contact(input(str("Enter your first name ")), input(str("Enter your phone number ")), input(str("Enter your address ")),
                       input(str("Enter your dob ")))
        print("Age: " + con1.name)
        print("Phone Number: " + con1.phone_num)
        print("Address: " + con1.address)
        print("Date of Birth: " + con1.dob)
        answer = input("Do you want to add another contact Yes/No ")
    else:
        print("No more contacts will be added")

        Info = "Age: " + con1.name, "Phone Number: " + con1.phone_num, "Address: " + con1.address, "Date of Birth: " + con1.dob

        file = open('contactinfo.txt','a')
        file.write('\n' +str(Info))
        file.close()























