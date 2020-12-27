x = str(input("enter your name:"))
print("welcome ",str.format(x))
word = 'python'
print('lets guess:(word with 5 character')
guess = str(input())
chance = 5 
fail=0
while chance < 5:
    if guess in word:
        print("good job")
        
    else:
        fail+=1
        print("oops")
g2 =str(input())  
if g2 in word:
        print("good job")
        print(str.format(guess),str.format(g2))
        
else:
        fail+=1
        print("oops")
g3 =str(input())  
if g3 in word:
        print("good job")
        print(str.format(guess),str.format(g2),str.format(g3))
        
else:
        fail+=1
        print("oops")
g4 =str(input())  
if g4 in word:
        print("good job")
        print(str.format(guess),str.format(g2,str.format(g3),str.format(g4)))
        
else:
        fail+=1
        print("oops")
g5 =str(input())  
if g5 in word:
        print("good job")
        print(str.format(guess),str.format(g2),str.format(g3),str.format(g4),str.format(g5),)
        
    else:
        fail+=1
        print("oops")
    break
    
       
    
     
     