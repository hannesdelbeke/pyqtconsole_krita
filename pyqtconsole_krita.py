from qtpy import QtCore
from qtpy.QtWidgets import QApplication
from pyqtconsole.console import PythonConsole
from pyqtconsole.highlighter import format
from krita import *


def open_console():
    # app = QApplication.instance()
    # if not app:
    #     app = QApplication(sys.argv)

    # hookup bqt if found to keep in foreground
    parent = None
    # if hasattr(app, 'blender_widget'):
    #     parent = app.blender_widget

    # todo get colors dynamically from blender style
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
    console.setWindowFlags(console.windowFlags() | QtCore.Qt.Tool)
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


# Krita.instance().addDockWidgetFactory(DockWidgetFactory("Python Console", DockWidgetFactoryBase.DockRight, MyDocker))
# And add the extension to Krita's list of extensions:
Krita.instance().addExtension(PyConsoleExtension(Krita.instance()))
