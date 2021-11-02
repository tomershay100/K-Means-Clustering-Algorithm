
# K-Means Clustering Algorithm
Implementation of a K-Means Clustering machine learning algorithm.

1. [General](#General)
    - [Background](#background)
    - [Running Instructions](https://github.com/tomershay100/K-Means-Clustering-Algorithm/blob/main/README.md#running-instructions)
2. [Dependencies](#dependencies) 
3. [Installation](#installation)

## General

### Background
Implementation of the ```K-Means``` algorithm in python, which allows you to turn an image displayed by lots of different colors into an image that contains a specific number of colors (k). This machine learning algorithm allows easy compression of the image.

By an image file, a number of colors and a couple of flags, the algorithm can be run on the image with the k that given by the user. After about 20 epochs or after the algorithm has converged, the program will export to an output files, the new image, a 3D model of the image (before and ater the algorithm), a ```.txt``` file that contains the k colors that the algorithm found to be the best, a ```.txt``` file that contains the minimum loss of the new image and a loss function graph. All of that of course, with the corresponding flags.

The 3D pixel diagram file that describing the state of the ```pixels``` and the ```centroids``` before running the algorithm, contains the pixels in their ```current color``` and in their location in the 3D graph, as well as contains the yellow and slightly larger centroids.
The 3D pixel diagram file that describing the image after the algorithm runs, contains the ```positions``` of the ```centroids``` (RGB values) in the three-dimensional space after moving during the algorithm, as well as in their new color.

The ```ex1.py``` code makes about 20 attempts to match the new colors to the image (using a K-Means algorithm that is executed over and over again), so that it can check at which time the lowest ```loss function``` was obtained. After realizing which colors are causing a lowest error, the program produces the new image as well as the rest of the files as described above.

The ```find_k.py``` code checkes all of the possible k's between 2 and 20 (by repeatedly running ```ex1.py``` with the ```-l``` flag), finds the loss of each of these k's and exports the information to a graph. Using this graph you can see which k brings the best results and use it to run ```ex1.py``` in order to export the final image.

You can see in the "output" folder examples of files that the algorithm created after running.### Running Instructions
#### ex1.py
The algorithm receives a couple of arguments in the following order:
First, the path to the ```image file``` (jpeg file). then a number (integer) that will be the number of colors the algorithm will used.

Also, the program gets up to 6 flags which can be added after the numbers of color argument:
* flag ```-c``` which instructs the program to export a ```colors_k{k}.txt``` file that contains the k colors that been use in the final image.
* flag ```-g``` which instructs the program to export the loss function graph to the ```loss_graph_k{k}.png``` file.
* flag ```-l``` which instructs the program to export the minimun loss value to the ```loss_k{k}.txt``` file.
* flag ```-i``` which instructs the program to export the image obtained after running the algorithm to the ```final_image_k{k}.jpeg``` file.
* flag ```-p``` which instructs the program to export a pair of images of the state of the pixels and centroids in three-dimensional space before and after running the algorithm. Note that this flag may cause the program to run for a long time.
* flag ```-o``` which instructs the program to perform only one round for the same k, of course while calculating all the other data. This flag should be used when it isn't necessary to find the minimum loss function or to calculate the final image in a shorter time.


running example (with ```-i``` and ```-p``` flags):
```
	$ python3 ex1.py dog.jpeg 2 -i -p
```
#### find_k.py
The program executes a call to ex1.py with any k between 2-20. The program receives as argument a path to the image file (jpeg file) on which the algorithm should be run each time. Running the program takes some time but you can save it by adding the ```-o``` flag which will cause the program to run for each k only once (actually, running ```ex1.py``` for each k with the ```-o``` flag).

running example (with ```-o``` flag):
```
	$ python3 find_k.py dog.jpeg -o
```
## Dependencies
* [Python 3.6+](https://www.python.org/downloads/)
* Git
* [NumPy](https://numpy.org/install/)
* [Matplotlib](https://matplotlib.org/stable/users/installing.html)

## Installation

1. Open the terminal
2. Clone the project by:
	```
	$ git clone https://github.com/tomershay100/K-Means-Clustering-Algorithm.git
	```	
3. Run the ```ex1.py``` file:
	```
	$ python3 ex1.py dog.jpeg 16 -i -l -p -c -g -o
	 ```
4. Or run the ```find_k.py``` file:
	```
	$ python3 find_k.py dog.jpeg -o
	 ```
