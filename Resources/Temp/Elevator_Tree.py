import gc
import os
import datetime
import numpy as np
import classid_list
import config

class ListOfTime:
    def __init__(self):
        self.head = None
        self.last = None
        self.parent = None
        self.child = None
        self.length = 0
        self.timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')

    def __del__(self):
        self.head = None
        self.last = None
        self.parent = None
        self.child = None
        self.length = 0
        self.timestamp = None

    def set_Root(self):
        self.parent = -1

    def return_if_root(self):
        if self.parent == -1:
            return 1
        else:
            return 0

    def clear_list(self):
        self.head = None
        self.last = None
        self.parent = None
        self.child = None
        self.length = 0
        self.timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')

    def append_Button(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.last = node
        else:
            self.last.next = node
            node.prev = self.last
            self.last = node
        self.length += 1

    def find_button(self, value):
        if self.head is not None:
            start = self.head
            while start is not None:
                if start.value == value:
                    return start
                start = start.next
        return None

    def delete_Button(self, value):
        node = self.find_button(value)
        if node is not None:
            if self.head == self.last:
                self.head = None
                self.last = None
            elif self.head == node:
                next = node.next
                node.next = None
                next.prev = None
                self.head = next
            elif self.last == node:
                prev = node.prev
                node.prev = None
                prev.next = None
                self.last = prev
            else:
                prev = node.prev
                next = node.next
                prev.next = next
                next.prev = prev
                node.prev = None
                node.next = None
            self.length -= 1
            del(node)
            return 1
        else:
            return 0

    def make_new_TimeList(self):
        list = ListOfTime()
        self.child = list
        list.parent = self

        return list

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None

    def return_value(self):
        return self.value

def print_list_Nodes(List) -> None:
    node = List.head
    while node is not None:
        print(node.value)
        node = node.next
    return None

def print_all_Nodes(List) -> None:
    #print("im {} parent {} child {}".format(List, List.parent, List.child))
    Temp = List
    Text = ""
    Text += List.timestamp + " "

    while Temp is not None:
        node = Temp.head
        while node is not None:
            #print("elem : {}".format(node.value))
            Text += str(node.value) + " "
            node = node.next
        Temp = Temp.child

    return Text

def get_node_from_all_Lists(List, value):
    while List is not None:
        node = List.find_button(value)
        if node is not None:
            return 1
        else:
            List = List.child
    return 0
def delete_node_from_all_Lists(List, value):
    while List is not None:
        node = List.find_button(value)
        if node is not None:
            flag = List.delete_Button(node.value)
            return List
        else:
            List = List.child
    return None

def return_lowest_child(Root):
    while Root.child is not None:
        Root = Root.child
    return Root

# def return_Node_and_List_From_Root(List, value) -> (LinkedList, Node):
#     node = List.head
#     while node is not None:
#         if node.elem == value:
#             return List, node
#         if node.child is not None:
#             (result_list, result_node) = return_Node_and_List_From_Root(node.return_Child_List(), value)
#             if result_list is not None:
#                 return (result_list, result_node)
#         node = node.next
#     return None, None

if __name__ == '__main__':
    Root = ListOfTime()
    Root.set_Root()

    Root.append_Button(1)
    Root.append_Button(3)
    Root.append_Button(5)

    Child1 = Root.make_new_TimeList()
    Child1.append_Button(2)
    Child1.append_Button(4)
    Child1.append_Button(6)

    Child2 = Child1.make_new_TimeList()
    Child2.append_Button(10)
    Child2.append_Button(12)
    Child2.append_Button(14)

    delete_node_from_all_Lists(Root, 12)
    #print(get_node_from_all_Lists(Root, 14))
    print_all_Nodes(Root)

    Child2.delete_Button(14)
    Child2.delete_Button(10)

    Child1.child = None
    Child2.parent = None

    del(Child2)

    print_all_Nodes(Root)