#2.soru
#kullanıcıdan vize ve final notları alacak.
#vize %40  final %60 etkili olacak
#vize ve final notları 50.5 gibi ondalıklı sayılar olabilir
#uygulama ortalamayı hesaplayacak ve ortalamaya göre
#0-49 FF
#50-59 DD
#60-69 CC
#70-79 BB
#80-100 AA
#not ortalamasını ve not harfini kullanıcıya gösterecek programı kodlayınız.

vize = float(input("Vize notunuzu giriniz: "))
final = float(input("Final notunuzu giriniz: "))
ortalama = (vize * 0.4) + (final * 0.6) 

if ortalama>=0 and ortalama<=49:
   print("FF")
elif ortalama>=50 and ortalama<=59:
   print("DD")
elif ortalama>=60 and ortalama<=69:
    print("CC")
elif ortalama>=70 and ortalama<=79:
   print("BB")
else :
 print("AA")
