#NIE TŁUMIONY 
#leap frog
#leap frog
import math
import numpy as np
import matplotlib.pyplot as plt
A = 5
k = 1
m = 1
f = 1
omega = math.sqrt(k/m)
dt = 0.01
t = np.arange(0, 100, dt)
x_l = []
x_l.append(A)
v_l = []
v_l.append(0)
a_l = []
a_l.append(-omega*omega*x_l[0])
for i in range(1,len(t)):
a_l.append(-omega*omega*x_l[i-1])
v_l.append(v_l[i-1] + (a_l[i] * dt))
x_l.append(x_l[i-1] + v_l[i] * dt)
plt.plot(t, x_l, '-b', t, v_l, '-r', t, a_l, '-g')
plt.xlim(0, 100)
plt.ylim(-7, 7)
plt.xlabel('t', fontsize = '14')
plt.ylabel('x(t), v(t), a(t)', fontsize = '14')
plt.legend(['x(t)', 'v(t)', 'a(t)'])
plt.grid(color = 'grey', linestyle = '--', linewidth = 0.2)
plt.show()
EK_l = []
EP_l = []
EC_l = []
for i in range(len(x_l)):
EK_l.append(0.5*m*v_l[i]**2)
EP_l.append(0.5*k*(x_l[i])**2)
EC_l.append(EK_l[i]+EP_l[i])
plt.plot(t, EC_l, '-b', t, EP_l, '-r', t, EK_l, '-g')
plt.xlim(0, 100)
plt.xlabel('t', fontsize = '14')
plt.ylabel('EC, EP, EK', fontsize = '14')
plt.legend(['EC', 'EP', 'EK'])
plt.grid(color = 'grey', linestyle = '--', linewidth = 0.2)
plt.show()



#TŁUMIONY

#LEAP FROG
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
x_l = []
x_l.append(A)
#x_l.append(A * math.exp(-gamma * dt) * math.cos(omega2 * dt))
#predkosc
v_l = []
v_l.append(0)
#v_l.append((x_s[1] - x_s[0]) / (dt))
#przyspieszenie
a_l = []
a_l.append(-omega2 * omega2 * x_l[0] - 2 * gamma * v_l[0])
#a_l.append(-omega2 * omega2 * x_l[1] - 2 * gamma * v_l[1])
#leap frog
for i in range(1, len(t)):
a_l.append(-omega2 * omega2 * x_l[i-1] - 2 * gamma * v_l[i-2])
v_l.append(v_l[i-1] + dt * a_l[i])
x_l.append(x_l[i-1] + dt * v_l[i])
EK_l = []
EP_l = []
EC_l = []
for i in range(len(x_l)):
EK_l.append(0.5 * m * v_l[i]**2) # Energia kinetyczna
EP_l.append(0.5 * k * x_l[i]**2) # Energia potencjalna
EC_l.append(EK_l[i] + EP_l[i]) # Energia całkowita
plt.plot(t, x_l, '-b', t, v_l, '-r', t, a_l, '-g')
plt.xlim(0, 25)
plt.ylim(-10, 10)
plt.xlabel('t', fontsize = '14')
plt.ylabel('x(t), v(t), a(t)', fontsize = '14')
plt.legend(['x(t)', 'v(t)', 'a(t)'])
plt.grid(color = 'grey', linestyle = '--', linewidth = 0.2)
plt.show()
plt.plot(t, EC_l, '-b', t, EP_l, '-r', t, EK_l, '-g')
plt.xlim(0, 25)
#plt.ylim(-10, 10)
plt.xlabel('t', fontsize = '14')
plt.ylabel('EC, EP, EK', fontsize = '14')
plt.legend(['EC', 'EP', 'EK'])
plt.grid(color = 'grey', linestyle = '--', linewidth = 0.2)
plt.show()
