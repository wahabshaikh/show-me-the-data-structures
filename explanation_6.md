# Problem 6: Union and Intersection

## Time Complexity: O(m * n)
## Space Complexity: O(m + n)

### Here, m and n are the lrngths of the linked lists respectively.

I have used a `set` to find the union and intersection of the two linked lists. 

In order to find the union, I traverse both the lists and add their elements to the same `set`. This removes any duplicate elements and gives us the union of both the lists. Traversing both the lists will take linear time `O(m + n)`. Adding to the set takes constant time `O(1)`.

In order to find the union, I traverse both the lists and add their respective elements to two different `sets` named `set_1` and `set_2`. Then I traverse the `set_2` and if the node is present in `set_1`, we add it to `intersection_set`. This takes `O(m * n)` time. 

I then convert the union and intersetion sets to a linked list in linear time `O(m + n)`. 

Hence, overall time complexity is `O(m * n)`.

Space complexity is `O(m + n)` to store both the linked lists and their intersection and union.