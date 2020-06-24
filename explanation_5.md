# Problem 5: Blockchain

## Time Complexity: O(n)
## Space Complexity: O(n)

### Here, n is the length of the blockchain

The blockchain is implemented using a `linked list`.
The blocks are linked together using SHA256 hashes. However, I have defined a `next_block` attribute in the `Block` class to help traverse the blockchain.

The `add` operation takes constant time `O(1)` because I keep track of the `last_block` in the chain. The `traverse` operation takes linear time `O(n)`. In the worst case scenario, `search` operation takes linear time `O(n)`, if the block is not present in the list.