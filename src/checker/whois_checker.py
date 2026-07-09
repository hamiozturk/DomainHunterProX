import subprocess

from src.models import Domain

from .base import BaseChecker
from .utils import get_whois_command


class WhoisChecker(BaseChecker):

    name = "whois"

    def __init__(self):

        self.command = get_whois_command()

    def check(self, domain: Domain) -> None:

        if self.command is None:

            domain.set_availability(
                available=False,
                status="WHOIS_NOT_FOUND",
                method="WHOIS",
            )

            return

        try:

            result = subprocess.run(
                [self.command, domain.name],
                capture_output=True,
                text=True,
                timeout=10,
            )

            output = (result.stdout + result.stderr).lower()

            domain.set_availability(
                available=False,
                status="WHOIS_OK",
                method="WHOIS",
            )

        except subprocess.TimeoutExpired:

            domain.set_availability(
                available=False,
                status="TIMEOUT",
                method="WHOIS",
            )

        except Exception as e:

            domain.set_availability(
                available=False,
                status=str(e),
                method="WHOIS",
            )