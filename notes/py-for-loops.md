# While Loops and For Loops

In programming we automate computer tasks. "Looping" is doing the same basic thing over and over. While and For Loops are two basic ways we can run code repeatedly.

A **while loop** runs a block of code until (or "while") a condition is met.
While Loops are based on a condition, for example "Print gallons of fuel while there is fuel in the tank".
In python that would look like this:

```py
fuel_gallons = 100

while fuel_gallons >= 0:
    print("you have ", fuel_gallons, " gallons of fuel left")
    fuel_gallons -= 5
    print("you used 5 gallons of fuel")
```

A **for loop** gives you a _generic_ way to perform a block of code once for _each item_ in a group.
Any sequence of items that is 'iterable' can use for loops.

This code can do anything!
For loops can change any group of data based on conditions, even strings.

```py
for letter in "python":
    print(letter)
```
will output
```py
p
y
t
h
o
n
```

This can be done with the range() function as well:

```py
for thing in range(5):
    print("I have ", thing, " things")
```
will output
```py
I have  0  things
I have  1  things
I have  2  things
I have  3  things
I have  4  things
```

Most often you will see it used on groups of data like lists, which we will cover later.

```py
receipt = [3.00, 2.50, 10.75]
total = 0
for cost in receipt:
    total += cost
```

Think carefully before using them, though.
90% of the things you want to do with a for loop, you already have functions to do.
The above would be better written using `sum()`, though.

```py
receipt = [3.00, 2.50, 10.75]
total = sum(receipt)
```
