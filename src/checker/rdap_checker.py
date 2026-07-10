from src.models import Domain
from src.rdap import RDAPChecker as RDAPEngine

from .base import BaseChecker


class RDAPChecker(BaseChecker):

    name = "rdap"

    def __init__(self):

        # RDAP Engine
        self.engine = RDAPEngine(workers=10)

    def check(self, domain: Domain) -> None:
        """
        Tek bir domain kontrol eder.
        Geriye dönük uyumluluk için korunuyor.
        """

        result = self.engine.check_domain(domain.name)

        self._apply_result(domain, result)

    def check_many(self, domains: list[Domain]) -> list[Domain]:
        """
        Birden fazla domaini ThreadPool ile kontrol eder.
        """

        names = [d.name for d in domains]

        results = self.engine.check_domains(names)

        result_map = {
            r["domain"]: r
            for r in results
        }

        for domain in domains:

            result = result_map.get(domain.name)

            if result:
                self._apply_result(domain, result)

        return domains

    def _apply_result(
        self,
        domain: Domain,
        result: dict
    ) -> None:

        domain.set_availability(
            available=result["available"],
            status=result["status"].upper(),
            method="RDAP"
        )