# =========================
# IF STATEMENT
# =========================
print("Starting if statement")
print("Example: Check if you are eligible to vote")
age = 18
if age >= 18:
    print("Eligible to vote")  # Executed if condition is True
# =========================
# IF ELSE STATEMENT
# =========================
print("Starting if-else statement...")
print("Example: Check whether you can buy a chocolate or lollipop")
money = 15
if money >= 10:
    print("Buy chocolate")  # Executed if condition is True
else:
    print("Buy lollipop")   # Executed if condition is False
# =========================
# IF ELIF ELSE LADDER
# =========================

print("Starting if-elif-else ladder")
print("Example: Grading system based on marks")
marks = 82

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")  # Executed if all above conditions are False

# =========================
# Loops
# =========================
# =========================
# FOR LOOP
# =========================

"""A for loop is used when the number of iterations is known.

range(start, end, step)

Important Notes:
1) End value follows the n-1 concept (end value is excluded)
2) Default start value is 0
3) Default step value is 1
4) Step value can also be negative
"""
# RANGE WITH START, END, STEP
print("Numbers from 1 to 19")
for i in range(1, 20, 1):
    print(i)

# RANGE WITH START AND END
print("Numbers from 20 to 50")
for i in range(20, 51):
    print(i)

# RANGE WITH ONLY END VALUE
print("Numbers from 0 to 9")
for i in range(10):
    print(i)

# RANGE WITH STEP VALUE
print("Even numbers from 2 to 20")
for i in range(2, 21, 2):
    print(i)

# RANGE WITH NEGATIVE STEP
print("Numbers from 10 to 1 in reverse order")
for i in range(10, 0, -1):
    print(i)

word = "PROGRAMMING"

for i in range(len(word)):
    print(word[i])

print("Printing characters using len()")
word1 = "Python Programming with Loops"
for i in range(len(word1)):
    print(word1[i])

print("Printing characters directly")
word2 = "Nature"
for char in word2:
    print(char)

# =========================
# BREAK STATEMENT
# =========================
"""The break statement is used to exit a loop immediately
when a certain condition is met."""
for i in range(1, 21):
    if i == 15:
        break
    else:
        print(i)


"""When else is used with a loop, it executes only if the
loop completes without encountering a break statement."""
# =========================
# CONTINUE STATEMENT
# =========================
"""The continue statement skips the current iteration
and moves to the next iteration of the loop."""
for i in range(1, 21):
    if i == 15:
        continue
    else:
        print(i)

# =========================
# WHILE LOOP
# =========================
#QS : Separate each digit of a number and print it on a new line
n = 245
while ( n >0): # while(condition)
    print(n % 10) # task
    n = n //10 #updation or increment decrement