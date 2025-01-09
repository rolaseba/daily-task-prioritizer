# models/task.py
from dataclasses import dataclass
from typing import List
from enum import Enum, auto

class TaskCategory(Enum):
    """Enumeration for task categories"""
    OBLIGATORY = auto()
    OPTIONAL = auto()

@dataclass
class Task:
    """Represents a single task with its properties"""
    description: str
    category: TaskCategory
    completed: bool = False

class TaskManager:
    """Manages task operations and maintains task state"""
    def __init__(self):
        self.tasks: List[Task] = []
        self.MAX_OBLIGATORY = 4
        self.MAX_OPTIONAL = 6

    def add_task(self, description: str, category: TaskCategory) -> bool:
        """
        Adds a new task if category limits haven't been reached
        Returns True if successful, False otherwise
        """
        category_count = sum(1 for task in self.tasks if task.category == category)
        max_tasks = (self.MAX_OBLIGATORY if category == TaskCategory.OBLIGATORY 
                    else self.MAX_OPTIONAL)
        
        if category_count >= max_tasks:
            return False
            
        self.tasks.append(Task(description, category))
        return True

    def toggle_task_completion(self, index: int, category: TaskCategory) -> bool:
        """Toggles the completion status of a task"""
        task = self.get_task(index, category)
        if task:
            task.completed = not task.completed
            return True
        return False

    def delete_task(self, index: int, category: TaskCategory) -> bool:
        """Deletes a task at the specified index and category"""
        task = self.get_task(index, category)
        if task:
            self.tasks.remove(task)
            return True
        return False

    def get_task(self, index: int, category: TaskCategory) -> Task | None:
        """Returns a task at the specified index and category"""
        filtered_tasks = [task for task in self.tasks if task.category == category]
        return filtered_tasks[index] if 0 <= index < len(filtered_tasks) else None

    def get_tasks_by_category(self, category: TaskCategory) -> List[Task]:
        """Returns all tasks of a specific category"""
        return [task for task in self.tasks if task.category == category]