# Logs, console, commands
import collections
import time


class TimeCounter:
    def __init__(self):
        self.total_time = 0.0
        self.time = time.perf_counter()
        self.frame_times = collections.deque(maxlen=60)

    def fps_tick(self):
        t1 = time.perf_counter()
        dt = t1 - self.time
        self.time = t1
        self.frame_times.append(dt)

    def time_tick(self, time_beta):
        self.total_time += time_beta

    def get_time_string(self):
        total_time_hou = int(self.total_time) // 3600
        total_time_min = int(self.total_time) // 60
        total_time_sec = int(self.total_time) % 60
        total_time_string = f"{total_time_hou:02d}:{total_time_min:02d}:{total_time_sec:02d}"
        return total_time_string

    def get_fps(self):
        total_time = sum(self.frame_times)
        if total_time == 0:
            return 0
        else:
            return len(self.frame_times) / sum(self.frame_times)


class LogSystem:
    def __init__(self):
        self._current_scene = None
        self.timer = TimeCounter()

    def setup(self, current_scene):
        self._current_scene = current_scene

    def log(self, event, x, y):
        engine_time = self.timer.get_time_string()
        known_events = {0: 'windowResized',
                        1: 'fullscreenMode'}

        if event == known_events[0]:
            print(f"{engine_time} Window resized to: {x}, {y}")
        if event == known_events[1]:
            print(f"{engine_time} Resolution changed to: {x}x{y}")
        if x == -1 and y == -1:
            print(f"{engine_time} {event}")