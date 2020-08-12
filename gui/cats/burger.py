import sys
sys.path.append('..')
from gui import GUIManager

def set(manager, itemFrame):
    gui = GUIManager.GUIManager(3, manager, itemFrame)
    manager.gui = gui

    # Lane1
    gui.addItem(0, "ham")
    gui.addItem(0, "")
    gui.addItem(0, "")
    gui.addItem(0, "")
    gui.addItem(0, "")
    gui.addItem(0, "")
    gui.addItem(0, "")
    gui.addItem(0, "")
    gui.addItem(0, "")

    # Lane2
    gui.addItem(1, "bur")
    gui.addItem(1, "")
    gui.addItem(1, "")
    gui.addItem(1, "")
    gui.addItem(1, "")
    gui.addItem(1, "")
    gui.addItem(1, "")
    gui.addItem(1, "")
    gui.addItem(1, "")

    # Lane3
    gui.addItem(2, "ger")
    gui.addItem(2, "")
    gui.addItem(2, "")
    gui.addItem(2, "")
    gui.addItem(2, "")
    gui.addItem(2, "")
    gui.addItem(2, "")
    gui.addItem(2, "")
    gui.addItem(2, "nick")
