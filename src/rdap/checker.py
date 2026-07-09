from concurrent.futures import ThreadPoolExecutor, as_completed

from .client import RDAPClient



class RDAPChecker:


    def __init__(
        self,
        workers=10
    ):

        self.client = RDAPClient()
        self.workers = workers



    def check_domains(
        self,
        domains
    ):

        results = []


        with ThreadPoolExecutor(
            max_workers=self.workers
        ) as executor:


            futures = {
                executor.submit(
                    self.client.check,
                    domain
                ): domain

                for domain in domains
            }



            for future in as_completed(futures):

                result = future.result()

                results.append(result)



        return results