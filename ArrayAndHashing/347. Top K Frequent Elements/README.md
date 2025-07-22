**347. Top K Frequent Elements**  
Link: [Top K Frequent Elements](https://neetcode.io/problems/top-k-elements-in-list?list=neetcode150)  
Difficulty: Medium  
Topics: Array, Sort, Hash

=======================================================================================

Given an integer array nums and an integer k, return the k most frequent elements within the array.

The test cases are generated such that the answer is always unique.

You may return the output in any order.

Example 1:

Input: nums = [1,2,2,3,3,3], k = 2

Output: [2,3]
Example 2:

Input: nums = [7,7], k = 1

Output: [7]
Constraints:

1 <= nums.length <= 10^4.
-1000 <= nums[i] <= 1000
1 <= k <= number of distinct elements in nums.

=======================================================================================

UMPIRE Method:

Understand
> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs.
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
- Can the input array be empty?
- Is there any time or space complexity requirement?
- If different numbers have the same frequency, and count is bigger than k. What should I return in this situation.

Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category
- Hash Map: Create a hash map to count the frequency of each number, and sort the elements based on their frequency. Return the top k elements from the sorted list. However, this approach has a time complexity O(n log n) due to the sorting step.
- Bucket Sort: Use a hash map to count the frequency of each element. Create an array of buckets, where each bucket corresponds to a specific frequency count. Next, place each number into the bucket based on their frequency. Iterate through the buckets in reverse order, collecting elements until k elements have been gathered. This method is more efficient since it has better time and space complexity.

Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high-level implementation with an existing diagram
- First idea(It’s less optimal for large inputs):
1. Create a hash map
2. Count the frequecy of each number
3. Convert the hash map into a key-value pair list
4. Sort the list based on frequency(descending)
5. Retrun the first k elements from the sorted list


- Improved idea:
1. Create a hash map
2. Count the frequency of each number
3. Initialize a bucket list to store index corresponding to the frequency
4. Append each number to its buckey based on its frequency
5. Iterate the list in reverse order and collect numbers until it meet k elements

Review
> - Re-check that your algorithm solves the problem by running through important examples
> - Go through it as if you are debugging it, assuming there is a bug

Evaluate
> - Finish by giving space and run-time complexity
> - Discuss any pros and cons of the solution


Time Complexity: O(n)
Space Complexity: O(n)
