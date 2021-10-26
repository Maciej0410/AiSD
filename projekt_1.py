from typing import Any


class Node :
    def __init__(self, value: Any) :
        self.value = value
        self.nastepny = None


class LinkedList :
    def __init__(self) :
        self.head = None
        self.tail = None

    def push(self, value: Any)->None :
        if self.head == None :
            wezel = Node(value)
            self.head = wezel
            self.tail = wezel
        else :
            wezel = Node(value)
            wezel.nastepny = self.head
            self.head = wezel

    def append(self, value: Any) -> None :
        if self.head != None :
            wezel = self.tail
            wezel.nastepny = Node(value)
            self.tail = wezel.nastepny
        else :
            self.push(value)

    def pop(self) -> Any:
        licznik = self.head
        nastepnik = licznik.nastepny
        self.head = nastepnik
        return licznik.value

    def node(self, at: int) -> Node:
        licznik = self.head
        if (licznik == None) :
            return None
        else :
            for i in range(at - 1) :
                licznik = licznik.nastepny
            return licznik

    def __len__(self) ->int:
        wezel = self.head
        wynik = 1
        if wezel == None :
            return wynik == None
        while (wezel.nastepny != None) :
            wezel = wezel.nastepny
            wynik += 1
        return wynik

    def __str__(self)->str:
        wezel = self.head
        tekst = "["
        while wezel != None :
            tekst += str(wezel.value)
            if wezel.nastepny != None :
                tekst += " -> "
            wezel = wezel.nastepny
        tekst += "]"
        return tekst

    def remove_last(self) ->Any:
        wezel = self.head
        wezel_2 = self.head
        if self.head.nastepny == None :
            licznik = self.head
            self.head = None
            return licznik
        while (wezel.nastepny != None) :
            wezel = wezel.nastepny
        while (wezel_2.nastepny != wezel) :
            wezel_2 = wezel_2.nastepny
        licznik = wezel
        wezel_2.nastepny = None
        return licznik.value

    def remove(self, after: Node) -> Node:
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

# list_ = LinkedList()
#
# print("Moja lista: ")
# list_.push('Maciek')
# list_.append('Warych')
# list_.push(10)
# list_.append(2000)
# list_.append(162606)
# list_.append('Projekt')
# list_.push('4')
# print(list_.__str__())
# dlugosc_1 = list_.__len__()
# print("Dlugosc listy -> len =", dlugosc_1)
# print("\n")
# print("Usunięcie pierwszego elementu:\n")
# usuniety = list_.pop()
# print("Usuniety element -> ", usuniety)
# print("Dlugosc listy -> len = ", list_.__len__())
# print(list_.__str__())
# print("\n")
# print("Zwrocenie 1 oraz 3 elementu listy:\n")
# pierwszy = list_.node(1).value
# trzeci = list_.node(3).value
# print("Pierwszy -> ", pierwszy)
# print("Trzeci -> ", trzeci)
# print("\n")
#
# print("Usuniecie ostatniego elementu:\n")
# ostatni = list_.remove_last()
# print(list_.__str__())
# print("Ostatni element -> ", ostatni)
# print("Dlugosc listy -> len = ", list_.__len__())
# print("\n")
# print("Usunięcie drugiego elementu:\n")
# drugi = list_.node(1)
# drugi_out = list_.remove(drugi)
# print(list_.__str__())
# print("Usuniety element -> ", drugi_out)
# print("Dlugosc listy -> len = ", list_.__len__())
# print("\n")
# print("Usunięcie trzeciego elementu aktualnej listy:\n")
# trzeci = list_.node(2)
# trzeci_out = list_.remove(trzeci)
# print(list_.__str__())
# print("Usuniety element -> ", trzeci_out)
# print("Dlugosc listy -> len = ", list_.__len__())
# print("\n")
# print("Dodanie elementu za pierwszy element listy:\n")
# wartosc='Maciek'
# wezel=list_.node(1)
# list_.insert(wartosc, wezel)
# print(list_.__str__())
# print("Dodany element -> ",wartosc)
# print("Dlugosc listy -> len = ", list_.__len__())


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
#         return tekst
#     def pop(self)->Any:
#         return self._storage.pop()
#
#
#
# stack = Stack()
# print("Moj stos:\n")
# stack.push('Maciek')
# stack.push('10.04.2000')
# stack.push('Warych')
# stack.push(100)
# stack.push(66)
# print(stack.__str__())
# stack.pop()
# print("Usuniecie elementu z gory:\n")
# print(stack.__str__())
# stack.pop()
# print("Usuniecie drugiego elementu z gory:\n")
# print(stack.__str__())



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
#             tekst += str(self._storage.node(i+1).value) + " | "
#         return tekst
#
#     def dequeue(self)->Any:
#         if self._storage.__len__()!= 0:
#             wartosc=self._storage.remove_last()
#             return wartosc

# queue = Queue()
#
#
# queue.enqueue('klient_1')
# queue.enqueue('klient_2')
# queue.enqueue('klient_3')
# queue.enqueue('klient_4')
# queue.enqueue('klient_5')
# queue.enqueue('klient_6')
# print(queue.__str__())
# print("Dlugosc kolejki -> liczba klientów = ", queue.__len__())
# print("\n")
# print("Obsluzenie pierwszego elementu w kolejece:\n")
# obsluzony_element=queue.dequeue()
# print(queue.__str__())
# print("Dlugosc kolejki -> liczba klientów = ", queue.__len__())
# print("Obsluzony element -> ",obsluzony_element)

