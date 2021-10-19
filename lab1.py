# imie= 'M'
# nazwisko= 'Warych'
#
# def lacze(imie, nazwisko):
#
#     kropka='.'
#
#     return imie+kropka+nazwisko
#
# print(lacze(imie, nazwisko))

# zadanie2

# imie='Maciej'
# nazwisko='Warych'
#
# def lacze (imie, nazwisko):
#
#     kropka='.'
#     litera=imie[0]
#
#     return litera+kropka+nazwisko
#
# print(lacze(imie,nazwisko))

#zadanie3

# a='20'
# b='21'
# wiek=21
#
# def rok_urodzenia(a,b,wiek)->int:
#
#     c=a+b
#     c=int(c)
#
#     wynik=c-wiek
#     return wynik

# print(rok_urodzenia(a,b,wiek))
#zadanie 4


# def lacze (imie, nazwisko)->str:
#
#     kropka='.'
#     litera=imie[0]
#
#     return litera+kropka+nazwisko
#
# def function3(imie,nazw,fun)->str:
#
#     napis=fun(imie,nazw)
#     return napis
#
#
# imie='Jan'
# nazwisko='Kowalski'
#
# print(function3(imie,nazwisko,lacze))

#zadanie5

# a=input("Podaj liczbe a: ")
# a=float(a)
#
# b=input("Podaj liczbe b: ")
# b=float(b)
#
# def dzielenie(a,b):
#     if(a>=0 and b>0):
#         return a/b
#
# print(dzielenie(a,b))

#zadanie6

# wynik=0
#
# while True:
#     a=input("Podaj liczbe : ")
#     a=int(a)
#     wynik+=a
#     if(wynik==100):
#         break

#zadanie7

# lista=['Poniedziałek','wtorek','10 kwietnia', 'maciek']
# lista2=[1,2,3,4,5,6,19,10]
#
# def krotka(lista):
#     krotka=tuple()
#     type(lista)
#     krotka=tuple(lista)
#     return krotka
#
# print(lista)
# print(lista2)
# print(krotka(lista))
# print(krotka(lista2))

#zadanie 8
# def krotka(lista):
#     krotka=tuple()
#     type(lista)
#     krotka=tuple(lista)
#     return krotka
#
#
# lista=[]
#
# while True:
#     liczba=input("Podaj liczbe: ")
#     liczba=int(liczba)
#     lista.append(liczba)
#     if len(lista)==10:
#             break
#
# print(lista)
# print(krotka(lista))


#zadanie9

# def dzien(a)->str:
#     a=str(a)
#     dni_tygodnia={'1':'poniedziałek', '2':'wtorek', '3':'środa','4':'czwartek', '5':'piątek','6':'sobota', '7': 'niedziela'}
#     return dni_tygodnia[a]
#
# ktory_dzien=input("Podaj ktory dzien: ")
# ktory_dzien=int(ktory_dzien)
#
# print((dzien(ktory_dzien)))

#zadanie10

# def zamiana_lista(tekst):
#     lista = []
#     dlugosc = len(tekst)
#
#     for i in range(0, dlugosc,1):
#         lista.append(tekst[i])
#     return lista
#
# def odwroc_lista(tekst):
#     lista = []
#     lista2 = []
#     lista = zamiana_lista(wyraz)
#     i = len(lista)
#     for i in range(len(lista) - 1, -1, -1):
#         lista2.append(lista[i])
#     return lista2
#
#
# def cz_palindrom(tekst)->bool:
#     lista=zamiana_lista(tekst)
#     lista2=odwroc_lista(lista)
#
#     for j in range(0,len(lista),1):
#         if lista[j]==lista2[j]:
#             return True
#         else:
#             return False
#
# wyraz=input("Podaj wyraz wprowadzajac male litery: ")
#
# if cz_palindrom(wyraz):
#     print("Wyraz jest palindromem")
# else:
#     print("Wyraz nie jest palindromem")









