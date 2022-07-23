from cmath import sqrt
from turtle import dot
import numpy
import fractions

#===============================================#
# Used for Computing an Orthonomal Basis in R^3 #
#===============================================#

A = [[2, 0, 0],
     [4, 2, 0],
     [-2, 2, 1]]

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

u2 = float(numpy.dot(v2, u1))
u2 = u2 / pow(numpy.linalg.norm(u1), 2)
u2 = numpy.multiply(u2, u1)
u2 = numpy.subtract(v2, u2)

u3 = float(numpy.dot(v3, u1))
u3 = u3 / pow(numpy.linalg.norm(u1), 2)
u3 = numpy.multiply(u2, u1)

u3_final = float(numpy.dot(v3, u2))
u3_final = u3_final / pow(numpy.linalg.norm(u2), 2)
u3_final = numpy.multiply(u3_final, u2)
u3 = numpy.subtract(u3, u3_final)

u1_norm = numpy.linalg.norm(u1)
u2_norm = numpy.linalg.norm(u2)
u3_norm = numpy.linalg.norm(u3)

u1 = numpy.divide(u1, u1_norm)
u2 = numpy.divide(u2, u2_norm)
u3 = numpy.divide(u3, u3_norm)

print("Orthonormal basis:")


#===========#
# FORMATTER #
#===========#

# numpy.set_printoptions(formatter={'all': lambda x: str(fractions.Fraction(x).limit_denominator())})

print("u1 =", end=" ")
print(u1)
print("u2 =", end=" ")
print(u2)
print("u3 =", end=" ")
print(u3)
