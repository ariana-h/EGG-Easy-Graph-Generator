# EGG: Easy Graph Generator

Contributors: Ariana Huhko, Katelyn Elliott, and Taylor Hunter  
SUNY Polytechnic Institute   
CS 512: Software Engineering

## Overview
Easy Graph Generator, or EGG, is a graphical data visualization tool for effective visualizations of data for presentations and reporting. Graphs are generated using user input functions or datasets.

## How to Download Executable and Run
Open the EGG.exe file in this repo, click the download raw data file. 
This will go into your download file in which from there you can put in directory of your choice (desktop is suggested so one can see logo better).
Once you have downloaded and placed the EGG.exe file in the place you desire double click on the exe file.
You might get a pop-up screen from your device saying unknown publisher warning. 
For windows user press the more info button and then run anyways to get the program to run.
It will take a second to load but once loaded the application will appear on your screen.
## Can't run due to protection on device
Some devices won't let you run the application even when trying to ignore the protection on your device,
so if that is true highly recommend using VS Code and cloning this repository and then running the python program
in VS Code and then follow the how to use the Easy Graph Generator discussed below.

## Code Installation
To run the code directly, the following dependencies may have to be installed in your environment.

On Windows, Tkinter should be installed with Python by default.  

Other dependencies:  
`pip install matplotlib`   
`pip install numpy`   
`pip install pandas`   
`pip install pillow`   
`pip install sympy`


## How to use EGG: Easy Graph Generator
Once you open up or run the application the user interface will appear.
You will see the user input side on the left hand side of the user interface and the graph on the right side of the interface.

## Drop-down Button (Choosing the Graph)
The user will begin by choosing the graph type they desire via the drop-down button in the user interface which is located on the 
left side of the user interface under the text "Select Graph Type". The drop-dowm button says "Choose a graph" when application is first run.
The following are the type of graphs user can choose from (in order in which they appear in drop down button):
- Line Plot
- Bar Graph
- Pie Chart
- Pictograph
- Histogram
- Area Graph
- Scatter Plot

## Inputs and Expectations for Graphs
Once a user picks the type of graph they desire an input box will appear below the buttons (below the clear graph button to be exact).
Depending on which graph was chosen inputs will vary.
Here are examples of inputs for each graphs:
Examples for Line Plot Graph:

![Screenshot 2024-11-30 230151](https://github.com/user-attachments/assets/6e842901-6e98-4886-b081-ba67901c9b0e)

Limitations for Line Plot graph are that square root or sqrt is sill not available.

Examples of inputs for the other types of graph:

![Screenshot 2024-11-30 230216](https://github.com/user-attachments/assets/0e519da7-2da2-477d-b88f-b4c11f694cec)

Expectations:

Bar Graph - If user inputs A, 5 then a bar graph will appear and will graph the desired values)

Pie Chart - If user inputs A, 75 B, 25 then a pie chart will appear and will show A as 75% of the circle and B as 25% of the circle. If user enters numbers that dont add up to 100 percent it will determine the percentage of each category for you so if user just inputs A, 5 it will show A as 100%

Pictograph​ - ​If user inputs cat, 4 dog, 6 it will display 4 cat emojis and 6 dog emojis on graph. Limitations: Can only graph a certain kinds of emojis for a list of emojis that will appear on graph look at Emojis for Pictograph.txt file. When user inputs a emoji not listed in the list a question mark will appear on graph as a placeholder, so unknown, 1 will graph 1 "?" on the graph

Histogram - If user inputs 1,1,3,4,2 it will graph almost like a bar graph and show the frequency of the values listed.

Area Graph​ - If user inputs 1,2,3 it will show the area of those three values.

Scatter Plot​ - If user inputs 3,1 (on next line) 4,1 it will graph a point at 3,1 and a point at 4,1 and will connect the two points

Those were examples of inputs and a small description of what the user should except for each graph.

## Generating the Graph
Once the user inputs the necessary inputs for the graph that they desire. The user will then press the "Generate Graph" button which is directly below the drop-down button for the graph types.
When the user presses the Generate Graph button the graph, they desired along with the inputs they put in will graph on the graph on the right of the user interface.
If user inputs an invalid input, then an error window will appear, and the user will be told what is wrong with the input they entered and will be told to put in a valid input.

## Saving the Graph
Once the user graphs the graph, they desire they can either save the graph via the "Save Graph" button which will appear after user presses Generate Graph button, or they can clear 
the graph via the "Clear Graph" button. 
If user presses the "Save Graph" button, then your file explorer will open and you will be able to save your graph with name of your choice
as a .png file
Example of save:
If a user graphs a Pictograph of 4 dogs and 3 cats and presses the save button, the users file explorer will open and the user can name their graph whatever they desire such as Pictograph_Example, then user can pick were 
they want the image to be saved on their device and then after user presses the save button in file explorer a confirmation window will appear for user along with the directory path in which it was saved. Then if user wants to view
that graph later on they can do so by going to the location in which they saved the image and open it up to review the graph they saved.

## Clearing the Graph
After the user saves the graph or is just done with the graph in general the user can then press the "Clear Graph" button, and it will reset the graph completely and clear the input box as well. 
Then the user can either choose another type of graph or can put different inputs into the graph they chose before.
Users can also add inputs along with the already existing ones and press the Generate Graph button with it graphing the new inputs the user put in and the already existing ones.

## Importing Data
Finally, there is the "Import Data" button located below the "Generate Graph" button, this button allows users to import data that is in either a CSV file or an Excel file.
Once the user picks the file, they want it will automatically graph what is inside that file. 
At the moment the Import Data can only handle graphing data points and equations at the moment so files that have equations like x + 1 and data points like 1,2 for the Scatter plot graph.
So, the files imported can only contain those two types of inputs to graph successfully. 
Users can also save or clear the graph as they need when importing data.
