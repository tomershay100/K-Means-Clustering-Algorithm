# Tomer Shay, 323082701

import matplotlib.pyplot as plt
import numpy as np
import sys

img_file_name = sys.argv[1]
centroid_file_name = sys.argv[2]
out_file_name = sys.argv[3]

loss_flag = 0
out_flag = 0
pixels_3d_flag = 0

for the report
if len(sys.argv) >= 5:
    if sys.argv[4] == "-i":
        out_flag = 1
    elif sys.argv[4] == "-l":
        loss_flag = 1
    elif sys.argv[4] == "-p":
        pixels_3d_flag = 1

if len(sys.argv) >= 6:
    if sys.argv[5] == "-i":
        out_flag = 1
    elif sys.argv[5] == "-l":
        loss_flag = 1
    elif sys.argv[5] == "-p":
        pixels_3d_flag = 1

if len(sys.argv) == 7:
    if sys.argv[6] == "-i":
        out_flag = 1
    elif sys.argv[6] == "-l":
        loss_flag = 1
    elif sys.argv[6] == "-p":
        pixels_3d_flag = 1

centroids = np.loadtxt(centroid_file_name)
orig_cents = centroids.copy()
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
    for i in range(len(centroids_arr)):
        cent = centroids_arr[i]
        dist = pixel_cet_dist(pixel_cor, cent)
        if dist < min_dist:
            min_dist = dist
            min_i = i
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
    for i in cents_map:
        new_cent = avg_pixels(cents_map[i])
        if new_cent == -1:  # if there is no pixels related to that centroid
            new_cents.append(centroids[i])
        else:
            new_cents.append(new_cent)
    return new_cents


# add all of the nearest pixels to the list of their centroid
def iteration(centroids_arr):
    cents_map = {}
    for i in range(len(centroids_arr)):
        cents_map[i] = []

    for i in range(len(pixels)):
        cents_map[close_cent(pixels[i], centroids_arr)].append(i)
    return cents_map


# calculate the average distance of all the pixels from their centroid.
def calc_loss(cents_map, cents):
    global img_pixels, pixels

    dist_sum = 0
    for i in cents_map:
        for pixel_i in cents_map[i]:
            dist_sum += pixel_cet_dist(pixels[pixel_i], cents[i])
    return dist_sum / len(img_pixels)


output_text, output_line, output_line_before = "", "", ""
centroids_map = {}

loss_val = []
iter_val = []

for iter in range(20):
    centroids_map = iteration(centroids)
    new_centroids = np.array(change_cents(centroids_map)).round(4)
    output_line = f"[iter {iter}]:{','.join([str(i) for i in new_centroids])}\n"
    output_text += output_line
    if np.array_equal(new_centroids, centroids):  # all centroids doesn't move at all
        break
    centroids = new_centroids

    if loss_flag:
        loss_val.append(calc_loss(centroids_map, centroids))
        iter_val.append(iter)

f = open(out_file_name, "w")
f.write(output_text)
f.close()

if out_flag:  # if there is -i flag, create the output compressed file.
    for i in range(len(centroids_map)):
        for j in range(len(centroids_map[i])):
            pixels[centroids_map[i][j]] = centroids[i]  # change the pixel by its centroid

    img_pixels = pixels.reshape(128, 128, 3)
    file_name_str = "image_k" + str(len(centroids)) + "means.jpeg"
    plt.imsave(file_name_str, img_pixels)

if loss_flag:  # if there is -l flag, create the output loss function graph.
    plt.plot(iter_val, loss_val)

    plt.text(iter_val[-1], loss_val[-1], str(round(loss_val[-1], 1)))

    plt.xlabel('iteration')
    plt.ylabel('loss value')
    title_str = "K-Means, k = " + str(len(centroids))
    plt.title(title_str)
    file_name_str = "graph_k" + str(len(centroids)) + "means.png"
    plt.savefig(file_name_str)

if pixels_3d_flag:  # if there is -p flag, create the output pixels graph.
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    temp_pixels = orig_pixels.reshape(-1, 3)
    for pixel in temp_pixels:
        r_val = pixel[0]
        g_val = pixel[1]
        b_val = pixel[2]
        ax.scatter(r_val * 255, g_val * 255, b_val * 255, facecolor=(r_val, g_val, b_val))

    for centroid in orig_cents:  # original centroids, before the k-means algorithm
        r_val = centroid[0]
        g_val = centroid[1]
        b_val = centroid[2]
        ax.scatter(r_val * 255, g_val * 255, b_val * 255, s=150, edgecolor="black", facecolor="gold")

    ax.set_xlabel('Red')
    ax.set_ylabel('Green')
    ax.set_zlabel('Blue')
    ax.view_init(25, 10)
    title_str = "K-Means, k = " + str(len(centroids))
    plt.title(title_str)
    plt.savefig("all_pixels" + str(len(centroids)) + "_before.png")

    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    for centroid in centroids:  # new centroids, after the k-means algorithm
        r_val = centroid[0]
        g_val = centroid[1]
        b_val = centroid[2]
        ax.scatter(r_val * 255, g_val * 255, b_val * 255, s=100, edgecolor=(1 - r_val, 1 - g_val, 1 - b_val),
                   facecolor=(r_val, g_val, b_val))

    ax.set_xlabel('Red')
    ax.set_ylabel('Green')
    ax.set_zlabel('Blue')
    ax.view_init(20, 10)
    title_str = "K-Means, k = " + str(len(centroids))
    plt.title(title_str)
    plt.savefig("all_pixels" + str(len(centroids)) + "_after.png")
