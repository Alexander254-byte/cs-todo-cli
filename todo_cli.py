# CS Capstone: CLI To-Do List (All concepts combined!)
import json
import os
from datetime import datetime  # For timestamps

TODO_FILE = "todos.json"

class TodoApp:
    def __init__(self):
        self.todos = []  # List of dicts: {"task": "...", "done": False, "date": "..."}
        self.load_todos()
    
    def load_todos(self):
        """Load from file"""
        if os.path.exists(TODO_FILE):
            try:
                with open(TODO_FILE, "r") as f:
                    self.todos = json.load(f)
                print(f"📂 Loaded {len(self.todos)} todos")
            except:
                self.todos = []
        else:
            self.todos = []
    
    def save_todos(self):
        """Save to file"""
        with open(TODO_FILE, "w") as f:
            json.dump(self.todos, f, indent=2)
        print("💾 Saved!")
    
    def add_todo(self, task):
        """Add new task"""
        todo = {
            "task": task,
            "done": False,
            "date": datetime.now().strftime("%Y-%m-%d")
        }
        self.todos.append(todo)
        self.save_todos()
        print(f"➕ Added: {task}")
    
    def list_todos(self):
        """Show all with status"""
        if not self.todos:
            print("No todos! 🎉")
            return
        
        print("\n📝 To-Do List:")
        for i, todo in enumerate(self.todos, 1):
            status = "✅" if todo["done"] else "⏳"
            print(f"{i}. {status} {todo['task']} ({todo['date']})")
    
    def toggle_done(self, index):
        """Mark as done/undone"""
        if 0 < index <= len(self.todos):
            self.todos[index-1]["done"] = not self.todos[index-1]["done"]
            status = "done!" if self.todos[index-1]["done"] else "undone!"
            self.save_todos()
            print(f"Marked todo {index} as {status}")
        else:
            print("❌ Invalid number!")
    
    def delete_todo(self, index):
        """Remove todo"""
        if 0 < index <= len(self.todos):
            removed = self.todos.pop(index-1)
            self.save_todos()
            print(f"🗑️ Deleted: {removed['task']}")
        else:
            print("❌ Invalid number!")

def main():
    app = TodoApp()
    print("=== CLI To-Do App ===")
    print("Commands: add 'task' | list | done X | delete X | quit")
    
    while True:
        command = input("\n> ").strip().lower()
        
        if command.startswith("add "):
            task = command[4:]  # String slicing
            if task:
                app.add_todo(task)
            else:
                print("❌ Need a task!")
        
        elif command == "list":
            app.list_todos()
        
        elif command.startswith("done "):
            try:
                index = int(command[5:])
                app.toggle_done(index)
            except ValueError:
                print("❌ Use: done 1")
        
        elif command.startswith("delete "):
            try:
                index = int(command[7:])
                app.delete_todo(index)
            except ValueError:
                print("❌ Use: delete 1")
        
        elif command == "quit":
            print("👋 Bye!")
            break
        
        else:
            print("🤔 Unknown command—type 'list' for help")

if __name__ == "__main__":
    main()