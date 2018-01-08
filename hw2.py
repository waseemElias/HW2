import random

def print_even_odd(x):
    if type(x) != int:
        print ("input {0} is not an integer!".format(x))
        return
    if x%2 == 0:
        print("Input {0} is even".format(x))
    else:
        print("Input {0} is odd".format(x))


def question1():
    print ("\nRunning Question 1 tests...\n")
    print("test1 ... verify even is identified correctly")
    x = 10
    print_even_odd(x)
    print("test2 ... verify input validation for integers")
    x = "test1"
    print_even_odd(x)
    print("test3 ... verify odd is identified correctly")
    x = 11
    print_even_odd(x)

def isDevidedEvenly(num,check):
    if num % check == 0:
        print("Input num {0} is divided evenly by check {1}".format(num, check))
    else:
        print("Input num {0} is not divided evenly by check {1}".format(num, check))


def question2():
    # two numbers num and check
    # if num%check == 0 report to user otherwise report to appropriate message
    print("\nRunning Question 2 tests...\n")
    isDevidedEvenly(10,2)
    isDevidedEvenly(11,2)


def RPS(player1,player2):
   print ("player1 draw is {0}, player2 draw is {1}".format(number_to_name(player1),number_to_name(player2)))
    p1=number_to_name(player1);
    p2 = number_to_name(player2);
    if p1 == 'scissors':
        if p2 == 'scissors':
            print ("Even result  - scissors vs. scissors")
        elif p2 == 'paper':
            print ("player 1 Win! - scissors vs. paper")
        elif p2 == 'rock':
            print("player 2 Win! - scissors vs. rock")
    elif p1 == 'paper':
        if p2 == 'scissors':
            print("palyer 2 Win! - paper    vs. scissors")
        elif p2 == 'paper':
            print("Even result  - paper    vs. paper")
        elif p2 == 'rock':
            print("player 1 Win! - paper    vs. rock")
    elif p1 == 'rock':
        if p2 == 'scissors':
            print("palyer 1 Win! - rock     vs. scissors")
        elif p2 == 'paper':
            print("palyer 2 Win! - rock     vs. paper")
        elif p2 == 'rock':
            print("Even result  - rock     vs. rock")


def RPSLS(player1,player2):
    print ("player1 draw is {0}, player2 draw is {1}".format(number_to_name(player1),number_to_name(player2)))
    p1=number_to_name(player1);
    p2=number_to_name(player2);
    if p1 == 'scissors':
        if p2 == 'scissors':
            print ("Even result  - scissors vs. scissors")
        elif p2 == 'paper':
            print ("player 1 Win! - scissors vs. paper")
        elif p2 == 'rock':
            print("player 2 Win! - scissors vs. rock")
        elif p2 == 'lizard':
            print("player 1 Win! - scissors vs. lizard")
        elif p2 == 'spock':
            print("player 2 Win! - scissors vs. spock")
    elif p1 == 'paper':
        if p2 == 'scissors':
            print("palyer 2 Win! - paper vs. scissors")
        elif p2 == 'paper':
            print("Even result  - paper vs. paper")
        elif p2 == 'rock':
            print("player 1 Win! - paper vs. rock")
        elif p2 == 'lizard':
            print("player 2 Win! - paper vs. lizard")
        elif p2 == 'spock':
            print("player 1 Win! - paper vs. spock")
    elif p1 == 'rock':
        if p2 == 'scissors':
            print("palyer 1 Win! - rock vs. scissors")
        elif p2 == 'paper':
            print("palyer 2 Win! - rock vs. paper")
        elif p2 == 'rock':
            print("Even result  - rock vs. rock")
        elif p2 == 'lizard':
            print("player 1 Win! - rock vs. lizard")
        elif p2 == 'spock':
            print("player 2 Win! - rock vs. spock")
    elif p1 == 'lizard':
        if p2 == 'scissors':
            print("palyer 2 Win! - lizard vs. scissors")
        elif p2 == 'paper':
            print("palyer 1 Win! - lizard vs. paper")
        elif p2 == 'rock':
            print("palyer 2 Win! - lizard vs. rock")
        elif p2 == 'lizard':
            print("Even result  - lizard vs. lizard")
        elif p2 == 'spock':
            print("player 1 Win! - lizard vs. spock")
    elif p1 == 'spock':
        if p2 == 'scissors':
            print("palyer 1 Win! - spock vs. scissors")
       elif p2 == 'paper':
            print("palyer 2 Win! - spock vs. paper")
        elif p2 == 'rock':
            print("palyer 1 Win!  - spock vs. rock")
        elif p2 == 'lizard':
            print("player 2 Win! - spock vs. lizard")
        elif p2 == 'spock':
            print("Even result  - spock vs. spock")


def number_to_name(num):
    if num == 0:
        result = 'scissors'
    elif num == 1:
        result = 'paper'
    elif num == 2:
        result = 'rock'
    elif num == 3:
        result = 'lizard'
    elif num == 4:
        result = 'spock'
    return result

def question3():
    print("\nRunning Question 3 tests...for Rock&Paper&Scissors\n")
    for i in range(5):
        print("test {0} -->".format(i+1))
        RPS( random.randrange(0, 3), random.randrange(0, 3))
    for i in range(5):
        print("test {0} -->".format(i + 1))
        RPSLS(random.randrange(0, 5), random.randrange(0, 5))


question1()
question2()
question3()
