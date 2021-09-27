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












