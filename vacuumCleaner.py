def fullClean(rooms):
  for i in rooms:
      if(i == "D"):
        return False
  return True


def clean_room():
  n = int(input("Enter number of rooms : "))
  rooms = ["D"]*n
  v = int(input("Enter the starting room"))
  v = v-1
  flag = False
  while not fullClean(rooms):
    if(rooms[v] == "D"):
      rooms[v] = "ND"
      print("Room ",v+1," cleaned!")
    elif(rooms[v] == "ND"):
      if(v == 0):
         v += 1
      elif(v == len(rooms) - 1):
         v -= 1
         flag = True
      else:
        if not flag:
          v += 1
        else:
          v -= 1
  print("All rooms cleaned!")

clean_room()
