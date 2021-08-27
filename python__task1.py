def crick():

     import random
     t = random.randint(0, p*36)
     print ('The target is' , t)
     import random
     b = random.randint(0, 6)
     a = int(input("Guess a number between 0 to 6:-"))
     if a >= t:
          print("you won by", a - t, "runs")
     else:
          sa = a
          count = 1
          while a!=b:

               print('You have guessed the number :-',a)
               print("The right number is:- ",b)
               import random
               b = random.randint(0, 6)
               a = int(input("Again enter a number:-"))
               sa = sa + a


               if sa >= t:
                    break
               count = count + 1
               if count >= p*5 :
                    print(" finished")
                    break

          print ("You scored ",sa)

          if sa > t:
               print ('You WON by ', sa-t,'runs')
          if sa == t:
               print (" Draw")
          if sa < t:
               print (" You Lost by", t - sa)
     print ("GAME OVER")
p = int(input('Enter the number of OVER you want to play:-'))
crick()