# Task management system
class Task:
    current_id = 0  
    def __init__(self, name, description, priority, status='невиконане'):
        Task.current_id += 1 
        self.id = Task.current_id 
        self.name = name
        self.description = description
        self.priority = priority  
        self.status = status  
    
    def update_status(self, new_status):
        self.status = new_status

class TaskList:
    def __init__(self):
        self.tasks = {} 
    
    def add_task(self, task):
        self.tasks[task.id] = task
    
    def change_status(self, task_id, new_status):
        if task_id in self.tasks:
            self.tasks[task_id].update_status(new_status)
        else:
            print(f"Завдання з id {task_id} не знайдено")
    
    def filter_by_priority(self, priority):
        return {task_id: task for task_id, task in self.tasks.items() if task.priority == priority}
    
    def filter_by_status(self, status):
        return {task_id: task for task_id, task in self.tasks.items() if task.status == status}
    
    def get_statistics(self):
        total_tasks = len(self.tasks)
        completed_tasks = sum(1 for task in self.tasks.values() if task.status == 'виконане')
        uncompleted_tasks = total_tasks - completed_tasks
        return {
            'total': total_tasks,
            'completed': completed_tasks,
            'uncompleted': uncompleted_tasks
        }


task_list = TaskList()
task1 = Task("Завдання 1", "Опис 1", "високий")
task2 = Task("Завдання 2", "Опис 2", "низький", "виконане")
task3 = Task("Завдання 3", "Опис 3", "середній")
task_list.add_task(task1)
task_list.add_task(task2)
task_list.add_task(task3)
task_list.change_status(1, "виконане")
high_priority_tasks = task_list.filter_by_priority("високий")
completed_tasks = task_list.filter_by_status("виконане")
stats = task_list.get_statistics()
print(stats)
