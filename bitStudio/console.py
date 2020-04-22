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
        total_time_min = int(self.total_time) // 60
        total_time_sec = int(self.total_time) % 60
        total_time_string = f"{total_time_min:02d}:{total_time_sec:02d}"
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
        self.current_events = []
        self.current_event = 0
        self.console_message = 'Error, no console message'

    def setup(self, current_scene):
        self._current_scene = current_scene
        self.current_events = ['00:00:00 Freezing ice ', '00:00:00 Water mixing', '00:00:00 Sprites? Who cares?',
                               '00:00:01 Pairing in progress']

    def log(self, event):
        engine_time = self.timer.get_time_string()
        if event:
            if self.current_event < 3:
                self.current_event += 1
            else:
                self.current_event = 0
            self.console_message = f"{engine_time} {event}"
            print(self.console_message)
            self.current_events[self.current_event] = self.console_message
            self.current_events.sort()