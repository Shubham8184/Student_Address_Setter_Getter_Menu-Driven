##........Student Address Menu Driven Program......###


from Student_Address_class import *


adr_list=[]
stu_list=[]

while True:
    print('__Select from Main Menu__\n'
      '1. Address\n'
      '2. Student\n'
      '3. Exit')
    ch=int(input('Enter Your Choice form above choices:-'))
    if ch==1:
        while True:
            print('\n__Select form Address Menu__\n'
                  '1. Create Address\n'
                  '2. Update Address\n'
                  '3. Delete Address\n'
                  '4. Show Address\n'
                  '5. Exit')
            ch1=int(input('\nEnter Your Choice from above choices for Address:-'))
            if ch1==1:
                n=int(input('\nHow many address you want to enter:-'))
                for i in range(n):
                    a=Address()
                    a.setCity(str(input('Enter City:-')))
                    a.setPincode(int(input('Enter Pincode:-')))
                    adr_list.append(a)
                
            elif ch1==2:
                try:
                    address_list_check(adr_list)
##                if adr_list:
                    for i in adr_list:
                        city=i.getCity()
                        pincode=i.getPincode()
                        print(f'City:-{city},Pincode:-{pincode}')
                    pin=int(input('\nEnter the Pincode to Update:-'))
                    for i in adr_list:
                        if pin==i.getPincode():
                            i.setCity(str(input('Enter New City:-')))
                            i.setPincode(int(input('Enter New Pincode:-')))
                            print('Address is Update successfullyy....!!!')
                            
                except AddressNotFound as e:
                    print(e)
                            
##                else:
##                    print('No data to Update Please Enter the Addresses 1st')
                
            elif ch1==3:
                try:
                    address_list_check(adr_list)
##                if adr_list:
                    for i in adr_list:
                        city=i.getCity()
                        pincode=i.getPincode()
                        print(f'City:-{city},Pincode:-{pincode}')
                    pin=int(input('\nEnter the Pincode to Delete:-'))
                    for i in adr_list:
                        if pin==i.getPincode():
                            adr_list.remove(i)
                            print('Address is delete successfullyy....!!!')
                            
                except AddressNotFound as e:
                    print(e)
##                else:
##                    print('No data to delete Please Enter the Addresses 1st')
                
                
            elif ch1==4:
                try:
                    address_list_check(adr_list)
##                if adr_list:
                    print('\n')
                    for i in adr_list:
                        city=i.getCity()
                        pincode=i.getPincode()
                        print(f'City:-{city},Pincode:-{pincode}')
                except AddressNotFound as e:
                    print(e)
##                else:
##                    print('No data to Show Please Enter the Addresses 1st')
                
            elif ch1==5:
                print('Exit')
                break
            
            else:
                print('Please Enter Valid Choice')
            
            

    elif ch==2:
        try:
            address_list_check(adr_list) 
##        if adr_list:
            while True:
                print('\n__Select from Student Menu__\n'
                      '1. Create Student\n'
                      '2. Update Student\n'
                      '3. Delete Student\n'
                      '4. Show Student\n'
                      '5. Show Student By Descending Marks\n'
                      '6. Exit')
                ch2=int(input('\nEnter Your Choice form above choices for Students:-'))
                if ch2==1:
                    n=int(input('\nHow many Student you want to enter:-'))
                    for i in range(n):
                        a=Student()
                        a.setRn(int(input('Enter Student Roll_No.:-')))
                        a.setName(str(input('Enter Student Name:-')))
                        a.setMarks(float(input('Enter Student Marks:-')))
                        #print(list(enumerate(adr_list,1)))
                        print('\n')
                        while True:
                            for i in adr_list:
                                print(f'City:- {i.getCity()}, Pincode:-{i.getPincode()}')

                            print('\nDo you want to insert Address From above Addresses:-\n'
                                  '1.Yes\n'
                                  '2.No\n'
                                  '3.Exit')
                            ch3=int(input('\nEnter Your Choice form above choices for Student Address Insertion:-'))
                            if ch3==1:
                                choice=int(input('\nPlease Enter the Pincode from above choices:-'))
                                for i in adr_list:
                                    if i.getPincode()== choice:
                                        a.setAddress(i)
                                        stu_list.append(a)
                                        print('\nStudent Address is enter Successfully....>>Now Exit it')
                                else:
                                    print('\nPlease enter the valid Pincode from choices')
                                 
                            elif ch3==2:
                                b=Address()
                                x=str(input('Enter City:-'))
                                y=int(input('Enter Pincode:-'))
                                b.setCity(x)
                                b.setPincode(y)
                                for i in adr_list:
                                    if i.getPincode() == y:
                                        print('\nOppss...You Entered Address is already Present')
                                        
                                    else:
                                        adr_list.append(b)
                                        for i in adr_list:
                                            if i.getPincode()== y:
                                                a.setAddress(i)
                                                stu_list.append(a)
                                                print('\nStudent Address is enter Successfully....>>Now Exit it')
                                        break
                                    
                            elif ch3==3:
                                print('Exit')
                                break
                            else:
                                print('Please Provide valid Choice')
                                
                            
                                
                elif ch2==2:
                    try:
                        student_list_check(stu_list)  
