# the zip function is names after zippers
# zip() takes in iterables and returns an iterator, a list that contains the i-th element from each of the iterables as a tuple at the i-th index

numbers = [1, 2, 3]
letters = ['a', 'f', 'z', 'x']

zipped = zip(letters, numbers)  # once the shortest iterable is exhausted, the remaining elements on the longest iterable are ignored. in this case, 'x' is not paired with anything

print(list(zipped))


# another example

s1 = {2, 5, 1}
s2 = {'b', 'g', 't'}

print(list(zip(s2, s1)))

# if you only pass one argument, the zip() function returns a one item tuple

t = [1, 2, 4]
zipped = zip(t)
print(list(zipped))