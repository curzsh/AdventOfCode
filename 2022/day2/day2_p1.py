with open('2022\day2\day2_input', 'r') as file:
  lines = [line.rstrip() for line in file]
  
RPS = {
  ("A", "X") : 4, # tie =  3, X(rock = 1)
  ("A", "Y") : 8, # win =  6, Y(paper = 2)
  ("A", "Z") : 3, # loss = 0, Z(scissors = 3)
  ("B", "X") : 1, # loss = 0, X(rock = 1)
  ("B", "Y") : 5, # tie =  3, Y(paper = 2)
  ("B", "Z") : 9, # win =  6, Z(scissors = 3)
  ("C", "X") : 7, # win =  6, X(rock = 1)
  ("C", "Y") : 2, # loss = 0, Y(paper = 2)
  ("C", "Z") : 6, # tie =  3, Z(scissors = 3)
}

#A = X, A < Y, A > Z
#B = Y, B < Z, B > X
#C = Z, C < X, C > Y 
  
#A = rock, B = paper, C = scissors
#X = rock = 1 point
#Y = paper = 2 points
#z = scissors = 3 points 
#win = 6 pts, tie = 3 pts, loss = 0
  
pts = 0;
for line in lines:
  leftSide, rightSide = line.split(' ', 1)
  pts += RPS[(leftSide, rightSide)]

print (pts)


  
