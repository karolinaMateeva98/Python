def reverse(text):
    return text[::-1]
'''
We use the slicing feature to reverse the text. We've already seen how we can make slices from sequences using the seq[a:b] code starting from position a to position b.
We can also provide a third argument that determines the step by which the slicing is done. The default step is 1 because of which it returns a continuous part of the text. 
Giving a negative step, i.e., -1 will return the text in reverse.
'''


def is_palindrome(text):
    return text == reverse(text)


something = input("Enter text: ")
if is_palindrome(something):
    print("Yes, it is a palindrome")
else:
    print("No, it is not a palindrome")