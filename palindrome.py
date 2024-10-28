def solution(S):
    # Convert to list for easier manipulation
    chars = list(S)
    N = len(chars)
    
    # Check for palindrome and fill in question marks
    for i in range(N // 2):
        # Get the corresponding positions from start and end
        left = chars[i]
        right = chars[N - 1 - i]
        
        # Case 1: If both are question marks    ??? aaa
        if left == '?' and right == '?':
            chars[i] = chars[N - 1 - i] = 'a'
        # Case 2: If only left is question mark ?b bb
        elif left == '?':
            chars[i] = right"
        # Case 3: If only right is question mark  a? aa
        elif right == '?':
            chars[N - 1 - i] = left
        # Case 4: If neither are question marks and don't match ab
        elif left != right:
            return "NO"
    
    # Handle middle character for odd length strings ab?ab ababa
    if N % 2 == 1 and chars[N // 2] == '?':
        chars[N // 2] = 'a'
    
    return ''.join(chars)

# Test cases
print(solution("?ab??a"))  # Should print "aabbaa"
print(solution("bab??a"))  # Should print "NO"
print(solution("?a?"))     # Should print "aaa"
