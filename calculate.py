#soru1

#Bir hesap makinesi kodladığımızı varsayalım, kullanıcı ilk olarak sırayla 2 adet sayı girecek ve bu sayılar arasında yapmak istediği dört işlemi seçecek.
# Seçerken verdiği değerler dört işlemden birisi değil ise kullanıcı uyarılacak ( + - * / ). 
#Girilen işleme göre bu iki sayı arasında ilgili işlem yapılarak kullanıcıya sonuç gösterilecek. 

sayi1=float(input("Sayı 1'i giriniz"))
sayi2=float(input("Sayı 2'yi giriniz"))
operator=input("Yapılacak islemi seciniz")

if operator=="+":
   print(sayi1+sayi2)
elif operator=="-":
   print(sayi1-sayi2)
elif operator=="*":
   print(sayi1*sayi2)
elif operator=="/":
   print(sayi1/sayi2)

else :
   print("Gecerli bir islem seciniz")
