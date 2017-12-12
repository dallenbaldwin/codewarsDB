# Trolls are attacking your comment section!
# A common way to deal with this situation is to remove all of the vowels from
# the trolls' comments, neutralizing the threat.
# Your task is to write a function that takes a string and return a new string
# with all vowels removed.
# For example, the string "This website is for losers LOL!" would become "Ths
# wbst s fr lsrs LL!".
# Note: for this kata y isn't considered a vowel.


def disemvowel(string):
    newstring = ''
    for letter in string:
        if letter not in ('aeiouAEIOU'):
            newstring += letter
    return newstring


if __name__ == '__main__':
    print(disemvowel('suck on this you liberal libtard trolls!'))
