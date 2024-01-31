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
        self.world.bdf24.draw_text(80, 138, "しりとり", 0)
        pyxel.blt(200, 140, 0, 48, 15, 29, 18, 0)
        pyxel.blt(240, 130, 0, 0, 0, 45, 39, 0)
        pyxel.blt(320, 140, 0, 48, 15, 29, 18, 0)
        pyxel.blt(380, 120, 0, 80, 8, 40, 48, 1) # 40 x 48
        
        
        self.world.bdf24.draw_text(145, 220, "[Enter/Return] を押してスタート", (pyxel.frame_count * 3 // self.world.FPS) % 16)
        self.world.bdf24.draw_text(80, 300, "遊び方")
        
        pyxel.rect(80, 330, 460, 260, 7)
        self.world.bdf16.draw_text(100, 340, "New! CPUと対戦できます！ (CPUは非常に強いです。)", 8)
        self.world.bdf16.draw_text(100, 370, "しりとりを始めよう。", 0)
        self.world.bdf16.draw_text(100, 400, "しりとりを始めたらスペースキーを押して履歴が見れる。", 0)
        self.world.bdf16.draw_text(100, 430, "しりとりをするにはキーボードが必要です。", 0)
        self.world.bdf16.draw_text(100, 460, "半角入力に切り替えて始めてください。", 0)
        
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
            text_color = 0
            count_words_hidden = max(len(siritori.history), 5)
            for i, word in enumerate(siritori.history[-5:]):
                text_color = 0
                if i + count_words_hidden < 3:
                    text_color = 0
                elif (i + count_words_hidden) % 2 == 0:
                    text_color = 8
                width = len(word) * 24
                self.world.bdf24.draw_text(self.world.SCREEN_SIZE[0]//2 - width//2, 70 + 70 * i, word, text_color)
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
        self.world.bdf16.draw_text(15, 10, "[Enter/Return] を押してゲームを再開", 0)
        
        for ent, (siritori) in self.world.get_component(CpmSiritori):
            last_word_top = 0
            x_i = 0
            y_i = 0
            for i, word in enumerate(siritori.history):
                text_color = 0
                if (i + 1) % 2 == 0:
                    text_color = 8
                if 0 < i and i % 9 == 0:
                    x_i += 1
                    y_i = 0
                    
                if 2 < x_i and 9 < y_i:
                    print("too many words")
                    return
                
                self.world.bdf24.draw_text(30 + 200 * x_i, 45 + 60 * y_i, f"{i+1} {word}", text_color)
                pyxel.blt(64 + 200 * x_i, 75 + 60 * y_i, 0, 54, 40, 26, 30, 0)
                last_word_top = 75 + 60 * y_i
                
                y_i += 1
            
            self.world.bdf24.draw_text(30 + 200 * x_i, last_word_top + 33, f"{len(siritori.history)+1}", 0)
            pyxel.rect(55 + 200 * x_i, last_word_top + 30, 100, 30, 7)