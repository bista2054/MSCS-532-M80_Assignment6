"""
Data Structures Implementation
This code implements arrays, matrices, stacks, queues, linked lists, and trees
"""


class MyArray:
    """Custom array implementation with dynamic resizing"""

    def __init__(self, capacity=10):
        # Initializing array with specified capacity
        self.capacity = capacity
        self.size = 0  # Current number of elements
        self.data = [None] * capacity  # Internal storage

    def __getitem__(self, index):
        # Accessing element at index with bounds checking
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        return self.data[index]

    def __setitem__(self, index, value):
        # Setting element at index with bounds checking
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        self.data[index] = value

    def append(self, value):
        # Adding element to the end of array, resize if full
        if self.size == self.capacity:
            self._resize()  # Double capacity when full
        self.data[self.size] = value
        self.size += 1

    def insert(self, index, value):
        # Inserting element at specific position
        if index < 0 or index > self.size:
            raise IndexError("Index out of bounds")

        # Resize if array is full
        if self.size == self.capacity:
            self._resize()

        # Shifting elements to the right to make space
        for i in range(self.size, index, -1):
            self.data[i] = self.data[i - 1]

        # Inserting new element
        self.data[index] = value
        self.size += 1

    def delete(self, index):
        # Removing element at specific position
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")

        # Shifting elements to the left to fill gap
        for i in range(index, self.size - 1):
            self.data[i] = self.data[i + 1]

        self.size -= 1
        return self.data[self.size]  # Return deleted value

    def _resize(self):
        # Doubling the capacity when array is full
        self.capacity *= 2
        new_data = [None] * self.capacity
        # Copying existing elements to new array
        for i in range(self.size):
            new_data[i] = self.data[i]
        self.data = new_data

    def __len__(self):
        # Returning current number of elements
        return self.size

    def __str__(self):
        # String representation of array
        return str([self.data[i] for i in range(self.size)])


class Matrix:
    """Custom matrix implementation with row/column operations"""

    def __init__(self, rows, cols, fill_value=0):
        # Initializing matrix with specified dimensions
        self.rows = rows
        self.cols = cols
        # Creating 2D list filled with initial value
        self.data = [[fill_value for _ in range(cols)] for _ in range(rows)]

    def __getitem__(self, indices):
        # Accessing element at (row, col)
        row, col = indices
        return self.data[row][col]

    def __setitem__(self, indices, value):
        # Setting element at (row, col)
        row, col = indices
        self.data[row][col] = value

    def insert_row(self, row_index, row_data=None):
        # Insertting new row at specified position
        if row_index < 0 or row_index > self.rows:
            raise IndexError("Row index out of bounds")

        # Creating new row with zeros or provided data
        if row_data is None:
            row_data = [0] * self.cols
        elif len(row_data) != self.cols:
            raise ValueError("Row data length must match number of columns")

        # Insertiing row and update dimensions
        self.data.insert(row_index, row_data)
        self.rows += 1

    def delete_row(self, row_index):
        # Removing row at specified position
        if row_index < 0 or row_index >= self.rows:
            raise IndexError("Row index out of bounds")

        del self.data[row_index]
        self.rows -= 1

    def insert_col(self, col_index, col_data=None):
        # Insering new column at specified position
        if col_index < 0 or col_index > self.cols:
            raise IndexError("Column index out of bounds")

        # Creating new column data
        if col_data is None:
            col_data = [0] * self.rows
        elif len(col_data) != self.rows:
            raise ValueError("Column data length must match number of rows")

        # Inserting column in each row
        for i in range(self.rows):
            self.data[i].insert(col_index, col_data[i])
        self.cols += 1

    def delete_col(self, col_index):
        # Removing column at specified position
        if col_index < 0 or col_index >= self.cols:
            raise IndexError("Column index out of bounds")

        # Removing column from each row
        for i in range(self.rows):
            del self.data[i][col_index]
        self.cols -= 1

    def __str__(self):
        # String representation of matrix
        return '\n'.join([' '.join(map(str, row)) for row in self.data])


class Stack:
    """Array-based stack implementation (LIFO)"""

    def __init__(self, capacity=10):
        # Initializing stack with specified capacity
        self.capacity = capacity
        self.size = 0  # Current number of elements
        self.data = [None] * capacity  # Internal storage

    def push(self, item):
        # Adding element to top of stack
        if self.is_full():
            self._resize()  # Resize if stack is full
        self.data[self.size] = item
        self.size += 1

    def pop(self):
        # Removing and return top element
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        self.size -= 1
        return self.data[self.size]  # Return top element

    def peek(self):
        # Returning top element without removing it
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self.data[self.size - 1]

    def is_empty(self):
        # Checking if stack is empty
        return self.size == 0

    def is_full(self):
        # Checking if stack is full
        return self.size == self.capacity

    def _resize(self):
        # Doubling capacity when stack is full
        self.capacity *= 2
        new_data = [None] * self.capacity
        # Copying existing elements to new array
        for i in range(self.size):
            new_data[i] = self.data[i]
        self.data = new_data

    def __len__(self):
        # Returning current number of elements
        return self.size

    def __str__(self):
        # String representation of stack
        return f"Stack({[self.data[i] for i in range(self.size)]})"


