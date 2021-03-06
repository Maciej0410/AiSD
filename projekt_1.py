from typing import Any


class Node :
    def __init__(self, value: Any) :
        self.value = value
        self.nastepny = None


class LinkedList :
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, value: Any)->None:
        if self.head == None:
            wezel = Node(value)
            self.head = wezel
            self.tail = wezel
        else:
            wezel = Node(value)
            wezel.nastepny = self.head
            self.head = wezel

    def append(self, value: Any) -> None:
        if self.head != None:
            wezel = self.tail
            wezel.nastepny = Node(value)
            self.tail = wezel.nastepny
        else :
            self.push(value)

    def pop(self) -> Any:
        wezel = self.head
        wezel_2 = wezel.nastepny
        self.head = wezel_2
        return wezel.value

    def node(self, at: int) -> Node:
        wezel = self.head
        if (wezel == None) :
            return None
        else:
            for i in range(at - 1):
                wezel = wezel.nastepny
            return wezel

    def __len__(self) ->int:
        wezel = self.head
        wynik = 1
        if wezel == None :
            return wynik == 0
        while (wezel.nastepny != None) :
            wezel = wezel.nastepny
            wynik += 1
        return wynik

    def __str__(self)->str:
        wezel = self.head
        tekst = "["
        while wezel != None:
            tekst += str(wezel.value)
            if wezel.nastepny != None :
                tekst += " -> "
            wezel = wezel.nastepny
        tekst += "]"
        return print(tekst)

    def remove_last(self) ->Any:
        wezel = self.head
        wezel_2 = self.head
        if self.head.nastepny == None:
            do_usuniecia = self.head
            self.head = None
            return do_usuniecia.value
        while (wezel.nastepny != None):
            wezel = wezel.nastepny
        while (wezel_2.nastepny != wezel) :
            wezel_2 = wezel_2.nastepny
        do_usuniecia = wezel
        wezel_2.nastepny = None
        return do_usuniecia.value

    def remove(self, after: Node) -> Any:
        wezel_2: Node=after
        while wezel_2 !=after.nastepny:
            wezel = after.nastepny
            wezel_2 = wezel.nastepny
            after.nastepny = wezel_2
        return wezel.value

    def insert(self, value: Any, after: Node)->None:
        if after == self.tail:
            self.append(value)
        wezel = Node(value)
        wezel.nastepny = after.nastepny
        after.nastepny = wezel

list_ = LinkedList()

print("Moja lista: ")
list_.push('Maciek')
list_.append('Warych')
list_.push(10)
list_.append(2000)
list_.append(162606)
list_.append('Projekt')
list_.push('4')
list_.__str__()
dlugosc_1 = list_.__len__()
print("Dlugosc listy -> len =", dlugosc_1)
print("\n")
print("Usuni??cie pierwszego elementu:\n")
list_.__str__()
usuniety = list_.pop()
print("Usuniety element -> ", usuniety)
print("Dlugosc listy -> len = ", list_.__len__())
list_.__str__()
print("\n")
print("Zwrocenie 1 oraz 3 elementu listy:\n")
list_.__str__()
pierwszy = list_.node(1).value
trzeci = list_.node(3).value
print("Pierwszy -> ", pierwszy)
print("Trzeci -> ", trzeci)
print("\n")
print("Usuniecie ostatniego elementu:\n")
list_.__str__()
ostatni = list_.remove_last()
list_.__str__()
print("Ostatni element -> ", ostatni)
print("Dlugosc listy -> len = ", list_.__len__())
print("\n")
print("Usuni??cie drugiego elementu:\n")
list_.__str__()
drugi = list_.node(1)
drugi_out = list_.remove(drugi)
list_.__str__()
print("Usuniety element -> ", drugi_out)
print("Dlugosc listy -> len = ", list_.__len__())
print("\n")
print("Usuni??cie trzeciego elementu aktualnej listy:\n")
list_.__str__()
trzeci = list_.node(2)
trzeci_out = list_.remove(trzeci)
list_.__str__()
print("Usuniety element -> ", trzeci_out)
print("Dlugosc listy -> len = ", list_.__len__())
print("\n")
print("Dodanie elementu za pierwszy element listy:\n")
list_.__str__()
wartosc='Maciek'
wezel=list_.node(1)
list_.insert(wartosc, wezel)
list_.__str__()
print("Dodany element -> ",wartosc)
print("Dlugosc listy -> len = ", list_.__len__())


# class Stack():
#
#     def __init__(self):
#         self._storage = LinkedList()
#
#     def push(self, element: Any)->None:
#         self._storage.push(element)
#
#     def __len__(self)->int:
#         return self._storage.__len__()
#
#     def __str__(self)->str:
#         tekst = ""
#         for i in range(self._storage.__len__()):
#             tekst += " " + str(self._storage.node(i+1).value) + "\n"
#         return print(tekst)
#     def pop(self)->Any:
#         return self._storage.pop()
#
#
#
# stack = Stack()
#
# print("Moj stos:\n")
# stack.push('Maciek')
# stack.push('10.04.2000')
# stack.push('Warych')
# stack.push('162606')
# stack.push(3)
# stack.__str__()
# print("Dlugosc stosu -> len = ",stack.__len__())
# stack.pop()
# print("Usuniecie elementu z gory:\n")
# stack.__str__()
# print("Dlugosc stosu -> len = ",stack.__len__())
# stack.pop()
# print("Usuniecie drugiego elementu z gory:\n")
# stack.__str__()
# print("Dlugosc stosu -> len = ",stack.__len__())



# class Queue():
#
#     def __init__(self):
#         self._storage=LinkedList()
#
#     def __len__(self)->int:
#         return self._storage.__len__()
#
#     def peek(self)->Any:
#         dlugosc=self._storage.__len__()
#         if dlugosc != 0:
#             return self._storage.tail.value
#         else:
#             print("Kolejka jest pusta")
#
#     def enqueue(self, element: Any)->None:
#         self._storage.push(element)
#
#     def __str__(self)->str:
#         tekst = ""
#         for i in range(self._storage.__len__()):
#             tmp=str(self._storage.node(i+1).value) + " | "
#             tekst += tmp
#         return print(tekst)
#
#     def dequeue(self)->Any:
#         if self._storage.__len__()!= 0:
#             return self._storage.remove_last()
#
#
# queue = Queue()
#
# print("Moja kolejka:\n")
# queue.enqueue('klient_1')
# queue.enqueue('klient_2')
# queue.enqueue('klient_3')
# queue.enqueue('klient_4')
# queue.enqueue('klient_5')
# queue.enqueue('klient_6')
# queue.__str__()
# print("Dlugosc kolejki -> liczba klient??w = ", queue.__len__())
# print("\n")
# print("Obsluzenie pierwszego elementu w kolejece:\n")
# queue.__str__()
# obsluzony_element=queue.dequeue()
# queue.__str__()
# print("Dlugosc kolejki -> liczba klient??w = ", queue.__len__())
# print("Obsluzony element -> ",obsluzony_element)
# print("Obsluzenie drugiego elementu w kolejece:\n")
# obsluzony_element_2=queue.dequeue()
# queue.__str__()
# print("Dlugosc kolejki -> liczba klient??w = ", queue.__len__())
# print("Obsluzony element -> ",obsluzony_element_2)
