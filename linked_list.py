class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data


class LinkedList:

    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for item in nodes:
                node.next = Node(data=item)
                node = node.next

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def add_first(self, node):
        node.next = self.head
        self.head = node
    
    def add_last(self, node):
        if self.head is None:
            self.head = node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = node
    
    def add_after(self, target_node_data,new_node):

        if self.head is None:
            raise Exception("Linked list is empty")
        node = self.head
        while node is not None:
            if node.data == target_node_data:
                new_node.next = node.next
                node.next = new_node
                return
            node = node.next
        raise Exception("Node with data '%s' not found" % target_node_data)


    def remove_node(self, target_node_data):
        if self.head is None:
            raise Exception("Linked list is empty")
        
        node = self.head
        while node:
            if node.data == target_node_data:
                prev_node = node
                node = node.next

        prev_node.next = node.next
        node = None
        


        


linked_list = LinkedList(nodes=["argentina", "armenia", "barbados"])
linked_list.add_last(Node("england"))
linked_list.add_after("barbados", Node("ireland"))
for node in linked_list:
    print(node)

