import random
def choose():
  words=['PROGRAMMING','MOVIE','LAPTOP','CODING','DATA','COMPUTER','KEYBOARD','GIRL']
  pick=random.choice(words)
  return pick
def jumble(word):
  random_word=random.sample(word,len(word))
  jumbled="-".join(random_word)
  return jumbled
def thank(p1name,p2name,pp1,pp2):
  print("Score of ",p1name,"=",pp1)
  print("Score of ",p2name,"=",pp2)
  if pp1>pp2:
    print("Congratulations ",p1name, "you won !")
    print("Your score is-",pp1)
  elif pp2>pp1:
    print("Congratulations ",p2name, "you won !")
    print("Your score is-",pp2)
  else:
    print("It was a draw\nBoth played well !")
  print("Thanks to both of you for playing !")
def play():
  p1name=input("Enter Name of First Player:")
  p2name=input("Enter Name of Second Player:")
  pp1=0
  pp2=0
  turn=0
  while True:
    word=choose()
    qn=jumble(word)
    print(qn)
    if turn%2==0:
      print(p1name," it's your turn :");
      ans=input()
      if(word==ans.upper()):
        pp1+=1
        print("Correct ! Your score is ",pp1)
        print("To continue press 1 or to end press 0")
        k=int(input())
        if(k==0):
          thank(p1name,p2name,pp1,pp2)
          break
        else:
          turn+=1
          continue
      else:
        print("Better Luck Next Time")
        print("I thought ","'",word,"'")
        print("To continue press 1 or to end press 0")
        k=int(input())
        if(k==0):
          thank(p1name,p2name,pp1,pp2)
          break
        else:
          turn+=1
          continue
    else:
      print(p2name," it's your turn :");
      ans=input()
      if(word==ans.upper()):
        pp2+=1
        print("Correct ! Your score is ",pp2)
        print("To continue press 1 or to end press 0")
        k=int(input())
        if(k==0):
          thank(p1name,p2name,pp1,pp2)
          break
        else:
          turn+=1
          continue
      else:
        print("Better Luck Next Time")
        print("I thought ","'",word,"'")
        print("To continue press 1 or to end press 0")
        k=int(input())
        if(k==0):
          thank(p1name,p2name,pp1,pp2)
          break
        else:
          turn+=1
          continue
play()
