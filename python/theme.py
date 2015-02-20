# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sys
try:
    import ttk
    from tkFont import Font
except ImportError:
    from tkinter import ttk
    from tkinter.font import Font

class _SnapPyStyle:
    def __init__(self):
        ttk_style = ttk.Style()
        if sys.platform == 'darwin':
            self.WindowBG = 'SystemDialogBackgroundActive'
            self.GroupBG = 'SystemSecondaryGroupBoxBackground'
        elif sys.platform == 'win32':
            self.WindowBG = self.GroupBG = 'SystemButtonHighlight'
        else:
            self.WindowBG = self.GroupBG = ttk_style.lookup('TLabelframe', 'background')
            self.font_info = fi = Font(font=ttk_style.lookup('TLabel', 'font')).actual()
            fi['size'] = abs(fi['size']) # Why would the size be negative???

    def configure(self):
        if sys.platform == 'win32':
            ttk_style.configure('TLabelframe', background=GroupBG)
            ttk_style.configure('TLabelframe.Label', background=GroupBG)
            ttk_style.configure('TLabel', background=GroupBG)

def SnapPyStyle(root):
    if root is None:
        if Tk_._default_root is None:
            root = Tk_.Tk(className='snappy')
            root.iconify()
        else:
            root = Tk_._default_root
    try:
        return root.style
    except AttributeError:
        root.style = style = _SnapPyStyle()
        style.configure()
        return style 