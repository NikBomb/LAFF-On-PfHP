import matplotlib.pyplot as plt
from output_IJP import data


n = [int(x) for x in data[0::6]]
time = [float(x) for x in data[3::6]]
GFLOPS = [float(x) for x in data[4::6]]
plt.plot(n, time)
plt.xlabel("matrix dimens m=n=k")
plt.ylabel("Time in sec.")

plt.show()

plt.plot(n, GFLOPS)
plt.xlabel("matrix dimens m=n=k")
plt.ylabel("GFLOPS")
ax = plt.gca()
ax.set_ylim([0, 4])

plt.show()

