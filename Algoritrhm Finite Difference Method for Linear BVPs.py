import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy.linalg import solve

#solve boundary value problem using linear finite difference
# initialised all parameters
N=3
p=1
q=1
h=1/(N+1)

#boundary conditions
g0=1
g1=0

#declare functions
def f(x):
    return -np.sin(np.pi*(x))

#create diagonal matrix A
diagonal=np.zeros((N,N))
diagonal[N-N,:]=-(1+(h/2)*p)
diagonal[N-2,:]=(2+q*(h**2))
diagonal[N-1,:]=-(1-(h/2)*p)

#create diagonal matrix B
b=np.zeros((N,N-2))
b[N-N,:]=((1.0+(1/2)*h*p)*g0)+(h**2)*f(0.25)
b[N-2,:]=h**2*f(0.5)
b[N-1,:]=((1.0-(1/2)*h*p))*g1+(h**2)*f(0.75)

#transform diagonalised matrix
A=scipy.sparse.spdiags(diagonal,[-1,0,1],N,N)
A=A.toarray()
u=solve(A,b)

print ('matrix A is', A)
print('matrix b is',b)
print ('matrix u is', u)

#plot graph
coordx=(0.25,0.5,0.75)
coordy=[]
for i in u:
    coordy.append(i)

plt.plot(coordx,coordy)
plt.xlabel('x')
plt.ylabel('u(x)')
plt.title('Algorithm Finite Difference method')
plt.show()

