'''
Models for the Task Manager application
Task: Represents a task in the task manager application
TaskManager: Functions to manage tasks
'''
import json
from datetime import datetime

class Task:
    '''
    Represents a task in the task manager application
    '''
    def __init__(self, title, description, due_date, status):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

    def __str__(self):
        return f"Title: {self.title}, Description: {self.description}, Due Date: {self.due_date}, Status: {self.status}"
    
class TaskManager:
    '''
    TaskManager: Functions to manage tasks
    '''
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def view_tasks(self):
        return self.tasks