##                    if stu_list:
                        no=int(input('\nEnter the Roll_No to Update:-'))
                        for i in stu_list:
                            if no==i.getRn():
##                                i.setRn(int(input('Enter Student Roll_No.:-')))
##                                i.setName(str(input('Enter Student Name:-')))
##                                i.setMarks(float(input('Enter Student Marks:-')))
##                                for i in adr_list:
##                                        print(i.getCity())
##                                choice=str(input('Please Enter the City from above choices for updation:-'))
##                                for j in adr_list:
##                                    if j.getCity==choice:
##                                        i.setAddress(j)
##                                        print('Student is Update successfullyy....!!!')
                                while True:
                                    for i in adr_list:
                                        print(f'City:- {i.getCity()}, Pincode:-{i.getPincode()}')

                                    print('\nDo you want to insert Address From above Addresses:-\n'
                                          '1.Yes\n'
                                          '2.No\n'
                                          '3.Exit')
                                    ch3=int(input('\nEnter Your Choice form above choices for Student Address Insertion:-'))
                                    if ch3==1:
                                        choice=int(input('\nPlease Enter the Pincode from above choices:-'))
                                        for i in adr_list:
                                            if i.getPincode()== choice:
                                                a.setAddress(i)
                                                stu_list.append(a)
                                                print('\nStudent Address is Update Successfully....>>Now Exit it')
                                        else:
                                            print('\nPlease enter the valid Pincode from choices')
                                         
                                    elif ch3==2:
                                        b=Address()
                                        x=str(input('Enter City:-'))
                                        y=int(input('Enter Pincode:-'))
                                        b.setCity(x)
                                        b.setPincode(y)
                                        for i in adr_list:
                                            if i.getPincode() == y:
                                                print('\nOppss...You Entered Address is already Present')
                                                
                                            else:
                                                adr_list.append(b)
                                                for i in adr_list:
                                                    if i.getPincode()== y:
                                                        a.setAddress(i)
                                                        stu_list.append(a)
                                                        print('\nStudent Address is Update Successfully....>>Now Exit it')
                                                break
                                            
                                    elif ch3==3:
                                        print('Exit')
                                        break
                                    else:
                                        print('Please Provide valid Choice')
    ##                                        
    ####                    else:
##                            print('Please Enter the Valid Roll_No for Updation')
                    except StudentNotFound as e:
                        print(e)
##                    else:
##                        print('No data to Update Please Enter the Students 1st')
                    
                    
                elif ch2==3:
                    try:
                        student_list_check(stu_list)
##                    if stu_list:                   
                        No=int(input('\nEnter the Roll_No to Delete:-'))
                        for i in stu_list:
                            if No==i.getRn():
                                stu_list.remove(i)
                                print('Student is delete successfullyy....!!!')
                                
##                        else:
##                            print('Please Enter the Valid Roll_No for Deletion')
                            
                    except StudentNotFound as e:
                        print(e)
##                    else:
##                        print('No data to delete Please Enter the Students 1st')
                        
                    
                    
                elif ch2==4:
                    try:
                        student_list_check(stu_list)
##                    if stu_list:
                        print('\n')
                        for i in stu_list:
                            roll_no=i.getRn()
                            name=i.getName()
                            marks=i.getMarks()
                            address=i.getAddress()
                            print(f'Student RollNo:-{roll_no}\nStudent Name:-{name}\nStudent Name:-{marks}\nStudent Address:-{address}\n\n')
                            
                    except StudentNotFound as e:
                        print(e)
  
##                    else:
##                        print('No data to Show Please Enter the Students 1st')
                        
                elif ch2==5:
                    try:
                        student_list_check(stu_list)
##                    if stu_list:
                        print('\n')
                        mark_list=stu_list.copy()
                        mark_list.sort(key=lambda x: x.getMarks(), reverse=True)
                        for i in mark_list:
                            print(f'Student Marks:-{i.getMarks()}\nStudent Name:-{i.getName()}\nStudent Roll No:-{i.getRn()}\nStudent Address:-{i.getAddress()}\n')
                            
                    except StudentNotFound as e:
                        print(e)
##                    else:
##                        print('No data to Show Please Enter the Students 1st')
                        
                elif ch2==6:
                    print('Exit')
                    break
                    
                else:
                    print('Please Enter Valid Choice')
        except AddressNotFound as e:
            print(e)
            
        
##        else:
##            print('No Addresses Present So Please Enter Address 1st')

            
    elif ch==3:
        print('Exit')
        break
    else:
        print('please Enter Valid Choice')
