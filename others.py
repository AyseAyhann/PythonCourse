# # is-in

# #identify op: is

# x=y=[1,2,3]
# z=[1,2,3]

# print(x==y) #value ları kıyaslar
# print(x==z)
# print(x is y) #referansları-adresleri kıyaslar-true
# print(x is z) #false

# x=[1,2,3]
# y=[2,4]

# del x[2]  #2. indexi siler
# y[1]=1    
# y.reverse()
# print(x is y) #false
# print(x is not y) #true
# print(x==y)   #true


# #membership op: in
x=['apple','banana']
print('banana' in x)

name='Aysh'
print('a' in name)
print('a' not in name)