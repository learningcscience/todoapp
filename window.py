import tkinter as tk

from manager import TaskManager
from view import TaskView
from controller import TaskController



class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("TODO List Manager")
        self.geometry("600x400")



        #init model, view and controller

        self.task_manager = TaskManager()
        
        self.task_controller = TaskController(self.task_manager)

        self.task_view = TaskView(self, self.task_controller)
        


        self.task_controller.view = self.task_view




