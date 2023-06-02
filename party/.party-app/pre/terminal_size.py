from os import get_terminal_size

def t_s_main():
    return {"width":get_terminal_size().columns, "height":get_terminal_size().lines}