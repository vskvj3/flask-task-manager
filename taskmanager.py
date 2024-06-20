'''
Models for the Task Manager application
Task: Represents a task in the task manager application
TaskManager: Functions to manage tasks
'''
import json
from datetime import date

class Task:
    '''
    Represents a task in the task manager application
    Attributes:
    title: Title of the task
    description: Description of the task
    due_date: Due date of the task
    status: Status of the task
    '''
    def __init__(self, title, description, due_date, status):
        self.title = title
        self.description = description
        year, month, day = map(int, due_date.split('-'))
        self.due_date =  due_date
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
        self.__tasks = []

    def add_task(self, task):
        '''
        Takes a task, adds it to the tasks list,
        '''
        self.__tasks.append(task)

    def view_tasks(self):
        '''
        Returns tasks list.
        '''
        # sort tasks based on due date
        self.__tasks = sorted(self.__tasks, key=lambda x: x.due_date, reverse=True)
        return self.__tasks

    def update_task(self, task_id, **kwargs):
        '''
         Takes task ID and attributes, updates the task based on the provided task ID and attributes.
        '''
        try:
            task = self.__tasks[task_id]
            for key, value in kwargs.items():
                setattr(task, key, value)
        except IndexError as e:
            raise ValueError('Invalid task ID') from e

    def delete_task(self, task_id):
        '''
        Takes a Task ID, deletes the task based on the provided task ID.
        '''
        try:
            del self.__tasks[task_id]
        except IndexError as e:
            raise ValueError('Invalid task ID') from e

    def save_tasks(self, filename):
        ''''
        Takes a filename, saves all tasks into the file.
        '''
        try:
            with open(filename, 'w') as file:
                tasks_dict = [task.__dict__ for task in self.__tasks]
                json.dump(tasks_dict, file)
        except Exception as e:
            raise ValueError('Error saving tasks') from e

    def load_tasks(self, filename):
        '''
        Takes a file name, loads all tasks from the file to the tasks list.
        '''
        try:
            with open(filename, 'r') as file:
                tasks_dict = json.load(file)
                self.__tasks = [Task(**task) for task in tasks_dict]
        except Exception as e:
            raise ValueError('Error loading tasks') from e