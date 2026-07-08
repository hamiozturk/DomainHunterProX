class DomainResult:


    def __init__(
        self,
        domain,
        available,
        method,
        status
    ):

        self.domain = domain
        self.available = available
        self.method = method
        self.status = status


    def to_dict(self):

        return {

            "domain": self.domain,
            "available": self.available,
            "method": self.method,
            "status": self.status

        }