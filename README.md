# Zen.py
Sudoku solver, with a simple, crisp user-interface.

# Running the algorithm:
To run *only* the core algorithm, run `Algo.py`, and enter the sudoku board as a 2D nested list, with 9 rows and 9 columns, where 0s represent empty cells.
To run the algorithm with the integrated interface, run `interface.py`.

# Requirements:
1. The core text-based algorithm needs a Python 3.x install; no modules / external dependencies are needed.
2. The Interface version needs [Pygame (2.x)](https://www.pygame.org/wiki/about), [threading](https://docs.python.org/3/library/threading.html), [time](https://docs.python.org/3/library/time.html).

# The Interface:
It uses Pygame to render the sudoku board as a 9x9 grid. The cells can be interacted with, by clicking on them, and clicking 1-9 on the keyboard, that changes value of that particular cell.
The "Solve" button runs the core algorithm whilst keeping the window up, and "Clear Board" does what it says, verbatim.

# Efficiency:
The algorithm steps a bit away from a traditional approach to solving the sudoku boards. It is faster than isolated Backtracking for positions where a unique solution exists.

# How the Algorithm works:
1) It stores a 2D array of all possible elements that can be filled in a cell according to sudoku rules.
2) It finds singletons and replaces them in the grid with its only possible value and further eliminates possible values in respective row, column and 3x3 box.
3) It fills the unique possible element in the cell which is not in its row(s), column(s) or 3x3 grid section.
4) It uses backtracking to further solve the sudoku board when it can't find any singletons or unique elements.

# Dependency usage:
`Pygame` is used for rendering absolutely everything on the screen. `Threading` (for parallelism) is essential, for the algorithm run times may vary, and if the pygame window instance does not get updated per frame, there is a huge possibility that it will crash and / or become unresponsive. As a result, the algorithm runs in a separate native thread, whilst the window stays up. 

`time` is used for measuring the time taken by the core algorithm in solving a particular position.

# The program in-action:
`NOTE: The program runs at a crisp 700+ FPS on an average on Windows (Not clocked).`
(The red square indicates where the mouse pointer is, inside of the root window.)

![image](https://user-images.githubusercontent.com/112420208/197784503-4aa17525-eed0-406a-a4f9-a08ac571900b.png)

![image](https://user-images.githubusercontent.com/112420208/197783181-2ceffce5-e3b6-4a05-94d2-45f4572366d3.png)
