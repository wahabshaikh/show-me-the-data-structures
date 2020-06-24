# Problem 2: File Recursion

## Time Complexity: O(n)
## Space Complexity: O(n)

### Here, n is the total number of files

The files ending with the given suffix are stored in an `array` implemented using Python's `list`, because the  `append` operation takes constant time (`O(1)`).

I have used `recursion` because the problem can be broken down into a smaller, repetitive sub-problem. In this case, we iterate through the contents of the directory. If a file is found and it ends with the given suffix, we append it to our list, otherwise we continue with the next iteration. However, if a sub-directory is found, we repeat the same procedure for the sub-directory.

Since, we iterate through all the files one by one, it takes linear time. Hence, time complexity is `O(n)`.

The space complexity is `O(n)` because in the worst case scenario, all the files end with the given suffix.