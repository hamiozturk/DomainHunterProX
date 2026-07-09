from src.models import Domain
from .providers import RDAP_PROVIDERS
from config import RDAP_TIMEOUT

import requests


class RDAPChecker:

    def check(self, domain: Domain) -> None:

        tld = domain.extension.replace(".", "")

        if tld not in RDAP_PROVIDERS:

            domain.set_availability(
                available=False,
                status="UNSUPPORTED_TLD",
                method="RDAP"
            )
            return

        url = RDAP_PROVIDERS[tld] + domain.name

        try:

            response = requests.get(
                url,
                timeout=RDAP_TIMEOUT
            )

            if response.status_code == 200:

                domain.set_availability(
                    available=False,
                    status="REGISTERED",
                    method="RDAP",
                    rdap_url=url
                )

            elif response.status_code == 404:

                domain.set_availability(
                    available=True,
                    status="AVAILABLE",
                    method="RDAP",
                    rdap_url=url
                )

            else:

                domain.set_availability(
                    available=False,
                    status=f"HTTP_{response.status_code}",
                    method="RDAP",
                    rdap_url=url
                )

        except Exception as e:

            domain.set_availability(
                available=False,
                status=str(e),
                method="RDAP",
                rdap_url=url
            )