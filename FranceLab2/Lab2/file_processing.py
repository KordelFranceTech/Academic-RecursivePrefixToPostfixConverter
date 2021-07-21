# file_processing.py
# Kordel France
########################################################################################################################
# This file contains functions that perform I/O file processing of the user-specified input and output files.
########################################################################################################################

from Lab2.CharStack import CharStack
from Lab2.conversion import prefix_to_postfix
import time


def reverse_stack(stack_fwd) -> CharStack:
    """
    Takes a CharStack and returns a new stack with the same elements in reverse order.
    :param stack_fwd: The stack to reverse the order of
    :return: A new stack with the same elements, but in reverse order
    """
    stack_rev = CharStack(int(stack_fwd.max_items))
    if stack_fwd.max_items > 1:
        for i in range(1, stack_fwd.max_items):
            stack_rev.push(stack_fwd.pop())
        return stack_rev
    else:
        return stack_fwd


def process_file_data(input_text_file, output_text_file) -> None:
    """
    Takes an input file to read data from line by line, character by character, and formats it for conversion of
    all valid prefix expressions to postfix expressions.
    :param input_text_file: the text file to read prefix expressions from.
    :param output_text_file: the text file to write corresponding postfix expressions to.
    """
    print('Processing input...')
    input_file = open(str(input_text_file), 'r')
    stack_length = 0
    last_char = ''
    expr_count = 1
    # read the entire file once and count the characters to know how large a CharStack should be initalized for
    while 1:
        single_char = input_file.read(1)
        if single_char == '\n' and last_char == '\n':
            continue
        elif single_char != ' ':
            stack_length += 1
        if single_char == '\n' and last_char != '\n':
            expr_count += 1
        if not single_char:
            break
        last_char = single_char
    # a bit of defensive programming and likely not needed: close and reopen file just to ensure we read exact same data as before
    input_file.close()
    input_file = open(str(input_text_file), 'r')
    char_stack_a = CharStack(int(stack_length))
    last_char = ''
    # read the entire file again, this time actually reading data in to the CharStack for use
    # clean the data as it is read
    while 1:
        single_char = input_file.read(1)
        if not single_char:
            break
        elif str(single_char) == ' ':
            continue
        elif single_char == '\n' and last_char == '\n':
            continue
        elif str(single_char) == '#':
            # '#' will be used later on as a delimiter for expression conversion
            # if the user put a '#' in their input file, replace it with a '@'
            char_stack_a.push('@')
        else:
            char_stack_a.push(str(single_char))
        last_char = single_char
    input_file.close()

    # open the output file and build a header for aesthetic appearance
    output_text_file = open(str(output_text_file), 'a')
    output_text_file.truncate(0)
    output_text_file.write(f'*****************************************************************************************\n')
    output_text_file.write(f'*****************************************************************************************\n')
    output_text_file.write(f'*****************************************************************************************\n')
    output_text_file.write(f'\t\t\t\t\t\t\t\t\t\tWelcome\n')
    output_text_file.write(f'*****************************************************************************************\n')
    output_text_file.write(f'\t\t\t\t\t\tStarting Prefix-To-Postfix Program\n')
    output_text_file.write(f'*****************************************************************************************\n')
    # let the user know how many expressions were found in the input file
    output_text_file.write(f'\t{expr_count} total expressions were read in\n')
    output_text_file.write(f'\tBeginning conversion of prefix expressions to postfix expressions...\n\n\n')
    print(f'\t{expr_count} total expressions were read in')
    print(f'\tBeginning conversion of prefix expressions to postfix expressions now.\n\n')
    # briefly pause processing so that the user can read the output to the console
    time.sleep(3)

    # initialize new CharStacks to be used for formatting the prefix expression correctly for conversion
    char_stack_b = CharStack(int(stack_length))     # used to get reverse order of the input file for processing
    char_stack_c = CharStack(int(stack_length))     # used as a temporary stack to hold each line in input file
    char_stack_d = CharStack(int(stack_length))     # used to get reverse order of char_stack_c to use for infix expression
    temp_count = 0
    expr_dec_count = 1
    pass_count = 0                                  # how many prefix strings passed in converting to postfix
    fail_count = 0                                  # how many prefix strings failed to convert to postfix

    # reverse the order of the CharStack into another stack
    for i in range(1, char_stack_a.max_items):
        char_stack_b.push(char_stack_a.pop())

    # read the entire CharStack line by line, character by character
    for i in range(1, char_stack_b.max_items):
        stack_length -= 1
        # an entire line was read, format it for processing as a prefix expression
        if char_stack_b.peek() == '\n' or stack_length == 1:
            char_stack_b.pop()
            # for j in range(1, temp_stack.max_items):
            for j in range(0, temp_count):
                char_stack_c.push(char_stack_d.pop())
            for k in range(0, temp_count):
                char_stack_d.push(char_stack_c.pop())
            prefix_string = ''
            for item in char_stack_d.items:
                prefix_string += str(item)
            # we've found a full prefix exprsesion, perform the prefixToPostfix conversion on it
            # postfix_string, error = prefixToPostfix(char_stack_d, temp_count)
            postfix_string, error = prefix_to_postfix(str(prefix_string))
            if error:
                fail_count += 1
                # ensure we write identical output to both the console and the output file
                output_text_file.write(f'{expr_dec_count}) For the prefix string: {prefix_string}, the equivalent '
                                       f'postfix string could not be found.\n{postfix_string}')
                print(f'{expr_dec_count}) For the prefix string: {prefix_string}, the equivalent postfix '
                      f'string could not be found.\n{postfix_string}')
            else:
                pass_count += 1
                # ensure we write identical output to both the console and the output file
                output_text_file.write(f'{expr_dec_count}) For the prefix string: {prefix_string}, the equivalent '
                                       f'postfix string is: {postfix_string}')
                print(f'{expr_dec_count}) For the prefix string: {prefix_string}, the equivalent '
                      f'postfix string is: {postfix_string}')
            output_text_file.write(
                f'\n-----------------------------------------------------------------------------------------\n')
            print(f'-----------------------------------------------------------------------------------------')
            char_stack_d.pop_all()
            temp_count -= temp_count
            expr_dec_count += 1
            # pause processing for 1 second after each new line to allow  user time to read the screen
            time.sleep(1)
        # the same line is still being read, so continue reading characters
        else:
            char_stack_d.push(char_stack_b.pop())
            temp_count += 1
    # output a footer for UI aesthetics
    output_text_file.write(
        '*****************************************************************************************\n')
    output_text_file.write(
        '*****************************************************************************************\n')
    # let the user know how many total expressions passed and failed, written to output file
    output_text_file.write(f'{pass_count} out of {expr_dec_count - 1} total non-blank lines were successfully converted '
                           f'to postfix expressions.\n')
    output_text_file.write(f'{fail_count} out of {expr_dec_count - 1} total non-blank lines failed to convert to postfix '
                           f'expressions.\n')
    output_text_file.write(
        '*****************************************************************************************\n')
    output_text_file.write(
        '*****************************************************************************************\n')
    output_text_file.write(
        '*****************************************************************************************\n')
    output_text_file.close()

    # print a footer for UI aesthetics
    print('*****************************************************************************************')
    print('*****************************************************************************************')
    # let the user know how many total expressions passed and failed, written to command-prompt
    print(f'{pass_count} out of {expr_dec_count - 1} total read prefix expressions were successfully converted to '
          f'postfix expressions.')
    print(f'{fail_count} out of {expr_dec_count - 1} total read prefix expressions failed to convert to postfix '
          f'expressions.')
    print('*****************************************************************************************')
    print('*****************************************************************************************')
    print('*****************************************************************************************')

