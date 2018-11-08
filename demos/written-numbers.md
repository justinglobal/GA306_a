# Demo: Written Numbers

Create a program that asks for a number in base-10 that's between 1 and 99 then prints out the name of it in English.

Use functions in your code, including a [main function](/notes/py-functions-main.md).

> 45
> fourty-five
>
> 11
> eleven

Hint: Use a separate variable for each digit then put them together.

Hint 2: Make it work for regular combinations (like "forty-five") greater than 19 first.

Hint 3: Use floor division (//) and modulo (%) to separate your digits, like this:

```py
tens = num // 10

ones = num % 10
```

<!-- [Source](/demos/written-numbers.py) -->
