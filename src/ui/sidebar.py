"""
DomainHunter Pro X
Version : 0.1.0-alpha
Module  : Sidebar
"""

from __future__ import annotations

from dataclasses import dataclass

from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import (
    QFrame,
    QPushButton,
    QSizePolicy,
    QVBoxLayout,
)


@dataclass(slots=True)
class SidebarItem:
    key: str
    title: str


class Sidebar(QFrame):
    """
    Application sidebar.
    """

    page_requested = Signal(str)

    def __init__(self) -> None:

        super().__init__()

        self.setObjectName("Sidebar")

        self._buttons: dict[str, QPushButton] = {}

        self._build_ui()

    def _build_ui(self) -> None:

        layout = QVBoxLayout(self)

        layout.setContentsMargins(12, 12, 12, 12)
        layout.setSpacing(8)
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        pages = [
            SidebarItem("dashboard", "🏠 Dashboard"),
            SidebarItem("generator", "🎲 Generator"),
            SidebarItem("scanner", "🔍 Scanner"),
            SidebarItem("favorites", "⭐ Favorites"),
            SidebarItem("settings", "⚙ Settings"),
            SidebarItem("about", "ℹ About"),
        ]

        for page in pages:

            button = QPushButton(page.title)

            button.setObjectName("SidebarButton")

            button.setCheckable(True)

            button.setCursor(Qt.CursorShape.PointingHandCursor)

            button.setMinimumHeight(42)

            button.setSizePolicy(
                QSizePolicy.Policy.Expanding,
                QSizePolicy.Policy.Fixed,
            )

            button.clicked.connect(
                lambda checked=False, key=page.key: self.select_page(key)
            )

            layout.addWidget(button)

            self._buttons[page.key] = button

        layout.addStretch()

        self.select_page("dashboard")

    def select_page(self, key: str) -> None:
        """
        Select active page.
        """

        if key not in self._buttons:
            return

        for page_key, button in self._buttons.items():
            button.setChecked(page_key == key)

        self.page_requested.emit(key)

    def current_page(self) -> str | None:
        """
        Returns selected page.
        """

        for page_key, button in self._buttons.items():

            if button.isChecked():
                return page_key

        return None

    def set_enabled(self, enabled: bool) -> None:
        """
        Enable / disable all sidebar buttons.
        """

        for button in self._buttons.values():
            button.setEnabled(enabled)