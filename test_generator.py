from src.generator import GeneratorEngine

engine = GeneratorEngine(

    length=2,

    tlds=[
        ".com",
        ".net",
        ".cat",
    ]

)

count = 0

for domain in engine.generate():

    print(domain)

    count += 1

    if count == 20:
        break

print()

print("Generated:", count)