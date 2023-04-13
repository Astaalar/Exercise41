def word(string):
    if (string==string[::-1]):
        return "The word is a palindrome."
    else: 
       return "The word is not a palindrome." 

string = "level"
#print(word(string))

def is_palindrome(word):
    return word == ''.join(reversed(word))

print(is_palindrome('kajak'))   