noktalar = [(1, 2), (4, 6), (7, 8), (2, 3)]

def oklid_mesafesi(nokta1, nokta2):
    return ((nokta2[0] - nokta1[0]) ** 2 + (nokta2[1] - nokta1[1]) ** 2) ** 0.5

mesafeler = []

for i in range(len(noktalar)):
    for j in range(i + 1, len(noktalar)):
        mesafe = oklid_mesafesi(noktalar[i], noktalar[j])
        mesafeler.append(mesafe)

min_mesafe = min(mesafeler)

print("Hesaplanan mesafeler:", mesafeler)
print("Minimum mesafe:", min_mesafe)