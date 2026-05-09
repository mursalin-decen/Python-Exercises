'''
2. The game() function in a program lets a user play a game and returns the score
as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or
contains the previous Hi-score. You need to write a program to update the Hiscore
whenever the game() function breaks the Hi-score
'''
import random
def game():
     print("You are Playing the game")
     score = random.randint(1,100)

     with open("Hi-score.txt","r")as f:
          highscore = f.read()
          if(highscore != ""):
               highscore = int(highscore)
          else:
               highscore=0
          print(f"Your Score is {score}")
        
          if(score>highscore):
               with open("Hi-score.txt","w") as f:
                    f.write(str(score))
    
                    return score
               
game()