import os
import numpy as np
import classid_list
import config

class LinkedList:
    def __init__(self):
        self.head = None
        self.last = None
        self.root = None
        self.parent = None
        self.length = 0

    def set_Root(self):
        if self.root is None:
            self.root = -1

    def reset_Root(self):
        if self.root is not None:
            self.root = None

    def append_Node(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.last = node
        else:
            self.last.next = node
            node.prev = self.last
            self.last = node
        self.length += 1

    def delete_Node(self, node, *args):
        #node = self.find_node(value)
        if node is not None:
            if node == self.head and self.length >=2:
                next = node.next
                next.prev = None
                node.next = None
                self.head = next
            elif node == self.last and self.length >=2:
                prev = node.prev
                prev.next = None
                node.prev = None
                self.last = node
            elif self.length >=2:
                prev = node.prev
                next = node.next

                node.prev = None
                node.next = None

                prev.next = next
                next.prev = prev
            elif self.length == 1:
                pass
            del(node)
            self.length -= 1
        return self

    def delete_List(self):
        pass

    def find_node(self, value):
        if self.last is not None:
            node = self.head
            while node is not None:
                #print(node.elem)
                if value == node.elem:
                    return node
                node = node.next
        return None

class Node:
    def __init__(self, value=None):
        self.elem = value
        self.next = None
        self.prev = None

        self.child = None

    def add_Child_List(self, child_value) -> LinkedList:
        node = Node(child_value)
        list = LinkedList()
        self.child = list
        list.parent = self
        list.head = node
        list.last = node

        return list

    def return_Child_List(self) -> LinkedList:
        return self.child


def add_child_list_with_node(parent_list, parent_node_value, child_node_value) -> LinkedList:
    node = parent_list.find_node(parent_node_value)
    child_list_with_node = node.add_Child_List(child_node_value)

    return child_list_with_node
def print_list_Nodes(List) -> None:
    node = List.head
    while node is not None:
        print(node.elem)
        node = node.next

    return None

def print_all_Nodes(List) -> None:
    node = List.head
    while node is not None:
        print("{} {}".format(node.elem, node.child))
        if node.child is not None:
            print_all_Nodes(node.return_Child_List())
        node = node.next
    return None

def return_Node_and_List_From_Root(List, value) -> (LinkedList, Node):
    node = List.head
    while node is not None:
        if node.elem == value:
            return List, node
        if node.child is not None:
            (result_list, result_node) = return_Node_and_List_From_Root(node.return_Child_List(), value)
            if result_list is not None:
                return (result_list, result_node)
        node = node.next
    return None, None

if __name__ == '__main__':
    Root = LinkedList()
    Root.set_Root()

    Root.append_Node(1)
    Root.append_Node(3)

    Child_List = add_child_list_with_node(Root, 3, 2)
    Child_List.append_Node(4)
    Child_List.append_Node(6)
    Child_List.append_Node(8)

    Child_List3 = add_child_list_with_node(Child_List, 8, 100)
    Child_List3.append_Node(200)
    Child_List3.append_Node(300)

    Root.append_Node(5)
    Root.append_Node(7)
    Root.append_Node(9)
    Root.append_Node(11)

    Child_List2 = add_child_list_with_node(Root, 9, 10)
    Child_List2.append_Node(12)

    tl, tn = return_Node_and_List_From_Root(Root, 200)
    tl.delete_Node(tn)
    print_all_Nodes(Root)