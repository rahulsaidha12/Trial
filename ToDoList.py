"""

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({'task': task, 'completed': False})

    def remove_task(self, task):
        self.tasks = [t for t in self.tasks if t['task'] != task]

    def list_tasks(self):
        return self.tasks

    def mark_completed(self, task):
        for t in self.tasks:
            if t['task'] == task:
                t['completed'] = True
                break

todo = TodoList()
todo.add_task("Learn Python")
todo.add_task("Build a project")
todo.mark_completed("Learn Python")
todo.remove_task("Learn Python")
print(todo.list_tasks())  # Output: [{'task': 'Learn Python', 'completed': True}, {'task': 'Build a project', 'completed': False}]

"""

class Classroom:
    def __init__(self):
        self.students=[]
    
    def addStudent(self,student,grade):
        self.students.append({'Name':student, 'grade': grade})
        
    def listStudent(self):
        return self.students
    
classroom=Classroom()
classroom.addStudent("Rahul",100)
classroom.addStudent("Nitin",95)
print(classroom.listStudent())


