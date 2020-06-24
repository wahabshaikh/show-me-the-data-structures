# Problem 1: LRU Cache

## Time Complexity: O(n)
## Space Complexity: O(n)

### Here, n is the capacity of the LRU cache

The `cache` is implemented using a Python `dictionary`, to replicate the behaviour of a `hash map`. This allows  `add`, `lookup`, and `delete` operations in constant time (`O(1)`).

The LRU element is tracked using a `queue`. The first element in the `queue` is the LRU element. I have used Python's `deque` for this purpose. This allows `enqueue (append)` and `dequeue (popleft)` operations in constant time (`O(1)`). However, `remove` operation takes linear time(`O(n)`).

Whenever, the `get` operation is used, the queue needs to be updated. So, we first `remove` the element from the `queue` and then `enqueue` it. This take liner time. Hence, the overall time complexity is `O(n)`.

The space complexity is `O(n)` because the LRU cache and the queue stores n entries at max.