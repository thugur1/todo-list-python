import json
import os
from datetime import datetime

class TodoList:
    def __init__(self, filename="todos.json"):
        self.filename = filename
        self.todos = []
        self.load_todos()
    
    def load_todos(self):
        """Load todos from JSON file"""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as file:
                    self.todos = json.load(file)
                print(f"✅ Loaded {len(self.todos)} tasks from file.")
            except json.JSONDecodeError:
                print("⚠️ Error reading file. Starting with empty list.")
                self.todos = []
        else:
            print("📝 No saved tasks found. Starting fresh!")
            self.todos = []
    
    def save_todos(self):
        """Save todos to JSON file"""
        try:
            with open(self.filename, 'w') as file:
                json.dump(self.todos, file, indent=4)
            return True
        except Exception as e:
            print(f"❌ Error saving tasks: {e}")
            return False
    
    def add_task(self, task, priority="medium"):
        """Add a new task"""
        new_task = {
            "id": len(self.todos) + 1,
            "task": task,
            "completed": False,
            "priority": priority,
            "created": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.todos.append(new_task)
        self.save_todos()
        print(f"✅ Task added: '{task}' (Priority: {priority})")
    
    def view_tasks(self, show_completed=True):
        """Display all tasks"""
        if not self.todos:
            print("\n📭 No tasks yet! Add some tasks to get started.")
            return
        
        print("\n" + "="*70)
        print("📋 YOUR TODO LIST")
        print("="*70)
        
        # Separate completed and pending tasks
        pending = [t for t in self.todos if not t["completed"]]
        completed = [t for t in self.todos if t["completed"]]
        
        # Show pending tasks
        if pending:
            print("\n⏳ PENDING TASKS:")
            print("-" * 70)
            for task in pending:
                priority_icon = self._get_priority_icon(task["priority"])
                print(f"{task['id']}. {priority_icon} {task['task']}")
                print(f"   Created: {task['created']}")
                print()
        
        # Show completed tasks
        if show_completed and completed:
            print("\n✅ COMPLETED TASKS:")
            print("-" * 70)
            for task in completed:
                print(f"{task['id']}. ✓ {task['task']}")
                print(f"   Created: {task['created']}")
                print()
        
        # Summary
        print("="*70)
        print(f"📊 Total: {len(self.todos)} | Pending: {len(pending)} | Completed: {len(completed)}")
        print("="*70)
    
    def _get_priority_icon(self, priority):
        """Get icon for priority level"""
        icons = {
            "high": "🔴",
            "medium": "🟡",
            "low": "🟢"
        }
        return icons.get(priority.lower(), "⚪")
    
    def complete_task(self, task_id):
        """Mark a task as completed"""
        for task in self.todos:
            if task["id"] == task_id:
                if task["completed"]:
                    print(f"⚠️ Task '{task['task']}' is already completed!")
                else:
                    task["completed"] = True
                    self.save_todos()
                    print(f"✅ Task completed: '{task['task']}'")
                return
        print(f"❌ Task with ID {task_id} not found!")
    
    def delete_task(self, task_id):
        """Delete a task"""
        for i, task in enumerate(self.todos):
            if task["id"] == task_id:
                deleted_task = self.todos.pop(i)
                # Reassign IDs
                for j, t in enumerate(self.todos):
                    t["id"] = j + 1
                self.save_todos()
                print(f"🗑️ Task deleted: '{deleted_task['task']}'")
                return
        print(f"❌ Task with ID {task_id} not found!")
    
    def edit_task(self, task_id, new_task):
        """Edit an existing task"""
        for task in self.todos:
            if task["id"] == task_id:
                old_task = task["task"]
                task["task"] = new_task
                self.save_todos()
                print(f"✏️ Task updated:")
                print(f"   Old: '{old_task}'")
                print(f"   New: '{new_task}'")
                return
        print(f"❌ Task with ID {task_id} not found!")
    
    def change_priority(self, task_id, new_priority):
        """Change task priority"""
        valid_priorities = ["high", "medium", "low"]
        if new_priority.lower() not in valid_priorities:
            print(f"❌ Invalid priority! Use: {', '.join(valid_priorities)}")
            return
        
        for task in self.todos:
            if task["id"] == task_id:
                task["priority"] = new_priority.lower()
                self.save_todos()
                print(f"🎯 Priority changed to '{new_priority}' for: '{task['task']}'")
                return
        print(f"❌ Task with ID {task_id} not found!")
    
    def clear_completed(self):
        """Remove all completed tasks"""
        completed_count = len([t for t in self.todos if t["completed"]])
        if completed_count == 0:
            print("⚠️ No completed tasks to clear!")
            return
        
        confirm = input(f"⚠️ Are you sure you want to delete {completed_count} completed task(s)? (y/n): ")
        if confirm.lower() == 'y':
            self.todos = [t for t in self.todos if not t["completed"]]
            # Reassign IDs
            for i, task in enumerate(self.todos):
                task["id"] = i + 1
            self.save_todos()
            print(f"🗑️ Cleared {completed_count} completed task(s)!")
        else:
            print("❌ Action cancelled.")

def display_menu():
    """Display main menu"""
    print("\n" + "="*70)
    print("📝 TODO LIST MENU")
    print("="*70)
    print("1. ➕ Add Task")
    print("2. 👀 View All Tasks")
    print("3. ✅ Complete Task")
    print("4. ✏️ Edit Task")
    print("5. 🎯 Change Priority")
    print("6. 🗑️ Delete Task")
    print("7. 🧹 Clear Completed Tasks")
    print("8. 🚪 Exit")
    print("="*70)

def main():
    """Main function to run the todo list application"""
    
    print("\n" + "="*70)
    print("📝 WELCOME TO TODO LIST MANAGER!")
    print("="*70)
    
    todo_list = TodoList()
    
    while True:
        display_menu()
        
        try:
            choice = input("\nEnter your choice (1-8): ").strip()
            
            if choice == "1":
                # Add task
                task = input("\n📝 Enter task description: ").strip()
                if not task:
                    print("❌ Task cannot be empty!")
                    continue
                
                print("\n🎯 Select priority:")
                print("1. High 🔴")
                print("2. Medium 🟡")
                print("3. Low 🟢")
                priority_choice = input("Enter choice (1-3, default is 2): ").strip()
                
                priority_map = {"1": "high", "2": "medium", "3": "low"}
                priority = priority_map.get(priority_choice, "medium")
                
                todo_list.add_task(task, priority)
            
            elif choice == "2":
                # View tasks
                show_completed = input("\n👀 Show completed tasks? (y/n, default is y): ").strip().lower()
                todo_list.view_tasks(show_completed != 'n')
            
            elif choice == "3":
                # Complete task
                todo_list.view_tasks(show_completed=False)
                try:
                    task_id = int(input("\n✅ Enter task ID to complete: "))
                    todo_list.complete_task(task_id)
                except ValueError:
                    print("❌ Invalid ID! Please enter a number.")
            
            elif choice == "4":
                # Edit task
                todo_list.view_tasks()
                try:
                    task_id = int(input("\n✏️ Enter task ID to edit: "))
                    new_task = input("Enter new task description: ").strip()
                    if new_task:
                        todo_list.edit_task(task_id, new_task)
                    else:
                        print("❌ Task description cannot be empty!")
                except ValueError:
                    print("❌ Invalid ID! Please enter a number.")
            
            elif choice == "5":
                # Change priority
                todo_list.view_tasks()
                try:
                    task_id = int(input("\n🎯 Enter task ID: "))
                    print("\nSelect new priority:")
                    print("1. High 🔴")
                    print("2. Medium 🟡")
                    print("3. Low 🟢")
                    priority_choice = input("Enter choice (1-3): ").strip()
                    priority_map = {"1": "high", "2": "medium", "3": "low"}
                    if priority_choice in priority_map:
                        todo_list.change_priority(task_id, priority_map[priority_choice])
                    else:
                        print("❌ Invalid priority choice!")
                except ValueError:
                    print("❌ Invalid ID! Please enter a number.")
            
            elif choice == "6":
                # Delete task
                todo_list.view_tasks()
                try:
                    task_id = int(input("\n🗑️ Enter task ID to delete: "))
                    confirm = input(f"⚠️ Are you sure you want to delete task {task_id}? (y/n): ")
                    if confirm.lower() == 'y':
                        todo_list.delete_task(task_id)
                    else:
                        print("❌ Deletion cancelled.")
                except ValueError:
                    print("❌ Invalid ID! Please enter a number.")
            
            elif choice == "7":
                # Clear completed
                todo_list.clear_completed()
            
            elif choice == "8":
                # Exit
                print("\n👋 Thanks for using Todo List Manager!")
                print("Your tasks have been saved automatically.")
                print("="*70)
                break
            
            else:
                print("❌ Invalid choice! Please enter 1-8.")
        
        except KeyboardInterrupt:
            print("\n\n👋 Exiting... Your tasks have been saved.")
            break
        except Exception as e:
            print(f"❌ An error occurred: {e}")

if __name__ == "__main__":
    main()
