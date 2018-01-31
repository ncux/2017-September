""" Write a procedure, called biggest, which returns the key corresponding to the entry with the largest number
 of values associated with it. If there is more than one such entry, return any one of the matching keys. """

def biggest(dictionary):
    k = dictionary[k]
    return len(dictionary[k])

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}
animals['d'] = ['donkey']
animals['d'].append('dingo')
animals['d'].append('dog')
print(animals)

dictionary = animals
print(biggest(animals))





