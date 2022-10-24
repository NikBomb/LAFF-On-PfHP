import matplotlib.pyplot as plt
from output_IJP import data


n = [int(x) for x in data[0::6]]
time = [float(x) for x in data[3::6]]

plt.plot(n, time)
plt.xlabel("matrix dimens m=n=k")
plt.ylabel("Time in sec.")


plt.show()

