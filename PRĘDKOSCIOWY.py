
#NIE TŁUMIONY

#predkosciowy
#predkosciowy
x_p = []
x_p.append(A)
v_p = []
v_p.append(0)
a_p = []
a_p.append(-omega*omega*x_l[0])
for i in range(1,len(t)):
a_p.append(-omega*omega*x_p[i-1])
x_p.append(x_p[i-1] + (dt * v_p[i-1]) + (((dt**2) * a_p[i-1] )/2))
v_p.append(v_p[i-1] + (( dt * ( a_p[i-1] + a_p[i] ) ) / 2))
plt.plot(t, x_p, '-b', t, v_p, '-r', t, a_p, '-g')
plt.xlim(0, 10)
plt.ylim(-7, 7)
plt.xlabel('t', fontsize = '14')
plt.ylabel('x(t), v(t), a(t)', fontsize = '14')
plt.legend(['x(t)', 'v(t)', 'a(t)'])
plt.grid(color = 'grey', linestyle = '--', linewidth = 0.2)
plt.show()
EK_p = []
EP_p = []
EC_p = []
for i in range(len(x_p)):
EK_p.append(0.5*m*v_p[i]**2)
EP_p.append(0.5*k*(x_p[i])**2)
EC_p.append(EK_p[i]+EP_p[i])
plt.plot(t, EC_p, '-b', t, EP_p, '-r', t, EK_p, '-g')
plt.xlim(0, 100)
plt.xlabel('t', fontsize = '14')
plt.ylabel('EC, EP, EK', fontsize = '14')
plt.legend(['EC', 'EP', 'EK'])
plt.grid(color = 'grey', linestyle = '--', linewidth = 0.2)
plt.show()



#TŁUMIONY

import math
import numpy as np
import matplotlib.pyplot as plt
A = 5
k = 1
m = 1
f = 1
omega = math.sqrt(k/m)
gamma = 0.1
dt = 0.01
t = np.arange(0, 100, dt)
omega2 = math.sqrt((omega * omega) - (gamma * gamma))
#polozenie
x_p = []
x_p.append(A)
#predkosc
v_p = []
v_p.append(0)
#przyspieszenie
a_p = []
a_p.append(-omega2 * omega2 * x_p[0] - 2 * gamma * v_p[0])
#leap frog
for i in range(1, len(t)):
x_p.append(x_p[i-1] + dt * v_p[i-1] + (dt * dt * a_p[i-1] * 0.5) )
a_p.append(-omega2 * omega2 * x_p[i-1] - 2 * gamma * v_p[i-2])
v_p.append(v_p[i-1] + 0.5 * dt * (a_p[i-1] + a_p[i]))
EK_p = []
EP_p = []
EC_p = []
for i in range(len(x_p)):
EK_p.append(0.5 * m * v_p[i]**2) # Energia kinetyczna
EP_p.append(0.5 * k * x_p[i]**2) # Energia potencjalna
EC_p.append(EK_p[i] + EP_p[i]) # Energia całkowita
plt.plot(t, x_p, '-b', t, v_p, '-r', t, a_p, '-g')
plt.xlim(0, 25)
plt.ylim(-10, 10)
plt.xlabel('t', fontsize = '14')
plt.ylabel('x(t), v(t), a(t)', fontsize = '14')
plt.legend(['x(t)', 'v(t)', 'a(t)'])
plt.grid(color = 'grey', linestyle = '--', linewidth = 0.2)
plt.show()
plt.plot(t, EC_p, '-b', t, EP_p, '-r', t, EK_p, '-g')
plt.xlim(0, 25)
#plt.ylim(-10, 10)
plt.xlabel('t', fontsize = '14')
plt.ylabel('EC, EP, EK', fontsize = '14')
plt.legend(['EC', 'EP', 'EK'])
plt.grid(color = 'grey', linestyle = '--', linewidth = 0.2)
plt.show()