"""Rewrite the grade program from the previous chapter using
a function called computegrade that takes a score as its parameter and
returns a grade as a string.
Score Grade
>= 0.9 A
>= 0.8 B
>= 0.7 C
>= 0.6 D
< 0.6 F"""
score=float(input("enter the score:"))
def computegrade(score):
    try:
        if(score > 1 or score < 0):
            return"bad score"
        elif(score > 0.9):
            return"A"
        elif(score > 0.8):
            return"B"
        elif(score > 0.7):
            return"C"
        elif(score > 0.6):
            return"D"
        elif(score <= 0.6):
            return"F"
        else:
            return"bad score"
    except:
        return"Bad score"
print(computegrade(score))
