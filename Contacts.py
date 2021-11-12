import sys
import fileinput
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
        print("Name: " + con1.name)
        print("Phone Number: " + con1.phone_num)
        print("Address: " + con1.address)
        print("Date of Birth: " + con1.dob)
        answer = input("Do you want to add another contact Yes/No ")
        Info = "Name: " + con1.name, "Phone Number: " + con1.phone_num, "Address: " + con1.address, "Date of Birth: " + con1.dob
        file = open('contactinfo.txt', 'a')
        file.write('\n' + str(Info))
        file.close()
    else:
        print("No more contacts will be added")

        findcon = input("Do you want to find a contacts' information? Yes/No ")
        while findcon =='Yes':
            # reference for searchbar https://www.kite.com/python/answers/how-to-search-for-text-in-a-file-in-python
            conname = input("What is the name of the contact you are looking for? ")
            contact = open("contactinfo.txt")
            for line in contact:
                if conname in line:
                    print(line)

        else:
            print("Program completed")

        replacecon = input("Do you want to change a contacts' information? Yes/No ")
        while replacecon =='Yes':
            replacecon = input("What is the Contact's name for which you want information to be changed? ")
            #if input == (open("contactinfo.txt", conname)):


        contact = open("contactinfo.txt")
        for line in contact:
            if replacecon in line:
                print(line)
        replaceconinfo1 = input("What do you want to change? Name/Phone Number/Address/DOB ")
        if replaceconinfo1 == ("Name"):
            newname = input("What new name do you want to replace it with?")
            with open("contactinfo.txt") as r:
                text= r.read().replace(replacecon, newname)
            with open("contactinfo.txt", "w") as w:
                w.write(text)



            #file = open("contactinfo.txt")
            #for line in file:
                #file.write(line.replace(ConInfo))
                #file.close()

            #def replace_in_file(contactinfo, search_text, new_text):
                #with fileinput.input(contactinfo, inplace=True) as f:
                    #for line in f:
                        #new_line = line.replace(search_text, new_text)
                        #print(new_line, end='')

else:
     print("Program closed")


































