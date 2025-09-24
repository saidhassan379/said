############################################################################
                 #Q1
############################################################################
def mh2kh(s):
    """(float)-> float
    Converts a speed s from miles/hour to kilometres/hour.
    Precondition: s is a non-negative numbers.
    """
    
    return (s*1.60934)


###############################################################################
                 #Q2
#################################################################################
import math
def pythagorean_pair(a,b):
    """
    (int, int) -> bool
    Returns True if integers a and b form a Pythagorean pair (i.e., there exists an integer c such that a^2 + b^2 = c^2), else False.
    Precondition: a and b are integers.
    """
    c=math.sqrt(a**2+b**2)
    return (math.sqrt(a**2+b**2))==int(math.sqrt(c**2))


    
####################################################################################
                  #Q3
###################################################################################
def in_out(xs,ys,side):
     """
     (float, float, float) -> None
     Prompts user for x and y coordinates of a point and prints True if the point is inside the square defined by bottom-left corner (xs, ys) and side length 'side'; otherwise prints False.
     Precondition: side >= 0
     """
     
     x=float(input('Enter a number for the x-cordinate of a querry point: ' ))
     y=float(input('Enter a number for the y-cordinate of a querry point: ' ))
     return (x>=xs and x<=xs+side and y>=ys and y<=ys+side)

############################################################################################
                 #Q4
#############################################################################################
def safe(n):
    """
    (int) -> bool
    Returns True if n is a safe number (does not contain the digit 9 and is not divisible by 9), else False.
    Precondition: 0 <= n <= 99
    """
    return(n>=0 and n%9!=0 and n%10!= 9 and n//10!=9) 
     
##########################################################################################################
                #Q5
###########################################################################################################
def quote_maker(quote,name,year):
    """
    (str, str, int) -> str
    Returns a formatted string: 'In year, a person called name said: "quote"'.
    Precondition: year is a positive integer.
    """
    return("in"+" "+str(year)+","+" a person called"+" "+ name+" " "said:"+" "+'"'+quote+'"')
########################################################################################################
                #Q6
#########################################################################################################
def quote_displayer():
    """
    () -> None
    Prompts the user for a quote, name, and year, then prints the formatted quote using quote_maker.
    Precondition: user inputs valid strings and integer year.
    """
    quote=input('give me a quote:')
    name=input('who said that?')
    year=input('what year did he/she say that?')
    sentence=quote_maker(quote,name,year)
    print(sentence)
#############################################################################################################
                #Q7
##############################################################################################################
def rps_winner():
    """
    () -> None
    Prompts two players for their choice of rock, paper, or scissors and prints whether player 1 wins and whether it's a tie.
    Precondition: players enter 'rock', 'paper', or 'scissors' in lowercase.
    """
    player1=input('what choice did player1 make?\nType of the following functions:rock,paper,scissors:')
    player2=input('what choice did player2 make?\nType of the following functions:rock,paper,scissors:')
    player1_wins = (player1 == "rock") and (player2 == "scissors") or (player1 == "paper") and (player2 == "rock")or (player1 == "scissors") and (player2 == "paper")
    draw = (player1 == player2)
    print('player1 wins, that is'+" "+str(player1_wins))
    print('it is a tie, that is not' +" "+str(not draw))
############################################################################################################
                  #Q8
############################################################################################################
def fun(x):
    """
    (float) -> float
    Solves 104*y = x + 3 for y and returns y.
    Precondition: x is a positive number.
    """
    y=math.log10(x+3)/4
    return(y)
###############################################################################################################
                  #Q9
################################################################################################################
def ascii_name_plaque(name):
  """
  (str) -> None
  Prints a decorative ASCII name plaque with the given name.
  Precondition: name is a non-empty string.
  """
  name= " "+ "__" + name + "__"+" "
  border="*" * (len(name)+4)
  empty="*" + " " * (len(name)+2)  + "*"
  print(border)
  print(empty)
  print("* "+name + " *")
  print(empty)
  print(border)

######################################################################################################################
                 #Q10
########################################################################################################################
import turtle

def draw_house():
    """
    () -> None
    Draws a house using Turtle graphics with at least two filled areas.
    Precondition: Turtle graphics module is imported.
    """
    s = turtle.Screen()
    t = turtle.Turtle()
    
    
    # Draw house base
    t.penup()
    t.goto(-100, -100)
    t.pendown()
    t.goto(100, -100)
    t.goto(100, 50)
    t.goto(-100, 50)
    t.goto(-100, -100)

    # Draw roof
    t.goto(-100, 50)
    t.goto(0, 150)
    t.goto(100, 50)
    t.goto(-100, 50)

    # Draw door
    t.penup()
    t.goto(-50, -100)
    t.pendown()
    t.goto(-50, -30)
    t.goto(0, -30)
    t.goto(0, -100)
    t.goto(-50, -100)

    #draw lock
    t.penup()
    t.goto(-50,-60)
    t.pendown()
    t.goto(-40,-60)
    t.goto(-40,-70)

    # Draw window
    t.penup()
    t.goto(30, -30)
    t.pendown()
    t.fillcolor("yellow")
    t.begin_fill()
    t.goto(70, -30)
    t.goto(70, 10)
    t.goto(30, 10)
    t.goto(30, -30)
    t.end_fill()

    # Window cross
    t.goto(30, -10)
    t.goto(70, -10)
    t.penup()
    t.goto(50, -30)
    t.pendown()
    t.goto(50, 10)

    # Draw chimney
    t.penup()
    t.goto(50, 100)
    t.pendown()
    t.goto(40, 130)
    t.goto(60, 130)
    t.goto(55, 100)

    # Draw sun/moon
    t.penup()
    t.goto(20, 70)
    t.pendown()
    t.fillcolor("yellow")
    t.begin_fill()
    t.circle(20)
    t.end_fill()
    s.exitonclick()




######################################################################################################################
                #Q11
#######################################################################################################################
def alogical(n):
    """
    (float) -> int
    Returns the minimum number of times n needs to be divided by 2 to get a number <= 1.
    Precondition: n >= 1
    """
    x=math.ceil((math.log10(n))/(math.log10(2)))
    return(x)
#########################################################################################################################
                 #Q12
#########################################################################################################################
def cad_cashier(price,payment):
    """
    (float, float) -> float
    Returns the change (rounded to the nearest 5 cents) owed to a customer for a given price and payment.
    Precondition: payment >= price and both have at most 2 decimal places.
    """
    cal=(payment-price)
    exact=round(cal,2)
    change=round(exact*20)/20
    return round(change,2)
#########################################################################################################################
                   #Q13
##########################################################################################################################
def min_CAD_coins(price,payment):
    """
    (float, float) -> tuple(int, int, int, int, int)
    Returns the minimum number of coins (toonies, loonies, quarters, dimes, nickels) needed for change.
    Precondition: payment >= price and valid for cad_cashier function.
    """
    change=cad_cashier(price,payment)
    amount=int(round(change*100))
     
    t = amount // 200
    amount= amount%200
    l =amount // 100
    amount=amount% 100
    q = amount // 25
    amount= amount%25 
    d = amount // 10
    amount=amount% 10
    n = amount // 5
    amount=amount% 10
    return(t,l,q,d,n)

    

