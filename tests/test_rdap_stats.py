from src.rdap import RDAPChecker



def test_stats():


    domains = [

        "google.com",

        "asdasdasdasd123456.com",

        "facebook.com"

    ]


    checker = RDAPChecker(
        workers=3
    )


    results = checker.check_domains(
        domains
    )


    for r in results:
        print(r)



    print("\nSTATISTICS")

    print(
        checker.stats.report()
    )



if __name__=="__main__":

    test_stats()