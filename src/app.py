"""
Main application script.
"""

from pigframe import World
import pyxel

from system import *
from screen import *
from event import *
from component import *
from font import BDFRenderer

class App(World):
    """Main application class.
    """
    def __init__(self):
        super().__init__()
        self.init()

    def init(self):
        """Initialize the application.
        """
        self.SCREEN_SIZE = (640, 640)
        self.FPS = 60
        pyxel.init(self.SCREEN_SIZE[0], self.SCREEN_SIZE[1], title="Siritori", fps=self.FPS, quit_key=pyxel.KEY_NONE)
        bdf24 = BDFRenderer("assets/b24.bdf")
        bdf16 = BDFRenderer("assets/b16.bdf")
        bdf14 = BDFRenderer("assets/b14.bdf")
        self.bdf24 = bdf24
        self.bdf16 = bdf16
        self.bdf14 = bdf14
        pyxel.mouse(True)
    
    def run(self):
        """Run the application.
        """
        pyxel.run(self.update, self.draw)
        
    def update(self):
        """Update the application systems.
        """
        self.process()
        
    def draw(self):
        """Update the application screens.
        """
        self.process_screens()

def construct():
    """Construct the application.
    """
    app = App()
    app.add_scenes(["start", "play", "settings", "history"])
    
    siritori = app.create_entity()
    cpu = app.create_entity()
    app.add_component_to_entity(siritori, CpmSiritori, current_word="", history=["しりとり", "りんご"])
    app.add_component_to_entity(cpu, CpmCpu)

    app.add_screen_to_scenes(ScStart, "start", 0)
    app.add_screen_to_scenes(ScPlay, "play", 0)
    app.add_screen_to_scenes(ScSettings, "settings", 0)
    app.add_screen_to_scenes(ScHistory, "history", 0)

    app.add_scene_transition("start", "play", lambda: pyxel.btn(pyxel.KEY_RETURN))
    app.add_scene_transition("play", "settings", lambda: pyxel.btn(pyxel.KEY_Q))
    app.add_scene_transition("settings", "play", lambda: pyxel.btn(pyxel.KEY_RETURN))
    app.add_scene_transition("settings", "history", lambda: pyxel.btn(pyxel.KEY_SPACE))
    app.add_scene_transition("history", "play", lambda: pyxel.btn(pyxel.KEY_RETURN))
    app.add_scene_transition("history", "settings", lambda: pyxel.btn(pyxel.KEY_Q))
    app.add_scene_transition("play", "history", lambda: pyxel.btn(pyxel.KEY_SPACE))

    
    app.add_system_to_scenes(SysInputText, "play", 0)
    app.add_system_to_scenes(SysCpuTurn, "play", 1, filepath="assets/word_list.csv")
    
    app.add_event_to_scene(EvSettingsCloseApp, "settings", lambda: pyxel.btn(pyxel.KEY_ESCAPE), 0)

    app.current_scene = "start"
    return app

if __name__ == "__main__":
    app = construct()
    app.run()