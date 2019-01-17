"""
Copyright (C) 2018 Wen Liang, Wen_Liang@student.uml.edu

"""

import re


def char_frequency(inputstr):
    """
    use a dictionary to store the frequency of all character in the string,
    and sort the dictionary in increasing order of character's frequency

    Args:
        input string

    Return:
        A dictionary holds the character in input string and their frequency.
        And the dictionary is sorted in increasing order of character's frequency
    """
    char_dict = {}
    for i in inputstr:
        keys = char_dict.keys()
        if i in keys:
            char_dict[i] += 1
        else:
            char_dict[i] = 1
    # sort in increasing order of each character's frequency
    char_dict = sorted(char_dict.items(), key=lambda x: x[1])
    return char_dict


def findPair(inputstr):
    """
    Algorithms:

    1.use a dictionary to store the frequency of all character in the string,
    and sort the dictionary in increasing order of character's frequency

    2.loop through the frequency dictionary, if we find frequency difference
    of two adjacent character in the dictionary is within 1, then we use
    the regular expression to remove all other character in the string
    (e.g., I use '[^ab]' to remove all other character and leave only
    character 'a', 'b' in the string). Once we have stripped string,
    loop through stripped string and count alternating pair in the
    stripped string to see if it is twisted pair

    Args:
        input string

    Return:
        return twisted pair if we find twisted pair in string, otherwise return empty string.

    """
    # ignore trailing and preceding whitespace
    inputstr = inputstr.strip()
    freq = char_frequency(inputstr)
    for i in range(len(freq)-1):
        if freq[i][1] > 1 and (freq[i][1] == freq[i+1][1] or freq[i][1] == freq[i+1][1]-1):
            reg_exp = '[^'+freq[i][0]+freq[i+1][0]+']'
            # if the regular expression inside the bracket also end with ']',
            # e.g. '[^*]]', then it will not strip the string correctly,
            # so change the occurrence of character inside the bracket to '[^]*]'
            if freq[i+1][0] == ']':
                reg_exp = '[^'+freq[i+1][0]+freq[i][0]+']'
            # avoid the effect of the escape character in the regular expression
            reg_exp = reg_exp.encode("unicode_escape").decode("utf-8")
            stripped_str = re.sub(reg_exp, '', inputstr)
            alternating_count = 0
            j = 0
            # the count of alternating pair in the stripped string indicate if it is twisted pair
            while j < len(stripped_str)-1:
                if stripped_str[j] != stripped_str[j+1]:
                    alternating_count += 1
                j += 1
            if alternating_count == (len(stripped_str)-1):
                #treat it as literal raw string, avoid the effect of escape character
                return stripped_str.encode("unicode_escape").decode("utf-8")
    return ''


if __name__ == '__main__':
    INPUTFILE = open("pairs-in.txt", "r")
    OUTPUTFILE = open("output.txt", "w")
    INPUT = INPUTFILE.readline()
    while INPUT != '':
        TWISTED_PAIR = findPair(INPUT)
        if TWISTED_PAIR != '':
            # write the twisted pair as the literal raw string
            OUTPUTFILE.write(TWISTED_PAIR.encode('utf-8').decode('unicode_escape'))
            OUTPUTFILE.write('\n')
        else:
            OUTPUTFILE.write('\n')
        INPUT = INPUTFILE.readline()
    OUTPUTFILE.close()
    INPUTFILE.close()
