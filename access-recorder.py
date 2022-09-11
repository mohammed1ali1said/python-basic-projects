from array import array
import time

class teachers:
    enter_time=0
    exit_time=0
    entrance=0
    exit=0
    def __init__(self,name='no_name',ID='123456789'):
      self.__name=name

      if(len(ID)==9):
          self.__ID=ID


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
        self.enter_time= time.time()

    def setexit(self):
        print(self.__name+"  "+"exit")
        self.exit=1
        self.exit_time = time.time()
        time_spent=self.exit_time-self.enter_time
        print("time spent=")
        print(time_spent)


    def __eq__(self,other):
        if(self.__name==other.__name and self.__ID==other.__ID):
            return 1


teacher2=teachers("myname2","myID2")
teacher3=teachers("myname3","myID3")
array= [teacher2,teacher3]
i=0
for i in range(2):
    print("enter name")
    name = input()
    print("enter ID")
    ID = input()
    teacher1=teachers(name,ID)
    if(teacher1==teacher2):
        teacher2.setentrance()
    if(teacher1==teacher3):
         teacher3.setentrance()


for i in range(2):
    print("enter name")
    name = input()
    print("enter ID")
    ID = input()
    teacher1=teachers(name,ID)
    if(teacher1==teacher2):
        teacher2.setexit()
    if(teacher1==teacher3):
         teacher3.setexit()



