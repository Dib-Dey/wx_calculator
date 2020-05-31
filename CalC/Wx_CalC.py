import os


def main():
    """
    Another method to entry to the Python
    """
    command_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "main_gui_frame.py")
    os.system(command_path)


if __name__ == "__main__":
    main()