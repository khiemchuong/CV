import matplotlib.pyplot as plt
import numpy as np

fig,ax = plt.subplots()
x=np.linspace(start=-10,stop=10,num=1000)
def ham_bac_4(a,b,x):
    f=a*x**4+b*x**2-3
    return f
def ham_bac_3(a,b,x):
    f = a*x**3+b*x
    return f
def ham_bac_2(a,b,x):
    f = a*x**2+b
    return f
def ham_bac_1(a,x):
    f = a*x
    return f
y1 = ham_bac_4(1,-2,x)
y2=ham_bac_3(4,-4,x)
y3=ham_bac_2(12,-4,x)
y4=ham_bac_1(24,x)
ax.plot(x,y1)
ax.plot(x,y2)
ax.plot(x,y3)
ax.plot(x,y4)
ax.plot(x,y1,label=r'$y=x^{4}-2x^{2}-3$')
ax.plot(x,y2,label=r'$y=4x^{3}-4x$')
ax.plot(x,y3,label=r'$y=12x^{2}-4$')
ax.plot(x,y4,label=r'$y=24x$')
ax.set_xlabel("trục hoành-x")
ax.set_ylabel("trục tung-y")
ax.legend()
plt.show()