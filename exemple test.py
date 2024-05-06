from schedcat.generator.tasksets import from_task_list
from schedcat.simulation.rta import is_schedulable

# Liste des tâches à planifier (à remplacer par vos propres tâches définies)
tasks = [
    {'name': 'task1', 'execution_time': 10, 'period': 100},
    {'name': 'task2', 'execution_time': 20, 'period': 200},
    {'name': 'task3', 'execution_time': 30, 'period': 300}
]

# Création de l'ensemble de tâches à partir de la liste
taskset = from_task_list(tasks)

# Vérification de la faisabilité (ordonnancement) du jeu de tâches
if is_schedulable(taskset):
    print("Le jeu de tâches est ordonnançable.")
else:
    print("Le jeu de tâches n'est pas ordonnançable.")
