import platform
import shutil


def get_whois_command() -> str | None:
    """
    Sistemde kullanılabilir whois komutunu bulur.
    """

    if platform.system() == "Windows":

        candidates = (
            "whois64.exe",
            "whois.exe",
        )

    else:

        candidates = (
            "whois",
        )

    for command in candidates:

        path = shutil.which(command)

        if path:
            return path

    return None