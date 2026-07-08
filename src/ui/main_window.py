from PySide6.QtWidgets import (
    QLabel,
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

        self.setup_ui()

    def setup_ui(self):

        central = QWidget()

        self.setCentralWidget(central)

        layout = QVBoxLayout(central)

        title = QLabel("🚀 DomainHunter Pro X")

        title.setStyleSheet("""
            font-size:28px;
            font-weight:bold;
            padding:20px;
        """)

        layout.addWidget(title)

        layout.addStretch()

        status = QStatusBar()

        status.showMessage("Ready")

        self.setStatusBar(status)