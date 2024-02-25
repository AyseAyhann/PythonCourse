#Dictionary
students={}

number=input("student number: ")
name=input("student name: ")
surname=input("student surname: ")
phone=input("student phone: ")

students[number]={
    'name':name,
    'surname':surname,
    'phone': phone,
}

#update ile de eklenebilir, birden fazla veri aynı anda eklenebilir
students.update({
    number: {
        'ad':name,
        'soyad':surname,
        'tel':phone,
    }
})

number=input("student number: ")
name=input("student name: ")
surname=input("student surname: ")
phone=input("student phone: ")

students.update({
    number: {
        'ad':name,
        'soyad':surname,
        'tel':phone,
    }
})


print(students)
print('*'*50)
#girilen numaraya sahip öğrencinin bilgilerini yazdırır
stdNumber: input('student no: ')
student=students[number]
print(f"The Student with the number {stdNumber} you have searched: ",student)
