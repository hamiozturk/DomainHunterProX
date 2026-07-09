import time

from .base import BaseChecker
from .result import DomainCheckResult


class DNSChecker(BaseChecker):

    name = "dns"

    def check(self, domain: str) -> DomainCheckResult:

        start = time.perf_counter()

        return DomainCheckResult(
            domain=domain,
            available=False,
            checker=self.name,
            response_time=time.perf_counter() - start,
        )