import json
import random

import pygame


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
        #self.board = [[(i + j) % 2 for i in range(self.width)] for j in range(self.height)]
        with open("patterns\\board_1.json", "r") as file:
            json_data = file.read()
        self.board = json.loads(json_data)
    
    # Create columns cells pattern
    def columns_board(self):
        #self.board = [[i % 2 for i in range(self.width)] for j in range(self.height)]
        with open("patterns\\board_2.json", "r") as file:
            json_data = file.read()
        self.board = json.loads(json_data)
    
    # Create rows cells pattern
    def rows_board(self):
        #self.board = [[j % 2 for i in range(self.width)] for j in range(self.height)]
        with open("patterns\\board_3.json", "r") as file:
            json_data = file.read()
        self.board = json.loads(json_data)
    
    # Create copperhead
    def copperhead_board(self):
        with open("patterns\\copperhead.json", "r") as file:
            json_data = file.read()
        self.board = json.loads(json_data)
    
    # Create Gosper Glider Gun
    def gosperglidergun_board(self):
        with open("patterns\\gosperglidergun.json", "r") as file:
            json_data = file.read()
        self.board = json.loads(json_data)
    
    # Create Pulsar
    def pulsar_board(self):
        with open("patterns\\pulsar.json", "r") as file:
            json_data = file.read()
        self.board = json.loads(json_data)
    
    # Create Penta-decathlon
    def pentadecathlon_board(self):
        with open("patterns\\pentadecathlon.json", "r") as file:
            json_data = file.read()
        self.board = json.loads(json_data)
    
    # Create Light Weight SpaceShip (LWSS)
    def LWSS_board(self):
        with open("patterns\\LWSS.json", "r") as file:
            json_data = file.read()
        self.board = json.loads(json_data)
    
    # Create Middle Weight SpaceShip (MWSS)
    def MWSS_board(self):
        with open("patterns\\MWSS.json", "r") as file:
            json_data = file.read()
        self.board = json.loads(json_data)
    
    # Create Heavy Weight SpaceShip (HWSS)
    def HWSS_board(self):
        with open("patterns\\HWSS.json", "r") as file:
            json_data = file.read()
        self.board = json.loads(json_data)
    
    # Create 106P135 pattern
    def cycledgliders_board(self):
        with open("patterns\\cycledgliders.json", "r") as file:
            json_data = file.read()
        self.board = json.loads(json_data)
    
    # Save board into a file
    def save_board(self):
        with open("patterns\\board.json", "w", encoding="UTF-8") as file:
            file.write("[\n")
            for i, sublist in enumerate(self.board):
                file.write(json.dumps(sublist))
                if i != len(self.board) - 1:
                    file.write(",\n")
                else:
                    file.write("\n")
            file.write("]")
   
    # -- For debug --
    #def load_board(self):
    #    with open("board.json", "r") as file:
    #        json_data = file.read()
    #    self.board = json.loads(json_data)
    #    print('NEW')


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
                pygame.draw.rect(screen, "#262626",
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

                RULE = "B3/S23"
                born, survive = extract_numbers(RULE)
                if str(s) in born:
                    new_board[y][x] = 1
                elif str(s) not in survive:
                    new_board[y][x] = 0

        self.board = new_board[:]


def extract_numbers(st):
    b_index, s_index = st.index('B') + 1, st.index('S') + 1
    b_number, s_number = '', ''

    while b_index < len(st) and st[b_index].isdigit():
        b_number += st[b_index]
        b_index += 1

    while s_index < len(st) and st[s_index].isdigit():
        s_number += st[s_index]
        s_index += 1

    return b_number, s_number

def add_delay():
    global speed
    speed += 1 if speed < 99 else 0

def reduce_delay():
    global speed
    speed -= 1 if not not speed else 0

def speed_reset():
    global speed
    speed = 5

def pause_play():
    global time_on
    time_on = not time_on

def main():
    global speed
    global time_on

    WIDTH_cells = 75
    HEIGHT_cells = 61
    LEFT_MARGIN = 10
    TOP_MARGIN = 10
    CELL_SIZE = 10

    pygame.init()
    size = 1000, 630  # The size of the game window
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    pygame.display.set_caption('The Game Of Life')

    board = Life(WIDTH_cells, HEIGHT_cells, LEFT_MARGIN, TOP_MARGIN, CELL_SIZE)  # Create a Life instance with specific dimensions

    time_on = False
    ticks = 0  # Counter to control the speed of animation
    speed = 5  # Initial speed value

    text_speed_label = Label("Delay", (900, 15), "black", 34)
    speed_label = Label(str(speed), (900, 90), "black", 70)

    clear_button = Button(780, 10, 80, 30, "Clear", "#df1d28", "#8d0209", 34, board.clear_board)
    random_button = Button(780, 55, 80, 30, "Random", "#FC328D", "#70163F", 27, board.random_board)
    chess_button = Button(780, 100, 80, 30, "Chess", "#262626", "#0D0D0D", 27, board.chess_board)
    columns_button = Button(780, 145, 80, 30, "Columns", "#262626", "#0D0D0D", 25, board.columns_board)
    rows_button = Button(780, 190, 80, 30, "Rows", "#262626", "#0D0D0D", 25, board.rows_board)
    speed_up_button = Button(900, 50, 70, 30, "More", "#23E016", "#10610A", 30, add_delay)
    speed_down_button = Button(900, 140, 70, 30, "Less", "#1929E0", "#0B1261", 28, reduce_delay)
    speed_reset_button = Button(890, 190, 90, 30, "Reset", "#EB7517", "#61310A", 30, speed_reset)
    pause_play_button = Button(890, 235, 90, 30, "Pause/Play", "#F01406", "#700A02", 24, pause_play)

    button_1 = Button(790 + 37 * 0 + 0, 530, 37, 37, "1", "#1C1C1C", "#000000", 35, board.copperhead_board)
    button_2 = Button(790 + 37 * 1 + 10, 530, 37, 37, "2", "#1C1C1C", "#000000", 35, board.gosperglidergun_board)
    button_3 = Button(790 + 37 * 2 + 20, 530, 37, 37, "3", "#1C1C1C", "#000000", 35, board.pulsar_board)
    button_4 = Button(790 + 37 * 3 + 30, 530, 37, 37, "4", "#1C1C1C", "#000000", 35, board.pentadecathlon_board)
    button_5 = Button(790 + 37 * 0 + 0, 577, 37, 37, "5", "#1C1C1C", "#000000", 35, board.LWSS_board)
    button_6 = Button(790 + 37 * 1 + 10, 577, 37, 37, "6", "#1C1C1C", "#000000", 35, board.MWSS_board)
    button_7 = Button(790 + 37 * 2 + 20, 577, 37, 37, "7", "#1C1C1C", "#000000", 35, board.HWSS_board)
    button_8 = Button(790 + 37 * 3 + 30, 577, 37, 37, "8", "#1C1C1C", "#000000", 35, board.cycledgliders_board)


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
                speed_up_button.handle_event(event)
                speed_down_button.handle_event(event)
                speed_reset_button.handle_event(event)
                pause_play_button.handle_event(event)
                button_1.handle_event(event)
                button_2.handle_event(event)
                button_3.handle_event(event)
                button_4.handle_event(event)
                button_5.handle_event(event)
                button_6.handle_event(event)
                button_7.handle_event(event)
                button_8.handle_event(event)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE or event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                time_on = not time_on  # Toggle the animation state on spacebar press or right mouse button click
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 4:
                speed += 1 if speed < 99 else 0 # Increase the animation speed on mouse wheel up
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 5:
                speed -= 1 if not not speed else 0  # Decrease the animation speed on mouse wheel down
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                mouse_pos = pygame.mouse.get_pos() # Get mouse coords (--debug)
                print(f"Mouse clicked at coordinates: {mouse_pos}")
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_w:
                board.save_board() # Save the board into the file
                print('Saved')
            #elif event.type == pygame.KEYDOWN and event.key == pygame.K_l:
            #    board.load_board() # Load the board
            #    print('Loaded')
        
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
        speed_reset_button.draw(screen)
        pause_play_button.draw(screen)

        button_1.draw(screen)
        button_2.draw(screen)
        button_3.draw(screen)
        button_4.draw(screen)
        button_5.draw(screen)
        button_6.draw(screen)
        button_7.draw(screen)
        button_8.draw(screen)

        pygame.draw.rect(screen, "black", (890, 10, 90, 170), 4)
        pygame.draw.rect(screen, "black", (780, 520, 198, 104), 4)

        if ticks >= speed:
            if time_on:
                board.next_move()  # Calculate and apply the next move if enough time has passed
            ticks = 0
        pygame.display.flip()
        clock.tick(120)
        ticks += 1
    pygame.quit()


if __name__ == "__main__":
    main()
