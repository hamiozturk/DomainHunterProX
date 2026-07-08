from src.checker.rdap import RDAPChecker


checker = RDAPChecker()


domains = [

    "google.com",
    "asdasdasdasd123456.com",
    "example.cat",
    "test.ai"

]


for domain in domains:

    result = checker.check(domain)

    print(
        result.to_dict()
    )