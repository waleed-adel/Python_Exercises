import os

#global var. so that it can be used in any function
Driver_Name = ''
path = ''
abst_layer = ''

#this function is the one responsible for creating the files inside driver folder
def createDriverFiles(path): 
  if path == '1' or path == '2':   
    if abst_layer.upper() == 'MCAL' or abst_layer.upper() == 'HAL':
      #create directory if path is at same directory since i didn't create it from the first place
      #if path == '2', we won't have to create directory because we already created it above
      if path == '1':
        os.mkdir(Driver_Name.upper())
        os.chdir('./%s' %(Driver_Name))
      
      if abst_layer.upper() == 'MCAL': 
        f = open (Driver_Name.upper()+'_register.h','w')
        f.write('/********************************/\n')
        f.write('/*Author	:	Waleed Adel	        */\n')
        f.write('/*Version :   	  				      */\n')
        f.write('/*Date		:	          		      */\n')
        f.write('/********************************/\n\n')
        f.write('#ifndef %s_REGISTER_H\n'%(Driver_Name.upper()))
        f.write('#define %s_REGISTER_H\n'%(Driver_Name.upper()))
        f.write('#endif')
      
      f = open (Driver_Name.upper()+'_interface.h','w')
      f.write('/********************************/\n')
      f.write('/*Author	:	Waleed Adel	        */\n')
      f.write('/*Version :   	  				      */\n')
      f.write('/*Date		:	          		      */\n')
      f.write('/********************************/\n\n')
      f.write('#ifndef %s_INTERFACE_H\n'%(Driver_Name.upper()))
      f.write('#define %s_INTERFACE_H\n'%(Driver_Name.upper()))
      f.write('#endif')
      
      f = open (Driver_Name.upper()+'_program.c','w')
      f.write('#include "STD_TYPES.h"\n')
      f.write('#include "BIT_MATH.h"\n')
      f.write('#include "%s_interface.h"\n'%(Driver_Name.upper()))
      f.write('#include "%s_private.h"\n'%(Driver_Name.upper()))
      if abst_layer.upper() == 'MCAL':
        f.write('#include "%s_register.h"\n'%(Driver_Name.upper()))
      f.write('#include "%s_config.h"\n'%(Driver_Name.upper()))
      
      f = open (Driver_Name.upper()+'_config.h','w')
      f.write('/********************************/\n')
      f.write('/*Author	:	Waleed Adel	        */\n')
      f.write('/*Version :   	  				      */\n')
      f.write('/*Date		:	          		      */\n')
      f.write('/********************************/\n\n')
      f.write('#ifndef %s_CONFIG_H\n'%(Driver_Name.upper()))
      f.write('#define %s_CONFIG_H\n'%(Driver_Name.upper()))
      f.write('#endif')
      
      f = open (Driver_Name.upper()+'_private.h','w')
      f.write('/********************************/\n')
      f.write('/*Author	:	Waleed Adel	        */\n')
      f.write('/*Version :   	  				      */\n')
      f.write('/*Date		:	          		      */\n')
      f.write('/********************************/\n\n')
      f.write('#ifndef %s_PRIVATE_H\n'%(Driver_Name.upper()))
      f.write('#define %s_PRIVATE_H\n'%(Driver_Name.upper()))
      f.write('#endif')
      
    else:
      print('\nInvalid Abstraction Layer!!')
      input('Press Enter to Exit')

Driver_Name = input("Please Enter Driver Name: ")
print("\nWhere Do you Want to Put it ?\n\n1- Current Directory Of The Running Script\n2- COTS\n")
path = input('Choose From The Above[1-2]: ')

#first, check on the path   
if path == '2':
  #choose an abstraction layer and check to see if the choice is available or not
  #here we have two choices only [MCAL] or [HAL]
  abst_layer = input("\nPlease Choose The Abstraction Layer, MCAL or HAL: ")
  if abst_layer.upper() == 'MCAL':
    #if the abst_layer is available then we must choose which uC file we want to place the driver in
    micro_Contoller = input("Please Choose the uC You Want, AVR or ARM: ")  
    if micro_Contoller.upper() == 'AVR':
      os.chdir (r'D:\COTS\01-%s\AVR' %(abst_layer.upper()))
      os.mkdir(Driver_Name.upper())
      os.chdir('./%s' %(Driver_Name))
      createDriverFiles(path)
    elif micro_Contoller.upper() == 'ARM': 
      os.chdir (r'D:\COTS\01-%s\ARM' %(abst_layer.upper()))
      os.mkdir(Driver_Name.upper())
      os.chdir('./%s' %(Driver_Name))
      createDriverFiles(path)
    else:
      print('\nInvalid MicroController!!!')
      input('Press Enter to Exit')  
  
  elif abst_layer.upper() == 'HAL': 
      os.chdir (r'D:\COTS\02-%s' %(abst_layer.upper()))
      os.mkdir(Driver_Name.upper())
      os.chdir('./%s' %(Driver_Name))
      createDriverFiles(path)
    
  else:
    print('\nInvalid Abstraction Layer!!')
    input('Press Enter to Exit')
    
elif path == '1':  
  #if the micro_Contoller or abst_layer doesn't exist
  #the folder will be made at the same path that the script is running in
  abst_layer = input("\nPlease Choose The Abstraction Layer, MCAL or HAL: ")
  createDriverFiles(path)

else:
  print('\nInvalid Path!!')
  input('Press Enter to Exit')


