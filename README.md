# Dijkstra at pixel level to solve/ navigate through a pixel puzzle.
The map of the puzzle is as shown below.
![Image of the Map](https://github.com/HKyatham/Pixel_Puzzle_Using_Dijstra/blob/main/Generated%20Images/Map_of_Environment.png)

This code is written specific to the above map. The dimentions of the map are shown in the below image.
![Image of the Map](https://github.com/HKyatham/Pixel_Puzzle_Using_Dijstra/blob/main/Generated%20Images/Map_of_Environment_with_Dimensions.png)

To run the code download the [dijkstra python file](https://github.com/HKyatham/Pixel_Puzzle_Using_Dijstra/blob/main/dijkstra_Hitesh_kyatham.py) and run it using the command
```python dijkstra_Hitesh_kyatham.py```

Once the code starts running it will ask for start index x value followed by start index y value, similarly for goal index x and y values. 

Once entered it will generate the environment image and as shown above.

Then the code will run based on selected start and goal indices and then generate as nodes are explored and this will be highlighted in green.

Finally the code will backtrack and highlight the shotest path from the start index to goal index.
![Image of the Map](https://github.com/HKyatham/Pixel_Puzzle_Using_Dijstra/blob/main/Generated%20Images/Shortest_Path_in_Map.png)
