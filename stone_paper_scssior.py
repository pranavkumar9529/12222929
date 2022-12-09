



rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
computer_choice=random.randint(1,3)
your_chioce=int(input("enter your choice:"))
if your_chioce==1:
  print(f"your choice is  ROCK {rock}")
elif your_chioce==2:
  print(f"your choice is PAPER {paper}")
elif your_chioce==3:
  print(f"your choice is SCISSORS {scissors}")

if computer_choice==1:
  print(f"computer choice is ROCK  {rock}")
elif computer_choice==2:
  print(f"computer choice is PAPER {paper}")
else:
  print(f"computer choice is SCISSORS {scissors}") 

#how i can win 
if (your_chioce==1) and (computer_choice==3):
  print("you won !")
elif (your_chioce==2) and (computer_choice==1):
  print("you won !")
elif(your_chioce==3) and (computer_choice==2):
  print("you won !")
elif (your_chioce>3):
  print("Enter the valid input")

#how can computer won

if (your_chioce==1) and (computer_choice==2):
  print("computer won")
elif (your_chioce==2) and (computer_choice==3):
  print("computer won")
elif (your_chioce==3) and (computer_choice==1):
  print("computer won")

#how match can tie
if your_chioce==computer_choice:
  print("it's tie!")