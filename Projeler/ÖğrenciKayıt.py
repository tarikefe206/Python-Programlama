student = {
    'ad': 'Ayşe',
    'soyad' : 'Kaya',
    'numara' : 20240101,
    'bölüm': 'Bilgisayar Programcılığı',
    'ortalama' : 3.52
}
student.update({'sınıf' : 2})
print (f"{student('ad')} {student('soyad')} - {student('numara')}")
print(student.get("sınıf"))
print(student.keys())
print(student.values())