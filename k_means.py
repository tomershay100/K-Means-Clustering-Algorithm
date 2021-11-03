# Tomer Shay, 323082701
import hashlib
import os
import random
import matplotlib.pyplot as plt
import numpy as np
import sys

if len(sys.argv) < 2:
    print("not enough arguments!")
    exit(-1)
img_file_name = sys.argv[1]

if len(sys.argv) < 3:
    print("you must enter the number of colors (k)!")
    exit(-1)
k = int(sys.argv[2])

# flags
colors_flag = "-c" in sys.argv
loss_graph_flag = "-g" in sys.argv
loss_value_flag = "-l" in sys.argv
image_out_flag = "-i" in sys.argv
pixels_3d_flag = "-p" in sys.argv
only_one = "-o" in sys.argv

str_for_hash = ""
flags_str = ""
if colors_flag:
    str_for_hash += "-c "
if loss_graph_flag:
    str_for_hash += "-g "
if loss_value_flag:
    str_for_hash += "-l "
if image_out_flag:
    str_for_hash += "-i "
if pixels_3d_flag:
    str_for_hash += "-p "
if only_one:
    str_for_hash += "-o "
flags_str = str_for_hash
str_for_hash += str(k)
str_for_hash += img_file_name

output_dir_name = f"output{hashlib.sha1(str_for_hash.encode('utf-8')).hexdigest()}"
if not os.path.exists(output_dir_name):
    os.mkdir(output_dir_name)

print("output folder name: " + output_dir_name)
printed_messages = ""

orig_pixels = plt.imread(img_file_name)
img_pixels = orig_pixels.astype(float) / 255.
orig_pixels = img_pixels.copy()
pixels = img_pixels.copy().reshape(-1, 3)  # pixels is array of all the pixels in the image


# calculate the distance between two 3D points
def pixel_cet_dist(a, b):  # a - pixel, b - centroid
    x = a[0] - b[0]
    y = a[1] - b[1]
    z = a[2] - b[2]
    return np.sqrt(x ** 2 + y ** 2 + z ** 2)


# calculate the closest centroid (by minimum distance)
def close_cent(pixel_cor, centroids_arr):
    min_dist = 3
    min_i = -1
    for e in range(len(centroids_arr)):
        cent = centroids_arr[e]
        dist = pixel_cet_dist(pixel_cor, cent)
        if dist < min_dist:
            min_dist = dist
            min_i = e
    return min_i


# calculate the average of 3D pixels (x avg, y avg and z avg)
def avg_pixels(pixels_arr):
    global pixels
    x_avg, y_avg, z_avg = 0, 0, 0  # x - red, y - green, z - blue

    pixels_index_arr = np.array(pixels_arr)
    pixel_count = len(pixels_index_arr)
    if pixel_count == 0:
        return -1

    for pixel_i in pixels_index_arr:
        x_avg += pixels[pixel_i][0]
        y_avg += pixels[pixel_i][1]
        z_avg += pixels[pixel_i][2]
    return [x_avg / pixel_count, y_avg / pixel_count, z_avg / pixel_count]


# for each centroid, calculate its new position (by average)
def change_cents(cents_map):
    global centroids
    new_cents = []
    for e in cents_map:
        new_cent = avg_pixels(cents_map[e])
        if new_cent == -1:  # if there is no pixels related to that centroid
            new_cents.append(centroids[e])
        else:
            new_cents.append(new_cent)
    return new_cents


# add all of the nearest pixels to the list of their centroid
def iteration(centroids_arr):
    cents_map = {}
    for e in range(len(centroids_arr)):
        cents_map[e] = []

    for e in range(len(pixels)):
        cents_map[close_cent(pixels[e], centroids_arr)].append(e)
    return cents_map


# calculate the average distance of all the pixels from their centroid.
def calc_loss(cents_map, cents):
    global img_pixels, pixels

    dist_sum = 0
    for e in cents_map:
        for pixel_i in cents_map[e]:
            dist_sum += pixel_cet_dist(pixels[pixel_i], cents[e])
    return dist_sum / len(img_pixels)


def rand_rgb():
    temp = []
    for _ in range(3):
        temp.append(random.randint(0, 255) / 255.)
    return temp


loss_cents_map = {}

num_of_checks = 20
if only_one:
    num_of_checks = 1

for i in range(num_of_checks):

    centroids = []
    for _ in range(k):
        centroids.append(rand_rgb())
    orig_cents = centroids.copy()

    centroids_map = {}

    loss_values = []
    iter_values = []
    new_centroids = []

    for iter in range(50):
        centroids_map = iteration(centroids)
        new_centroids = np.array(change_cents(centroids_map)).round(4)

        if np.array_equal(new_centroids, centroids):  # all centroids didn't move at all
            break
        centroids = new_centroids

        loss_values.append(calc_loss(centroids_map, centroids))
        iter_values.append(iter)

    loss_cents_map[round(loss_values[-1], 2)] = {"centroids": centroids.copy(), "original centroids": orig_cents.copy(),
                                                 "loss values": loss_values.copy(),
                                                 "iteration values": iter_values.copy(),
                                                 "centroids map": centroids_map.copy()}

    if (i > 5 and len(loss_cents_map.keys()) == 1) or (i > 10 and len(loss_cents_map.keys()) <= 3):
        break
    # print(f"[iter {k}]: loss: {round(loss_values[-1], 2)}")

