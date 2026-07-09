import time


class RDAPStats:


    def __init__(self):

        self.total = 0

        self.cache_hits = 0

        self.cache_misses = 0

        self.available = 0

        self.registered = 0

        self.errors = 0

        self.total_time = 0



    def start_timer(self):

        return time.time()



    def record(
        self,
        result,
        elapsed,
        from_cache=False
    ):


        self.total += 1

        self.total_time += elapsed


        if from_cache:

            self.cache_hits += 1

        else:

            self.cache_misses += 1



        if result["available"] is True:

            self.available += 1


        elif result["available"] is False:

            self.registered += 1


        else:

            self.errors += 1



    def report(self):

        average = 0

        if self.total:

            average = self.total_time / self.total



        return {

            "total_checked": self.total,

            "cache_hits": self.cache_hits,

            "cache_misses": self.cache_misses,

            "available": self.available,

            "registered": self.registered,

            "errors": self.errors,

            "average_time": round(
                average,
                4
            )

        }