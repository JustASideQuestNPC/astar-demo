import PySimpleGUI as sg
from maze_generator import Maze_Generator

COLOR_CODES = {
    'selected': 'red',
}

generator = Maze_Generator((30, 20))

def process_maze(grid: list[str], special_points: dict, color_codes: dict = COLOR_CODES) -> str:
    return ''.join(f'{row}\n' for row in grid)

layout = [
    [sg.Text('A* Pathfinding (WIP)')],
    [sg.Multiline(process_maze(generator.decode_grid(), {}), size = (50, 20), disabled = True)],
    [sg.Exit()]
]

window = sg.Window('A* Pathfinding (WIP)', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'exit':
        break

window.close()