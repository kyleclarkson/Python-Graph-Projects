

class Schedule:

    __slots__ = '_indices', '_tasks', '_release_times', '_due_times'

    def __init__(self, indices, tasks, relase_times, due_times):
        self._indices = indices
        self._tasks = tasks
        self._relase_times = release_times
        self.due_times = due_times

class Env:

    