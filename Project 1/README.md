# Project 1: Search

### Problem statement: [Project 1](Project%201%20-%20Search.pdf)
### Work division

Project framework building division:
| Student ID | Name                 |
| ---------- | -------------------- |
| 22125108   | Vòng Vĩnh Toàn       |

Visualization division:
| Student ID | Name                 |
| ---------- | -------------------- |
| 22125077   | Nguyễn Hoàng Phúc    |

Validation division:
| Student ID | Name                 |
| ---------- | -------------------- |
| 22125038   | Huỳnh Đăng Khoa      |
| 22125049   | Huỳnh Hà Phương Linh |

Algorithm implementations division:
| Student ID | Name                 | Algorithm            |
| ---------- | -------------------- | -------------------- |
| 22125038   | Huỳnh Đăng Khoa      | Breadth First Search |
| 22125049   | Huỳnh Hà Phương Linh | Depth First Search   |
| 22125077   | Nguyễn Hoàng Phúc    | Uniform Cost Search  |
| 22125108   | Vòng Vĩnh Toàn       | A* Search            |

Test generation division:
| Student ID | Name                 | Test generation      |
| ---------- | -------------------- | -------------------- |
| 22125038   | Huỳnh Đăng Khoa      | input-01 to input-05 |
| 22125049   | Huỳnh Hà Phương Linh | input-06 to input-10 |

Please write the test case overviews after designing the test cases below.
| Test case | row | col | rockCount | description |
| --------- | --- | --- | --------- | ----------- |
| input-01  |  6   | 11    | 1          |   Easy: There is one stone in line with the agent and the switch           |
| input-02  |  10   | 20    |   3        |   Hard: Switches are scattered in many directions on the map. Although two of them are surrounded by walls, complete paths are required to reach the solution.          |
| input-03  |  8 | 12 | 2 | Moderate: Two stones are placed in a vertical line with two switches and there is only one way to push the rocks into the switches
| input-04  | 12    |  30   |     4      |  Moderate:  The large map with switches are next to each other in the centre of the maze.         |
| input-05  |  13   |  35   |    5       |  Hard: Four switches are to the corners of the map while the remaining one is in the centre. Additionally, there are two rocks next to each other, requiring the agent to choose an appropriate solution           |
| input-06  |  6 | 12   | 2          |  Easy: Clear path from rocks to switches.       |
| input-07  |   9 |7    | 4          |  Moderate: One rock pre-placed on incorrect switch. Initial maneuvering required for two rocks, remaining steps are straightforward.       |
| input-08  |   7  | 12    |      3     |   Hard: Narrow maze with three rocks (two adjacent, two near a wall), requiring careful maneuvering.          |
| input-09  |  7  |   9 |      6     |   Hard: Narrow maze with six rocks. Four rocks are incorrectly positioned on switches, and two completely block the path. Rocks cannot be pushed all the way, requiring careful maneuvering and strategic placement to create space to reach other rocks.          |
| input-10  |  11   | 20    |    1       |   Hard: Even though there is only one stone and switch and they are only separated by a wall, there is no answer for this case. This is because walls are designed to create a loop path that curbs the agent from reaching the solution           |

### Run the project

To run the project, run the following command:
```bash
cd ./22125038_22125049_22125077_22125108/Source/
python main.py
```

### Project notes

Everyone is recommended to use Anaconda/Miniconda for managing the environments.

To create the environment, run the following command:
```bash
conda create -n AI-P1 python=3.10
conda activate AI-P1
```

If you cannot afford a Anaconda/Miniconda manager, you can create a new virtual environment integrated into Python itself. Make sure before creating the environment, your Python version is atleast 3.10. To check your Python version, run:
```bash
python --version
```

To create a new virtual environment, make sure you are in the directory (relative to this file) `./22125038_22125049_22125077_22125108/Source/` and run this command:
```bash
python -m venv venv
```

Now each time you open the project, make sure to activate the environment, to activate you can run something like this:
```bash
.\venv\Scripts\activate
```
Depends on the Python version you have, the path to `activate` may be different.

Now to check that the environment is activated, your command line should look something like this:
![Indication for your success in activating the environment](Environment%20successfully%20activated.png)

To install the required packages, run the following command:
```bash
cd ./Source/22125038_22125049_22125077_22125108/
pip install -r requirements.txt
```

To update the packages in your Python environment, please run:
```bash
pip freeze > requirements.txt
```

We will use **Pygame** for visualization.

Commit frequently and use Github Copilot for better commit messages.
![Copilot commit suggestion](Copilot%20commit%20suggestion.png)
