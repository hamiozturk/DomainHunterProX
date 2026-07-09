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



    def calculate(self, domain: Domain) -> None:

        name = domain.sld
        pattern = domain.pattern

        score = 0

        if len(name) == 2:
            score += 50

        elif len(name) == 3:
            score += 35

        elif len(name) == 4:
            score += 20

        for c in name:

            score += self.LETTER_VALUES.get(c, 4)
            score += self.BAD_LETTERS.get(c, 0)

        if pattern == "VV":
            score += 20

        elif pattern in ("VC", "CV"):
            score += 15

        elif pattern == "CC":
            score += 5

        if len(set(name)) == 1:
            score += 15

        if domain.extension == ".com":
            score += 15

        elif domain.extension == ".cat":
            score += 5

        domain.set_score(min(score, 100))