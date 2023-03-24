from qtpy import QtCore
from qtpy.QtWidgets import QApplication
from pyqtconsole.console import PythonConsole
from pyqtconsole.highlighter import format
from krita import *


class PythonConsole2(PythonConsole):
    def keyPressEvent(self, event):
        print(event)
        super().keyPressEvent(event)

def open_console():
    parent = Krita.instance().activeWindow().qwindow()  # this steals keyboard focus if windowflag is tool

    console = PythonConsole(formats={
        'keyword':    format('darkred', 'bold'),
        'operator':   format('orange'),
        'brace':      format('orange'),
        'defclass':   format('greenyellow', 'bold'),
        'string':     format('gold'),
        'string2':    format('goldenrod'),
        'comment':    format('grey', 'italic'), # done
        'self':       format('mediumorchid', 'italic'),
        'numbers':    format('deepskyblue'),
        'inprompt':   format('white', 'bold'),
        'outprompt':  format('deepskyblue', 'bold'),
        },
        parent=parent)

    console.setStyleSheet("QWidget {background-color:#222222}")
    console.setWindowFlags(console.windowFlags() | QtCore.Qt.Window )
    console.setWindowTitle("Python Console")
    console.show()
    console.eval_queued()


class PyConsoleExtension(Extension):

    def __init__(self, parent):
        # This is initialising the parent, always important when subclassing.
        super().__init__(parent)

    def setup(self):
        pass

    def createActions(self, window):
        action = window.createAction("pyqtConsoleAction", "Python Console", "tools")
        action.triggered.connect(open_console)


# And add the extension to Krita's list of extensions:
Krita.instance().addExtension(PyConsoleExtension(Krita.instance()))


# make it dockable, but keys are captured by parent for shortcuts. e.g. b is brush
# class PyQtConsoleDocker(DockWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Python Console")
#         self.console = PythonConsole()
#         self.setWidget(self.console)
#         self.console.eval_queued()
#
#         # self.console.setFocusPolicy(Qt.StrongFocus)
#         # self.console.setFocusProxy(parent_widget)
#         # hookup eventfilter from self.console to parent_widget
#         # self.console.installEventFilter(self)
#
#     def canvasChanged(self, canvas):
#         pass
#
# Krita.instance().addDockWidgetFactory(DockWidgetFactory("Python Console", DockWidgetFactoryBase.DockRight, PyQtConsoleDocker))