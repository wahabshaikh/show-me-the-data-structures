# Problem 4: Active Directory

## Time Complexity: O(m + n)
## Space Complexity: O(m + n)

### Here, m and n are the total number of groups and users respectively


The groups and users are stored in a Python `list`. The `append` operation takes constant time (`O(1)`).

I have used `recursion` because the problem can be broken down into a smaller, repetitive sub-problem. In this case, we iterate through the list of users. If the user is found, we return `True`, otherwise we iterate through the groups. We can then repeat the same procedure for each group, and if a match is not found, we return `False` finally.

In worst case scenario, we iterate through all the users one by one, it takes linear time. Hence, time complexity is `O(n)`. The same is applicable to the groups, which will take `O(m)` time. Hence, total time complexity is `O(m + n)`. 

The space complexity is `O(m + n)` to store all the groups and users.