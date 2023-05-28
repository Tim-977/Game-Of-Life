import pygame


class Board:

    def __init__(self, width, height, left=10, top=10, cell_size=30):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 0  # Left margin
        self.top = 0  # Top margin
        self.cell_size = 0
        self.set_view(left, top, cell_size)

    # Render method is responsible for drawing the board on the screen.
    def render(self, screen):
        for y in range(self.height):
            for x in range(self.width):
                # The outline of each cell on the screen
                pygame.draw.rect(screen, pygame.Color(0, 0, 0), 
                (x * self.cell_size + self.left, y * self.cell_size + self.top, self.cell_size, self.cell_size), 1)

    # View parameters for the board
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    # Handle the click event on the board
    def on_click(self, cell):
        pass

    # Convert mouse position to cell coordinates
    def get_cell(self, mouse_pos):
        cell_x = (mouse_pos[0] - self.left) // self.cell_size
        cell_y = (mouse_pos[1] - self.top) // self.cell_size
        # Check if the cell coordinates are within the board boundaries
        if cell_x < 0 or cell_x >= self.width or cell_y < 0 or cell_y >= self.height:
            return None
        return cell_x, cell_y

    # Handle the click event by calling the on_click method with cell coordinates
    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        if cell:
            self.on_click(cell)


class Life(Board):

    def __init__(self, width, height, left=10, top=10, cell_size=30):
        super().__init__(width, height, left, top, cell_size)

    # Handle the click event on the Game of Life board
    def on_click(self, cell):
        # Toggle the state of the clicked cell
        # Alive - 1
        # Dead - 0
        self.board[cell[1]][cell[0]] = (self.board[cell[1]][cell[0]] + 1) % 2

    # Render method overrides the parent's render method to draw alive cells in black.
    def render(self, screen):
        for y in range(self.height):
            for x in range(self.width):
                if self.board[y][x]:
                    # Draw alive cells in black
                    pygame.draw.rect(screen, pygame.Color("black"), 
                    (x * self.cell_size + self.left, y * self.cell_size + self.top, self.cell_size, self.cell_size))
                # Draw the outline of each cell
                pygame.draw.rect(screen, pygame.Color(0, 0, 0),
                (x * self.cell_size + self.left, y * self.cell_size + self.top, self.cell_size, self.cell_size), 1)

    # Calculate the next move
    def next_move(self):
        new_board = [[cell for cell in row] for row in self.board]

        for y in range(self.height):
            for x in range(self.width):
                s = 0  # Sum of neighbor cells
                for dy in range(-1, 2):
                    for dx in range(-1, 2):
                        # Skip cells outside the board boundaries
                        if (x + dx < 0 or x + dx >= self.width or y + dy < 0 or y + dy >= self.height):
                            continue
                        s += self.board[y + dy][x + dx]  # Add the state of the neighbor cell
                s -= self.board[y][x]  # Subtract the state of the current cell
                # Rules: B3/S23
                if s == 3:
                    new_board[y][x] = 1
                elif s < 2 or s > 3:
                    new_board[y][x] = 0

        self.board = new_board[:]


def main():
    pygame.init()
    size = 1000, 600  # The size of the game window
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    pygame.display.set_caption('The Game Of Life')

    board = Life(20, 20, 10, 10, 25)  # Create a Life instance with specific dimensions
    # (width_cells, height_cells, left_margin=10, top_margin=10, cell_size=30)

    time_on = False
    ticks = 0  # Counter to control the speed of animation
    speed = 30  # Initial speed value

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False  # Exit the game loop if the window is closed
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                board.get_click(event.pos)  # Handle left mouse button click
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE or event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                time_on = not time_on  # Toggle the animation state on spacebar press or right mouse button click
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 4:
                speed += 1  # Increase the animation speed on mouse wheel up
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 5:
                speed -= 1  # Decrease the animation speed on mouse wheel down

        screen.fill(('gray'))
        board.render(screen)
        if ticks >= speed:
            if time_on:
                board.next_move()  # Calculate and apply the next move if enough time has passed
            ticks = 0
        pygame.display.flip()
        clock.tick(100)
        ticks += 1
    pygame.quit()


if __name__ == "__main__":
    main()