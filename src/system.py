"""
system classes are bundled in this module.
"""

from jaconv import alphabet2kana, kana2alphabet
from pigframe import System
import pyxel

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
                    if (siritori.history[-1][-1] == text_jp[0]) and (text_jp not in siritori.history):
                        siritori.history.append(text_jp)
                        siritori.current_word = ""
                        siritori.current_word_jp = ""
                    elif text_jp in siritori.history:
                        print("same word!")
                        