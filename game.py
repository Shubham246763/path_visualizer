import pygame
import sys
from collections import deque
from tkinter import messagebox, Tk
import math

# Initialize Pygame
pygame.init()

# Define the screen size
size = (width, height) = 1000, 480
win = pygame.display.set_mode(size)
pygame.display.set_caption("Dijkstra's, BFS, and A* Path Finding")
clock = pygame.time.Clock()

# Define the number of columns and rows for the grid
cols, rows = 48, 32
w = width // (3 * cols)
h = height // rows

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (220, 220, 220)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Define grid, queue, visited nodes, and path for all algorithms
grid_dijkstra = []
queue_dijkstra = deque()
path_dijkstra = []

grid_bfs = []
queue_bfs = deque()
path_bfs = []

grid_a_star = []
open_set_a_star = []
closed_set_a_star = []
path_a_star = []

# Class for each spot in the grid
class Spot:
    def __init__(self, i, j):
        self.x, self.y = i, j
        self.f, self.g, self.h = 0, 0, 0
        self.neighbors = []
        self.prev = None
        self.wall = False
        self.visited = False

    def show(self, win, col, offset_x=0):
        """Draw the spot on the screen."""
        if self.wall:
            col = BLACK
        pygame.draw.rect(win, col, (self.x * w + offset_x, self.y * h, w - 1, h - 1))

    def add_neighbors(self, grid):
        """Add neighbors to the spot."""
        if self.x < cols - 1:
            self.neighbors.append(grid[self.x + 1][self.y])
        if self.x > 0:
            self.neighbors.append(grid[self.x - 1][self.y])
        if self.y < rows - 1:
            self.neighbors.append(grid[self.x][self.y + 1])
        if self.y > 0:
            self.neighbors.append(grid[self.x][self.y - 1])

def heuristic(a, b):
    """Heuristic function for A*."""
    return abs(a.x - b.x) + abs(a.y - b.y)

# Function to handle mouse movement for adding walls
def hoverWall(pos):
    i = pos[0] // w
    j = pos[1] // h
    if i < cols and j < rows:
        if i < cols:
            grid_dijkstra[i][j].wall = True
            grid_bfs[i][j].wall = True
            grid_a_star[i][j].wall = True

# Create the grids
for i in range(cols):
    arr_dijkstra = []
    arr_bfs = []
    arr_a_star = []
    for j in range(rows):
        arr_dijkstra.append(Spot(i, j))
        arr_bfs.append(Spot(i, j))
        arr_a_star.append(Spot(i, j))
    grid_dijkstra.append(arr_dijkstra)
    grid_bfs.append(arr_bfs)
    grid_a_star.append(arr_a_star)

# Add neighbors to each spot
for i in range(cols):
    for j in range(rows):
        grid_dijkstra[i][j].add_neighbors(grid_dijkstra)
        grid_bfs[i][j].add_neighbors(grid_bfs)
        grid_a_star[i][j].add_neighbors(grid_a_star)

# Define start and end spots
start_dijkstra = grid_dijkstra[0][0]
end_dijkstra = grid_dijkstra[cols - 1][rows - 1]
start_bfs = grid_bfs[0][0]
end_bfs = grid_bfs[cols - 1][rows - 1]
start_a_star = grid_a_star[0][0]
end_a_star = grid_a_star[cols - 1][rows - 1]

start_dijkstra.wall = False
end_dijkstra.wall = False
start_bfs.wall = False
end_bfs.wall = False
start_a_star.wall = False
end_a_star.wall = False

# Initialize queues and start nodes
queue_dijkstra.append(start_dijkstra)
start_dijkstra.visited = True

queue_bfs.append(start_bfs)
start_bfs.visited = True

open_set_a_star.append(start_a_star)

