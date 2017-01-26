year = input("Jelenlegi év: ")
név = input('Hogy híjják kendet? ')
kor = input('És hány éves kend? ') # itt még stringet kapunk
kor = int(kor) # átalakítjuk egész számmá, azaz int-té
születési_év = 2016 - kor
print(név, ', kend ', születési_év, '-ban született.', sep='')
if 18-kor>=0:
    print(18-kor, "év múlva érettségizik.")
else:
    print(kor-18, "éve érettségizett.")
