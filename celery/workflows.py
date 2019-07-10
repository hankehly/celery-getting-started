from celery import chain, group, chord

from .tasks import add, mul, xsum


# When you pass tasks to canvas functions, you pass "signatures"
# which carry all the arguments and information necessary to execute the task


def group_example():
    """
    Performs a list of tasks *in parallel*
    """
    tasks = (add.s(i, i) for i in range(10))
    g = group(tasks)
    result = g()
    print(result.get())


def chain_example():
    """
    Performs tasks 1-by-1 in order

    Notice how the result from the previous task
    is set as the first argument of the next task
    """
    # (4 + 4) * 2 = 16
    tasks = add.s(4, 4) | mul.s(2)
    c = chain(tasks)
    result = c()
    # >>> celery_1  | [2019-07-10 00:55:09,168: WARNING/ForkPoolWorker-3] x: 8
    # >>> celery_1  | [2019-07-10 00:55:09,169: WARNING/ForkPoolWorker-3] y: 2
    print(result.get())


def chord_example():
    """
    chord performs a group of tasks (first argument)
    then executed a callback (second argument)
    with the results from those tasks

    its a group with a callback
    """
    # sum([0 + 5, 1 + 6, 2 + 7, 3 + 8, 4 + 9]) = 45
    g = group(add.s(i, i + 5) for i in range(5))
    ch = chord(g, xsum.s())
    result = ch()
    print(result.get())
