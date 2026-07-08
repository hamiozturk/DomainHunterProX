from PySide6.QtCore import Qt

from PySide6.QtWidgets import (
    QLabel,
    QFrame,
    QHBoxLayout,
    QMainWindow,
    QStatusBar,
    QVBoxLayout,
    QWidget,
)


class MainWindow(QMainWindow):

    def __init__(self, config, database):

        super().__init__()

        self.config = config
        self.database = database

        self.setWindowTitle(
            self.config.get("app", "name")
        )

        self.resize(
            self.config.get("window", "width"),
            self.config.get("window", "height"),
        )

        self.build_ui()

    def build_ui(self):

        root = QWidget()

        self.setCentralWidget(root)

        root_layout = QVBoxLayout(root)
        root_layout.setContentsMargins(0, 0, 0, 0)
        root_layout.setSpacing(0)

        # HEADER

        header = QFrame()
        header.setObjectName("Header")
        header.setFixedHeight(60)

        header_layout = QHBoxLayout(header)

        title = QLabel("DomainHunter Pro X")
        title.setObjectName("Title")

        header_layout.addWidget(title)
        header_layout.addStretch()

        root_layout.addWidget(header)

        # BODY

        body = QWidget()

        body_layout = QHBoxLayout(body)
        body_layout.setContentsMargins(0, 0, 0, 0)
        body_layout.setSpacing(0)

        # Sidebar

        sidebar = QFrame()
        sidebar.setObjectName("Sidebar")
        sidebar.setFixedWidth(230)

        # Content

        content = QFrame()
        content.setObjectName("Content")

        content_layout = QVBoxLayout(content)

        lbl = QLabel("Dashboard")

        lbl.setAlignment(Qt.AlignCenter)

        lbl.setStyleSheet("""
            font-size:28px;
            font-weight:bold;
        """)

        content_layout.addStretch()
        content_layout.addWidget(lbl)
        content_layout.addStretch()

        body_layout.addWidget(sidebar)
        body_layout.addWidget(content)

        root_layout.addWidget(body)

        status = QStatusBar()

        status.showMessage("Ready")

        self.setStatusBar(status)