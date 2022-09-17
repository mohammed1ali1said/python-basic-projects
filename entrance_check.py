import time
from datetime import datetime

class teachers:
    enter_time=0
    exit_time=0
    entrance=0
    exit=0
    def __init__(self,name='no_name',ID='123456789'):
      self.__name=name
      if(len(ID)==9):
        self.__ID=ID


    def getentrance(self):
        return self.entrance
    def getexit(self):
        return self.exit
    def getid(self):
        return self.__ID

    def getname(self):
        return self.__name

    def setname(self,name):
        self.__name=name
    def setid(self,id):
        if(len(id)==9):
            self.__ID=id

    def setentrance(self):
        print((self.__name+"  " +"enter"))
        self.entrance=1
        self.exit=0
        self.enter_time= time.time()

    def setexit(self):
        print(self.__name+"  "+"exit")
        self.exit=1
        self.entrance=0
        self.exit_time = time.time()
        time_spent=(self.exit_time-self.enter_time)
        print("time spent=")
        print(time_spent)


    def __eq__(self,other):
        if(self.__name==other.__name and self.__ID==other.__ID):
            return 1

print("this is the filling process where you need to enter manually all teachers names and ID ")
mylist=list()
for i in range(2):
    print("enter name and then enter ID")
    mylist.append(teachers(input(),input()))
i=0
now=datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)
while 1==1:
   print("enter name")
   name = input()
   print("enter ID")
   ID = input()
   teacherenter=teachers(name,ID)
   if(teacherenter in mylist):
    index=mylist.index(teacherenter)
    print(index)
    if(mylist[index].getentrance()==1):
      mylist[index].setexit()
      continue

    if(mylist[index].getentrance()==0):
          mylist[index].setentrance()
   else:
       print("invalid teachers verifications")






