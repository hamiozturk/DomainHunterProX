from src.rdap import RDAPChecker
import time



def test_cache_flow():


    domains = [

        "google.com",
        "asdasdasdasd123456.com"

    ]


    checker = RDAPChecker(
        workers=2
    )


    print("\n--- İlk Çalışma ---")

    start=time.time()

    result1 = checker.check_domains(
        domains
    )

    print(result1)

    print(
        "Süre:",
        round(time.time()-start,2)
    )



    print("\n--- İkinci Çalışma ---")

    start=time.time()

    result2 = checker.check_domains(
        domains
    )

    print(result2)

    print(
        "Süre:",
        round(time.time()-start,2)
    )



if __name__=="__main__":

    test_cache_flow()