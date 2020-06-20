

class DataPoint:

    __slots__ = '_vertex', '_release_time', '_due_time', '_is_queried'

    def __init__(self, vertex, release_time, due_time):
        self._vertex = vertex
        self._release_time = release_time
        self._due_time = due_time
        self._is_queried = False

    def query(self, deltaTime):
        if deltaTime >= self._release_time:
            self._is_queried = True

    def is_overdue(self, deltaTime):
        return deltaTime >= self._due_time

    def __str__(self):
        return 'vertex: {} release: {} due: {}'.format(self._vertex, self._release_time, self._due_time)

class Schedule:

    __slots__ = '_data_points'

    def __init__(self):
        self._data_points = []

    def add_data_point(self, data_point):
        self._data_points.append(data_point)

    def __str__(self):
        return '\n'.join(map(str, self._data_points))


if __name__ == '__main__':

    schedule = Schedule()
    schedule.add_data_point(DataPoint('v1', 0, 1))
    schedule.add_data_point(DataPoint('v3', 1, 3))
    schedule.add_data_point(DataPoint('v5', 3, 5))
    schedule.add_data_point(DataPoint('v1', 3, 5))
    schedule.add_data_point(DataPoint('v2', 5, 5))
    schedule.add_data_point(DataPoint('v5', 6, 8))