# Main loop for the application
def main():
    flag_dijkstra = False
    noflag_dijkstra = True
    startflag_dijkstra = False

    flag_bfs = False
    noflag_bfs = True
    startflag_bfs = False

    flag_a_star = False
    noflag_a_star = True
    startflag_a_star = False

    while True:
        # Event handling loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEMOTION:
                if pygame.mouse.get_pressed()[0] or pygame.mouse.get_pressed()[2]:
                    hoverWall(pygame.mouse.get_pos())
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    startflag_dijkstra = True
                    startflag_bfs = True
                    startflag_a_star = True

        # Dijkstra's Algorithm loop
        if startflag_dijkstra:
            if len(queue_dijkstra) > 0:
                current = queue_dijkstra.popleft()
                if current == end_dijkstra:
                    temp = current
                    while temp.prev:
                        path_dijkstra.append(temp.prev)
                        temp = temp.prev
                    if not flag_dijkstra:
                        flag_dijkstra = True
                        print("Dijkstra's Algorithm Done")
                if not flag_dijkstra:
                    for i in current.neighbors:
                        if not i.visited and not i.wall:
                            i.visited = True
                            i.prev = current
                            queue_dijkstra.append(i)
            else:
                if noflag_dijkstra and not flag_dijkstra:
                    Tk().wm_withdraw()
                    messagebox.showinfo("No Solution", "There was no solution for Dijkstra's Algorithm")
                    noflag_dijkstra = False

        # BFS Algorithm loop
        if startflag_bfs:
            if len(queue_bfs) > 0:
                current = queue_bfs.popleft()
                if current == end_bfs:
                    temp = current
                    while temp.prev:
                        path_bfs.append(temp.prev)
                        temp = temp.prev
                    if not flag_bfs:
                        flag_bfs = True
                        print("BFS Algorithm Done")
                if not flag_bfs:
                    for i in current.neighbors:
                        if not i.visited and not i.wall:
                            i.visited = True
                            i.prev = current
                            queue_bfs.append(i)
            else:
                if noflag_bfs and not flag_bfs:
                    Tk().wm_withdraw()
                    messagebox.showinfo("No Solution", "There was no solution for BFS Algorithm")
                    noflag_bfs = False

        # A* Algorithm loop
        if startflag_a_star:
            if len(open_set_a_star) > 0:
                current = min(open_set_a_star, key=lambda o: o.f)
                if current == end_a_star:
                    temp = current
                    while temp.prev:
                        path_a_star.append(temp.prev)
                        temp = temp.prev
                    if not flag_a_star:
                        flag_a_star = True
                        print("A* Algorithm Done")
                if not flag_a_star:
                    open_set_a_star.remove(current)
                    closed_set_a_star.append(current)
                    for neighbor in current.neighbors:
                        if neighbor in closed_set_a_star or neighbor.wall:
                            continue
                        temp_g = current.g + 1
                        new_path = False
                        if neighbor not in open_set_a_star:
                            open_set_a_star.append(neighbor)
                            new_path = True
                        elif temp_g < neighbor.g:
                            new_path = True
                        if new_path:
                            neighbor.g = temp_g
                            neighbor.h = heuristic(neighbor, end_a_star)
                            neighbor.f = neighbor.g + neighbor.h
                            neighbor.prev = current
            else:
                if noflag_a_star and not flag_a_star:
                    Tk().wm_withdraw()
                    messagebox.showinfo("No Solution", "There was no solution for A* Algorithm")
                    noflag_a_star = False

        # Drawing loop
        win.fill(GRAY)

        # Draw Dijkstra's grid
        for i in range(cols):
            for j in range(rows):
                spot = grid_dijkstra[i][j]
                spot.show(win, WHITE)
                if spot in path_dijkstra:
                    spot.show(win, GREEN)
                    spot.show(win, RED, 0)
                elif spot.visited:
                    spot.show(win, BLUE)
                if spot in queue_dijkstra and not flag_dijkstra:
                    spot.show(win, WHITE)
                    spot.show(win, BLUE, 0)
                if spot == start_dijkstra:
                    spot.show(win, GREEN)
                if spot == end_dijkstra:
                    spot.show(win, BLUE)

        # Draw BFS grid
        for i in range(cols):
            for j in range(rows):
                spot = grid_bfs[i][j]
                spot.show(win, WHITE, offset_x=width // 3)
                if spot in path_bfs:
                    spot.show(win, GREEN, offset_x=width // 3)
                    spot.show(win, RED, 0)
                elif spot.visited:
                    spot.show(win, BLUE, offset_x=width // 3)
                if spot in queue_bfs and not flag_bfs:
                    spot.show(win, WHITE, offset_x=width // 3)
                    spot.show(win, BLUE, 0)
                if spot == start_bfs:
                    spot.show(win, GREEN, offset_x=width // 3)
                if spot == end_bfs:
                    spot.show(win, BLUE, offset_x=width // 3)

        # Draw A* grid
        for i in range(cols):
            for j in range(rows):
                spot = grid_a_star[i][j]
                spot.show(win, WHITE, offset_x=2 * width // 3)
                if spot in path_a_star:
                    spot.show(win, GREEN, offset_x=2 * width // 3)
                    spot.show(win, RED, 0)
                elif spot in closed_set_a_star:
                    spot.show(win, BLUE, offset_x=2 * width // 3)
                if spot in open_set_a_star and not flag_a_star:
                    spot.show(win, WHITE, offset_x=2 * width // 3)
                    spot.show(win, BLUE, 0)
                if spot == start_a_star:
                    spot.show(win, GREEN, offset_x=2 * width // 3)
                if spot == end_a_star:
                    spot.show(win, BLUE, offset_x=2 * width // 3)

        pygame.display.flip()
        clock.tick(60)

# Run the main function
if __name__ == "__main__":
    main()
