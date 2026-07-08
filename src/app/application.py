from PySide6.QtWidgets import QApplication


class Application(QApplication):
    """Main Qt application."""

    def __init__(self, argv):

        super().__init__(argv)

        self.setApplicationName("DomainHunter Pro X")
        self.setApplicationVersion("0.1.0-alpha")
        self.setOrganizationName("Hami Software")