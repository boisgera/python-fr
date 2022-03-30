---
title: Itération & compréhensions
author: 
  - "[Sébastien Boisgérault](mailto:Sebastien.Boisgerault@mines-paristech.fr)" 
affiliation: "MINES ParisTech, Université PSL"
license: "[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)"
---

# Iteration

``` python
for i in [1, 2, 3]:
    print(i)

it = iter([1, 2, 3]) # it is an iterator
it

next(it)

next(it)

next(it)

next(it)

---------------------------------------------------------------------------
StopIteration                             Traceback (most recent call last)
/tmp/ipykernel_13823/600241529.py in <module>
----> 1 next(it)

StopIteration: 

it = iter([1, 2, 3]) # iterable: can produce iterators with iter(iterable)
it # iterator: next(it) makes sense

l = [1, 2, 3]

it1 = iter(l)
print(next(it1))
print(next(it1))

it2 = iter(l)
print(next(it2))
print(next(it2))

l = [1, 2, 3]

it1 = iter(l)
it2 = iter(it1) # not very useful ...

print(it1 is it2)

print(next(it1))
print(next(it1))

print(next(it2))
print(next(it2))

---------------------------------------------------------------------------
StopIteration                             Traceback (most recent call last)
/tmp/ipykernel_13823/3453743032.py in <module>
     10 
     11 print(next(it2))
---> 12 print(next(it2))

StopIteration: 

l = list(range(100))
for i in l:
    print(i)
    l.pop(0) # modification during iteration => undefined

l = list(range(100))
for i in l[:]: # safer to iterate on a copy of the list
    print(i)
    l.pop(0)
```

# Iterables

    lists

    tuples

    dicts

        dict keys

        dict values

        dict items

    sets

    strings

    files

    range(100)

    enumerate(...)

``` python

d = {"a": 1, "b": 2}

d.keys()

iter(d.keys())

for c in "Hello world!":
    print(c)

enumerate([6, 7, 8])

for i, number in enumerate([6, 7, 8]):
    print(i, number)

iter(enumerate([6, 7, 8]))

l1 = [1, 2, 3]
l2 = [4, 8, 16]
for item in zip(l1, l2): # simultaneous iteration on l1 and l2
    print(item)

help(list)

list([1, 2, 3])

list({1: "a", 2: "b", 3: "c"})

list("abc")

help(max)

max(1, 2, 3)

max([1, 2, 3])

max("Hello world!")
```

# Compréhension

``` python
l = [1, 2, 3]
squares_l = []
for i in l:
    square = i * i
    squares_l.append(square)
squares_l

[i*i for i in l]

l = range(10)
[i*i for i in l if i*i > 20] # "filter in" elements

type([i*i for i in l if i*i > 20])

{i*i for i in l if i*i > 20}

{i: str(i) for i in range(100)}
```


## generator expressions

``` python
max([x*x for x in range(10)])

max(x*x for x in range(10)) # does not allocate a list of 10 elements

max((x*x for x in range(10))) # does not allocate a list of 10 elements

x*x for x in range(10)

  File "/tmp/ipykernel_13823/2347081421.py", line 1
    x*x for x in range(10)
        ^
SyntaxError: invalid syntax

(x*x for x in range(10))
```

 

