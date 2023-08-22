import datetime
import config

def log_timelist(frame, Text):
    with open(config.Config_Log.timelist_log_file_path, "a") as f:
        f.write(Text)
class TimeList:
    def __init__(self):
        self.head = None
        self.last = None

    def addNode(self):
        node = TimeNode()
        if self.head is None and self.last is None:
            self.head = node
            self.last = node
        else:
            last = self.last
            node.prev = last
            last.next = node
            self.last = node
        return node

    def printLastNodes(self):
        Text = ""
        start = self.last
        Text += "\nTimestamp is {}\nFrame is {}\n, Current Floor is {}\n, Button List is {}\n, InOut is {}\n\n".format(
            start.timestamp,
            start.frame,
            start.currentFloor,
            start.pressedButton,
            start.InOut
        )
        return Text

    def printAllNodes(self):
        Text = ""
        start = self.head
        while start is not None:
            Text += "\nTimestamp is {}\nFrame is {}\n, Current Floor is {}\n, Button List is {}\n, InOut is {}\n\n".format(
                start.timestamp,
                start.frame,
                start.currentFloor,
                start.pressedButton,
                start.InOut
            )
            #print(Text)
            start = start.next
        return Text

class TimeNode:
    def __init__(self):
        self.timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        self.frame = 0
        self.currentFloor = None
        self.pressedButton = []
        self.InOut = None

        self.next = None
        self.prev = None

    def set_time(self, value):
        self.timestamp = value

    def set_frame(self, value):
        self.frame = value

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