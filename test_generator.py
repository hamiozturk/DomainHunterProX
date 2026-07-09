from src.generator import GeneratorEngine



engine = GeneratorEngine(

    length=2,

    tlds=[
        ".com",
        ".cat"
    ]

)

count = 0

for domain in engine.generate():

    print(

        domain.fqdn,

        domain.pattern,

        domain.length

    )

    count += 1

    if count == 15:
        break