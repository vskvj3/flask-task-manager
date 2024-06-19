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
    Class with methodes to manage tasks
    
    methods:
    add_task(self, task): Method to add a new task.
    view_tasks(self): Method to view all tasks.
    update_task(self, task_id, **kwargs):
        Method to update a task based on the provided task ID and attributes.
    delete_task(self, task_id): Method to delete a task based on the provided task ID.
    save_tasks(self, filename): Method to save tasks to a file.
    load_tasks(self, filename): Method to load tasks from a file.
    '''
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        '''
        Takes a task, adds it to the tasks list,
        '''
        self.tasks.append(task)

    def view_tasks(self):
        '''
        Returns tasks list.
        '''
        return self.tasks

    def update_task(self, task_id, **kwargs):
        '''
         Takes task ID and attributes, updates the task based on the provided task ID and attributes.
        '''
        try:
            task = self.tasks[task_id]
            for key, value in kwargs.items():
                setattr(task, key, value)
        except IndexError as e:
            raise ValueError('Invalid task ID') from e

    def delete_task(self, task_id):
        '''
        Takes a Task ID, deletes the task based on the provided task ID.
        '''
        try:
            del self.tasks[task_id]
        except IndexError as e:
            raise ValueError('Invalid task ID') from e
