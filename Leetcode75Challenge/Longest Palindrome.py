def longestPalindrome(s: str) -> int:
    letter_count = {}
    for char in s:
        if char in letter_count:
            letter_count[char]+=1
        else:
            letter_count[char]=1

    palindrome_length = 0
    has_odd_count = False

    for i in letter_count.values():
        if i % 2 == 0:
            palindrome_length+=i
        else:
            palindrome_length+=i-1
            has_odd_count = True

    if has_odd_count:
        palindrome_length+=1

    return palindrome_length

print(longestPalindrome("abccccdd"))