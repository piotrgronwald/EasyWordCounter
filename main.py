tekst = input('Wpisz tekst: ')

slowa = tekst.split(' ')
sin_slowa = set(slowa)

for slowo in sin_slowa:
    print(f"'{slowo}' occurs {slowa.count(slowo)} times.")
