class DomainScorer:
    BAD_LETTERS = {
    "q":-8,
    "x":-6,
    "z":-4,
    "j":-5
    }


    LETTER_VALUES = {

        "a":10,
        "e":10,
        "i":9,
        "o":9,
        "l":8,
        "n":8,
        "r":8,
        "s":8,
        "t":8,

        "m":7,
        "c":6,
        "d":6,
        "b":5,
        "p":5,

        "q":2,
        "x":2,
        "z":2,
        "j":2
    }



    def calculate(self, domain, pattern=None):

        name = domain.split(".")[0].lower()

        score = 0


        # uzunluk

        if len(name)==2:
            score += 50

        elif len(name)==3:
            score += 35

        elif len(name)==4:
            score += 20



        # harf kalitesi

        for c in name:

            score += self.LETTER_VALUES.get(c,4)

            score += self.BAD_LETTERS.get(c,0)



        # pattern

        if pattern:

            if pattern=="VV":
                score +=20

            elif pattern=="VC" or pattern=="CV":
                score +=15

            elif pattern=="CC":
                score +=5



        # çift harf

        if len(set(name))==1:
            score +=15



        # uzantı

        if domain.endswith(".com"):
            score +=15

        elif domain.endswith(".cat"):
            score +=5



        return min(score,100)