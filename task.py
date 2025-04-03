
class Task:
    def __init__(self, title, description, due_date, completed):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.completed = completed


    def toggle_completed(self):
        self.completed = not self.completed


    def __str__(self):
        status = "Completed" if self.completed else "Not Completed"
        due = self.due_date.strftime("%Y-%m-%d") if self.due_date else "No Due Date"
        return f"{self.title} ({due}) [{status}]"        


