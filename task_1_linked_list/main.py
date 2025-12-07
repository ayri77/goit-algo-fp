"""
Головний файл для демонстрації та тестування завдання 1.

Містить приклади використання методів класу LinkedList для реверсування, 
сортування та об'єднання списків.
"""

from linked_list import LinkedList


def main():
    """Демонстрація роботи з однозв'язним списком."""
    print("=" * 60)
    print("Демонстрація роботи з однозв'язним списком")
    print("=" * 60)
    
    # 1. Демонстрація реверсування (in-place)
    print("\n1. Реверсування списку (in-place метод reverse()):")
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    print(f"   Початковий список: {ll}")
    ll.reverse()
    print(f"   Після reverse():   {ll}")
    
    # 2. Демонстрація reversed() (створює новий список)
    print("\n2. Реверсування зі створенням нового списку (метод reversed()):")
    ll2 = LinkedList()
    ll2.append(10)
    ll2.append(20)
    ll2.append(30)
    print(f"   Початковий список: {ll2}")
    reversed_ll = ll2.reversed()
    print(f"   Новий реверсований: {reversed_ll}")
    print(f"   Оригінал не змінений: {ll2}")
    
    # 3. Демонстрація сортування (in-place)
    print("\n3. Сортування списку (in-place метод sort()):")
    ll3 = LinkedList()
    ll3.append(5)
    ll3.append(2)
    ll3.append(8)
    ll3.append(1)
    ll3.append(9)
    print(f"   Початковий список: {ll3}")
    ll3.sort()
    print(f"   Після sort():      {ll3}")
    
    # 4. Демонстрація sorted() (створює новий список)
    print("\n4. Сортування зі створенням нового списку (метод sorted()):")
    ll4 = LinkedList()
    ll4.append(7)
    ll4.append(3)
    ll4.append(6)
    ll4.append(1)
    print(f"   Початковий список: {ll4}")
    sorted_ll = ll4.sorted()
    print(f"   Новий відсортований: {sorted_ll}")
    print(f"   Оригінал не змінений: {ll4}")
    
    # 5. Демонстрація об'єднання списків (статичний метод)
    print("\n5. Об'єднання двох відсортованих списків (статичний метод merge()):")
    list1 = LinkedList()
    list1.append(1)
    list1.append(3)
    list1.append(5)
    
    list2 = LinkedList()
    list2.append(2)
    list2.append(4)
    list2.append(6)
    
    print(f"   Перший список:  {list1}")
    print(f"   Другий список:   {list2}")
    merged = LinkedList.merge(list1, list2)
    print(f"   Об'єднаний:      {merged}")
    
    # 6. Демонстрація merge_with() (метод екземпляра)
    print("\n6. Об'єднання списків (метод екземпляра merge_with()):")
    list3 = LinkedList()
    list3.append(10)
    list3.append(30)
    
    list4 = LinkedList()
    list4.append(20)
    list4.append(40)
    
    print(f"   Перший список:  {list3}")
    print(f"   Другий список:   {list4}")
    merged2 = list3.merge_with(list4)
    print(f"   Об'єднаний:      {merged2}")
    
    print("\n" + "=" * 60)


if __name__ == "__main__":
    main()

