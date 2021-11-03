import hashlib
import os
import sys
import random

from matplotlib import pyplot as plt

if len(sys.argv) < 2:
    print("not enough arguments!")
    exit(-1)
img_file_name = sys.argv[1]

only_one = "-o" in sys.argv

str_for_hash = "-l "
if only_one:
    str_for_hash += "-o "
str_for_hash += img_file_name

output_dir_name = f"find_k_output{hashlib.sha1(str_for_hash.encode('utf-8')).hexdigest()}"
if not os.path.exists(output_dir_name):
    os.mkdir(output_dir_name)

loss_values = []
run_index = []

for k in range(2, 21):
    flags = "-l"
    if only_one:
        flags += " -o"
    os.system(f"python3 k_means.py {img_file_name} {k} {flags} > /dev/null")
    str_for_hash = "-l -o " + str(k) + img_file_name
    hash_val = hashlib.sha1(str_for_hash.encode('utf-8')).hexdigest()
    file_name = f"output{hash_val}/loss_k{k}.txt"
    f = open(file_name, "r")
    loss_values.append(float(f.read()))
    f.close()
    os.remove(f"output{hash_val}/loss_k{k}.txt")
    os.remove(f"output{hash_val}/details.txt")
    os.rmdir(f"output{hash_val}")
    run_index.append(k)
    print(f"k = {k} finished! loss value: {loss_values[-1]}")

plt.plot(run_index, loss_values)

plt.xlabel('k')
plt.ylabel('loss value')
plt.title("K-Means")
plt.savefig(output_dir_name + "/" + "loss_graph.png")
