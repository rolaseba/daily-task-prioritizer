# App Structure Explanation

## Application Structure

The application is built using the **Model-View-Controller (MVC)** architecture, which separates the application into three main components:

1. **Model**: Manages the data and business logic.
2. **View**: Handles the user interface and presentation.
3. **Controller**: Acts as the intermediary between the Model and the View.

In addition to these core components, the application includes **supporting components** for **Configuration** and **Translations**, which enhance functionality and maintainability.

---

### **1. Model (`models/task.py`)**

The **Model** is responsible for managing tasks and their properties. It defines the data structures and logic for adding, deleting, and toggling tasks.

#### Key Components

- **`TaskCategory` Enum**:
  - Defines the two categories of tasks: `OBLIGATORY` (mandatory) and `OPTIONAL` (non-mandatory).
  
- **`Task` Dataclass**:
  - Represents a single task with properties like `description`, `category`, and `completed` (a boolean indicating whether the task is done).

- **`TaskManager` Class**:
  - Manages the list of tasks and provides methods to:
    - Add tasks (with limits for each category: 4 mandatory and 6 non-mandatory tasks).
    - Toggle the completion status of tasks.
    - Delete tasks.
    - Retrieve tasks by category or by index.

---

### **2. View (`ui/task_view.py`)**

The **View** is responsible for the user interface and how the data is presented to the user. It uses the `tkinter` library to create the GUI and handles user interactions.

#### Key Components:
- **`TaskView` Class**:
  - Manages the graphical user interface (GUI).
  - Creates and configures the main window, input fields, buttons, and task lists.
  - Handles user interactions such as:
    - Adding tasks.
    - Marking tasks as completed.
    - Deleting tasks.
    - Switching languages.
  - Communicates with the `TaskManager` (Model) to update the task lists and reflect changes in the UI.
  - Uses the `TranslationManager` to load translations for all text displayed in the UI.

#### Key Methods:
- **`setup_ui`**:
  - Initializes and configures all UI components (input section, task lists, buttons, language settings).
- **`_update_task_lists`**:
  - Updates the task lists to reflect the current state of tasks, including the translated `completed_label`.
- **`_change_language`**:
  - Changes the application language and rebuilds the UI with the new translations.

---

### **3. Controller (`main.py`)**
The **Controller** acts as the intermediary between the **Model** and the **View**. It initializes the application and sets up the interaction between the UI and the data.

#### Key Components:
- **`main()` Function**:
  - Initializes the `tkinter` root window.
  - Creates an instance of `TaskManager` (Model) to manage tasks.
  - Creates an instance of `TaskView` (View) and passes the `TaskManager` and the default language to it.
  - Starts the main event loop of the application using `root.mainloop()`.

---

### **4. Supporting Components**
In addition to the core MVC components, the application includes **supporting components** for **Configuration** and **Translations**, which enhance functionality and maintainability.

#### **4.1 Configuration (`config/`)**
The **Configuration** component stores application-wide settings and constants.

##### Key Files:
- **`constants.py`**:
  - Defines constants for UI configuration, such as `WINDOW_WIDTH`, `WINDOW_HEIGHT`, `BUTTON_WIDTH`, `MAX_CHARACTERS`, and `ENTRY_WIDTH`.
  
- **`settings.py`**:
  - Defines runtime settings, such as the default language (`DEFAULT_LANGUAGE`).

##### Role:
- Provides configuration data to the **View** and **Controller**.
- For example, the **View** uses `UIConstants` to set up the UI, and the **Controller** uses `DEFAULT_LANGUAGE` to initialize the application.

#### **4.2 Translations (`locales/`)**
The **Translations** component stores language-specific text for the UI.

##### Key Files:
- **`en.json`**:
  - Contains English translations for all text displayed in the UI.
  
- **`es.json`**:
  - Contains Spanish translations for all text displayed in the UI.

##### Role:
- Provides translated text to the **View** via the `TranslationManager`.
- For example, the **View** uses the `TranslationManager` to load and display translated text for labels, buttons, and warnings.

#### **4.3 Translation Manager (`utils/translation_manager.py`)**
The **Translation Manager** is responsible for loading and managing translations.

##### Key Components:
- **`TranslationManager` Class**:
  - Loads the appropriate JSON file based on the selected language.
  - Provides a method (`get`) to retrieve translations for specific keys.
  - Supports dynamic updates when the language is changed.

##### Role:
- Acts as a bridge between the **Translations** component and the **View**.
- For example, the **View** uses the `TranslationManager` to load and display translated text.

---

### **Project Structure**
Here’s the updated project structure, including the core MVC components and supporting components:

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

---

### **How It All Works Together**
1. **Initialization**:
   - When the application starts, `main.py` (Controller) initializes the `TaskManager` (Model) and `TaskView` (View).
   - The `TaskView` sets up the GUI and binds user actions (like clicking buttons) to methods in the `TaskManager`.

2. **User Interaction**:
   - When a user adds a task, the `TaskView` validates the input and calls the `add_task` method in the `TaskManager`.
   - The `TaskManager` checks if the task can be added (based on category limits) and updates the task list.
   - The `TaskView` then updates the UI to reflect the new task.

3. **Language Switching**:
   - When the user selects a new language, the `TaskView` updates the `TranslationManager` and rebuilds the UI with the new translations.

4. **Task Management**:
   - Users can mark tasks as completed or delete them. These actions are handled by the `TaskView`, which communicates with the `TaskManager` to update the task list.
   - The UI is refreshed to show the updated task status.

---

### **Key Features**
- **Task Categorization**: Tasks are divided into mandatory and non-mandatory, helping users prioritize effectively.
- **Task Limits**: The application enforces limits on the number of tasks per category to prevent overcommitment.
- **Language Support**: Users can switch between English and Spanish, and all text is dynamically translated.
- **Simple UI**: The interface is clean and easy to use, with clear separation between task categories.
- **Task Completion Tracking**: Users can mark tasks as completed, and the UI updates to reflect this.

---
