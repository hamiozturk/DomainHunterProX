from src.models import Domain, DomainCandidate


class DomainFactory:

    @staticmethod
    def from_candidate(candidate: DomainCandidate) -> Domain:

        domain = Domain(
            name=candidate.fqdn,
            pattern=candidate.pattern
        )

        return domain