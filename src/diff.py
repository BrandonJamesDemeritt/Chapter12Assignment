'''
Created on Nov 29, 2022

@author: Brandon Demeritt
'''

cont = True

while cont:
    userfile1 = input("Please enter first filename: ")
    userfile2 = input("Please enter second filename: ")
    file1 = open(userfile1)
    file2 = open(userfile2)
    for line in file1:
        file1contents = line.split('\n')
    for line in file2:
        file2contents = line.split('\n')        
    for item in range(len(file1contents)):
        if file1contents[item] != file2contents[item]:
            print("No")
            print(file1contents[item])
            print(file2contents[item])
            cont = False
            break
        else:
            print("Yes")
    