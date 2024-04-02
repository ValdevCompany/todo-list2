from flask import Flask, render_template, request, make_response, redirect
import os

app = Flask(__name__, template_folder='C:/Users/User/Desktop/Projects/html code')

TASKS_FILE = 'tasks.txt'


def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as f:
            return f.read().splitlines()
    else:
        return []


def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as f:
        for task in tasks:
            f.write(task + '\n')


def delete_task(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        del tasks[index]
        save_tasks(tasks)
        return True
    else:
        return False


@app.route('/', methods=['POST', 'GET'])
def main():
    tasks = load_tasks()
    if request.method == 'POST':
        task = request.form['task']
        if task:
            tasks.append(task)
            save_tasks(tasks)
            # Redirect to avoid form resubmission
            return redirect('/')
    return render_template('todo.html', tasks=tasks)


@app.route('/delete_task', methods=['POST'])
def delete_task_route():
    index = int(request.form['index'])
    if delete_task(index):
        # Redirect to avoid form resubmission
        return redirect('/')
    else:
        return 'Failed to delete task'


if __name__ == '__main__':
    app.run(debug=True, port=5050)
