#Generator Excercises

#Problem 1
#Create a generator, primes_gen that generates prime numbers starting from 2.

def primes_gen():
    i=2
    while True:
        for n in range(2, i+1):
            if i%n==0 and n!=i:
                break
            elif n==i:
                yield i
        i+=1     
        

gen = primes_gen()
for _ in range(10):
    print(next(gen), end=' ')
# Expected output
# 2 3 5 7 11 13 17 19 23 29
#----------------------------------------------------------------------------

#Problem 2
#Create a generator, unique_letters that generates unique letters from
#the input string. It should generate the letters in the same order as
#from the input string.

def unique_letters(string):
    i=0
    l = list(string)
    while i<len(string):
        s = string[i]
        l.remove(s)
        if s not in l:
            yield s
        i+=1


for letter in unique_letters('hello'):
    print(letter, end=' ')

# Expected output
# h e l o
def get_sequence_upto(x):
    for i in range(x):
        yield i