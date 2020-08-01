class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.container = []
        self.overflow = 0

    def append(self, item):
        # check if container is at capacity
        # if not, things can be appended normally
        if len(self.container) < self.capacity:
            self.container.append(item)
        # else, replace the item at the overflow index, and increment overflow
        elif len(self.container) == self.capacity:
            self.container[self.overflow] = item
            if self.overflow == self.capacity-1:
                self.overflow = 0
            else:
                self.overflow += 1

    def get(self):
        return self.container
