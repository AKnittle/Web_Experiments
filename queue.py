"""Queue Helper Class"""


class queue:

    # The option to initialize with just data or with pre-existing child nodes
    def __init__(self, queue_list=None):
        self.queue_list = queue_list

    def add_to_queue(self, data):
        if self.queue_list is None:
            print("Creating New Queue...")
            self.queue_list = [data]
        else:
            print("Appending Queue...")
            self.queue_list.append(data)

    def pop_queue(self):
        if self.queue_list is not None:
            head_val = self.queue_list[0]
            queue_len = len(self.queue_list)
            if queue_len >= 2:
                del self.queue_list[0]
            else:
                self.queue_list = None
            return head_val
        else:
            raise ValueError("Queue is already empty")
