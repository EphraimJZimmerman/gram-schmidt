from turtle import dot
import numpy
import fractions

#===============================================#
# Used for Computing an Orthogonal Basis in R^3 #
#===============================================#

A = [[2, 0, 0],
     [4, 2, 2],
     [-2, 2, -1]]

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



#===========#
# FORMATTER #
#===========#

# numpy.set_printoptions(formatter={'all':lambda x: str(fractions.Fraction(x).limit_denominator())})


print("u1 =", end=" ")
print(u1)
print("u2 =", end=" ")
print(u2)
print("u3 =", end=" ")
print(u3)