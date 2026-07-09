from dataclasses import dataclass
from datetime import datetime


@dataclass
class Domain:

    name: str

    extension: str = ""

    length: int = 0

    pattern: str = ""

    score: int = 0

    available: bool = False

    check_status: str = ""

    check_method: str = ""

    checked_at: datetime | None = None

    rdap_url: str = ""

    def __post_init__(self):

        self.name = self.name.lower()

        if "." in self.name:

            parts = self.name.split(".")

            self.extension = "." + parts[-1]

            self.length = len(parts[0])


    def set_score(self, score):

        self.score = score


    def set_availability(self,
                         available,
                         status="",
                         method="",
                         rdap_url=""):

        self.available = available

        self.check_status = status

        self.check_method = method

        self.rdap_url = rdap_url

        self.checked_at = datetime.utcnow()


    @property
    def sld(self):

        return self.name.split(".")[0]


    def __str__(self):

        return f"{self.name} ({self.score})"


    def to_dict(self):

        return {

            "domain": self.name,

            "sld": self.sld,

            "extension": self.extension,

            "length": self.length,

            "pattern": self.pattern,

            "score": self.score,

            "available": self.available,

            "status": self.check_status,

            "method": self.check_method,

            "checked_at": self.checked_at,

            "rdap_url": self.rdap_url

        }