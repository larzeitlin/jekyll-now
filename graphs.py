import numpy as np
import matplotlib.pyplot as plt

# Create a figure of size 8x6 inches, 80 dots per inch
plt.figure(figsize=(20, 6), dpi=80)

# Create a new subplot from a grid of 1x1
plt.subplot(1, 1, 1)

X = np.linspace(0, 20., 1000, endpoint=True)
C, S = np.cos(X - 1), np.sin(X - 1)

ax = plt.gca()  # gca stands for 'get current axis'
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))



# Set x limits
plt.xlim(0., 20.0)

# Set x ticks
plt.xticks(np.linspace(0, 0, 0, endpoint=True))

# Set y limits
plt.ylim(-1.5, 1.5)

# Set y ticks
plt.yticks(np.linspace(-1.0, 1.0, 5, endpoint=True))



plt.plot(X, C, color="blue", linewidth=2.5, linestyle="-", label="cosine (N-1)")
plt.plot(X, S, color="red",  linewidth=2.5, linestyle="-", label="i sine (N-1)")

plt.legend(loc='upper left')

# Save figure using 72 dots per inch
# plt.savefig("exercice_2.png", dpi=72)

# Show result on screen



plt.show()