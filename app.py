'''
Flask app
'''

from flask import Flask, render_template
from taskmanager import Task, TaskManager

app = Flask(__name__)
task_manager = TaskManager()

@app.route('/')
def index():
    '''
    Index page
    '''
    task = Task('title', 'description', 'due_date', 'status')
    task2 = Task('title1', 'description1', 'due_date1', 'status1')
    task_manager.add_task(task)
    task_manager.add_task(task2)
    tasks = task_manager.view_tasks()
    print(tasks[0])
    return render_template('index.html', tasks=tasks)

if __name__ == '__main__':
    app.run(debug=True)