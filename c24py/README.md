### Calculate from a set of numbers to get 24 (or any number).

### Excamples:

Get 24 from: 2 3 4

    $c24.py 2 3 4
    2*(3*4)

Get 24 from 1 1 1 1

    $c24.py 1 1 1 1
    (no output, because there's no solution)

Get 24 from: 5 5 5 5

    $c24.py 5 5 5 5
    (5*5)-(5/5)

Get 24 from: 5 5 5 5 5

    $c24.py 5 5 5 5 5
    ((5*(5*5))-5)/5

Get 15 from: 1 2 3 4

    $c24.py c15 1 2 3 4
    1+(2+(3*4))

Get 999 from: 1 2 3 4 5 6 7

    $c24.py c999 1 2 3 4 5 6 7
    1+(2*((3*(4*(6*7)))-5))

c24.py without any argument will print out solutions for all combination of 4 poker card numbers.

When the length of numbers is greater than 7, the calculation time will be really long because the algorithm is recursive.

See this blog post: http://blog.wensheng.org/2006/06/calculate-24-python-implementation-24.html

Online demo: http://calculate24.appspot.com/ (on Google AppEngine)

### Note 2021

15 years ago, I wrote the [permu recipe](https://code.activestate.com/recipes/496819-a-recursive-function-to-get-permutation-of-a-list/) specifically for this task.  Since then, [itertools.permutations](https://docs.python.org/3/library/itertools.html#itertools.permutations) has been added to standard library.  For this task, itertools.permutations should be used because it's faster.  However my permu function is still useful for list with redundant items.
