"""
system classes are bundled in this module.
"""

from jaconv import alphabet2kana, kana2alphabet
from pigframe import System
import pyxel
import csv

from component import *

class SysInputText(System):
    def process(self):
        for ent, (siritori) in self.world.get_component(CpmSiritori):
            text: str = siritori.current_word
            if pyxel.btnp(pyxel.KEY_BACKSPACE) or pyxel.btnp(pyxel.KEY_KP_BACKSPACE):
                print("backspace")
                if (siritori.current_word_jp != "") and (0 < len(siritori.current_word_jp)):
                    print("erase")
                    siritori.current_word_jp = siritori.current_word_jp[:-1]
                    siritori.current_word = kana2alphabet(siritori.current_word_jp)
                    return
                    
            if pyxel.btnp(pyxel.KEY_A):
                text += "a"
            if pyxel.btnp(pyxel.KEY_B):
                text += "b"
            if pyxel.btnp(pyxel.KEY_C):
                text += "c"
            if pyxel.btnp(pyxel.KEY_D):
                text += "d"
            if pyxel.btnp(pyxel.KEY_E):
                text += "e"
            if pyxel.btnp(pyxel.KEY_F):
                text += "f"
            if pyxel.btnp(pyxel.KEY_G):
                text += "g"
            if pyxel.btnp(pyxel.KEY_H):
                text += "h"
            if pyxel.btnp(pyxel.KEY_I):
                text += "i"
            if pyxel.btnp(pyxel.KEY_J):
                text += "j"
            if pyxel.btnp(pyxel.KEY_K):
                text += "k"
            if pyxel.btnp(pyxel.KEY_L):
                text += "l"
            if pyxel.btnp(pyxel.KEY_M):
                text += "m"
            if pyxel.btnp(pyxel.KEY_N):
                text += "n"
            if pyxel.btnp(pyxel.KEY_O):
                text += "o"
            if pyxel.btnp(pyxel.KEY_P):
                text += "p"
            if pyxel.btnp(pyxel.KEY_Q):
                text += "q"
            if pyxel.btnp(pyxel.KEY_R):
                text += "r"
            if pyxel.btnp(pyxel.KEY_S):
                text += "s"
            if pyxel.btnp(pyxel.KEY_T):
                text += "t"
            if pyxel.btnp(pyxel.KEY_U):
                text += "u"
            if pyxel.btnp(pyxel.KEY_V):
                text += "v"
            if pyxel.btnp(pyxel.KEY_W):
                text += "w"
            if pyxel.btnp(pyxel.KEY_X):
                text += "x"
            if pyxel.btnp(pyxel.KEY_Y):
                text += "y"
            if pyxel.btnp(pyxel.KEY_Z):
                text += "z"
            if pyxel.btnp(pyxel.KEY_MINUS):
                text += "-"
            if text[-2:] == "si":
                text = text[:-2] + "shi"
            if text[-2:] == "ti":
                text = text[:-2] + "chi"
            if text[-2:] == "tu":
                text = text[:-2] + "tsu"
            text_jp: str = alphabet2kana(text)
            if (text_jp != "") and (0 < len(text_jp)):
                siritori.current_word_jp = text_jp
                siritori.current_word = text
                if pyxel.btnp(pyxel.KEY_RETURN) or pyxel.btnp(pyxel.KEY_RETURN2):
                    prev_word = siritori.history[-1]
                    if prev_word[-1] == "っ":
                        prev_word = prev_word[:-1] + "つ"
                    if prev_word[-1] == "ゃ":
                        prev_word = prev_word[:-1] + "や"
                    if prev_word[-1] == "ゅ":
                        prev_word = prev_word[:-1] + "ゆ"
                    if prev_word[-1] == "ょ":
                        prev_word = prev_word[:-1] + "よ"
                    if prev_word[-1] == "ぁ":
                        prev_word = prev_word[:-1] + "あ"
                    if prev_word[-1] == "ぃ":
                        prev_word = prev_word[:-1] + "い"
                    if prev_word[-1] == "ぅ":
                        prev_word = prev_word[:-1] + "う"
                    if prev_word[-1] == "ぇ":
                        prev_word = prev_word[:-1] + "え"
                    if prev_word[-1] == "ぉ":
                        prev_word = prev_word[:-1] + "お"
                    if prev_word[-1] == "ゎ":
                        prev_word = prev_word[:-1] + "わ"
                    if prev_word[-1] == "ー":
                        prev_word = prev_word[:-1]
                    
                    if text_jp in siritori.history:
                        return
                    if text_jp[-1] == "ん":
                        return
                        
                    if (text_jp[0] == prev_word[-1]):
                        siritori.history.append(text_jp)
                        siritori.current_word = ""
                        siritori.current_word_jp = ""
                        siritori.turn_who = "cpu"
                        
                        for ent, (cpu) in self.world.get_component(CpmCpu):
                            cpu.word_this_turn = ""
                            cpu.frame_started = pyxel.frame_count
                        
