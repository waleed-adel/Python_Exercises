import os   
import json

#Global Var. that is used to close the script and exits while loop
exit_flag = 0 

#this flag is used to indicate whether a match has been found successfully or not
found_flag = 0

#Global Var. that is used to determine whether a delete process took place successfully or not
remove_flag = 0

#this counter is for tracing the index of the found element inside list
#it's value changes inside Search Function
#starts from -1 so that when the loop enters first iteration it starts counting from 0
#otherwise it will give you the [index+1]    
count = -1

def listContacts():
  #writing global before the var allow the function to use the global var
  #instead of creatiion a local one
  global list 
  if len(list) > 0:
    print('\nContact List: ')
    for i in list:
      print(i)
  else:
    print('\nContact List = []')

def addContact(filename,name,number,email):
  f = open (filename,'a')
  dictConvertedToString = ''
  global list
  #increasing the list length by 1
  list = [i for i in range(len(list)+1)]
  #appending the contact info at last element of list
  list[len(list)-1] = {"Name": name,"Number": number,"Email": email}
  #converting list to a string with a special format before adding to the PhoneBook.txt File
  #this special format is used with json.loads() method which is used for converting string to a dictionary
  dictConvertedToString = '{"Name": '+ '"%s"'%(name) + ', "Number": ' + str(number) +', "Email": ' + '"%s"'%(email) + '}'
  dictConvertedToString =  "%s"%(dictConvertedToString)
  #listConvertedToString = '{"Name": name,"Number": number,"Email": email}'
  f.write(dictConvertedToString+'\n')
  f.close()

def removeContact (filename,index):
  f = open(filename,'r')
  file_lines = f.readlines()
  f.close()
  f = open(filename,'w')
  global remove_flag 
  remove_flag = 0
  dictConvertedToString = '{"Name": '+ '"%s"'%(list[index]["Name"]) + ', "Number": ' + str(list[index]["Number"]) +', "Email": ' + '"%s"'%(list[index]["Email"]) + '}'
  dictConvertedToString =  "%s"%(dictConvertedToString)
  for line in file_lines:
  #compare between each line in file but after stripping it (getting rid of) from '\n' 
  #present at the end of each line
    if line.strip('\n') != dictConvertedToString:
      f.write(line)
    else:
      remove_flag = 1    
  del list[index]    
  f.close()
  
  
def Search(filename,key):
  f = open(filename,'r')
  global found_flag
  found_flag = 0
  global count 
  #initialize count every time we use the search function
  count = -1
  global list
  
  if key == '1':
    name = input('\nPlease Enter A Name To Search For: ')
    for j in list:
      count += 1
      if j['Name'] == name:
        #just printing in a new line [mlhash lazma nadafa bs]
        print()
        print(j)
        found_flag = 1  
 
  elif key == '2':
    number = input('\nPlease Enter A Number To Search For: ')
    for j in list:
      count += 1
      if j['Number'] == int(number):
        print()
        print(j)
        found_flag = 1
      
  elif key == '3':
    email = input('\nPlease Enter An Email To Search For: ')
    for j in list:
      count += 1
      if j['Email'] == email:
        print()
        print(j)
        found_flag = 1
  else:
    print('\nInvalid Choice!!')
  
  if found_flag == 0 and key >= '1' and key <= '3':
    print('\nNOT FOUND!!')  
  f.close()      
  
  
while (exit_flag == 0):
  if os.path.exists('PhoneBook.txt'):
    f = open('PhoneBook.txt','r')
    list = [json.loads(i[:-1]) for i in f]
    f.close()
  else:
    phonebook_file = open ('PhoneBook.txt','w')
    list = []
    phonebook_file.close()
  
  print('\nPlease Choose An Option From Below: ')
  print('1- List Contacts\n2- Add Contact\n3- Remove Contact\n4- Search\n5- Exit')
  option = input('Enter A Number[1-5]: ')
  
  if option == '1':
    listContacts()
  
  elif option == '2': 
    name = input('\nPlease Enter A Name: ')
    number = int(input('Please Enter A Number: '))
    email = input('Please Enter An Email: ')
    addContact('PhoneBook.txt',name,number,email)  
    
  elif option == '3':
    if len(list) > 0:
      print('\nSearch For The Contact You Want To Remove by: ')
      print('1- Name\n2- Number\n3- Email')
      key = input('Enter A Number[1-3]: ')
      Search('PhoneBook.txt',key)  
      if found_flag == 1:
        removeContact('PhoneBook.txt',count)
        if remove_flag == 1:
          print('The Above Contact Has Been Removed Successfully')
        elif  remove_flag == 0:
          print('\nFailed To Remove!!')
      else:
        print('Couldn\'t Find A Match to remove!!')
    else:
      print('\nYou Cannot Remove From An Empty List!!')
  
  elif option == '4':
    if len(list) > 0:
      print('\n1- Name\n2- Number\n3- Email')
      key = input('Please Choose The Type Of Search You Want: ')
      Search('PhoneBook.txt',key)
    else:
      print('\nYou Cannot Search in an Empty List!!')
    
  elif option == '5':
    exit_flag = 1
    input('\n***Have A Nice Day***\n Press Enter To Exit')
  
  else:
    print('\nInvalid Choice!!')  