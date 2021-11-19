import sys
import fileinput
import os
class contact:
    def __init__(self, name, phone_num, address, dob):
        self.name = name
        self.phone_num = phone_num
        self.address = address
        self.dob = dob

if __name__=="__main__":


    EveryCon = input("Do you want to see all contacts available? Yes/No ")
    if EveryCon =='Yes':
        file = open("contactinfo.txt")
        lines = file.readlines()
        for line in lines:
            print (line)
        file.close()
    else:
        print("")


    Answer = input("Do you want to add another contact Yes/No ")
    while Answer == 'Yes':
        Con1 = contact(input(str("Enter your first name ")), input(str("Enter your phone number ")), input(str("Enter your address ")),
                       input(str("Enter your dob ")))
        print("Name: " + Con1.name)
        print("Phone Number: " + Con1.phone_num)
        print("Address: " + Con1.address)
        print("Date of Birth: " + Con1.dob)
        Answer = input("Do you want to add another contact Yes/No ")
        Info = "Name: " + Con1.name, "Phone Number: " + Con1.phone_num, "Address: " + Con1.address, "Date of Birth: " + Con1.dob
        file = open('contactinfo.txt', 'a')
        file.write('\n' + str(Info))
        file.close()
    else:
        print("No more contacts will be added")

        FindCon = input("Do you want to find a contacts' information? Yes/No ")
        while FindCon =='Yes':
            # reference for searchbar https://www.kite.com/python/answers/how-to-search-for-text-in-a-file-in-python
            ConName = input("What is the name of the contact you are looking for? ")
            Contact = open("contactinfo.txt")
            for line in Contact:
                if ConName in line:
                    print(line)
            FindCon = input("Do you want to find a contacts' information? Yes/No ")
        else:
            print("")


    DeleteCon = input("Do you want to delete a contact? Yes/No ")

    if DeleteCon == 'Yes':
        f = open("contactinfo.txt")
        NameChange = input("What is the Contact's name for which you want information to be changed? ")

        with open("contactinfo.txt", 'r') as file:
            lines = file.readlines()
        with open("contactinfo.txt", 'w') as file:
            for line in lines:
                if line.find(NameChange) != -1:
                    pass
                else:
                    file.write(line)
        DeleteCon = input("Do you want to delete a contact? Yes/No ")

    else:

        print("")

    ReplaceCon = input("Do you want to change a contacts' information? Yes/No ")
    while ReplaceCon =='Yes':
        ReplaceCon = input("What is the Contact's name for which you want information to be changed? ")



        contact = open("contactinfo.txt")
        for line in contact:
            if ReplaceCon in line:
                print(line)
        ReplaceConInfo1 = input("What do you want to change? Name/Phone Number/Address/DOB ")
        if ReplaceConInfo1 == ("Name"):
            NewName = input("What new name do you want to replace it with? ")
            with open("contactinfo.txt") as r:
                text = r.read().replace(ReplaceCon, NewName)
            with open("contactinfo.txt", "w") as w:
                w.write(text)
    else:
        print("Program closed")

        #if ReplaceConInfo1 == ("Phone Number"):

           # NewPhoneNum = input("What new number do you want to change it to? ")
            #with open("contactinfo.txt") as r:
               # text = r.read().replace(ReplaceCon, NewPhoneNum)
           # with open("contactinfo.txt", "w") as w:
               # w.write(text)







































