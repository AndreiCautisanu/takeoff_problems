from collections import Counter


def topK(nums, k):

    if k < 1 or k > len(nums):
        raise ValueError('input a valid k')


    # get frequency dictionary in O(N)
    counter = Counter(nums)

    # freq_buckets[i] = the numbers in the list which appear i times
    # no frequency can be larger than the length of the list
    freq_buckets = [[] for _ in range(len(nums) + 1)]


    # getting the frequencies into their buckets is also O(N)
    for num, freq in counter.items():
        freq_buckets[freq].append(num)


    # go through the list of buckets in reverse order to get the list of unique elements in the list in descending order of their frequencies
    # this parsing is also done in O(N)
    ordered_nums = []
    for i in range(len(freq_buckets)-1, -1, -1):
        bucket = freq_buckets[i]
        ordered_nums.extend(bucket)
    
    return ordered_nums[:k]

    

if __name__ == '__main__':
    print(topK([6,5,2,6,6,2,1,7,3,3,3], 3))
    print(topK([6,2,2,2,6,6,6,6,5,1,2,0,9,0,0,0,0,0,0,0,0,2], 2))

