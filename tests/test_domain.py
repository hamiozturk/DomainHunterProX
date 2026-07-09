from src.models import Domain

domain = Domain(
    name="aa.com",
    pattern="VV"
)

domain.set_score(100)

domain.set_availability(
    available=True,
    status="AVAILABLE",
    method="RDAP",
    rdap_url="https://rdap.verisign.com/com/v1/domain/aa.com"
)

print(domain)
print()
print(domain.to_dict())
print()
print("SLD:", domain.sld)
print("Extension:", domain.extension)
print("Length:", domain.length)
print("Checked:", domain.checked_at)