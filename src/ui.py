from PySide6.QtWidgets import (QStackedWidget, QStyle, QFrame, QVBoxLayout)
from PySide6.QtCore import QSize, QMargins , Qt
from PySide6.QtGui import QIcon, QGuiApplication

from style import stylesheet
import components


class UiApp(object):

    def init_gui(self, app):

        app.setWindowTitle('Container')
        app.setObjectName('main_app')
        # app.setWindowIcon(QIcon(':/images/logo.ico'))
        app.setBaseSize(QSize(1200, 700))
        app.setMinimumSize(app.baseSize())
        # app.setWindowFlags(Qt.FramelessWindowHint)
        app.setWindowFlags(Qt.NoDropShadowWindowHint)
        app.setAttribute(Qt.WA_TranslucentBackground)

        # center window
        app.setGeometry(QStyle.alignedRect(
            Qt.LeftToRight,
            Qt.AlignCenter,
            app.baseSize(),
            QGuiApplication.primaryScreen().availableGeometry(),
        ))
        
        # container
        self._bg_container = QFrame(app)
        self._bg_container.setLayout(QVBoxLayout())
        self._bg_container.layout().setSpacing(0)
        self._bg_container.layout().setContentsMargins(QMargins(0, 0, 0, 0))
        self._bg_container.setStyleSheet(stylesheet.app_bg)

        self._components_container = QStackedWidget()
        self._bg_container.layout().addWidget(self._components_container)
        app.setCentralWidget(self._bg_container)
        
        self._foo = components.Foo(app)
        self._components_container.addWidget(self._foo)

        # default
        self._components_container.setCurrentWidget(self._foo)