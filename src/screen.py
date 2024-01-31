"""
screen classes are bundled in this module.
"""

import pyxel
from pigframe import Screen

from component import *

class ScStart(Screen):
    """Start screen class.
    """
    def __init__(self, world, priority: int = 0, **kwargs) -> None:
        super().__init__(world, priority, **kwargs)
        # pyxel.images[0].load(0, 0, "assets/img.pyxres")
        pyxel.load("assets/img.pyxres")
        
    def draw(self):
        """Draw the screen.
        """
        pyxel.cls(13)
        pyxel.blt(220, 200, 0, 0, 0, 45, 39, 0)
        pyxel.blt(300, 210, 0, 48, 15, 29, 18, 0)
        pyxel.blt(360, 190, 0, 80, 8, 40, 48, 1) # 40 x 48
        self.world.bdf24.draw_text(265, 265, "しりとり", 0)
        
        self.world.bdf24.draw_text(145, 360, "[Enter/Return] を押してスタート", 0)
        
class ScPlay(Screen):
    """Play screen class.
    """
    def draw(self):
        """Draw the screen.
        """
        pyxel.cls(13)
        self.world.bdf16.draw_text(20, 20, "<[Q] ポーズ", 0)
        
        last_word_top = 0
        for ent, (siritori) in self.world.get_component(CpmSiritori):
            for i, word in enumerate(siritori.history[-5:]):
                width = len(word) * 24
                self.world.bdf24.draw_text(self.world.SCREEN_SIZE[0]//2 - width//2, 70 + 70 * i, word, 0)
                pyxel.blt(self.world.SCREEN_SIZE[0]//2 - 13, 105 + 70 * i, 0, 54, 40, 26, 30, 0)

                last_word_top = 105 + 70 * i
            
            input_width = min(max(len(siritori.current_word_jp) * 24 + 20, 200), 600)
            pyxel.rect(self.world.SCREEN_SIZE[0]//2 - input_width//2, last_word_top + 30, input_width, 40, 7)
            
            width = len(siritori.current_word_jp) * 24
            text_render_x = self.world.SCREEN_SIZE[0]//2 - width//2
            self.world.bdf24.draw_text(text_render_x, last_word_top + 38, siritori.current_word_jp, 0)
            
            text_bar_colors = [0, 7]
            pyxel.rect(text_render_x + width + 4, last_word_top + 38, 2, 24, text_bar_colors[(pyxel.frame_count // (self.world.FPS//2)) % 2])
        
        
class ScSettings(Screen):
    """Settings screen class.
    """
    def draw(self):
        """Draw the screen.
        """
        pyxel.cls(13)
        pyxel.text(50, 50, "Settings", 0)
        
        self.world.bdf24.draw_text(50, 100, "[Enter/Return] を押してゲームを再開", 0)
        self.world.bdf24.draw_text(50, 160, "[ESC] を押してゲームを閉じる", 0)
        self.world.bdf24.draw_text(50, 220, "[Space] を押してしりとり履歴を表示", 0)

class ScHistory(Screen):
    """History screen class.
    """
    def draw(self):
        """Draw the screen.
        """
        pyxel.cls(13)
        self.world.bdf16.draw_text(20, 20, "[Enter/Return] を押してゲームを再開", 0)
        
        for ent, (siritori) in self.world.get_component(CpmSiritori):
            last_word_top = 0
            for i, word in enumerate(siritori.history):
                self.world.bdf24.draw_text(50, 50 + 60 * i, word, 0)
                pyxel.blt(50, 80 + 60 * i, 0, 54, 40, 26, 30, 0)
                last_word_top = 80 + 60 * i
            
            pyxel.rect(50, last_word_top + 30, 180, 30, 7)