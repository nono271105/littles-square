import tkinter as tk
from tkinter import colorchooser

class ColoredGrid:
    def __init__(self, root):
        self.root = root
        self.root.title("Grille de Couleurs")

        self.grid_size = 10
        self.square_size = 80  # Size of each square in pixels

        # Predefined colors to cycle through
        self.colors = ["white", "red", "blue", "green", "yellow", "purple", "orange"]
        self.current_color_index = [[0 for _ in range(self.grid_size)] for _ in range(self.grid_size)]

        self.squares = []

        self.create_widgets()

    def create_widgets(self):
        self.canvas = tk.Canvas(self.root, width=self.grid_size * self.square_size,
                                height=self.grid_size * self.square_size, bg="lightgray", bd=0, highlightthickness=0)
        self.canvas.pack(padx=10, pady=10)

        for row in range(self.grid_size):
            row_of_squares = []
            for col in range(self.grid_size):
                x1 = col * self.square_size
                y1 = row * self.square_size
                x2 = x1 + self.square_size
                y2 = y1 + self.square_size
                
                # Create a rectangle on the canvas
                square_id = self.canvas.create_rectangle(x1, y1, x2, y2,
                                                         fill=self.colors[0], outline="black", width=1)
                
                # Bind a click event to each square
                self.canvas.tag_bind(square_id, "<Button-1>", lambda event, r=row, c=col: self.on_square_click(event, r, c))
                row_of_squares.append(square_id)
            self.squares.append(row_of_squares)

        # Button to choose a custom color
        self.custom_color_button = tk.Button(self.root, text="Choisir une couleur personnalisée", command=self.choose_custom_color)
        self.custom_color_button.pack(pady=5)
        self.custom_color = "white" # Default custom color

    def on_square_click(self, event, row, col):
        # Cycle to the next color in the list for the clicked square
        self.current_color_index[row][col] = (self.current_color_index[row][col] + 1) % len(self.colors)
        new_color = self.colors[self.current_color_index[row][col]]
        self.canvas.itemconfig(self.squares[row][col], fill=new_color)

    def choose_custom_color(self):
        color_code = colorchooser.askcolor(title="Choisissez une couleur")
        if color_code[1]:  # If a color is selected (not cancelled)
            self.custom_color = color_code[1]
            # Add the custom color to the list if it's not already there
            if self.custom_color not in self.colors:
                self.colors.append(self.custom_color)
                # To make new custom color the next color to be displayed, set current index of newly selected squares to that of custom color
                for row in range(self.grid_size):
                    for col in range(self.grid_size):
                        self.current_color_index[row][col] = self.colors.index(self.custom_color) - 1

if __name__ == "__main__":
    root = tk.Tk()
    app = ColoredGrid(root)
    root.mainloop()