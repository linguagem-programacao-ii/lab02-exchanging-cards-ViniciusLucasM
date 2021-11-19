while True:
    alice, betty = input().split()

    if alice == '0' and betty == '0':
        break

    cartas_alice = list()
    cartas_betty = list()

    for i in input().split():
        cartas_alice.append(i)

    for i in input().split():
        cartas_betty.append(i)

    alice = set(cartas_alice)
    betty = set(cartas_betty)

    cartas = betty

    if len(alice) < len(betty):
        cartas = alice
        alice = betty

    cartas = [x for x in cartas if x not in alice]
    print(len(cartas))
