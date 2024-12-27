#liner shooting method

import numpy as np
import matplotlib.pyplot as plt

#define parameters
n=[4,8,16]

x1=0 #first boundary
x2=2 #second boundary

#set initial guess
guess1=2
guess2=-2

y_vals1=[0]
u_vals1=[0]
y_vals2=[0]
u_vals2=[0]
u_ans=[0]
y_ans=[0]


for a in n:
    x_vals = np.linspace(0, 2, a+1)
    print(x_vals)
    h = 1 / a  # step size
    #euler method for guess1
    u0 = 0
    x0 = 0
    guess = guess1
    for j in range(a):
        u1 = u0 + h * guess
        u_vals1.append(u1)

        y1 = guess + h * (4 * (u0 - x0))
        y_vals1.append(y1)

        u0 = u1
        x0 = x0 + h
        guess = y1

    # euler method for guess2
    u0 = 0
    x0 = 0
    guess = guess2
    for j in range(a):
        u1 = u0 + h * guess
        u_vals2.append(u1)

        y1 = guess + h * (4 * (u0 - x0))
        y_vals2.append(y1)

        u0 = u1
        x0 = x0 + h
        guess = y1

    # Print results
    print('For time step n=',a)
    print("Results for guess1: u(x) =", u_vals1)
    print(f"Results for guess2: u(x) =", u_vals2)

    # secant method
    u2_at_x2 = u_vals2[-1]
    u1_at_x2 = u_vals1[-1]
    corrected_slope = guess1 + (((guess2 - guess1) / (u2_at_x2 - u1_at_x2)) * (x2 - u1_at_x2))
    print('The corrected slope is',corrected_slope)


    # Euler method to solve for corrected slope
    u0 = 0
    x0 = 0
    ans = corrected_slope
    for j in range(a):
        u1 = u0 + h * ans
        u_ans.append(u1)

        y1 = ans + h * (4 * (u0 - x0))
        y_ans.append(y1)

        u0 = u1
        x0 = x0 + h
        ans = y1

    print(u_ans, y_ans)
    print()

    # exact solution
    y_exact = []
    for i in x_vals:
        y = np.exp(2) * (np.exp(2 * i) - 1) * (np.exp(2 * i) - np.exp(-2 * i)) + i
        y_exact.append(y)

u_all_vals=[]
u_all_vals.append(u_ans)
u_all_vals = u_ans
plotu1 = u_all_vals[:5]
plotu2 = [0]+u_all_vals[5:13]
plotu3 = [0]+u_all_vals[13:]

plotx1 = [0,0.5,1,1.5, 2]
plotx2 = [0,0.25,0.5,0.75,1,1.25,1.5,1.75,2]
plotx3 =[0, 0.125, 0.25,  0.375, 0.5, 0.625, 0.75,  0.875, 1, 1.125, 1.25,  1.375,1.5, 1.625, 1.75,  1.875, 2]


plt.plot(plotx1,plotu1,label='n=4')
plt.plot(plotx2,plotu2,label='n=8')
plt.plot(plotx3,plotu3,label='n=16')
plt.title("Linear Shooting Method")
plt.xlabel("x")
plt.ylabel("u(x)")
plt.legend()
plt.grid()
plt.show()

