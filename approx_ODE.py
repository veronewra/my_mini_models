import numpy as np
import matplotlib.pyplot as plt
import math
import random

#use finite differencing to solve ordinary differential equation
# T_n+1 = F \delta t + (1 - \delta t / tau) T_n
def equation(initial, f, tau, dt, end):
    ints = int(end / dt)
    u = np.zeros(ints + 1)
    t = np.linspace(0, end, ints + 1)

    u[0] = initial
    for n in range(1, ints + 1):
        u[n] = f(n * dt) * dt + (1 - dt / tau) * u[n-1]

    return t, u

ts = [0.1, 0.5, 1, 3] #time steps
for step in ts:
    x, y = equation(0, lambda _: 1, 1, step, 10)
    plt.plot(x, y, label=step)

x_analytical = np.linspace(0, 10, 1000)
y_analytical = [1 - math.exp(-i) for i in x_analytical]
plt.plot(x_analytical, y_analytical, 'k')
plt.title("Force-Damped equation")
plt.legend()
plt.show()
# note the numerical instability 

#doubling Co2 climate forcing (F = 4 W/m^2)
# longwave cooling coefficient is about 10 days
x, y = equation(0, lambda _: 4, 1.3, .1, 10)
plt.plot(x, y)
plt.show()

#Now, forcing varies with time (like diurnal or seasonal cycle)
x, y = equation(0, lambda t: math.sin(6*t)+2, 1.3, .1, 10)
plt.plot(x,y)
plt.title('Varied Forcing')
plt.show()

#both diurnal and seasonal?
x, y = equation(0, lambda t: (math.sin(6*t)+2)*math.sin(t), 1.3, .1, 10) 
plt.plot(x, y)
plt.show()

# lets apply this to something other than weather modelling:
# time complexity of a binary search algorithm
#shows the rate at which runtime of algorithm increases
#tau is the max runtime  
#t is now an increasing array size/ workload
#add some randomization
x, y = equation(0, lambda n: random.randint(0,50), 100, 1, 1000)
plt.plot(x, y, "m")
plt.xlabel("number of elements to search through")
plt.ylabel("search time")
plt.show()