class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        U:  1) we need to find the frequency of each number and store it somewhere for later
            comparisons.
            2) sort, rearrange the numbers based on their frequency
            3) return the top k elements after the frequency rearrangement

        P:  1) need to store the number and its frequency -> dict (key value) easy lookup O(1)
            2) find a way to sort in descending order (built in desc function)


        I:
        """

        num_count=defaultdict()
        #iterate through the list and populate the dict

        for n in nums:
            num_count[n] = num_count.get(n, 0) + 1
        #nums_count={1:1; 2:2; 3:3}

        #rearranging = desc function
        ordered = sorted(num_count, key=lambda n: num_count[n], reverse=True)   # O(n log n)
        return ordered[:k]


