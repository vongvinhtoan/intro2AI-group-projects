import queue
from typing import Any, Callable, TypeVar, Generic

T = TypeVar('T')

class PrioritizedItem(Generic[T]):
    def __init__(self, item: T, priority: float):
        self.item = item
        self.priority = priority

    def __lt__(self, other: 'PrioritizedItem'):
        return self.priority < other.priority

class PriorityQueue(queue.PriorityQueue, Generic[T]):
    def __init__(self, maxsize: int = 0, priority: Callable[[T], Any] = lambda x: x):
        super().__init__(maxsize)
        self.priority = priority

    def put(self, item: T):
        super().put(PrioritizedItem(item, self.priority(item)))

    def get(self) -> T:
        return super().get().item