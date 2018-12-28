import collections

class Solution(object):
    '''
    2018-12-28
    '''
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        # count
        charFreq = collections.defaultdict(int)
        for c in s:
            charFreq[c] += 1

        # sort
        tuples = [(freq, c) for c, freq in charFreq.items()]
        tuples.sort(reverse=True)

        res = []
        for freq, c in tuples:
            res+=[c]*freq

        return "".join(res)