class Queue:
    """Array-based queue implementation (FIFO) using circular buffer"""

    def __init__(self, capacity=10):
        # Initializing queue with specified capacity
        self.capacity = capacity
        self.size = 0  # Current number of elements
        self.front = 0  # Index of front element
        self.rear = -1  # Index of rear element
        self.data = [None] * capacity  # Internal storage

    def enqueue(self, item):
        # Adding element to rear of queue
        if self.is_full():
            self._resize()  # Resize if queue is full

        # Calculating new rear position using modulo for circular buffer
        self.rear = (self.rear + 1) % self.capacity
        self.data[self.rear] = item
        self.size += 1

    def dequeue(self):
        # Removing and return front element
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")

        item = self.data[self.front]
        # Moving front pointer using modulo for circular buffer
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return item

    def peek(self):
        # Returning front element without removing it
        if self.is_empty():
            raise IndexError("Peek from empty queue")
        return self.data[self.front]

    def is_empty(self):
        # Checking if queue is empty
        return self.size == 0

    def is_full(self):
        # Checking if queue is full
        return self.size == self.capacity

    def _resize(self):
        # Doubling capacity when queue is full
        new_capacity = self.capacity * 2
        new_data = [None] * new_capacity

        # Copyiing elements maintaining order from front to rear
        for i in range(self.size):
            new_data[i] = self.data[(self.front + i) % self.capacity]

        self.data = new_data
        self.capacity = new_capacity
        self.front = 0
        self.rear = self.size - 1

    def __len__(self):
        # Returning current number of elements
        return self.size

    def __str__(self):
        # String representation of queue
        elements = []
        for i in range(self.size):
            elements.append(self.data[(self.front + i) % self.capacity])
        return f"Queue({elements})"


class ListNode:
    """Node for linked list implementation"""

    def __init__(self, value=0, next_node=None):
        self.value = value  # Data stored in node
        self.next = next_node  # Reference to next node

    def __str__(self):
        return str(self.value)


class LinkedList:
    """Singly linked list implementation"""

    def __init__(self):
        self.head = None  # First node in list
        self.size = 0  # Number of nodes in list

    def insert_at_beginning(self, value):
        # Inserting new node at beginning of list
        new_node = ListNode(value)
        new_node.next = self.head  # New node points to current head
        self.head = new_node  # Update head to new node
        self.size += 1

    def insert_at_end(self, value):
        # Insertiing new node at end of list
        new_node = ListNode(value)
        if not self.head:
            # If list is empty, new node becomes head
            self.head = new_node
        else:
            # Traverse to last node and update its next pointer
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1

    def insert_at_position(self, value, position):
        # Inserting new node at specified position
        if position < 0 or position > self.size:
            raise IndexError("Position out of bounds")

        if position == 0:
            self.insert_at_beginning(value)
            return

        new_node = ListNode(value)
        current = self.head
        # Traverse to node before insertion position
        for _ in range(position - 1):
            current = current.next

        # Updating pointers to insert new node
        new_node.next = current.next
        current.next = new_node
        self.size += 1

    def delete_at_beginning(self):
        # Removing and return first node
        if not self.head:
            raise IndexError("Delete from empty list")

        deleted_value = self.head.value
        self.head = self.head.next  # Move head to next node
        self.size -= 1
        return deleted_value

    def delete_at_end(self):
        # Removing and return last node
        if not self.head:
            raise IndexError("Delete from empty list")

        if not self.head.next:
            # Only one node in list
            return self.delete_at_beginning()

        current = self.head
        # Traverse to second last node
        while current.next.next:
            current = current.next

        deleted_value = current.next.value
        current.next = None  # Remove last node
        self.size -= 1
        return deleted_value

    def delete_at_position(self, position):
        # Remove node at specified position
        if position < 0 or position >= self.size:
            raise IndexError("Position out of bounds")

        if position == 0:
            return self.delete_at_beginning()

        current = self.head
        # Traverse to node before deletion position
        for _ in range(position - 1):
            current = current.next

        deleted_value = current.next.value
        # Skip over node to be deleted
        current.next = current.next.next
        self.size -= 1
        return deleted_value

    def search(self, value):
        # Find position of first occurrence of value
        current = self.head
        position = 0
        while current:
            if current.value == value:
                return position
            current = current.next
            position += 1
        return -1  # Value not found

    def traverse(self):
        # Return list of all values in order
        elements = []
        current = self.head
        while current:
            elements.append(current.value)
            current = current.next
        return elements

    def __len__(self):
        # Return number of nodes in list
        return self.size

    def __str__(self):
        # String representation of linked list
        return " -> ".join(map(str, self.traverse())) + " -> None"


