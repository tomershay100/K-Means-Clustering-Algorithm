
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

By an image file, a ```txt``` file containing 3D points (RGB pixels values) and a cupel of flags, the algorithm can be run on the image with the clusters specified in the ```txt``` file. After about 20 epochs or after the algorithm has converged, the program will export to an output file, the new cluster locations. You can also add flags to export the image obtained after running the algorithm, export the loss function graph during the iterations and also export a 3D diagram of the positions of the pixels and the centroids, before and after the algorithm run.

The 3D pixel diagram file that describing the state of the ```pixels``` and the ```centroids``` before running the algorithm, contains the pixels in their ```current color``` and in their location in the 3D graph, as well as contains the yellow and slightly larger centroids.
The 3D pixel diagram file that describing the image after the algorithm runs, contains the ```positions``` of the ```centroids``` (RGB values) in the three-dimensional space after moving during the algorithm, as well as in their new color.

### Running Instructions
In order to run the program, one has to create a ```txt``` file containing 3 numbers between 0 and 1 in each row separated by spaces. The number of rows will be the number of centroids to be used in the algorithm (k).

The algorithm receives as input a number of arguments in the following order:
First, the path to the ```image file``` (jpeg file). then a path to the ```centroids file``` (txt file) and a file name that the program will create in order to export the centroids positions obtained after running the algorithm.

Also, the program gets 3 flags which can be added at the end of the arguments:
* flag ```-i``` which instructs the program to export the image obtained after running the algorithm.
* flag ```-l``` which instructs the program to export the loss function graph to the file.
* flag ```-p``` which directs the program to export a pair of images of the state of the pixels and centroids in three-dimensional space before and after running the algorithm. Note that this flag may cause the program to run for a long time.

running example (with ```-i``` and ```-p``` flags):
```
	$ python3 ex1.py dog.jpeg cents_k2means.txt out.txt -i -p
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
3. Run the ex1.py file:
	```
	$ python3 ex1.py dog.jpeg cents_k2means.txt out.txt -i -l -p
	 ```
