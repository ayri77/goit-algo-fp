"""
Базовий клас однозв'язного списку.

Містить реалізацію вузла (Node) та класу LinkedList з основними операціями.
"""


class Node:
    """
    Вузол однозв'язного списку.
    
    Attributes:
        data: Дані, що зберігаються у вузлі
        next: Посилання на наступний вузол
    """
    
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """
    Однозв'язний список.
    
    Містить базові операції для роботи зі списком:
    - append: додавання елемента в кінець
    - prepend: додавання елемента на початок
    - reverse: in-place реверсування списку
    - reversed: повертає новий реверсований список
    - sort: in-place сортування списку
    - sorted: повертає новий відсортований список
    - merge: статичний метод для об'єднання двох відсортованих списків
    - merge_with: об'єднання поточного списку з іншим
    - __str__: рядкове представлення списку
    - __iter__: ітерація по елементах списку
    - __len__: довжина списку
    
    Attributes:
        head: Посилання на перший вузол списку
        tail: Посилання на останній вузол списку (для оптимізації append)
    """
    
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        return " -> ".join(str(node.data) for node in self)
    
    def __iter__(self):
        current = self.head
        while current is not None:
            yield current
            current = current.next

    def __len__(self):
        return len(list(iter(self)))

    def append(self, data):
        """Додає елемент в кінець списку."""        
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
    
    def prepend(self, data):
        """Додає елемент на початок списку."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
    
    def reverse(self):
        """
        Реверсує список in-place, змінюючи посилання між вузлами.
        
        Returns:
            self для підтримки method chaining
        """
        prev = None
        current = self.head
        # Оновлюємо tail на початку (стане head після реверсування)
        old_tail = self.tail
        self.tail = self.head
        
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        self.head = prev
        return self
    
    def reversed(self):
        """
        Повертає новий реверсований список, не змінюючи поточний.
        
        Returns:
            Новий LinkedList з реверсованими елементами
        """
        new_list = LinkedList()
        for node in self:
            new_list.prepend(node.data)
        return new_list
    
    def sort(self):
        """
        Сортує список in-place за допомогою сортування злиттям.
        
        Returns:
            self для підтримки method chaining
        """
        if self.head is None or self.head.next is None:
            return self
        
        def _split_list(head):
            """Розділяє список на дві частини."""
            if head is None or head.next is None:
                return head, None
            slow = head
            fast = head.next
            while fast is not None and fast.next is not None:
                slow = slow.next
                fast = fast.next.next
            right = slow.next
            slow.next = None
            return head, right
        
        def _merge_lists(left, right):
            """Зливає дві відсортовані частини списку."""
            if left is None:
                return right
            if right is None:
                return left
            if left.data <= right.data:
                left.next = _merge_lists(left.next, right)
                return left
            else:
                right.next = _merge_lists(left, right.next)
                return right
        
        def _sort_list(head):
            """Сортує список рекурсивно."""
            if head is None or head.next is None:
                return head
            left, right = _split_list(head)
            left = _sort_list(left)
            right = _sort_list(right)
            return _merge_lists(left, right)
        
        self.head = _sort_list(self.head)
        # Оновлюємо tail після сортування
        if self.head is not None:
            current = self.head
            while current.next is not None:
                current = current.next
            self.tail = current
        
        return self
    
    def sorted(self):
        """
        Повертає новий відсортований список, не змінюючи поточний.
        
        Returns:
            Новий відсортований LinkedList
        """
        new_list = LinkedList()
        for node in self:
            new_list.append(node.data)
        new_list.sort()
        return new_list
    
    def merge_with(self, other):
        """
        Об'єднує поточний список з іншим відсортованим списком.
        
        Args:
            other: Інший відсортований LinkedList
            
        Returns:
            Новий відсортований LinkedList з елементами обох списків
        """
        return LinkedList.merge(self, other)
    
    @staticmethod
    def merge(list1, list2):
        """
        Об'єднує два відсортовані однозв'язні списки в один відсортований список.
        
        Args:
            list1: Перший відсортований однозв'язний список
            list2: Другий відсортований однозв'язний список
            
        Returns:
            Новий відсортований однозв'язний список, що містить елементи обох списків
            
        Примітка:
            Функція працює за час O(n + m), де n і m - довжини списків.
            Не потрібно викликати сортування після об'єднання.
        """
        new_list = LinkedList()
        current1 = list1.head
        current2 = list2.head
        
        while current1 is not None and current2 is not None:
            if current1.data <= current2.data:
                new_list.append(current1.data)
                current1 = current1.next
            else:
                new_list.append(current2.data)
                current2 = current2.next
        
        # Додаємо залишкові елементи з першого списку
        while current1 is not None:
            new_list.append(current1.data)
            current1 = current1.next
        
        # Додаємо залишкові елементи з другого списку
        while current2 is not None:
            new_list.append(current2.data)
            current2 = current2.next
        
        return new_list