class TreeNode:
    """Node for tree implementation using linked lists for children"""

    def __init__(self, value=0):
        self.value = value
        self.children = []  # List of child nodes
        self.parent = None  # Reference to parent node

    def add_child(self, child_node):
        # Add child node and set parent reference
        child_node.parent = self
        self.children.append(child_node)

    def remove_child(self, child_node):
        # Remove child node and clear parent reference
        if child_node in self.children:
            self.children.remove(child_node)
            child_node.parent = None

    def get_level(self):
        # Calculate depth level of node (root is level 0)
        level = 0
        current = self.parent
        while current:
            level += 1
            current = current.parent
        return level

    def __str__(self):
        return str(self.value)


class RootedTree:
    """Tree implementation using linked lists for node relationships"""

    def __init__(self, root_value=0):
        self.root = TreeNode(root_value)

    def insert(self, parent_value, value):
        # Insert new node as child of specified parent
        parent_node = self._find_node(self.root, parent_value)
        if parent_node:
            new_node = TreeNode(value)
            parent_node.add_child(new_node)
            return True
        return False  # Parent not found

    def delete(self, value):
        # Remove node with specified value (cannot delete root)
        node_to_delete = self._find_node(self.root, value)
        if node_to_delete and node_to_delete != self.root:
            node_to_delete.parent.remove_child(node_to_delete)
            return True
        return False  # Node not found or is root

    def _find_node(self, current_node, value):
        # Recursively find node with specified value
        if current_node.value == value:
            return current_node

        # Search in children
        for child in current_node.children:
            found = self._find_node(child, value)
            if found:
                return found
        return None  # Node not found

    def traverse_preorder(self, node=None):
        # Depth-first traversal: root, then children
        if node is None:
            node = self.root

        result = [node.value]  # Visit root first
        for child in node.children:
            result.extend(self.traverse_preorder(child))  # Then children
        return result

    def traverse_postorder(self, node=None):
        # Depth-first traversal: children, then root
        if node is None:
            node = self.root

        result = []
        for child in node.children:
            result.extend(self.traverse_postorder(child))  # Children first
        result.append(node.value)  # Then root
        return result

    def get_height(self, node=None):
        # Calculate height of tree (longest path from root to leaf)
        if node is None:
            node = self.root

        if not node.children:
            return 0  # Leaf node has height 0

        # Height is 1 + max height of children
        return 1 + max(self.get_height(child) for child in node.children)

    def print_tree(self):
        # Print tree structure with indentation
        self._print_node(self.root)

    def _print_node(self, node, level=0):
        # Recursively print node and its children with proper indentation
        prefix = "  " * level + "|-- " if level > 0 else ""
        print(prefix + str(node.value))
        for child in node.children:
            self._print_node(child, level + 1)


def demonstrate_data_structures():
    """Demonstrating all implemented data structures with examples"""

    print("=== Arrays and Matrices ===")
    # Array demonstration
    arr = MyArray()
    for i in range(5):
        arr.append(i * 10)
    print(f"Array: {arr}")
    arr.insert(2, 25)
    print(f"After insertion: {arr}")
    arr.delete(3)
    print(f"After deletion: {arr}")

    # Matrix demonstration
    mat = Matrix(2, 3)
    mat[0, 0] = 1
    mat[0, 1] = 2
    mat[0, 2] = 3
    mat[1, 0] = 4
    mat[1, 1] = 5
    mat[1, 2] = 6
    print("\nMatrix:")
    print(mat)

    print("\n=== Stacks and Queues ===")
    # Stack demonstration
    stack = Stack()
    for i in range(5):
        stack.push(i)
    print(f"Stack: {stack}")
    print(f"Popped: {stack.pop()}")
    print(f"Stack after pop: {stack}")

    # Queue demonstration
    queue = Queue()
    for i in range(5):
        queue.enqueue(i)
    print(f"Queue: {queue}")
    print(f"Dequeued: {queue.dequeue()}")
    print(f"Queue after dequeue: {queue}")

    print("\n=== Linked Lists ===")
    # Linked list demonstration
    ll = LinkedList()
    ll.insert_at_end(10)
    ll.insert_at_end(20)
    ll.insert_at_beginning(5)
    ll.insert_at_position(15, 2)
    print(f"Linked List: {ll}")
    print(f"Search 15: Position {ll.search(15)}")
    ll.delete_at_position(1)
    print(f"After deletion: {ll}")

    print("\n=== Rooted Trees ===")
    # Tree demonstration
    tree = RootedTree(1)
    tree.insert(1, 2)
    tree.insert(1, 3)
    tree.insert(2, 4)
    tree.insert(2, 5)
    tree.insert(3, 6)
    print("Tree structure:")
    tree.print_tree()
    print(f"Preorder: {tree.traverse_preorder()}")
    print(f"Postorder: {tree.traverse_postorder()}")
    print(f"Tree height: {tree.get_height()}")


if __name__ == "__main__":
    demonstrate_data_structures()