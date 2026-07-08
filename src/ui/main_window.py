"""
DomainHunter Pro X

Main Window
"""

from __future__ import annotations

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

from src.ui.sidebar import Sidebar


class MainWindow(QMainWindow):
    """Application main window."""

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

        self.sidebar: Sidebar | None = None
        self.content_frame: QFrame | None = None
        self.content_label: QLabel | None = None

        self.build_ui()

    def build_ui(self) -> None:

        root = QWidget(self)

        self.setCentralWidget(root)

        root_layout = QVBoxLayout(root)
        root_layout.setContentsMargins(0, 0, 0, 0)
        root_layout.setSpacing(0)

        # =====================================================
        # HEADER
        # =====================================================

        header = QFrame()
        header.setObjectName("Header")
        header.setFixedHeight(60)

        header_layout = QHBoxLayout(header)
        header_layout.setContentsMargins(15, 0, 15, 0)

        title = QLabel("DomainHunter Pro X")
        title.setObjectName("Title")

        header_layout.addWidget(title)
        header_layout.addStretch()

        root_layout.addWidget(header)

        # =====================================================
        # BODY
        # =====================================================

        body = QWidget()

        body_layout = QHBoxLayout(body)
        body_layout.setContentsMargins(0, 0, 0, 0)
        body_layout.setSpacing(0)

        # ---------------- Sidebar ----------------

        self.sidebar = Sidebar()

        self.sidebar.setFixedWidth(
            self.config.get(
                "ui",
                "sidebar_width",
                default=230,
            )
        )

        self.sidebar.page_requested.connect(
            self.change_page
        )

        body_layout.addWidget(self.sidebar)

        # ---------------- Content ----------------

        self.content_frame = QFrame()

        self.content_frame.setObjectName("Content")

        content_layout = QVBoxLayout(self.content_frame)

        content_layout.setContentsMargins(20, 20, 20, 20)

        self.content_label = QLabel("Dashboard")

        self.content_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.content_label.setStyleSheet("""
            font-size:28px;
            font-weight:bold;
        """)

        content_layout.addStretch()
        content_layout.addWidget(self.content_label)
        content_layout.addStretch()

        body_layout.addWidget(self.content_frame, 1)

        root_layout.addWidget(body, 1)

        # =====================================================
        # STATUS BAR
        # =====================================================

        status = QStatusBar()

        status.showMessage("Ready")

        self.setStatusBar(status)

    def change_page(self, page: str) -> None:
        """
        Sidebar page selection.
        """

        titles = {
            "dashboard": "Dashboard",
            "generator": "Generator",
            "scanner": "Scanner",
            "favorites": "Favorites",
            "settings": "Settings",
            "about": "About",
        }

        text = titles.get(page, page.title())

        if self.content_label:
            self.content_label.setText(text)

        self.statusBar().showMessage(
            f"Current Page : {text}"
        )