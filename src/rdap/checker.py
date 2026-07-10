from concurrent.futures import ThreadPoolExecutor, as_completed
import time

from .client import RDAPClient
from .cache import RDAPCache
from .stats import RDAPStats



class RDAPChecker:


    def __init__(
        self,
        workers=10
    ):

        self.client = RDAPClient()

        self.cache = RDAPCache()

        self.stats = RDAPStats()

        self.workers = workers



    def check_domain(
        self,
        domain
    ):

        print(type(domain), domain)

        start = time.time()


        # Önce cache kontrolü

        cached = self.cache.get(domain)


        if cached:

            cached["from_cache"] = True


            self.stats.record(
                cached,
                time.time() - start,
                True
            )


            return cached



        # Cache yoksa RDAP sorgusu

        result = self.client.check(domain)



        # Cache'e kaydet

        self.cache.set(result)



        result["from_cache"] = False



        self.stats.record(
            result,
            time.time() - start,
            False
        )


        return result




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
                    self.check_domain,
                    domain
                ): domain

                for domain in domains

            }



            for future in as_completed(futures):

                result = future.result()

                results.append(result)



        return results