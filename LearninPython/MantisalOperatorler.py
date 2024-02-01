# Mantıksal oğeratörler
# and,or,not

ehliyet = False;
araba = True;

if ehliyet and araba:
    print("Araba kullanabilirsin.");
    # değil in kullanımı
elif araba and not ehliyet:
    print("Bizim kursumuz ile ehliyet alabilirsiniz")
elif ehliyet or araba:
    print("Araba kullanmana çok az kaldı.");
else:
    print("Araba kullanmana için çok zaman var.");