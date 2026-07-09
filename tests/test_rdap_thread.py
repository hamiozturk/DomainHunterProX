import time

from src.rdap import RDAPChecker



def test_thread_rdap():


    domains = [

        "google.com",
        "facebook.com",
        "amazon.com",
        "asdasdasdasd123456.com",
        "xyzzzz999999.com"

    ]


    checker = RDAPChecker(
        workers=5
    )


    start=time.time()


    results = checker.check_domains(
        domains
    )


    end=time.time()


    for r in results:
        print(r)


    print(
        "Süre:",
        round(end-start,2),
        "sn"
    )



if __name__=="__main__":
    test_thread_rdap()