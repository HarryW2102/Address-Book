# Address-Book
## Project Overview:

* This application allows a user to access and manipulate contact information via 'Yes/No' inputs from an external file that contains a contact's name , address, phone number and date of birth that has been previously saved there.
* The application can list all the contacts and their details for the user to see by retrieving it from the .txt file
* It can also add  contacts by allowing the user to type in their answers to the questions provided
* There is also code that allows the user to look up a contact's information by only inputting the contact's name that they want finding 
    
`ConName = input("What is the name of the contact you are looking for? ")
           Contact = open("contactinfo.txt")
            for line in Contact:
                if ConName in line:
                    print(line)`
* The application can also edit contact information. It can do this by either completely deleting a contact's details from the file or by changing just the name of a particular contact.




## Assumptions:
  
* I assumed the inputs are valid and not erroneous sets of data  meaning for inputs like the contact's phone number, letters could be technically inputted as I have coded it as a string.
* The inputs are case-sensitive 
* I have stored birthdays as a string and not in the date format but the user can do this themselves

## How to run:

* The application was done through python version 3.7 and can be run through the python terminal as it only uses a .txt file to store contact information to the memory.

## Use Case:

For example a way for the user to add a contact is through the code 
`Answer = input("Do you want to add another contact Yes/No ")
    while Answer == 'Yes':`
The user will than either type 'Yes' or 'No' (case-sensitive) and then they input answers to each statement shown below.

`
        Con1 = contact(input(str("Enter your full name ")), input(str("Enter your phone number ")), input(str("Enter your address ")),
                       input(str("Enter your dob ")))`

The user enters their inputs to each statement , it will be set out with each attribute than their answer and saved to the .txt file. This can be seen through the code


`Info = "Name: " + Con1.name, "Phone Number: " + Con1.phone_num, "Address: " + Con1.address, "Date of Birth: " + Con1.dob
        file = open('contactinfo.txt', 'a')
        file.write('\n' + str(Info))
        file.close()`

This can happen because I have previously made a class called 'contact' and so a value can be linked to each attribute.
