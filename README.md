# Game of Life Simulation

This is an implementation of Conway's Game of Life, a cellular automaton devised by mathematician John Conway. The simulation consists of a grid of cells that can be either alive or dead, and evolves based on a set of rules.

## Rules (3B/S23)

1. Any live cell with fewer than two live neighbors dies, as if by underpopulation.
2. Any live cell with two or three live neighbors lives on to the next generation.
3. Any live cell with more than three live neighbors dies, as if by overpopulation.
4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

## Getting Started

### Prerequisites

To run this simulation, you need to have [Python](https://www.python.org/) installed on your system.

### Installation

1. Clone the repository or download the source code. `git clone https://github.com/Tim-977/Game-Of-Life`
2. Navigate to the project directory. `cd Game-Of-Life`
3. Install the required dependencies. `pip install -r requirements.txt`


### Usage

1. Start the simulation by running the main script. `python main.py`
2. The simulation will launch a graphical window displaying the initial state of the grid.
3. You can change rules of the game my modifying `RULE` in `B/S` format.
4. Set state for cells that you want to and press **Play/Pause** button to run it or you can use **Right Mouse Button** as well as **Space Bar**.
5. You can pause/resume the simulation at any time by clicking the **Play/Pause** button.
6. You can controle the delay (**Mouse weel up/down**) or press **More** and **Less** buttons to change the speed, you can **reset** speed as well.
7. To clear the board, click the **Clear** button.
8. You can generate random patterns by pressing **Random** button.
9. You can generate prepared patterns by pressing **Chess**; **Columns** and **Rows** buttons.
10. Buttons **1 - 8** create famouse constructions:

    **1 - Copperhead**

    **2 - Gosper Glider Gun**

    **3 - Pulsar**

    **4 - Penta-decathlon**

    **5 - Light Weight SpaceShip (LWSS)**

    **6 - Middle Weight SpaceShip (MWSS)**
    
    **7 - Heavy Weight SpaceShip (HWSS)**

    **8 - 106P135**

## Customization

You can customize the simulation by modifying the following parameters in the `main.py` script:

- `WIDTH_cells`: Sets horisontal dimension of the grid.
- `HEIGHT_cells`: Sets vertical dimension of the grid.
- `LEFT_MARGIN`: Sets horisontal offset.
- `TOP_MARGIN`: Sets vertical offset.
- `CELL_SIZE`: Sets the size of each cell.

Feel free to experiment with different values to create unique patterns and observe their evolution.

## Technologies Used

* [PyGame](https://www.pygame.org)

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request. 

You can follow these steps:

1.  Fork this repository
2.  Create a new branch: `git checkout -b feature/my-new-feature`
3.  Make changes and commit: `git commit -am 'Add some feature'`
4.  Push to the branch: `git push origin feature/my-new-feature`
5.  Submit a pull request


## Acknowledgments

- John Conway for his remarkable Game of Life concept.

## Credits

This project was created by Tim-977. 
>[GitHub](https://github.com/Tim-977)
>[Telegram](https://t.me/timbrzm)
>[Discord](https://discord.com/users/618793085735927808)

## *Have fun exploring the fascinating world of the Game of Life!*


