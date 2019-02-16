import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1, 1, 50)
y1 = 2*x + 1
y2 = 5*x**2 - 1

plt.figure()

# difine the range of x and y
plt.xlim((-1, 1))
plt.ylim((-1, 3))

# define the label of x,y axis
plt.xlabel('X')
plt.ylabel('Y')

# define the ticks for each axis
xticks = ['bad', 'normal', 'good', r'$pretty\ good$']
plt.xticks([-1, -0.5, 0, 1], xticks)
plt.yticks([-1, 0, 0.5, 1.5, 2])

# gca(): get current axis
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data', 0))

# define plot what functions
l1, = plt.plot(x, y1, linewidth=1.0, linestyle='--', label='up')
l2, = plt.plot(x, y2, 'r', label='down')
plt.legend(handles=[l2, l1], labels=['aaa', 'bbb'], loc='best')

# add limited line
x0 = .25
y0 = 2
plt.scatter(x0, y0, s=50, color='black')
plt.plot([x0, x0], [0, y0], 'k--', lw=0.5)

# method 1 for adding annotation
plt.annotate(r'$%s+\alpha$' % y0, xy=(x0, y0), xycoords='data',
             xytext=(+30, -30), textcoords='offset points',
             fontsize=16,
             arrowprops=dict(arrowstyle='->', connectionstyle='arc3, rad=.2'))
# method 2 for adding annotation
plt.text(-0.5, 1, r'$\lambda{\sum_{i=1}^{yy}}\Omega$',
         fontdict={'size': 16, 'color': 'k'})

plt.show()
