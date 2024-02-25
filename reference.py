# value type

x=5
y=25

x=y
y=10
print(x,y)

# reference types=>list
a=['apple','banana']
b=['mango','cherry']

a=b  
# listede ikisi de aynı adresi taşıdığından iki obje de otomatik değişir
# value type aksine, adresler eşitlenir, adresi tutulur
#adres kopyalandığında tüm verilerin değerine ulaşmak yerine kopyalanan adres üzerinden tüm verilere erişim sağlanır
b[0]='grape'
print(a,b)