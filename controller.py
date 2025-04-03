from tkinter import messagebox, simpledialog
from datetime import datetime
from task import Task


class TaskController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.refresh_view()


    def refresh_view(self):
        tasks = self.model.get_tasks()
        self.view.update_task_list(tasks)



    def add_task(self):
        title = simpledialog.askstring("Add Task", "Task Title:")

        if title:
            due_date_str = simpledialog.askstring("Add Task", "Due Date (YYYY-MM-DD):")
            due_date = None

            if due_date_str:

                try:
                    due_date = datetime.strptime(due_date_str, "%Y-%m-%d")
                except ValueError:
                    messagebox.showerror("Invalid Date", "Please enter a valid date in YYYY-MM-DD format.")
                    return


            new_task = Task(title=title, due_date=due_date)
            self.model.add_task(new_task)
            self.refresh_view()



    def remove_task(self):
        index = self.view.get_selected_index()

        if index is not None:
            self.model.remove_task(index)
            self.refresh_view()
        else:
            messagebox.showwarning("No Selection", "Please select a task to remove.")



    def toggle_task(self):
        index = self.view.get_selected_index()

        if index is not None:
            self.model.tasks[index].toggle_completed()
            self.refresh_view()
        else:
            messagebox.showwarning("No Selection", "Please select a task to toggle.")
            
                


