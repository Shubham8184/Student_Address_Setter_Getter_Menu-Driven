##.....Student Address Setter Getter Classes.......###


class Address:
    def getCity(self):
        return self.city
    def setCity(self,city):
        self.city=city

    def getPincode(self):
        return self.pincode
    def setPincode(self,pincode):
        self.pincode=pincode
        

class Student:
    def getRn(self):
        return self.rn
    def setRn(self,rn):
        self.rn=rn

    def getName(self):
        return self.name
    def setName(self,name):
        self.name=name

    def getMarks(self):
        return self.marks
    def setMarks(self,marks):
        self.marks=marks

    def getAddress(self):
        return self.address
    def setAddress(self,address):
        self.address=address

class AddressNotFound(Exception):
    def __init__(self,message):
        self.message=message

class StudentNotFound(Exception):
    def __init__(self,message):
        self.message=message
        
def address_list_check(list):
    if len(list)>0:
        return list
    else:
        raise AddressNotFound('Addresses are not present so please enter address 1st')
    
def student_list_check(list):
    if len(list)>0:
        return list
    else:
        raise StudentNotFound('Students are not present so please enter Students 1st')
'''
adr_list=[]
stu_list=[]

##a1=Address()
##a1.setCity('Pune')
##a1.setPincode(123456)
##print(a1.getCity())
##print(a1.getPincode()) 

while True:
    print('__Select__\n'
      '1. Address\n'
      '2. Student\n'
      '3. Exit')
    ch=int(input('Enter Your Choice:-'))
    if ch==1:
        while True:
            print('__Select__\n'
                  '1. Create Address\n'
                  '2. Update Address\n'
                  '3. Delete Address\n'
                  '4. Show Address\n'
                  '5. Exit')
            ch1=int(input('Enter Your Choice:-'))
            if ch1==1:
                n=int(input('How many address you want to enter:-'))
                for i in range(n):
                    a=Address()
                    a.setCity(str(input('Enter City:-')))
                    a.setPincode(int(input('Enter Pincode:-')))
                    adr_list.append(a)
                break
            elif ch1==2:
                if adr_list:
                    cit=input('Enter the City to Update:-')
                    for i in adr_list:
                        if cit==i.getCity():
                            i.setCity(str(input('Enter New City:-')))
                            i.setPincode(int(input('Enter New Pincode:-')))
                            break
                        else:
                            print('Please Enter the Valid City for Updation')
                else:
                    print('No data to Update Please Enter the Addresses 1st')
                break
            elif ch1==3:
                if adr_list:                   
                    cit=input('Enter the City to Delete:-')
                    for i in adr_list:
                        if cit==i.getCity():
                            adr_list.remove(i)
                            break
                    else:
                        print('Please Enter the Valid City for Updation')
                else:
                    print('No data to delete Please Enter the Addresses 1st')
                break
                
            elif ch1==4:
                if adr_list:
                    for i in adr_list:
                        city=i.getCity()
                        pincode=i.getPincode()
                        print(f'City:-{city},Pincode:-{pincode}')
                else:
                    print('No data to Show Please Enter the Addresses 1st')
                break
            elif ch1==5:
                print('Exit')
                break
            
            else:
                print('Please Enter Valid Choice')
            
            

    elif ch==2:
        if adr_list:
            print('__Select__\n'
              '1. Create Student\n'
              '2. Update Student\n'
              '3. Delete Student\n'
              '4. Show Student\n'
              '5. Exit')
            ch2=int(input('Enter Your Choice for Students:-'))
            while True:
                if ch2==1:
                    n=int(input('How many Student you want to enter:-'))
                    for i in range(n):
                        a=Student()
                        a.setRn(int(input('Enter Student Roll_No.:-')))
                        a.setName(str(input('Enter Student Name:-')))
                        a.setMarks(float(input('Enter Student Marks:-')))
                        #print(list(enumerate(adr_list,1)))
                        for i in adr_list:
                            print(i.getCity())
                        choice=str(input('Please Enter the City from above choices:-'))
                        for i in adr_list:
                            if i.getCity==choice:
                                a.setAddress(i)
                                break
                        stu_list.append(a)
                    print(stu_list)
                    break
                
                elif ch2==2:
                    if stu_list:
                        no=input('Enter the Roll_No to Update:-')
                        for i in stu_list:
                            if no==i.getRn():
                                i.setRn(int(input('Enter Student Roll_No.:-')))
                                i.setName(str(input('Enter Student Name:-')))
                                i.setMarks(float(input('Enter Student Marks:-')))
                                for i in adr_list:
                                        print(i.getCity())
                                choice=str(input('Please Enter the City from above choices:-'))
                                for j in adr_list:
                                    if j.getCity==choice:
                                        i.setAddress(j)
                                        break
##                        else:
##                            print('Please Enter the Valid Roll_No for Updation')
                    else:
                        print('No data to Update Please Enter the Students 1st')
                    break
                elif ch2==3:
                    if stu_list:                   
                        No=input('Enter the Roll_No to Delete:-')
                        for i in stu_list:
                            if No==i.getRn():
                                stu_list.remove(i)
                                break
                        else:
                            print('Please Enter the Valid Roll_No for Deletion')
                    else:
                        print('No data to delete Please Enter the Students 1st')
                    break
                    
                elif ch2==4:
                    if stu_list:
                        for i in stu_list:
                            roll_no=i.getRn()
                            name=i.getName()
                            marks=i.getMarks()
                            address=i.getAddress()
                            print(f'Student RollNo:-{roll_no}\nStudent Name:-{name}\nStudent Name:-{marks}\nStudent Address:-{address}\n\n')
                        break
                    else:
                        print('No data to Show Please Enter the Students 1st')
                    break
                elif ch2==5:
                    print('Exit')
                    break
                else:
                    print('Please Enter Valid Choice')
                
        else:
            print('No Addresses Present So Please Enter Address 1st')

            
    elif ch==3:
        print('Exit')
        break
    else:
        print('please Enter Valid Choice')
        
'''











