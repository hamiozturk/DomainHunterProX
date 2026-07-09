import requests
import time


class RDAPClient:

    def __init__(
        self,
        timeout=5,
        retries=3
    ):
        self.timeout = timeout
        self.retries = retries

        self.session = requests.Session()

        self.session.headers.update({
            "User-Agent": "DomainHunterProX/1.0"
        })


    def check(self, domain):

        url = f"https://rdap.org/domain/{domain}"


        for attempt in range(1, self.retries + 1):

            try:

                response = self.session.get(
                    url,
                    timeout=self.timeout
                )


                # Domain bulundu
                if response.status_code == 200:

                    return {
                        "domain": domain,
                        "available": False,
                        "status": "registered"
                    }


                # Domain yok
                elif response.status_code == 404:

                    return {
                        "domain": domain,
                        "available": True,
                        "status": "available"
                    }


                else:

                    return {
                        "domain": domain,
                        "available": None,
                        "status": f"http_{response.status_code}"
                    }


            except requests.exceptions.Timeout:

                print(
                    f"Timeout {domain} "
                    f"attempt {attempt}/{self.retries}"
                )


            except requests.exceptions.RequestException as e:

                print(
                    f"RDAP error {domain}: {e}"
                )


            if attempt < self.retries:
                time.sleep(attempt * 2)



        return {
            "domain": domain,
            "available": None,
            "status": "failed"
        }