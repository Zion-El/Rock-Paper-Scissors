def find_anagram(word, anagram):
    # [assignment] Add your code here
    if len(word) == len(anagram):
        if sorted(word) == sorted(anagram):
            return True
        else:
            return False
    else:
        return False


if find_anagram('bad', 'dab') == True:
    print('Good')
else:
    print('Bad')
