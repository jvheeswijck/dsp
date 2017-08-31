import numpy as np

# Matrix Algebra
import numpy as np

A = np.array([1,2,3,2,7,4]).reshape(2,3)
B = np.array([1,-1,0,1]).reshape(2,2)
C = np.array([5,-1,9,1,6,0]).reshape(3,2)
D = np.array([3,-2,-1,1,2,3]).reshape(2,3)
u = np.array([6,2,-3,5])
v = np.array([3,5,-1,4])
w = np.array([1,8,0,5])
alpha = 6

# Q1
names = 'A B C D u v w'.split()
matrices = [A,B,C,D,u,v,w]

for names, e in zip(names, matrices):
    print('{0} = {1}'.format(names, e.shape,))

#Q2.1
print('u + v = ' + str(u + v))
#Q2.2
print('u - v = ' + str(u - v))
#Q2.3
print('alpha * u = ' + str(alpha * u))
#Q2.4
print('u.v = ' + str(u.dot(v)))
#Q2.5
print('||u|| = ' + str(np.sqrt(u.dot(u))))


#Q3.1
try:
    print('A + C = ' + str(A + C))
except:
    print('A + C = Undefined')
print('')

#Q3.2
try:
    print('A - C.T = ' + str(A - C.T))
except:
    print('A + C.T = Undefined')
print('')

#Q3.3
try:
    print('C.T + 3D = ' + str(C.T + 3*D))
except:
    print('C.T + 3D = Undefined')
print('')

#Q3.4
try:
    print('BA = ' + str(B.dot(A)))
except:
    print('BA = Undefined')
print('')

#Q3.5
try:
    print('BA.T = ' + str(B.dot(A.T)))
except:
    print('BA.T = Undefined')
print('')
#Q3.6
try:
    print('BC = ' + str(B.dot(C)))
except:
    print('BC = Undefined')
print('')
#Q3.7
try:
    print('CB = ' + str(C.dot(B)))
except:
    print('CB = Undefined')
print('')
#Q3.8
try:
    print('B*4 = ' + str(np.linalg.matrix_power(B, 4)))
except:
    print('B*4 = Undefined')
print('')
#Q3.9
try:
    print('AA.T = ' + str(A.dot(A.T)))
except:
    print('AA.T = Undefined')
print('')
#Q3.10
try:
    print('D.T*D = ' + str(D.T.dot(D)))
except:
    print('D.T*D = Undefined')
print('')

