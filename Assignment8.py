import os

directory_path = input("Please enter the path where you would like to save your file: ")
filename = input("Please enter the file name: ")
#check directory exists
if(os.path.exists(directory_path)):

    with open(directory_path + "/" + filename, 'a') as file_object:
        name = input("Please enter your name: ")
        address = input("Please enter your address on one line: ")
        phone_number= input("Please enter your phone number: ")
        contact = ("Name: " + (name) + "\nAddress: " + (address) + "\nPhone Number: " + (phone_number) + "\n\n")
        file_object.write(contact)
        file_object.close()

else:
    print("Directory does not exists")

with open(directory_path + "/" + filename, 'r') as file_object:
    for line in file_object:
            print(line)
