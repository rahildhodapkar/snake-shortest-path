# Snake Shortest Path
## Table of Contents
1. [Description](#description)
2. [Demo](#demo)
3. [How to Use](#how-to-use)
4. [Gameplay](#gameplay)
5. [Technologies Used](#technologies-used)
6. [Contact Information](#contact-information)

## Description
Snake Shortest Path is a program that allows a user to either manually play Snake, or utilize a shortest-path algorithm to automatically control the snake's movement. The game currently has three algorithms:   
1. [Breadth-First-Search](https://www.freecodecamp.org/news/exploring-the-applications-and-limits-of-breadth-first-search-to-the-shortest-paths-in-a-weighted-1e7b28b3307/)
2. [A* Search](https://en.wikipedia.org/wiki/A*_search_algorithm)
3. [Greedy Best-First Search](https://en.wikipedia.org/wiki/Best-first_search)

![image](https://github.com/rahildhodapkar/snake-shortest-path/assets/115059842/b9d4ae67-4660-4780-a98d-ed5551317388)

## Demo
1. Vid 1
2. Vid 2
3. Vid 3
4. Vid 4
## How to Use
Ensure you have the following:
1. Python 3.x
2. Dependencies listed in 'requirements.txt'

First, clone this repository:
```
git clone https://github.com/rahildhodapkar/snake-shortest-path.git
```
Navigate to the cloned directiory and install the required dependencies using:
```
pip install -r requirements.txt
```
To launch the game, run the following command in the cloned directory:
```
python main.py
```
## Gameplay
On startup, the user will be greeted by the following:

![image](https://github.com/rahildhodapkar/snake-shortest-path/assets/115059842/32efa7fa-bf18-4f0a-b7dd-31f9783e4c46)

Using their keyboard, the user can choose which gamemode they would like to use. 

If they choose to play manually, the arrow keys or WASD keys are to be used for controlling the snake's moves, and the snake will not begin moving until one of those eight keys is pressed. 

If they choose to use one of the shortest-path algorithms, the snake will automatically begin utilizing the algorithm to find efficient paths between the snake and the next bit of food.

## Technologies Used
Snake Shortest Path is written entirely in Python3. The project uses the retro game engine [Pyxel](https://github.com/kitao/pyxel). 

## Contact Information
Developer: Rahil Dhodapkar

Email: rahildhodapkar@gmail.com


Thank you for checking Snake Shortest Path out!



