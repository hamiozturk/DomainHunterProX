from .whois_checker import WhoisChecker
from .rdap_checker import RDAPChecker
from .dns_checker import DNSChecker


class CheckerManager:

    def __init__(self, checker: str = "rdap"):

        self._checkers = {
            "whois": WhoisChecker(),
            "rdap": RDAPChecker(),
            "dns": DNSChecker(),
        }

        if checker not in self._checkers:
            raise ValueError(f"Unsupported checker: {checker}")

        self.checker = self._checkers[checker]

    def check(self, domain):
        self.checker.check(domain)