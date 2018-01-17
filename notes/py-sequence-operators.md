# Sequence Operators

All sequences, like strings and lists, have a few useful operators.

## Length

Many sequences have a **length**.
You can use the built-in function `len()` to get it.

```py
name = 'Justin'
len(name)  #> 6
names = ['David', 'Helen']
len(names)  #> 2
```

## Indexing and Slicing

Sequences have the **subscript operator** or **get operator**, `[]`.
It returns the value contained at a numbered position in the sequence, called an **index**.
In Python, all sequences start counting from _zero_.
If you attempt to access an index that doesn't exist, an `IndexError` is thrown.

```py
name = 'Justin'
ages = [5, 10, 15]
name[0]  #> 'J'
name[4]  #> 'i'
name[10]  # Throws IndexError
ages[1]  #> 10
```

Most sequences support **negative indices** which count backwards from the end of sequence.

```py
name[-1]  #> 'n'
name[-3]  #> 't'
ages[-1]  #> 15
```

You can also use the subscript operator to **slice** a sequence, or get part of it.
Pass a starting index, then a colon `:`, then an _exclusive_ ending index.
If you leave out a starting or ending index, it defaults to the beginning or end of the sequence, respectively.

```py
name[2:4]  #> 'st'
name[:4]  #> 'Just'
name[2:]  #> 'stin'
ages[1:]  #> [10, 15]
```

Remember, `[]` is just an operator that returns a value, so you can put them anywhere an expression is needed.

```py
x = [[1, 2], [3, 4]]
x[1][0]  #> 3
['a', 'b', 'c'][[1, 2, 3][1]]  #> 'c'
```

## Concatenation

Sequences can be **concatenated** in order by using plus `+`.

```py
[1, 2] + [3]  #> [1, 2 ,3]
'Hello, ' + 'Justin'  #> 'Hello, Justin'
```

## In Operator

You can test if a single inner value exists in a sequence by using the `in` operator.
It only checks single values and containment at the _top level_.

```py
4 in [2, 4, 6]  #> True
's' in 'Justin'  #> True
's' in ['Justin']  #> False
[2, 4] in [2, 4, 6]  #> False
```
