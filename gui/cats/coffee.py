"""Coffee

This class lays out the default item layout."""

import sys
sys.path.append('..')
from gui import GUIManager

def build(manager, item_frame):
    """This function involves the GUI manager and builds the layout"""

    gui = GUIManager.GUIManager(3, manager, item_frame)
    manager.gui = gui

    # Lane1
    gui.add_item(0, "Cappuccino")
    gui.add_item(0, "Espresso")
    gui.add_item(0, "")
    gui.add_item(0, "")
    gui.add_item(0, "")
    gui.add_item(0, "")
    gui.add_item(0, "")
    gui.add_item(0, "")
    gui.add_item(0, "")

    # Lane2
    gui.add_item(1, "Latte")
    gui.add_item(1, "")
    gui.add_item(1, "")
    gui.add_item(1, "")
    gui.add_item(1, "")
    gui.add_item(1, "")
    gui.add_item(1, "")
    gui.add_item(1, "")
    gui.add_item(1, "")

    # Lane3
    gui.add_item(2, "Iced Coffee")
    gui.add_item(2, "")
    gui.add_item(2, "")
    gui.add_item(2, "")
    gui.add_item(2, "")
    gui.add_item(2, "")
    gui.add_item(2, "")
    gui.add_item(2, "")
    gui.add_item(2, "")
