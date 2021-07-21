# constants.py
# Kordel France
########################################################################################################################
# This file contains the specification for which single-character strings are allowed for the interpretation of the
# prefix strings in this program.
########################################################################################################################

#characters that are acceptable as operands for the evaluation of prefix strings.
acceptable_chars = ['A', 'B', 'C' ,'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
                    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                    '*', '/', '+', '-', '$']
#characters that are acceptable as operators for the evaluation of prefix strings.
acceptable_operators = ['*', '/', '+', '-', '$']

#characters that are not acceptable as operators or operands are temporarily stored here
illegal_chars = []