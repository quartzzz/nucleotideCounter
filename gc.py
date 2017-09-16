#Python project for counting nucleotides
import string

data = open("DNA.txt", "r")

#Variables
t = 0
a = 0
g = 0
c = 0

for line in data:
    for char in line:
        if char == "T":
            t += 1
        if char == "A":
            a += 1
        if char == "G":
            g += 1
        if char == "C":
            c += 1

print "There are ", t," T nucleotides."
print "There are ", a," A nucleotides."
print "There are ", g," G nucleotides."
print "There are ", c," C nucleotides."

print "gc content: ", float(g+c) / float(g+c+a+t) 

