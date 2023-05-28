import random

import pygame

#TODO:
# ~~ Play/Pause button
# ~~ Mouse hold
# ~~ Patterns (Objects)
# ~~ New organisms...


class Label:
    def __init__(self, text, position, color, font):
        self.text = text
        self.position = position
        self.color = color
        self.font = font
    
    def update(self, text=None, position=None, color=None, font=None):
        if text is not None:
            self.text = text
        if position is not None:
            self.position = position
        if color is not None:
            self.color = color
        if font is not None:
            self.font = font

    def draw(self, surface):
        font = pygame.font.SysFont(None, self.font)
        label_text = font.render(self.text, True, self.color)
        surface.blit(label_text, self.position)


class Button:
    def __init__(self, x, y, width, height, text, color, hover_color, font, callback):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.font = font
        self.callback = callback

    def draw(self, screen):
        pygame.draw.rect(screen, self.hover_color if self.is_hovered() else self.color, self.rect)
        font = pygame.font.Font(None, self.font)
        text = font.render(self.text, True, (255, 255, 255))
        text_rect = text.get_rect(center=self.rect.center)
        screen.blit(text, text_rect)

    def is_hovered(self):
        return self.rect.collidepoint(pygame.mouse.get_pos())

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.is_hovered():
                self.callback()


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
    
    # Kill all the cells
    def clear_board(self):
        self.board = [[0] * self.width for _ in range(self.height)]
    
    # Create random cells pattern
    def random_board(self):
        self.board = [[random.randint(0, 1) for i in range(self.width)] for j in range(self.height)]
    
    # Create chessboard cells pattern
    def chess_board(self):
        self.board = [[(i + j) % 2 for i in range(self.width)] for j in range(self.height)]
    
    # Create columns cells pattern
    def columns_board(self):
        self.board = [[i % 2 for i in range(self.width)] for j in range(self.height)]
    
    # Create rows cells pattern
    def rows_board(self):
        self.board = [[j % 2 for i in range(self.width)] for j in range(self.height)]


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
    size = 1000, 630  # The size of the game window
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    pygame.display.set_caption('The Game Of Life')

    board = Life(75, 61, 10, 10, 10)  # Create a Life instance with specific dimensions
    # (width_cells, height_cells, left_margin=10, top_margin=10, cell_size=30)

    time_on = False
    ticks = 0  # Counter to control the speed of animation
    speed = 10  # Initial speed value

    text_speed_label = Label("Delay", (900, 15), "black", 34)
    speed_label = Label(str(speed), (900, 90), "black", 70)

    clear_button = Button(780, 10, 80, 30, "Clear", "#df1d28", "#8d0209", 34, board.clear_board)
    random_button = Button(780, 55, 80, 30, "Random", "#FC328D", "#70163F", 27, board.random_board)
    chess_button = Button(780, 100, 80, 30, "Chess", "#262626", "#0D0D0D", 27, board.chess_board)
    columns_button = Button(780, 145, 80, 30, "Columns", "#262626", "#0D0D0D", 25, board.columns_board)
    rows_button = Button(780, 190, 80, 30, "Rows", "#262626", "#0D0D0D", 25, board.rows_board)
    speed_up_button = Button(900, 50, 70, 30, "NULL", "#23E016", "#10610A", 30, board.clear_board)
    speed_down_button = Button(900, 140, 70, 30, "NULL", "#1929E0", "#0B1261", 30, board.clear_board)


    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False  # Exit the game loop if the window is closed
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                board.get_click(event.pos)  # Handle left mouse button click
                clear_button.handle_event(event)
                random_button.handle_event(event)
                chess_button.handle_event(event)
                columns_button.handle_event(event)
                rows_button.handle_event(event)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE or event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                time_on = not time_on  # Toggle the animation state on spacebar press or right mouse button click
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 4:
                speed += 1 if speed < 99 else 0 # Increase the animation speed on mouse wheel up
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 5:
                speed -= 1 if not not speed else 0  # Decrease the animation speed on mouse wheel down
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                mouse_pos = pygame.mouse.get_pos()
                print(f"Mouse clicked at coordinates: {mouse_pos}")
        
        speed_label.update(text=str(speed))

        screen.fill(('gray'))
        board.render(screen)

        speed_label.draw(screen)
        text_speed_label.draw(screen)

        clear_button.draw(screen)
        random_button.draw(screen)
        chess_button.draw(screen)
        columns_button.draw(screen)
        rows_button.draw(screen)
        speed_up_button.draw(screen)
        speed_down_button.draw(screen)

        pygame.draw.rect(screen, "black", (890, 10, 90, 170), 1)

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
