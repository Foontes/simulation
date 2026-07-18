class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cells = [[0 for _ in range(width)] for _ in range(height)]

    def set_cell(self, x, y, value):
        self.cells[y][x] = value

    def get_cell(self, x, y):
        return self.cells[y][x]

    def display(self):
        for row in self.cells:
            print(" ".join(str(cell) for cell in row))