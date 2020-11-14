# Python-for-Everybody-Functions
In the context of programming, a function is a named sequence of statements that
performs a computation
Why functions?
It may not be clear why it is worth the trouble to divide a program into functions.
There are several reasons:
• Creating a new function gives you an opportunity to name a group of statements, which makes your program easier to read, understand, and debug.
• Functions can make a program smaller by eliminating repetitive code. Later,
if you make a change, you only have to make it in one place.
• Dividing a long program into functions allows you to debug the parts one at
a time and then assemble them into a working whole.
• Well-designed functions are often useful for many programs. Once you write
and debug one, you can reuse it.
Exercise 6: Rewrite your pay computation with time-and-a-half for overtime and create a function called computepay which takes two parameters
(hours and rate).
Enter Hours: 45
Enter Rate: 10
Pay: 475.0
Exercise 7: Rewrite the grade program from the previous chapter using
a function called computegrade that takes a score as its parameter and
returns a grade as a string.
Score Grade
>= 0.9 A
>= 0.8 B
>= 0.7 C
>= 0.6 D
< 0.6 F
Enter score: 0.95
A
Enter score: perfect
Bad score
Enter score: 10.0
Bad score
Enter score: 0.75
C
Enter score: 0.5
F
Run the program repeatedly to test the various different values for input.
