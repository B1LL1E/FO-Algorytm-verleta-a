#NIE TŁUMIONY

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
#Standardowy
x_s = []
x_s.append(A)
x_s.append(math.sqrt(A**2 - omega*omega*(A*dt)**2))
v_s = []
v_s.append(0)
a_s = []
a_s.append(-omega*omega*x_s[0])
a_s.append(-omega*omega*x_s[1])
for i in range(2, len(t)):
x_s.append(2*x_s[i-1]-x_s[i-2]+(dt**2)*a_s[i-1])
a_s.append(-omega*omega*x_s[i])
v_s.append((x_s[i]-x_s[i-2])/(2*dt))
ostatni_x = 2*x_s[i-1]-x_s[i-2]+(dt**2)*a_s[i-1]
v_s.append((ostatni_x-x_s[i-2])/(2*dt))
EK_s = []
EP_s = []
EC_s = []
#energia
for i in range(len(x_s)):
EK_s.append(0.5*m*v_s[i]**2)
EP_s.append(0.5*k*(x_s[i])**2)
EC_s.append(EK_s[i]+EP_s[i])
plt.plot(t, x_s, '-b', t, v_s, '-r', t, a_s, '-g')
plt.xlim(0, 100)
plt.ylim(-7, 7)
plt.xlabel('t', fontsize = '14')
plt.ylabel('x(t), v(t), a(t)', fontsize = '14')
plt.legend(['x(t)', 'v(t)', 'a(t)'])
plt.grid(color = 'grey', linestyle = '--', linewidth = 0.2)
plt.show()
plt.plot(t, EC_s, '-b', t, EP_s, '-r', t, EK_s, '-g')
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
x_s = []
x_s.append(A)
x_s.append(A * math.exp(-gamma * dt) * math.cos(omega2 * dt))
#predkosc
v_s = []
v_s.append(0)
v_s.append((x_s[1] - x_s[0]) / (dt))
#przyspieszenie
a_s = []
a_s.append(-omega2 * omega2 * x_s[0] - 2 * gamma * v_s[0])
a_s.append(-omega2 * omega2 * x_s[1] - 2 * gamma * v_s[1])
#standardowe
for i in range(2, len(t)):
x_s.append( 2 * x_s[i-1] - x_s[i-2] + (dt**2) * a_s[i-1])
a_s.append(-omega2 * omega2 * x_s[i] - 2 * gamma * v_s[i-1])
v_s.append((x_s[i] - x_s[i-2]) / (2*dt))
EK_s = []
EP_s = []
EC_s = []
for i in range(len(x_s)):
EK_s.append(0.5 * m * v_s[i]**2) # Energia kinetyczna
EP_s.append(0.5 * k * x_s[i]**2) # Energia potencjalna
EC_s.append(EK_s[i] + EP_s[i]) # Energia całkowita
plt.plot(t, x_s, '-b', t, v_s, '-r', t, a_s, '-g')
plt.xlim(0, 25)
plt.ylim(-10, 10)
plt.xlabel('t', fontsize = '14')
plt.ylabel('x(t), v(t), a(t)', fontsize = '14')
plt.legend(['x(t)', 'v(t)', 'a(t)'])
plt.grid(color = 'grey', linestyle = '--', linewidth = 0.2)
plt.show()
plt.plot(t, EC_s, '-b', t, EP_s, '-r', t, EK_s, '-g')
plt.xlim(0, 25)
#plt.ylim(-10, 10)
plt.xlabel('t', fontsize = '14')
plt.ylabel('EC, EP, EK', fontsize = '14')
plt.legend(['EC', 'EP', 'EK'])
plt.grid(color = 'grey', linestyle = '--', linewidth = 0.2)
plt.show()