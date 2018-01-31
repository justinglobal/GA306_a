# String Formatting

When making complex strings, using the plus `+` operator can get clunky.
Instead use **string formatting**.
You supply a **template** string and then the other strings you want interpolated into the template.
Any double braces `{}` will be filled in with the arguments to format _in order_.

```py
'Hello, {}! my name is {}.'.format('David', 'Helen')  #> 'Hello, David! my name is Helen.'
```

You can also modify the way that objects are filled in the template spots using a [special mini-language](https://docs.python.org/3/library/string.html#formatstrings).

```py
price = 10 / 3
'That cost: ${:.2f}'.format(price)  #> 'That cost: $3.33'
```

Here are all the options for printing with examples that Python uses:

Pass it as a tuple:
```py
print("Total score for %s is %s" % (name, score))
```
Pass it as a dictionary:

```py
print("Total score for %(n)s is %(s)s" % {'n': name, 's': score})
```

There's also new-style string formatting, which might be a little easier to read:

```py
print("Total score for {} is {}".format(name, score))
```

Use the new-style string formatting with numbers (useful for reordering or printing the same one multiple times):

```py
print("Total score for {0} is {1}".format(name, score))
```

Use the new-style string formatting with explicit names:

```py
print("Total score for {n} is {s}".format(n=name, s=score))
```

The clearest two, in my opinion:
Pass the values as parameters and print will do it:

```py
print("Total score for", name, "is", score)
```
If you don't want spaces to be inserted automatically by print in the above example, change the sep parameter:

```py
print("Total score for ", name, " is ", score, sep='')
```

If you're using Python 2, won't be able to use the last two because print isn't a function in Python 2. You can, however, import this behavior from __future__:

```py
from __future__ import print_function
```

Use the new f-string formatting in Python 3.6:

```py
print(f'Total score for {name} is {score}')
```
