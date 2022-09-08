

def tic_tac_toe():
   map[3][3]=-1
   print("you will insert two values row and col ")
   i=0
   while(i<9):
    row=0
    col=0
    loopend=1
   take_input()
   if(i%2==1):
     map[row][col]=0
   else:
     map[row][col]=1
   if(i==9):
    win1 = check_rows(map)
    win2 = check_cols(map)
    win3 = check_diags(map)
    if(win1==0 and win2==0 and win3==0):
     print("draw")




def take_input():
 while (loopend):
  loopend = 0
  row = input()
  col = input()
  if (row > 2 or col > 2 or row < 0 or col < 0):
   print("invalid input")
   loopend = 1
  if (map[row][col] != -1):
   print("already taken")
   loopend = 1

def check_rows(map):
    for i in range(3):
       if(map[i][1]==map[i][2] and map[i][1]==map[i][3]):
          if(map[i][1]==0):
           print("0 wins ")
          elif(map[i][1]==1):
           print("x wins")
       return 1


def check_cols(map):
 for i in range(3):
  if (map[1][i] == map[2][i] and map[1][i] == map[3][i]):
   if (map[1][i] == 0):
    print("0 wins ")
    return 1
   elif(map[1][i]==1):
    print("x wins")
    return 1

def check_diags(map):
 first=1
 second=2
 third=3
 if(map[first][first]==map[second][second] and map[second][second]==map[third][third]):
   if(map[first][first]==1):
     print("x wins")
   elif(map[first][first]==0):
    print("0 wins")
    return 1
 elif(map[first][third]==map[second][second] and map[second][second]==map[third][first]):
  if (map[first][first] == 1):
   print("x wins")
  elif (map[first][first] == 0):
   print("0 wins")
   return 1
