import arcade


class Scene:
    def __init__(self):
        self._current_scene_ = None


class Intro(Scene):
    def __init__(self):
        super().__init__()
        self._visibility = False
        self._current_scene = None

    def setup(self, current_scene):
        self._current_scene = current_scene

    def on_draw(self):
        pass

    def update(self):
        pass


class Screen(Scene):
    def __init__(self):
        super().__init__()
        self._visibility = False
        self._current_scene = None
        self.mouse_position_x = 0
        self.mouse_position_y = 0

    def setup(self, current_scene):
        self._current_scene = current_scene

    def draw_cursor(self, position_x, position_y):
        self.mouse_position_x = position_x
        self.mouse_position_y = position_y

    def on_draw(self, mouse_x, mouse_y):
        self.draw_cursor(mouse_x, mouse_y)

    def on_draw_developer_mode(self, mode_switch, width, height, engine_time, engine_fps, current_scene, logs):
        if mode_switch:
            # DEVELOPER MODE: Draw totalTime/FPS/sysInfo:
            arcade.draw_text(f"Time: {engine_time}", 10, height - 20, arcade.color.BLACK, 12, )
            arcade.draw_text(f"FPS: {engine_fps:3.0f}", 10, height - 40, arcade.color.BLACK, 12)
            # DEVELOPER MODE: Draw mouse positions (screen + map tile)
            arcade.draw_text(f"Position: {self.mouse_position_x:3.0f}/{width:3.0f},"
                             f"{self.mouse_position_y:3.0f}/{height:3.0f}", 10, height - 60, arcade.color.BLACK, 12)
            arcade.draw_text(f"Scene: {current_scene}", 10, height - 80, arcade.color.BLACK, 12, )
            # Logs: Display last 4 logs:
            arcade.draw_text(f"{logs[0]}", 300, height - 20, arcade.color.BLACK, 12, )
            arcade.draw_text(f"{logs[1]}", 300, height - 40, arcade.color.BLACK, 12, )
            arcade.draw_text(f"{logs[2]}", 300, height - 60, arcade.color.BLACK, 12, )
            arcade.draw_text(f"{logs[3]}", 300, height - 80, arcade.color.BLACK, 12, )
        else:
            pass

    def update(self):
        pass

