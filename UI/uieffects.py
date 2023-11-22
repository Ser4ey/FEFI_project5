import ctypes
from ctypes.wintypes import DWORD, ULONG
from ctypes import windll, c_bool, c_int, POINTER, Structure

from PyQt6 import uic
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFontDatabase
from UI.uiconstants import UIConst


class AccentPolicy(Structure):
    _fields_ = [
        ('AccentState', DWORD),
        ('AccentFlags', DWORD),
        ('GradientColor', DWORD),
        ('AnimationId', DWORD),
    ]


class WINCOMPATTRDATA(Structure):
    _fields_ = [
        ('Attribute', DWORD),
        ('Data', POINTER(AccentPolicy)),
        ('SizeOfData', ULONG),
    ]


SetWindowCompositionAttribute = windll.user32.SetWindowCompositionAttribute
SetWindowCompositionAttribute.restype = c_bool
SetWindowCompositionAttribute.argtypes = [c_int, POINTER(WINCOMPATTRDATA)]


def blur_background(window):
    window.setWindowFlag(Qt.WindowType.FramelessWindowHint)
    window.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
    accent_policy = AccentPolicy()
    accent_policy.AccentState = 3

    win_comp_attr_data = WINCOMPATTRDATA()
    win_comp_attr_data.Attribute = 19
    win_comp_attr_data.SizeOfData = ctypes.sizeof(accent_policy)
    win_comp_attr_data.Data = ctypes.pointer(accent_policy)

    SetWindowCompositionAttribute(c_int(int(window.winId())), ctypes.pointer(win_comp_attr_data))


def setup_ui_form(window, ui_form):
    with open(f"{UIConst.styles_path}/{window.theme}.css") as style:
        uic.loadUi(f'data/ui/{ui_form}.ui', window)
        QFontDatabase.addApplicationFont(f"{UIConst.fonts_path}/Comfortaa/Comfortaa-Medium.ttf")
        window.setStyleSheet(style.read())
        window.show()
