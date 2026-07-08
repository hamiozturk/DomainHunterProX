from src.scorer import DomainScorer


scorer=DomainScorer()


tests=[
    ("aa.com","VV"),
    ("ab.com","VC"),
    ("qx.com","CC"),
    ("zz.com","CC"),
    ("ae.cat","VV")
]


for domain,pattern in tests:

    print(
        domain,
        "=>",
        scorer.calculate(domain,pattern)
    )