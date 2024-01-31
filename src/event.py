"""Event module
"""
from pigframe import Event
import pyxel

class EvSettingsCloseApp(Event):
    """Settings event class.
    """
    def _Event__process(self):
        """Process the event.
        """
        pyxel.quit()