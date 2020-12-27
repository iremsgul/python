import random
name = str(input("Please etner your name:"))
false = 0
while false <= 3:
    x = str(input(name))
    if x != name:
        false += 1
        print("Please try again later")
        continue
    else:
      course = ["math","hist","lit","eng","spn","phy"]
      print("how many courses do you want?")
      num= int(input("number of course:"))
      list_of_random = random.sample(course, num)
      if num<3:
          print("You failed in class")
          break
      elif num>=6:
          print("You cannot choose more than 5")
          break
      else:
        print(list_of_random)
        print("Please entering your grades one of the courses")
        mid= float(input())
        final= float(input())
        project= float(input())
        notes = mid*0.3 + final*0.5 + project*0.2
        print(float(notes))
        if notes>=90:
         print("AA") 
        elif notes>=70 and notes<90:
         print("BB")
        elif notes>=50 and notes<70:
         print("CC")
        elif notes>=30 and notes<50:
         print("DD")
        elif notes<30:
         print("FF")
         print("You failure")
      




        
    
    
    