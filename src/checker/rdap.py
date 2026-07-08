import requests

from .providers import RDAP_PROVIDERS
from .result import DomainResult

from config import RDAP_TIMEOUT



class RDAPChecker:


    def check(self, domain):

        tld = domain.split(".")[-1]


        if tld not in RDAP_PROVIDERS:

            return DomainResult(
                domain,
                False,
                "RDAP",
                "UNSUPPORTED_TLD"
            )


        url = (
            RDAP_PROVIDERS[tld]
            +
            domain
        )


        try:

            response = requests.get(
                url,
                timeout=RDAP_TIMEOUT
            )


            # 200 = kayıt var

            if response.status_code == 200:

                return DomainResult(
                    domain,
                    False,
                    "RDAP",
                    "REGISTERED"
                )


            # 404 = bulunamadı

            elif response.status_code == 404:

                return DomainResult(
                    domain,
                    True,
                    "RDAP",
                    "AVAILABLE"
                )


            else:

                return DomainResult(
                    domain,
                    False,
                    "RDAP",
                    f"HTTP_{response.status_code}"
                )


        except Exception as e:


            return DomainResult(
                domain,
                False,
                "RDAP",
                str(e)
            )