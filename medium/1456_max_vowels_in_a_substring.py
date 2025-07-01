def maxVowels(s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        vowels = "aeiou"
        max_vowels = 0
        curr_vowels = 0

        l = 0

        for x in range(k):
            if s[x] in vowels:
                curr_vowels += 1

        max_vowels = max(max_vowels, curr_vowels)

        for x in range(k, len(s)):
            if s[l] in vowels:
                curr_vowels -= 1
                l += 1
            else:
                l += 1

            if s[x] in vowels:
                curr_vowels += 1

            max_vowels = max(max_vowels, curr_vowels)

        return max_vowels