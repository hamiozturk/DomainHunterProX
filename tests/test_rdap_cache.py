from src.rdap import RDAPCache



def test_cache():


    cache = RDAPCache(
        "data/test_cache.db"
    )


    data = {

        "domain":"testexample123.com",

        "available":True,

        "status":"available"

    }


    cache.set(data)



    result = cache.get(
        "testexample123.com"
    )


    print(result)



if __name__=="__main__":

    test_cache()