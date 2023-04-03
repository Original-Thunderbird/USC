import matplotlib.pyplot as plt
import numpy as np

input_size = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
CPU_efficient = np.array([0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5])
CPU_basic = np.array([0.25, 1.5, 1.75, 2.5, 2.75, 3.5, 3.75, 4.5, 4.75, 5.5])

memory_efficient = np.array([0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5])
memory_basic = np.array([0.25, 1.5, 1.75, 2.5, 2.75, 3.5, 3.75, 4.5, 4.75, 5.5])


fig, ax = plt.subplots(1, 2)

ax[0].plot(input_size, CPU_basic, marker='o')
ax[0].plot(input_size, CPU_efficient, marker='P')
ax[0].set_title('CPU Time vs problem size')
ax[0].legend(['basic', 'memory efficient'])
ax[0].set(xlabel = 'problem size - product of sizes of two strings', ylabel= 'CPU time (s)')

ax[1].plot(input_size, memory_basic, marker='o')
ax[1].plot(input_size, memory_efficient, marker='P')
ax[1].set_title('Memory Usage')
ax[1].legend(['basic', 'memory efficient'])
ax[1].set(xlabel = 'problem size - product of sizes of two strings', ylabel= 'memory usage (kb)')

plt.show()