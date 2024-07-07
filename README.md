
# Pathfinding Visualization

This repository contains a Pygame-based visualization of three popular pathfinding algorithms: Dijkstra's Algorithm, Breadth-First Search (BFS), and A* Search Algorithm.

## Features

- **Visualization**: Displays the execution of Dijkstra's, BFS, and A* algorithms side-by-side on a grid.
- **Interactive Grid**: Click and drag the mouse to create walls, adding obstacles for the algorithms to navigate around.
- **Real-time Updates**: Watch the algorithms as they explore the grid and find the shortest path.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/Shubham246763/Pathfinding-Visualization.git
    cd Pathfinding-Visualization
    ```

2. Install the required dependencies:
    ```sh
    pip install pygame
    ```

## Usage

1. Run the script:
    ```sh
    python pathfinding_visualization.py
    ```

2. Use the mouse to draw walls on the grid:
    - Left-click to add a wall.
    - Right-click to remove a wall.

3. Press the `Enter` key to start the pathfinding algorithms.

## Algorithms

### Dijkstra's Algorithm
Dijkstra's Algorithm finds the shortest path from the start node to the end node by exploring the nodes with the smallest cumulative cost first.

### Breadth-First Search (BFS)
BFS explores all nodes at the present depth level before moving on to nodes at the next depth level, ensuring the shortest path in an unweighted grid.

### A* Search Algorithm
A* uses a heuristic to prioritize nodes that are estimated to be closer to the goal, combining the benefits of Dijkstra's Algorithm and Greedy Best-First-Search.

## Controls

- **Left-click**: Add a wall.
- **Right-click**: Remove a wall.
- **Enter**: Start the pathfinding algorithms.



## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

