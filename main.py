# main.py
import tkinter as tk
import ttkbootstrap as ttk
from models.task import TaskManager
from ui.task_view import TaskView
from config.settings import Settings

def main():
    root = ttk.Window()  # No need to specify the theme here
    root.title("Daily Task Prioritizer")
    task_manager = TaskManager()
    task_view = TaskView(root, task_manager, language=Settings.DEFAULT_LANGUAGE)
    root.mainloop()

if __name__ == "__main__":
    main()