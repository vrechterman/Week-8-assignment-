class Patient:
    def __init__(self, name, urgency):
        """Stores a patient's name and urgency level (1 = most urgent)."""
        self.name = name
        self.urgency = urgency

    def __repr__(self):
        return f"{self.name} ({self.urgency})"


class MinHeap:
    def __init__(self):
        """Initializes an empty heap."""
        self.data = []

   
    def _heapify_up(self, index):
        """Restores heap property after insertion."""
        parent_index = (index - 1) // 2
        if index <= 0:
            return

        if self.data[index].urgency < self.data[parent_index].urgency:
            self.data[index], self.data[parent_index] = self.data[parent_index], self.data[index]
            self._heapify_up(parent_index)

    def _heapify_down(self, index):
        """Restores heap property after removal."""
        left = 2 * index + 1
        right = 2 * index + 2
        smallest = index

        if left < len(self.data) and self.data[left].urgency < self.data[smallest].urgency:
            smallest = left
        if right < len(self.data) and self.data[right].urgency < self.data[smallest].urgency:
            smallest = right

        if smallest != index:
            self.data[index], self.data[smallest] = self.data[smallest], self.data[index]
            self._heapify_down(smallest)

    def insert(self, patient):
        """Adds a patient to the heap and reorders it."""
        if not isinstance(patient, Patient):
            print("Error: Only Patient objects can be inserted.")
            return

        self.data.append(patient)
        self._heapify_up(len(self.data) - 1)

    def print_heap(self):
        """Prints the heap in readable format."""
        print("Current Queue:")
        for p in self.data:
            print(f"- {p.name} ({p.urgency})")
        print()

    def peek(self):
        """Returns the most urgent patient without removing them."""
        if not self.data:
            print("Queue is empty.")
            return None
        return self.data[0]

    def remove_min(self):
        """Removes and returns the most urgent patient."""
        if not self.data:
            print("Queue is empty. No patients to remove.")
            return None

        if len(self.data) == 1:
            return self.data.pop()

        min_patient = self.data[0]
        self.data[0] = self.data.pop()  
        self._heapify_down(0)
        return min_patient



if __name__ == "__main__":
    heap = MinHeap()
    heap.insert(Patient("Jordan", 3))
    heap.insert(Patient("Taylor", 1))
    heap.insert(Patient("Avery", 5))

    heap.print_heap()

    next_up = heap.peek()
    print(f"Next up: {next_up.name}, Urgency: {next_up.urgency}")

    served = heap.remove_min()
    print(f"Served: {served.name}")
    heap.print_heap()

  
    heap.remove_min()
    heap.remove_min()
    heap.remove_min()  
    heap.insert("Not a Patient")  

# Test your MinHeap class here including edge cases
Current Queue:
- Taylor (1)
- Jordan (3)
- Avery (5)

Next up: Taylor, Urgency: 1
Served: Taylor
Current Queue:
- Jordan (3)
- Avery (5)

Queue is empty. No patients to remove.
Queue is empty. No patients to remove.
Error: Only Patient objects can be inserted.

''' memo 
For this assignment the tree structure is well suited for the doctor reporting 
system because it models the hierarchical relationships. With the doctor system 
it can have two reports, which are the left and right. With these two reports it 
allows for the program to be able to basically mimic an organizational chart in a 
way where it is easier to understand, logical, and most importantly simple. Now 
moving onto the tree traversal methods, these methods are used in different ways 
depending on the goal you have with your code. When you want to be able to print 
the hierarchy from top to bottom, you would want it, root then left then right, this is 
called preorder traversal. On the other hand, there is inorder traversal where it is 
left then root then right, and lastly, postorder traversal, it is left then right then root. 
They are each helpful in their different ways depending on the order you want the system to be. 
Now for the last thing is, heaps. Heaps are effective when you are wanting real time systems, 
for example; emergency room intakes. This is because you can order it to highest priority 
where it will always remain at the root. 
'''