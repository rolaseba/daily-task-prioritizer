# ui/task_view.py
import tkinter as tk
import ttkbootstrap as ttk
from tkinter import messagebox
from models.task import TaskCategory
from utils.translation_manager import TranslationManager
from config.constants import UIConstants
from config.settings import Settings  

class TaskView:
    """
    A GUI view for managing tasks, including adding, marking as completed, and deleting tasks.
    The view displays tasks in two categories: obligatory and optional.
    """
    def __init__(self, root, task_manager, language=Settings.DEFAULT_LANGUAGE):
        """
        Initializes the TaskView.

        Args:
            root (tk.Tk): The root window for the application.
            task_manager (TaskManager): The task manager responsible for handling task logic.
            language (str, optional): The language for the UI. Defaults to Settings.DEFAULT_LANGUAGE.
        """
        self.root = root
        self.task_manager = task_manager
        self.translation_manager = TranslationManager(language)
        self.setup_ui()

    def setup_ui(self):
        """Sets up the user interface for the task view."""
        self.root.geometry(f"{UIConstants.WINDOW_WIDTH}x{UIConstants.WINDOW_HEIGHT}")
        self.root.resizable(False, False)

        # Apply the theme from settings
        style = ttk.Style()  # Create a Style object
        style.theme_use(Settings.DEFAULT_THEME)  # Apply the theme

        # Task Entry Section
        self.task_entry_frame = ttk.Frame(self.root)
        self.task_entry_frame.pack(fill=tk.X, padx=10, pady=10)  # Expand horizontally

        self.task_entry_label = ttk.Label(self.task_entry_frame, text=self.translation_manager.get("task_entry_label"))
        self.task_entry_label.pack(anchor="w")  # Align to the left

        self.task_entry = ttk.Entry(self.task_entry_frame)
        self.task_entry.pack(fill=tk.X, pady=5)  # Expand horizontally

        # Category Selection (Radio Buttons)
        self.category_var = tk.StringVar(value=TaskCategory.OBLIGATORY.name)
        self.category_obligatory = ttk.Radiobutton(
            self.task_entry_frame,
            text=self.translation_manager.get("obligatory_label"),
            variable=self.category_var,
            value=TaskCategory.OBLIGATORY.name
        )
        self.category_obligatory.pack(anchor="w")  # Align to the left

        self.category_optional = ttk.Radiobutton(
            self.task_entry_frame,
            text=self.translation_manager.get("optional_label"),
            variable=self.category_var,
            value=TaskCategory.OPTIONAL.name
        )
        self.category_optional.pack(anchor="w")  # Align to the left

        self.add_task_button = ttk.Button(self.task_entry_frame, text=self.translation_manager.get("add_task_button"), command=self.add_task)
        self.add_task_button.pack(pady=10, anchor="w")  # Align to the left

        # Task Lists Section
        self.task_lists_frame = ttk.Frame(self.root)
        self.task_lists_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)  # Expand to fill available space

        self.obligatory_label = ttk.Label(self.task_lists_frame, text=self.translation_manager.get("obligatory_label"))
        self.obligatory_label.pack(anchor="w")  # Align to the left

        self.obligatory_tree = ttk.Treeview(self.task_lists_frame, columns=("Description", "Status"), show="headings", height=5)
        self.obligatory_tree.heading("Description", text="Description")
        self.obligatory_tree.heading("Status", text="Status")
        self.obligatory_tree.column("Status", width=50, anchor="center")  # Reduce width of Status column
        self.obligatory_tree.pack(fill=tk.BOTH, expand=True, pady=5)  # Expand to fill available space

        # Add blank space between the first task table and the "Tareas no obligatorias" label
        self.blank_space = ttk.Label(self.task_lists_frame, text="")  # Empty label for spacing
        self.blank_space.pack(pady=5)  # Add vertical padding

        self.optional_label = ttk.Label(self.task_lists_frame, text=self.translation_manager.get("optional_label"))
        self.optional_label.pack(anchor="w")  # Align to the left

        self.optional_tree = ttk.Treeview(self.task_lists_frame, columns=("Description", "Status"), show="headings", height=5)
        self.optional_tree.heading("Description", text="Description")
        self.optional_tree.heading("Status", text="Status")
        self.optional_tree.column("Status", width=50, anchor="center")  # Reduce width of Status column
        self.optional_tree.pack(fill=tk.BOTH, expand=True, pady=5)  # Expand to fill available space

        # Task Actions Section
        self.task_actions_frame = ttk.Frame(self.root)
        self.task_actions_frame.pack(fill=tk.X, padx=10, pady=10)  # Expand horizontally

        # Center the buttons horizontally
        self.button_container = ttk.Frame(self.task_actions_frame)
        self.button_container.pack(expand=True)  # Center the container

        # Add buttons to the container
        self.mark_completed_button = ttk.Button(
            self.button_container,
            text=self.translation_manager.get("mark_completed_button"),
            command=self.mark_completed,
            width=20  # Set a fixed width
        )
        self.mark_completed_button.pack(side=tk.LEFT, padx=5)

        self.delete_task_button = ttk.Button(
            self.button_container,
            text=self.translation_manager.get("delete_task_button"),
            command=self.delete_task,
            width=20  # Set a fixed width
        )
        self.delete_task_button.pack(side=tk.LEFT, padx=5)

        # Bind keyboard shortcuts
        self.root.bind("<Control-Return>", lambda event: self.add_task())
        self.root.bind("<Control-d>", lambda event: self.delete_task())

    def add_task(self, event=None):
        """
        Adds a new task to the task manager based on the user input.

        Args:
            event (tk.Event, optional): The event that triggered this method (e.g., keyboard shortcut). Defaults to None.
        """
        description = self.task_entry.get()
        category = TaskCategory[self.category_var.get()]
        if not description:
            messagebox.showwarning(self.translation_manager.get("warning_no_task"), self.translation_manager.get("warning_no_task"))
            return
        if not self.task_manager.add_task(description, category):
            max_tasks = self.task_manager.MAX_OBLIGATORY if category == TaskCategory.OBLIGATORY else self.task_manager.MAX_OPTIONAL
            messagebox.showwarning(self.translation_manager.get("warning_max_tasks"), self.translation_manager.get("warning_max_tasks", max_tasks=max_tasks, category=category.name.lower()))
            return
        self._update_task_lists()
        self.task_entry.delete(0, tk.END)

    def mark_completed(self):
        """Marks the selected task as completed."""
        selected = self.obligatory_tree.selection()
        if selected:
            task_index = self.obligatory_tree.index(selected[0])
            self.task_manager.toggle_task_completion(task_index, TaskCategory.OBLIGATORY)
        else:
            selected = self.optional_tree.selection()
            if selected:
                task_index = self.optional_tree.index(selected[0])
                self.task_manager.toggle_task_completion(task_index, TaskCategory.OPTIONAL)
        self._update_task_lists()

    def delete_task(self, event=None):
        """Deletes the selected task."""
        selected = self.obligatory_tree.selection()
        if selected:
            task_index = self.obligatory_tree.index(selected[0])
            self.task_manager.delete_task(task_index, TaskCategory.OBLIGATORY)
        else:
            selected = self.optional_tree.selection()
            if selected:
                task_index = self.optional_tree.index(selected[0])
                self.task_manager.delete_task(task_index, TaskCategory.OPTIONAL)
        self._update_task_lists()

    def _update_task_lists(self):
        """Updates the task lists in the UI to reflect the current state of the task manager."""
        for row in self.obligatory_tree.get_children():
            self.obligatory_tree.delete(row)
        for row in self.optional_tree.get_children():
            self.optional_tree.delete(row)

        # Add tasks to Treeview
        for task in self.task_manager.get_tasks_by_category(TaskCategory.OBLIGATORY):
            self.obligatory_tree.insert("", "end", values=(task.description, "✓" if task.completed else ""))

        for task in self.task_manager.get_tasks_by_category(TaskCategory.OPTIONAL):
            self.optional_tree.insert("", "end", values=(task.description, "✓" if task.completed else ""))