# LT2222 V21 Assignment 3

Your name: Patricia Grau (gusgraupa)

## Part 1

Instructions: train.py is already complete, and you will not modify it. Instead, in README.md, you will explain what the functions a, b, and g do, as well as the meaning of the command-line arguments that are being processed via the argparse module. You will then run train.py on the training file.  train.py will save a model.



FUNCTION A

Separates the letters of a file and gets its set.


Takes a file (f) and separates it into the smallest elements that it contains: letters, numbers, punctuation, spaces and new lines ('\n'). The beginning of the file is marked with '<\s>' '<\s>', and the end, with '<\e>' '<\e>'. It also gets the set of the letters, that is, all the different elements without repeating them (types).

Args:
- f: a file.

Returns: 
- mm: the smallest elements of the file
- list(set(mm)): the set of the elements.



FUNCTION G

Returns an nd-array containing 0 in all positions except 1, whose value is 1.

Line by line:

- 25: z is a numpy d-array that contains as many zeros as the length of the list p.
- 26: p.index(x) gives the index of the element x in the list p. That is, the position of the element x in the list. 
- 26: z will contain a 1 in the position where the element of p is x.
- 27: z is returned.

Args:
- p: a list.
- x: an element of that list.

Returns:
- z: an nd-array containing 0 in all positions except one, where its value is 1.



FUNCTION B

From the smallest elements of a file and its set, it returns two numpy arrays. One contains the index of the vowels of the file (according to the vowel list), and the other contains arrays with 0 in most positions and 1 in others (depending on the function g).


Line by line:

- 32: Looping through a range of the length of the elements of a file, minus 4 because we are going to check four elements forward of the integer looping through (v).
- 33: If an element (v+2 to avoid '<\s>') is a vowel...
- 37: Save in gt the index of the vowel in the vowel list
- 39: Append to gr the concatenation of g(u[v], p), g(u[v+1], p), g(u[v+2], p), g(u[v+3], p) and g(u[v+4], p). gr will contain arrays with 0 in most elements, and 1 in the positions where the first argument of g appears.


Args:
- u: smallest elements of a file (letters, punctuation, spaces, new lines, etc.).
- p: the set of u.

Returns:
- np.array(gr): a numpy array containing arrays. features?
- np.array(gt): a numpy array containing the index of the vowels (in the vowel list in the beginning). classes?



COMMAND-LINE ARGUMENTS OF ARGPARSE

m and h are positional arguments (strings). 

- m is a file, about which we want to predict the vowels (training data).
- h is the file name/the path.

k and r are optional arguments (k is set to 200 by default and r, to 100.)

- k is the hiddensize (default = 200)
- r is the number of epochs (default = 100).


Line by line:
- 53: q is a tuple that contains two lists: the elements of the file m and the set of the elements.
- 54: w is a tuple that contains two numpy arrays. The first contains the indexes of the vowels in the file according to the vowel list. The second contains arrays with 0 in most elements, and 1 in the positions where a specific element of a sentence appear.
- 55: Calls the function "train" in model.py with five elements: an array containing the indexes of the vowels in the file according to the vowel list; an array of arrays with 0 in most elements, and 1 in the positions where a specific element of a sentence appear; the set of elements in a file; and two integers (set to 200 and 100, respectively).
- 57: Saves the result of the function "train" with the name of h.


## Part 2

## Part 3

## Bonuses

## Other notes
