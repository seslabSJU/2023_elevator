import config
import classid

try:
    from config import Config_Elevator_HW, Config_Elevator_SW
    config_ELEVATOR_HW = Config_Elevator_HW
    config_ELEVATOR_SW = Config_Elevator_SW

except:
    pass
class Linked_List:
    def __init__(self):
        self.head = None
        self.last = None
        self.length = 0

    def get_value(self, node):
        return node.value
    def get_length(self):
        return self.length

    def get_node(self, value):
        temp = self.head
        while temp is not None:
            if temp.value == value:
                return temp
            else:
                temp = temp.next
        return None

    def change_value(self, value_now, value_to):
        node = self.get_node(value_now)
        if node is not None:
            node.value = value_to

    def add_Node_Right(self, value, Direction):
        node = Node(value)
        if self.head == None:
            self.head = node
            self.last = node
            node.direction = Direction
        else:
            self.last.next = node
            node.prev = self.last
            self.last = node
        self.length += 1

    def remove_Node(self, node, delete=False):
        #node = self.get_node(remove_value)
        if node is not None:
            if node == self.head:
                next = node.next
                next.prev = None
                self.head = next

            elif node == self.last:
                prev = node.prev
                prev.next = None
                self.last = prev

            else:
                prev = node.prev
                next = node.next
                prev.next = next
                next.prev = prev

        if delete:
            del node
            self.length -= 1
        else:
            node.next = None
            node.prev = None

            return node

    def insert_Node(self, prev_Node, next_Node, node):
        if prev_Node.next != next_Node and next_Node.prev != prev_Node:
            print("Insert Node Relationship Error")
            return None

        prev_Node.next = node
        next_Node.prev = node

        node.next = next_Node
        node.prev = prev_Node

    def remove_and_insert_Node(self, prev_Node, next_Node, node):
        node = self.remove_Node(node)
        self.insert_Node(prev_Node, next_Node, node)


    def print_All_Nodes(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None
        self.direction = None

def get_weight(value):
    keys = config_ELEVATOR_SW.Location_Weight.keys()

    for key in keys:
        if value == key:
            return config_ELEVATOR_SW.Location_Weight[key]

    return None
def sort_Nodes_via_Direction(LinkedList, Start_Location, Direction):
    # Direction = 1 is Upside, 0 is downside
    if LinkedList.length <= 1:
        print("List Length is less then 1")
        return None

    else:
        start_location_weight = get_weight(Start_Location)
        if Direction:
            print("ASD")
        else:
            sort_start_node = LinkedList.head.next
            sort_start_direction = sort_start_node.direction

            datum_node = get_first_Different_Direction_Node(sort_start_node, start_location_weight, sort_start_direction)
            if datum_node is not None:
                move_downside_floors_to_left(start_location_weight, LinkedList, datum_node)

            left_sort_start_node = sort_start_node
            left_sort_end_node = datum_node.prev

            right_sort_start_node = datum_node
            right_sort_end_node = LinkedList.last

            left_sort_end_node.next = None
            right_sort_start_node.prev = None

            temp = merge_sort(left_sort_start_node, left_sort_end_node, Direction)
            temp2 = merge_sort(right_sort_start_node, right_sort_end_node, not Direction)

            erase_start = LinkedList.head.next

            LinkedList.head.next = temp
            temp.prev = LinkedList.head

            while temp.next is not None:
                temp = temp.next

            temp.next = temp2
            temp2.prev = temp

            while temp2.next is not None:
                temp2 = temp2.next
            LinkedList.last = temp2

            #LinkedList.print_All_Nodes()
            return LinkedList


def merge_sort(sort_start, sort_end, Direction=False):
    if not sort_start or sort_start == sort_end:
        return sort_start

    middle_node = find_middle_node(sort_start, sort_end)
    second_half = middle_node.next
    middle_node.next = None

    # print("middle_node is {}".format(middle_node.value))
    # print("second_half is {}\n\n".format(second_half.value))


    left_sorted_part = merge_sort(sort_start, middle_node, Direction)
    right_sorted_part = merge_sort(second_half, sort_end, Direction)

    return merge_linked_list(left_sorted_part, right_sorted_part, Direction)

def find_middle_node(start_node, end_node):
    next_node = start_node
    next_next_node = start_node

    while next_next_node != end_node and next_next_node.next != end_node:
        next_node = next_node.next
        next_next_node = next_next_node.next.next

    return next_node

def merge_linked_list(left_sorted_node, right_sorted_node, ascending=False):
    dummy_node = Node()
    current = dummy_node

    # print("Sort start is {}".format(left_sorted_node.value))
    # print("Sort end is {}".format(right_sorted_node.value))

    while left_sorted_node and right_sorted_node:
        if (get_weight(left_sorted_node.value) < get_weight(right_sorted_node.value)) if ascending else (get_weight(left_sorted_node.value) > get_weight(right_sorted_node.value)):
            current.next = left_sorted_node
            left_sorted_node = left_sorted_node.next
        else:
            current.next = right_sorted_node
            right_sorted_node = right_sorted_node.next

        current = current.next

    if left_sorted_node:
        current.next = left_sorted_node
    elif right_sorted_node:
        current.next = right_sorted_node

    temp = dummy_node.next
    # while temp is not None:
    #     print(temp.value)
    #     temp = temp.next

    return dummy_node.next

def get_first_Different_Direction_Node(sort_start_node, head_weight, Direction=False):
    temp = sort_start_node
    while temp is not None:
        location_weight = get_weight(temp.value)

        if Direction and (head_weight > location_weight):
            return temp
        elif not Direction and (head_weight < location_weight):
            return temp
        else:
            temp = temp.next

    return None

def move_downside_floors_to_left(head_weight, LinkedList, datum_node):
    start_node = datum_node.next

    next_node = datum_node
    prev_node = datum_node.prev

    while start_node is not None:
        node_weight = get_weight(start_node.value)
        if head_weight > node_weight:
            LinkedList.remove_and_insert_Node(prev_node, next_node, start_node)
            prev_node = start_node

        start_node = start_node.next

if __name__ == "__main__":
    pass
    config_HW = config.Config_Elevator_HW
    Direction = True if config_HW.Accelerator['Velocity']>=0 else False

    LL = Linked_List()
    # LL.add_Node_Right("2", Direction)
    # LL.add_Node_Right("1", Direction)
    # LL.add_Node_Right("B4", Direction)
    # LL.add_Node_Right("5", Direction)
    # LL.add_Node_Right("B5", Direction)
    #
    # LL = sort_Nodes_via_Direction(LL, "2", Direction)
    # LL.print_All_Nodes()
    list = classid.get_classid_list_from_log()
    for i, elem in enumerate(list):
        print("Num {}, Elem {}".format(i, elem))
    # if len(list) != 0:
    #     for elem in list:
    #         LL.add_Node_Right(elem, Direction)
    #
    # LL = sort_Nodes_via_Direction(LL, "8", Direction)
    # LL.print_All_Nodes()