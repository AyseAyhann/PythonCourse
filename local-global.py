
x='global x'
#globa scope

def function():
    #local scope
    x='local x'

function()
print(x) #global x

#fonksiyon içinde global keywordü kullanılırsa değişken globalde değişir
# global x