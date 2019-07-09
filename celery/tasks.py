from celery import Celery

# first argument is the name of the current module
# broker is used to send and receive messages
# backend is used to store results and the status of results.
# Without it, you cannot retrieve the return value of the task
app = Celery('tasks')
app.config_from_object('celeryconfig')


@app.task
def add(x, y):
    return x + y

# docker exec -it celery-getting-started_celery_1 poetry run python
#
# >>> from tasks import add
# >>> add.delay(4, 4)
# <AsyncResult: 9e0e1c5e-030f-46df-9040-4c91ae1ebf4b>
#
# Received task: basic.tasks.add[9e0e1c5e-030f-46df-9040-4c91ae1ebf4b]
# Task basic.tasks.add[9e0e1c5e-030f-46df-9040-4c91ae1ebf4b] succeeded in 0.0003735700000007114s: 8
#
#
# >>> result = add.delay(5, 5)
# >>> result.ready()
# True
# >>> result.get()
# 10
#
