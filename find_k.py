import os
import sys

from matplotlib import pyplot as plt

if len(sys.argv) < 2:
    print("not enough arguments!")
    exit(-1)
img_file_name = sys.argv[1]

only_one = "-o" in sys.argv

loss_values = []
run_index = []

for i in range(2, 21):
    flags = "-l"
    if only_one:
        flags += " -o"
    os.system(f"python3 ex1.py {img_file_name} {i} {flags} > /dev/null")
    file_name = f"loss_k{i}.txt"
    f = open(file_name, "r")
    loss_values.append(float(f.read()))
    run_index.append(i)
    print(f"k = {i} finished! loss value: {loss_values[-1]}")

plt.plot(run_index, loss_values)

plt.xlabel('k')
plt.ylabel('loss value')
plt.title("K-Means")
plt.savefig("loss_graph.png")
