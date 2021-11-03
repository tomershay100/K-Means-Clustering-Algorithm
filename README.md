
# K-Means Clustering Algorithm
Implementation of a K-Means Clustering machine learning algorithm.

1. [General](#General)
    - [Background](#background)
    - [Program Structure](https://github.com/tomershay100/K-Means-Clustering-Algorithm/blob/main/README.md#program-structure)
    - [Running Instructions](https://github.com/tomershay100/K-Means-Clustering-Algorithm/blob/main/README.md#running-instructions)
    - [About The Output Files](https://github.com/tomershay100/K-Means-Clustering-Algorithm/blob/main/README.md#about-the-output-files)
2. [Dependencies](#dependencies) 
3. [Installation](#installation)

## General

### Background
Implementation of the ```K-Means``` algorithm in python, which allows you to turn an image displayed by lots of different colors into an image that contains a specific number of colors (k). This machine learning algorithm allows easy compression of the image.

By an image file, a number of colors and a couple of flags, the algorithm can be run on the image with the k that given by the user. After about 20 epochs or after the algorithm has converged, the program will export to an output files the new image, a 3D model of the image (before and ater the algorithm), a ```.txt``` file that contains the k colors that the algorithm found to be the best, a ```.txt``` file that contains the minimum loss of the new image and a loss function graph. All of that of course, with the corresponding flags.

### Program Structure
The ```k_means.py``` code makes about 20 attempts to match the new colors to the image (using a K-Means algorithm that is executed over and over again), so that it can check at which time the lowest ```loss function``` was obtained. After realizing which colors are causing a lowest error, the program produces the new image as well as the rest of the files as described above.

The ```find_k.py``` code checkes all of the possible k's between 2 and 20 (by repeatedly running ```k_means.py``` with the ```-l``` flag), finds the loss of each of these k's and exports the information to a graph. Using this graph you can see which k brings the best results and use it to run ```k_means.py``` in order to export the final image.

### About The Output Files
#### k_means.py
As stated above, with the help of corresponding flags the program can export several files:
* ```details.txt``` file contains information about the program execution, such as the image on which the algorithm was run, the number k and the flags with which the program ran. In addition, contains the program output (the text printed to the screen).
* ```colors_k.txt``` file contains the final colors to which the algorithm has converged. These are the colors used to create the new image.
* ```loss_graph_k.png``` file contains the graph of the loss function of the new image during the iterations of the algorithm.
* ```loss_k.txt``` file contains the final loss value of the new image.
* ```final_image_k.jpeg``` file contains the final image obtained after running the algorithm.
* ```3D_model_init_k.png``` file contains a three-dimensional model of the pixels and the centroids values in space. The pixels are shown in their original color in the image while the centroids are larger than them and are also shown in yellow.
* ```3D_model_after_k.png``` file contains a three-dimensional model of the centroid values in space. The centroids are shown in their original and final color in the image. In fact, each pixel changed its color according to the centroid closest to it.

All of these files are created within an output folder with a unique name that corresponds to the program execution values (by hash). You can see examples of some runs in the output folder

#### find_k.py
The program executes a call to ```k_means.py``` with any k between 2-20 with the flag ```-l```. The code reads the ```k_means.py``` output in the ```loss_k.txt``` file and then deletes the created folder. At the end of the pass on all of the k's the code exports into the output folder (unique calculated by the arguments using hash) a ```loss_graph.png``` file containing the loss as a dependency on k.

 You can see examples of some runs in the output folder

### Running Instructions
#### k_means.py
The algorithm receives a couple of arguments in the following order:
First, the path to the ```image file``` (jpeg file). then a number (integer) that will be the number of colors the algorithm will used.

Also, the program gets up to 6 flags which can be added after the numbers of color argument:
* flag ```-c``` which instructs the program to export the ```colors_k.txt``` file.
* flag ```-g``` which instructs the program to export the loss function graph to the ```loss_graph_k.png``` file.
* flag ```-l``` which instructs the program to export the minimun loss value to the ```loss_k.txt``` file.
* flag ```-i``` which instructs the program to export the image obtained after running the algorithm to the ```final_image_k.jpeg``` file.
* flag ```-p``` which instructs the program to export the 3D models to the  ```3D_model_init_k.png``` and the  ```3D_model_after_k.png``` files.
* flag ```-o``` which instructs the program to perform only one round for the same k. This flag should be used when it isn't necessary to find the minimum loss function or to calculate the final image in a shorter time.


running example (with ```-i``` and ```-p``` flags):
```
	$ python3 k_means.py dog.jpeg 2 -i -p
```
#### find_k.py
The program executes a call to ex1.py with any k between 2-20. The program receives as argument a path to the image file (jpeg file) on which the algorithm should be run each time. Running the program takes some time but you can save it by adding the ```-o``` flag which will cause the program to run for each k only once (actually, running ```k_means.py``` for each k with the ```-o``` flag).

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
3. Run the ```k_means.py``` file:
	```
	$ python3 k_means.py dog.jpeg 16 -i -l -p -c -g -o
	 ```
4. Or run the ```find_k.py``` file:
	```
	$ python3 find_k.py dog.jpeg -o
	 ```
