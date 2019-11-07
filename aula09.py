#a = str(input("Digite"))

a = "Curso em Video Python"

print("""
Teste
Casa
Cavalo
Pedro
"""
)

print(a[9:21:2])
print(a[:5])
print(a[15:])
print(a[9::3])
print(len(a))
print(a.count('o'))
print(a.count('o',0,13))
print(a.find('deo'))
print(a.find('Android')) # -1
print('Curso' in a)
print(a.replace('Python', 'Android'))
print(a.upper())
print(a.lower())
print(a.capitalize())
print(a.title())
print(a.strip()) # versao trim do python
print(a.rstrip())
print(a.lstrip())
print(a.split())
print('-'.join(a.split()))


