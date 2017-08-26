# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

### Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

Python lists and tuples are data-types that can hold a collection of elements of any type. They both support indexing through the use of square-brackets `[]` allowing elements within to be retrieved.

They are different in that Lists are mutable while Tuples are not. That is, elements within the list can be changed and reassigned whereas Tuples does not allow such actions. In order to change an element in a tuple, the entire Tuple must be reassigned.

With regard as to how they are represented in a script, tuples are comma seperated elements enclosed by `()` while lists are similarly seperated by commas but enclosed by `[]`.

Tuples will work as keys in Dictionaries but Lists will not. This is due to the fact that tuples are immutable while lists are not. Dictionaries are collections of key-value pairs implemented by a hashtable. The key of a dictionary goes through a hash function and results in a location in memory. If the key were to change, the address would change, and the value the key is normally associated to would not be able to be retrieved. Since tuples are immutable, they are hashable and can be used as keys in a dictionary.

---

### Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

Python lists and sets are both built-in data structure types that hold a collection of elements. They are both mutable and allow elements to be added and removed.

Lists and sets differ in a number of ways:  
* Sets do not support indexing, Lists do.
* Sets, like dictionaries, are implemented by a hashtable while Lists are not.
* Sets can only contain unique elements, Lists may have duplicate elements.
* Sets may only contain hashable elements (since sets are implemented by a hashtable). Lists may contain any type element
* Lists are ordered while Sets are unordered
* Within a script, lists are enclosed by `[]` while sets are enclosed by `{}`

For finding an element, a Set generally has better performance as it uses a hashtable and its average time complexity is O(1). When an object is added to a set, its location is determined by its hash. To check for the existence of an element, the element is run through the hash function, giving a location and then the location is checked for the existence of an object. In searching a list, the list of memory addresses must be iterated through and compared to the element to determine if it exists within the List. This can have a average time complexity of O(n).

---

### Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

Python's lambda allows a user to pass a one line function to another function without having to define a function using `def`. That is, it is an anonymous function. It is useful when specifying operations for functions such as `map`,`reduce` and `filter` or even passing functions to `sorted()`.

Using an example, we can sort a list of strings ignoring case, by passing a lambda function in `key` arguement:  
```python
sorted(list, key=lambda x: x.lower())
```

---

### Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

List comprehensions are a Python way of constructing lists in a single line of code. Rather than delcaring a `for` loop and performing operations on elements to determine the elements of the list, list comprehensions allows all these steps to be written in a single line of code.

For example, if I wish to create a list of all the odd squares of the numbers 1 through 10, a loop would be written the following way:  
```python
squares = []
for i in range(1,11):
    square = i**2
    if square % 2 == 1:
        squares.append(i**2)
```
A list comprehension would be written in the following way:
```python
squares = [x**2 for x in range(1,11) if x % 2 == 1]
```
This can also be equivalently be done with the `map` and `filter` functions. The `map` function takes a function and an iterable as arguements and runs each element within the iterable through the function. The `filter` function similarly takes a function that evaluates to a boolean and iterable and returns a iterable that returns elements that evaluated to `True` once passed through the function.
Implementing the above example using `filer` and `map`, we have:
```python
squares = list(filter(lambda x: x % 2 == 1, map(lambda x: x**2, range(1,11))))
```
As you can see, list comprehensions is a powerful, and simple way to combine many operations into a single line of code.

Performance-wise, list comprehensions generally have better performance over traditional loops and `map` and `filter`. The exception is if a built-in function is passed, such as `str`, `len`, or `max`, `map` will have better performance.

Additionally, comprehensions are not limited to lists, but can also be used with both dictionaries and sets. For example, one can initialize a tally, or counting dictionary with people and their scores with the following:  
```python
names = 'James John Emily Nina Josh'.split()
scores = {name:0 for name in names}
'''
>>> {'Emily': 0, 'James': 0, 'John': 0, 'Josh': 0, 'Nina': 0}
'''
```
With a set, we can create, like a list, a collection of the odd square numbers of the numbers 1 through 10:  
```python
squares = {x**2 for x in range(1,11) if x % 2 == 1}
'''
>>> {1, 9, 25, 49, 81}
'''
---

### Complete the following problems by editing the files below:

### Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE  (answer will be in number of days)

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

### Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)
*Completed*
---

### Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)
*Completed*
---

### Q8. Parsing
Write a script as indicated (using the football data) in [q8_parsing.py](python/q8_parsing.py)
*Completed*




