# Koşullu ifadeler
"""
örn:

Eğer hava yağmurlu ise:
    ceketimi giyeceğim
Eğer hava güneşli ise:
    güneş gözlüğümü takacağım
bunların hiçbiri değilse:
    normal bir şekilde dışarı çıkacağım

"""

yagmurlu = True;
gunuseli= True;

if yagmurlu and gunuseli==False:
    print("Ceketini giy")
elif yagmurlu== False and gunuseli :
    print("Gözlüğünü tak")
elif yagmurlu and gunuseli:
    print("Ceketini giy ve Gözlüğünü tak")
else:
    print("Normal bir şekildi dışarı çık")





