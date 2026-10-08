
"""
Problem 1: Duplicate Tracker
Return True when a product ID shows up more than once.
"""

def has_duplicates(product_ids):
    # I used a set because it only keeps one of each ID.
    # Checking and adding in a set is usually O(1), so the whole thing is O(n).
    seen = set()
    for id in product_ids:
        if id in seen:
            return True
        seen.add(id)
    return False


"""
Problem 2: Order Manager
Add tasks and remove the oldest one first.
"""

class TaskQueue:
    def __init__(self):
        # A list works as a basic queue since tasks stay in the order I add them.
        # append is O(1) usually, but removing the first task is O(n) because items shift.
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_oldest_task(self):
        if len(self.tasks) == 0:
            return None
        return self.tasks.pop(0)


"""
Problem 3: Unique Value Counter
Keep track of how many different values were added.
"""

class UniqueTracker:
    def __init__(self):
        # I picked a set so duplicate numbers don't get counted more than once.
        # Adding is usually O(1) and len is O(1), so getting the count is fast.
        self.numbers = set()

    def add(self, value):
        self.numbers.add(value)

    def get_unique_count(self):
        return len(self.numbers)
