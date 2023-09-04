import datetime
import config

class TimeList:
    def __init__(self):
        self.head = None
        self.last = None

    def addNode(self, timestamp):
        node = TimeNode()
        node.set_time(timestamp)
        
        if self.head is None and self.last is None:
            self.head = node
            self.last = node
        else:
            last = self.last
            node.prev = last
            last.next = node
            self.last = node
        return node

    def find_Node(self, value):
        pass

    def removeNode(self):
        pass

    def printLastNodes(self):
        Text = ""
        start = self.last
        Text += "\nTimestamp is {}\nCurrent Floor is {}\nButton List is {}\nInOut is {}\n\n".format(
            datetime.datetime.strftime(start.timestamp, '%Y%m%d_%H%M%S'),
            start.currentFloor,
            start.pressedButton,
            start.InOut
        )
        return Text

    def printAllNodes(self):
        Text = ""
        start = self.head
        while start is not None:
            Text += "\nTimestamp is {}\nCurrent Floor is {}\nButton List is {}\nInOut is {}\n\n".format(
                datetime.datetime.strftime(start.timestamp, '%Y%m%d_%H%M%S'),
                start.currentFloor,
                start.pressedButton,
                start.InOut
            )
            #print(Text)
            start = start.next
        return Text

class TimeNode:
    def __init__(self):
        self.timestamp = None
        self.currentFloor = None
        self.pressedButton = []
        self.InOut = None

        self.next = None
        self.prev = None

    def set_time(self, value):
        self.timestamp = value

    def set_currentFloor(self, value):
        self.currentFloor = value

    def set_pressedButton(self, list):
        self.pressedButton = list

    def add_pressedButton(self, value):
        self.pressedButton.append(value)

    def set_InOut(self, InOut):
        if InOut:
            self.InOut = True
        else:
            self.InOut = False
