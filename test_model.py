from models import Domain


domain = Domain(
    "aa.com",
    pattern="VV"
)


domain.set_score(100)


domain.set_availability(
    True,
    "AVAILABLE",
    "RDAP"
)


print(domain)

print()

print(domain.to_dict())