min_key = min(loss_cents_map.keys())
min_values = loss_cents_map[min_key]

if colors_flag:  # if there is -c flag, output the final chosen colors to "colors_k{k}.txt" file.
    file_name_str = f"colors_k{k}.txt"
    f = open(output_dir_name + "/" + file_name_str, "w")
    f.write(f"{','.join([str(i) for i in np.array(min_values['centroids'] * 225).astype(int)])}")
    f.close()

    to_print = f"{file_name_str} contains the only {len(min_values['centroids'])} colors that been used in the final " \
               f"image. "
    printed_messages += "\n" + to_print
    print(to_print)

if loss_value_flag:  # if there is -l flag, output the final loss value to "loss_k{k}.txt" file.
    file_name_str = f"loss_k{k}.txt"
    f = open(output_dir_name + "/" + file_name_str, "w")
    f.write(f"{min_key}")
    f.close()

    to_print = f"{file_name_str} contains the final loss value of the best iteration."
    printed_messages += "\n" + to_print
    print(to_print)

if image_out_flag:  # if there is -k flag, create the output compressed file.
    for i in range(len(min_values["centroids map"])):
        for j in range(len(min_values["centroids map"][i])):
            pixels[min_values["centroids map"][i][j]] = min_values["centroids"][i]  # change the pixel by its centroid

    img_pixels = pixels.reshape(128, 128, 3)
    file_name_str = f"final_image_k{k}.jpeg"
    plt.imsave(output_dir_name + "/" + file_name_str, img_pixels)

    to_print = f"{file_name_str} contains the final image with only {len(min_values['centroids'])} colors."
    printed_messages += "\n" + to_print
    print(to_print)

if loss_graph_flag:  # if there is -g flag, create the output loss function graph.
    plt.plot(min_values["iteration values"], min_values["loss values"])

    plt.text(min_values["iteration values"][-1], min_values["loss values"][-1],
             str(round((min_values["loss values"])[-1], 2)))

    plt.xlabel('iteration')
    plt.ylabel('loss value')
    title_str = "K-Means, k = " + str(len(min_values["centroids"]))
    plt.title(title_str)
    file_name_str = f"loss_graph_k{k}.png"
    plt.savefig(output_dir_name + "/" + file_name_str)

    to_print = f"{file_name_str} contains the loss function graph of the algorithm."
    printed_messages += to_print
    print(to_print)

if pixels_3d_flag:  # if there is -p flag, create the output pixels graph.
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    temp_pixels = orig_pixels.reshape(-1, 3)
    for pixel in temp_pixels:
        r_val = pixel[0]
        g_val = pixel[1]
        b_val = pixel[2]
        ax.scatter(r_val * 255, g_val * 255, b_val * 255, facecolor=(r_val, g_val, b_val))

    for centroid in min_values["original centroids"]:  # original centroids, before the k-means algorithm
        r_val = centroid[0]
        g_val = centroid[1]
        b_val = centroid[2]
        ax.scatter(r_val * 255, g_val * 255, b_val * 255, s=150, edgecolor="black", facecolor="gold")

    ax.set_xlabel('Red')
    ax.set_ylabel('Green')
    ax.set_zlabel('Blue')
    ax.view_init(25, 10)
    title_str = "K-Means, k = " + str(len(min_values["centroids"]))
    plt.title(title_str)
    file_name_str = f"3D_model_init_k{k}.png"
    plt.savefig(output_dir_name + "/" + file_name_str)

    to_print = f"{file_name_str} contains the centroids and the pixels position in a 3D space. The centroids are " \
               f"bigger and their color is yellow. "
    printed_messages += "\n" + to_print
    print(to_print)

    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    for centroid in min_values["centroids"]:  # new centroids, after the k-means algorithm
        r_val = centroid[0]
        g_val = centroid[1]
        b_val = centroid[2]
        ax.scatter(r_val * 255, g_val * 255, b_val * 255, s=100, edgecolor=(1 - r_val, 1 - g_val, 1 - b_val),
                   facecolor=(r_val, g_val, b_val))

    ax.set_xlabel('Red')
    ax.set_ylabel('Green')
    ax.set_zlabel('Blue')
    ax.view_init(20, 10)
    title_str = "K-Means, k = " + str(len(min_values["centroids"]))
    plt.title(title_str)
    file_name_str = f"3D_model_after_k{k}.png"
    plt.savefig(output_dir_name + "/" + file_name_str)

    to_print = f"{file_name_str} contains the centroids position in a 3D space. The centroid's color is their real " \
               f"color. "
    printed_messages += to_print
    print(to_print)

f = open(output_dir_name + "/details.txt", "w")
f.write(
    f"This output folder contains all the output files for the K-Means algorithm with k = {k} on the {img_file_name}"
    f" image file.\nThe flags used in the algorithm are: {flags_str}\n\n" + printed_messages)
f.close()
