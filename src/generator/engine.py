"""
DomainHunter Pro X
Version : 0.2.0-alpha

Generator Engine
"""

from __future__ import annotations

from itertools import product
from typing import Generator

from src.models import DomainCandidate

DEFAULT_ALPHABET = "abcdefghijklmnopqrstuvwxyz"


class GeneratorEngine:
    """
    Generates domain candidates.
    """

    def __init__(
        self,
        length: int,
        alphabet: str = DEFAULT_ALPHABET,
        tlds: list[str] | None = None,
    ) -> None:

        self.length = length
        self.alphabet = alphabet

        self.tlds = tlds or [
            ".com",
        ]

    def generate(self) -> Generator[DomainCandidate, None, None]:

        vowels = {"a", "e", "i", "o", "u"}

        for chars in product(
            self.alphabet,
            repeat=self.length,
        ):

            name = "".join(chars)

            pattern = "".join(
                "V" if c in vowels else "C"
                for c in name
            )

            has_number = any(
                c.isdigit()
                for c in name
            )

            has_hyphen = "-" in name

            for tld in self.tlds:

                yield DomainCandidate(
                    name=name,
                    tld=tld,
                    fqdn=f"{name}{tld}",
                    length=len(name),
                    pattern=pattern,
                    has_number=has_number,
                    has_hyphen=has_hyphen,
                )