class SysCpuTurn(System):
    def __init__(self, world, priority: int = 0, **kwargs) -> None:
        super().__init__(world, priority, **kwargs)
        
        if "filepath" not in kwargs:
            raise ValueError("cpu is not specified.")
        
        self.filepath: str = kwargs["filepath"]
        words: list = []
        try:
            with open(self.filepath, "r", encoding="utf-8", errors="ignore") as f:
                words = f.readlines()[1:]
            
            words_new = []
            for word in words:
                word = word.replace("\n", "")
                words_new.append(word)
            self.words: list[str] = words_new
        except FileNotFoundError:
            raise FileNotFoundError("file not found.")
        
        
    def process(self):
        for ent, (siritori) in self.world.get_component(CpmSiritori):
            if siritori.turn_who == "cpu":
                for ent, (cpu) in self.world.get_component(CpmCpu):
                    for word in self.words:
                        prev_word = siritori.history[-1]
                        if prev_word[-1] == "っ":
                            prev_word = prev_word[:-1] + "つ"
                        if prev_word[-1] == "ゃ":
                            prev_word = prev_word[:-1] + "や"
                        if prev_word[-1] == "ゅ":
                            prev_word = prev_word[:-1] + "ゆ"
                        if prev_word[-1] == "ょ":
                            prev_word = prev_word[:-1] + "よ"
                        if prev_word[-1] == "ぁ":
                            prev_word = prev_word[:-1] + "あ"
                        if prev_word[-1] == "ぃ":
                            prev_word = prev_word[:-1] + "い"
                        if prev_word[-1] == "ぅ":
                            prev_word = prev_word[:-1] + "う"
                        if prev_word[-1] == "ぇ":
                            prev_word = prev_word[:-1] + "え"
                        if prev_word[-1] == "ぉ":
                            prev_word = prev_word[:-1] + "お"
                        if prev_word[-1] == "ゎ":
                            prev_word = prev_word[:-1] + "わ"
                        if prev_word[-1] == "ー":
                            prev_word = prev_word[:-1]
                        if word[0] == prev_word[-1]:
                            if word not in siritori.history:
                                cpu.word_this_turn = word
                                break
                    
                    count_letters_jp = (pyxel.frame_count - cpu.frame_started) * 2 // self.world.FPS
                    if len(cpu.word_this_turn) < count_letters_jp:
                        count_letters_jp = len(cpu.word_this_turn)
                    siritori.current_word_jp = cpu.word_this_turn[:count_letters_jp]
                    siritori.current_word = kana2alphabet(siritori.current_word_jp)
                    
                    if count_letters_jp == len(cpu.word_this_turn):
                        siritori.history.append(cpu.word_this_turn)
                        siritori.current_word = ""
                        siritori.current_word_jp = ""
                        siritori.turn_who = "player"
                        
                        cpu.word_this_turn = ""
                        cpu.frame_started = None
                        break