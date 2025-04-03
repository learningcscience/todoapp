import tkinter as tk

class TaskView(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.create_widgets()



    def create_widgets(self):
        self.pack(fill=tk.BOTH, expand=True)


        # listbox
        self.task_listbox = tk.Listbox(self, height=15, width=50)
        self.task_listbox.pack(padx=10, pady=10)


        # frame for buttons

        button_frame = tk.Frame(self)
        button_frame.pack(pady=10)


        self.add_button = tk.Button(button_frame, text="Add Task", width=15, command=self.controller.add_task)
        self.add_button.grid(row=0, column=0, padx=5)


        self.remove_button = tk.Button(button_frame, text="Remove Task", width=15, command=self.controller.remove_task)
        self.remove_button.grid(row=0, column=1, padx=5)

        self.toggle_button = tk.Button(button_frame, text="Toggle Completed", width=15, command=self.controller.toggle_task)
        self.toggle_button.grid(row=0, column=2, padx=5)



    def update_task_list(self, tasks):
        self.task_listbox.delete(0, tk.END)
        for task in tasks:
            self.task_listbox.insert(tk.END, str(task))



    def get_selected_index(self):
        selection = self.task_listbox.curselection()
        if selection:
            return selection[0]
        else:
            return None



