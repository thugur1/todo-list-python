# Todo List Manager

A feature-rich command-line todo list application with persistent storage, priority levels, and task management capabilities.

## Features
- ➕ Add tasks with priority levels
- 👀 View all tasks (pending and completed)
- ✅ Mark tasks as completed
- ✏️ Edit existing tasks
- 🎯 Change task priority (High, Medium, Low)
- 🗑️ Delete individual tasks
- 🧹 Clear all completed tasks at once
- 💾 Automatic saving to JSON file
- 📊 Task statistics and summary
- ⏰ Timestamp for each task

## Priority Levels
- 🔴 **High** - Urgent and important tasks
- 🟡 **Medium** - Regular tasks (default)
- 🟢 **Low** - Less urgent tasks

## How to Use
1. Clone the repository
2. Run: `python todo_list.py`
3. Use the menu to manage your tasks

## Data Storage
Tasks are automatically saved to `todos.json` in the same directory. Your tasks persist between sessions.

## Example Usage
```
📝 TODO LIST MENU
1. ➕ Add Task
2. 👀 View All Tasks
3. ✅ Complete Task
4. ✏️ Edit Task
5. 🎯 Change Priority
6. 🗑️ Delete Task
7. 🧹 Clear Completed Tasks
8. 🚪 Exit
```

## Requirements
- Python 3.x

## Technologies
- Python
- JSON for data persistence
- datetime module for timestamps
