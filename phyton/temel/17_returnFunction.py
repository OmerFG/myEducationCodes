def sayHello(isim=" bro"):#eğer isim vermezsen dostum olarak kullanırım ismi demektir bu. yani default ayarlama yapmaktır
    print("hello" + isim)
def sayHello2(isim=" ziyaretçi", soyIsim = " arkadaş"): #defatult değer vermezsen o değerleri atamasını sen yapmalısın.
    print("hello" + isim + soyIsim) #default değerleri her zaman en sona koymalısın yani (isim,soyisim="bilinmiyor")çünkü
    #fonksiyonlarda değerleri atama yaparken sırayla yaparsın.
    return 10.5 #herşeyi yazabilirsin.

sayHello(" ömer")
sayHello(" engin")
sayHello()
print(sayHello2(" engin")) #değerleri sırasıyla verir