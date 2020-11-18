tasks = [
    { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
    { "description": "Clean Windows", "completed": False, "time_taken": 15 },
    { "description": "Make Dinner", "completed": True, "time_taken": 30 },
    { "description": "Feed Cat", "completed": False, "time_taken": 5 },
    { "description": "Walk Dog", "completed": True, "time_taken": 60 },
]


#1.

def find_uncompleted_task(task_list):
    uncompleted_tasks = []
    
    for task in task_list:
        if task["completed"] == False:
            uncompleted_tasks.append(task)
    print(uncompleted_tasks) 

find_uncompleted_task(tasks)


#2.

def find_completed_task(task_list):
    completed_tasks = []
    
    for task in task_list:
        if task["completed"] == True:
            completed_tasks.append(task)
    print(completed_tasks) 

find_completed_task(tasks)

#3.

def task_description(task_list):
    task_descriptions = []
    for task in task_list:
        task_descriptions.append(task["description"])
           
    print(task_descriptions) 

task_description(tasks)    

#4.

def find_15minute_tasks(task_list):
    all_15minute_tasks = []
    
    for task in task_list:
        if task["time_taken"] >= 15:
            all_15minute_tasks.append(task)
    print(all_15minute_tasks) 

find_15minute_tasks(tasks)

#5. UNCOMPLETED

def print_list(task_list):
    
    for task in task_list:
        if task["description"] == description:
            all_15minute_tasks.append(task)
    return(tasks)

find_15minute_tasks(tasks)
        

         