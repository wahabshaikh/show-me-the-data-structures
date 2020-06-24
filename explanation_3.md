# Problem 3: Huffman Coding

## Time Complexity: O(nlogn)
## Space Complexity: O(n)

### Here, n is the number of characters in the string message

The frequency of each character in the string message is stored in a `dictionary`, because it takes constant time (`O(1)`) to `add`, `lookup` and `update` data.

I have used Python's `heapq` module to implement a `min-heap` to store the Nodes of the Huffman's tree. The `heapush` and `heappop` opertions take logarithmic time (`O(logn)`) for a heap. The `heapify` function converts an existing `iterable` to a `min-heap` in linear time (`O(n)`).

In worst case scenario, all the characters of the string message are unique. Hence, it would take linear time (`O(n)`) to iterate through the `min-heap`. Popping out the two least priority nodes and pushing back the internal node would take logarithmic time (`O(logn)`) each. Hence, it would take 'O(nlogn)` time to complete this procedure.

Traversing each node of the Huffman tree to calculate the Huffman code and creatng the encoded data will take linear time (`O(n)`) each.

Decoding the encoded data requires reaching out every leaf node. Hence, it will take linear time (`O(n)`) as well.

Hence, overall time complexity is `O(nlogn)`.

In worst case scenario, each character in the string message is unique. Hence, the space complexity will be `O(n)`.