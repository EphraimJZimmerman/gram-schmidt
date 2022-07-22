from turtle import dot
import numpy
import fractions

# Gram-Schmidt Process
# Used for Computing an Orthogonal Basis in R^3

A = [[6, -2, 0],
     [-4, 0, 2],
     [2, 0, -1],
     [6, -1, 0]]

v1 = []
v2 = []
v3 = []

for row in A:
    v1.append(row[0])
    v2.append(row[1])
    v3.append(row[2])

u1 = v1
u2 = []
u3 = []

u2 = (numpy.dot(v2, u1) / numpy.dot(u1, u1))
u2 = numpy.multiply(u2, u1)
u2 = numpy.subtract(v2, u2)

u3 = numpy.dot(v3, u1) / numpy.dot(u1, u1)
u3 = numpy.multiply(u1, u3)
u3 = numpy.subtract(v3, u3)
u3_final = numpy.dot(v3, u2) / numpy.dot(u2, u2)
u3_final = numpy.multiply(u3_final, u2)
u3 = numpy.subtract(u3, u3_final)

#This is a commonly used formatter that helps with the floating point issue
#Remove this if you want decimal answers
numpy.set_printoptions(formatter={'all':lambda x: str(fractions.Fraction(x).limit_denominator())})

# there should be little arrows on top of the 'U', but that isn't possible in Python
print("u1 =", end=" ")
print(u1)
print("u2 =", end=" ")
print(u2)
print("u3 =", end=" ")
print(u3)