from src.rdap import RDAPClient


def test_rdap_check():

    client = RDAPClient()

    domains = [
        "google.com",
        "asdasdasdasd123456.com"
    ]

    for domain in domains:

        result = client.check(domain)

        print(result)


if __name__ == "__main__":
    test_rdap_check()