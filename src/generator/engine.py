"""
DomainHunter Pro X
Version : 0.2.0-alpha

Generator Engine
"""

from __future__ import annotations

from itertools import product
from typing import Generator


DEFAULT_ALPHABET = "abcdefghijklmnopqrstuvwxyz"


class GeneratorEngine:

    def __init__(
        self,
        length: int,
        alphabet: str = DEFAULT_ALPHABET,
        tlds: list[str] | None = None,
    ):

        self.length = length
        self.alphabet = alphabet

        self.tlds = tlds or [
            ".com"
        ]

    def generate(self) -> Generator[str, None, None]:

        for chars in product(
            self.alphabet,
            repeat=self.length,
        ):

            name = "".join(chars)

            for tld in self.tlds:

                yield f"{name}{tld}"