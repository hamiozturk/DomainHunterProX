"""
DomainHunter Pro X
Version : 0.2.0-alpha

Domain Candidate Model
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class DomainCandidate:

    # Domain

    name: str

    tld: str

    fqdn: str

    # Properties

    length: int

    pattern: str

    has_number: bool

    has_hyphen: bool

    # Scanner

    available: bool | None = None

    # Score

    score: int = 0

    # Notes

    note: str = ""