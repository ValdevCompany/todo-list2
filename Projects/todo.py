from flask import Flask, render_template,request,make_response
import os
app = Flask(__name__,template_folder = 'C:/Users/User/Desktop/Projects/htm code')
 
TASKS_FILE = 'tasks.txt'
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as f:
            return f.read().splitlines()
    else:
        return []

# Функция для сохранения задач в файл
def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as f:
        for task in tasks:
            f.write(task + '\n')

tasks = load_tasks()



@app.route('/',methods = ['POST','GET'])
def main():
    if request.method == 'POST':

        task = request.form['task']

        response = make_response(render_template('todo.html', tasks=tasks))
        response.set_cookie('task', task)
        if task:
            tasks.append(task)
            save_tasks(tasks)
    return render_template('todo.html',tasks = tasks)


if __name__ == __name__:
    app.run(debug = True,port = '5050')