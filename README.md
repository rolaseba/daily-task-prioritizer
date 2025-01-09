# Daily Task Prioritizer

A Python-based task management application that helps you focus on what truly matters by implementing an enhanced timeboxing methodology. The application distinguishes between mandatory tasks (those with consequences if not completed today) and non-mandatory tasks (those without immediate consequences), helping you prioritize effectively.

## Methodology

The Daily Task Prioritizer is built on the foundation of timeboxing methodology with a crucial enhancement: task categorization based on consequences. This approach helps you:

1. Identify tasks that genuinely need completion today
2. Reduce anxiety by clearly separating urgent from non-urgent tasks
3. Focus your energy on tasks with real impact
4. Maintain a balanced daily workload

The application enforces task limits to prevent overcommitment:

- Maximum 4 mandatory tasks
- Maximum 6 non-mandatory tasks

## Installation

### Prerequisites

- Python 3.8 or higher
- Tkinter (usually comes with Python)
- ttkbootstrap (for modern UI themes)

### Setup Steps

1. Clone the repository

```bash
git clone https://github.com/rolaseba/daily-task-prioritizer.git
cd daily-task-prioritizer
```

2. Run the application

```bash
python main.py
```

## Project Structure

```
daily-task-prioritizer/
├── models/                     # Model: Manages data and business logic
│   └── task.py
├── ui/                         # View: Handles the user interface
│   └── task_view.py
├── config/                     # Configuration: Stores settings and constants
│   ├── constants.py
│   └── settings.py
├── locales/                    # Translations: Stores language-specific text
│   ├── en.json
│   └── es.json
├── utils/                      # Utilities: Reusable components (e.g., TranslationManager)
│   └── translation_manager.py
├── main.py                     # Controller: Initializes the application
└── README.md                   # Documentation
```

### Detailed Structure Documentation

For detailed information about the application structure, refer to the [Application Structure Documentation](STRUCTURE.md).

## Usage

1. **Adding Tasks**
   - Enter your task description
   - Select the category:
     - Mandatory: Tasks with consequences if not completed today
     - Non-Mandatory: Tasks that can be postponed without immediate consequences
   - Click "Añadir Tarea" (Add Task)

2. **Managing Tasks**
   - Mark tasks as complete by selecting them and clicking "Marcar Completado"
   - Remove tasks using the "Eliminar Tarea" button
   - Tasks are displayed in separate lists based on their category

3. **Daily Review**
   - At the start of each day, review your tasks
   - Update task lists based on current priorities
   - Transfer incomplete tasks that are still relevant
   - Add new tasks as needed

## Best Practices

1. **Morning Planning**
   - Start each day by reviewing and updating your task lists
   - Be honest about which tasks truly have consequences
   - Limit your mandatory tasks to maintain focus

2. **Throughout the Day**
   - Focus on mandatory tasks first
   - Use non-mandatory tasks as a backup list when time permits
   - Update task status as you complete them

3. **End of Day**
   - Review incomplete tasks
   - Consider whether incomplete mandatory tasks need immediate attention
   - Plan tentatively for tomorrow

## Features

- Clear distinction between mandatory and non-mandatory tasks
- Task limits to prevent overcommitment
- Simple, distraction-free interface
- Task completion tracking
- Easy task management (add, complete, delete)

## Development

The application is built using:

- Python for core functionality
- Tkinter for the graphical user interface
- Object-oriented design principles
- Type hints for better code maintainability

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
