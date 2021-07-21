#conversion.py
#Kordel France
########################################################################################################################
#This file performs all operations in converting mathematical prefix expressions to postfix expressions.
#The function 'prefix_to_postfix_recursive' is the function recursively called to evaluate the prefix expression.
########################################################################################################################

from Lab2.constants import acceptable_chars, acceptable_operators


"""
Flags and global variables used during the conversion of the prefix expression.
"""
fullTree = []
postfix_string = ''
op_flag = False


def format_root_node_as_right(node):
    """
    Takes an array simulating a binary tree formatted with root node on the left and reformats the array as a binary tree
        formatted with the root node on the right.
    :param node: an array acting as a binary tree with the root at the left-most index and one or two leaf nodes.
    :returns [str]: an array acting as a binary tree with the root at the right-most index, and one or two leaf nodes.
    """
    newNode = []
    root = node[0]
    if len(root) > 1:
        root = format_root_node_as_right(node)
    root = root[0]
    # if operator is at the right-most index, tree is already formatted correctly, so return
    if root not in acceptable_operators:
        return node
    leftChild = node[1]
    # tree has both children
    if len(node) > 2:
        rightChild = node[2]
        newNode.append(leftChild[0])
        newNode.append(rightChild[0])
        newNode.append(root[0])
        newNode = [leftChild, rightChild, root]
    # tree has only one child
    else:
        newNode = [leftChild, root]
    return newNode


def print_binary_tree_as_string(tree) -> str:
    """
    Converts an array acting as a binary tree and formats the contents to print out as a single string.
    Essentially converts the binary tree to a readable format.
    :param tree: an array representing a complete binary tree with a root node and leaf nodes.
    :returns str: a string containing all elements of the binary tree, representing the final postfix expression.
    """
    treeString = ''
    # tree has both children
    if len(tree) == 3:
        root = tree[2]
        right = tree[1]
        left = tree[0]
        if len(left) > 1:
            treeString += print_binary_tree_as_string(left)
        else:
            treeString += str(left)
        if len(right) > 1:
            treeString += print_binary_tree_as_string(right)
        else:
            treeString += str(right)
        treeString += str(root)
    # tree has only one child
    elif len(tree) == 2:
        root = tree[1]
        left = tree[0]
        if len(left) > 1:
            treeString += print_binary_tree_as_string(left)
        else:
            treeString += str(left)
        treeString += str(root)
    # only a leaf node is found
    else:
        left = tree[0]
        treeString += str(left)
    return treeString


def prefix_to_postfix_recursive(prefix_expression, illegals):
    """
    Takes an array of characters (a string) representing a prefix expression and builds a binary tree as an array
        to represent the expression. The binary tree is formatted initially as an array so that the root node is at
        index 0, the left child node at index 1, and the right child node at index 2. If the tree has only one node,
        it fills index 1 and index 2 is left blank.
    :param prefix_expression: an array of characters containing the prefix expression to be converted.
    :param illegals: an array of illegal characters within the expression gathered throughout the expression evaluation.
    """
    pe = prefix_expression
    global fullTree
    global postfix_string
    global op_flag
    illegal_chars = illegals
    # make sure that we haven't reached the end of the expression
    # if it is, begin building the binary tree
    if len(pe) > 0:
        t = pe[0]
        # if the character read is an operator, create a root node at index 0
        if t in acceptable_operators:
            root = [str(t)]
            fullTree.append(root)
        # if the character read is an operand, create a leaf node
        elif t in acceptable_chars and t not in acceptable_operators:
            if len(fullTree[len(fullTree) - 1]) == 2:  # add right child
                tree = fullTree[len(fullTree) - 1]
                tree.append(str(t))
                # reformat the node so the right and left children swap indices
                fullTree[len(fullTree) - 1] = format_root_node_as_right(tree)
                # find the appropriate subtree to add to
                if len(fullTree[len(fullTree) - 2]) < 3:
                    rootAndLeft = fullTree[len(fullTree) - 2]
                    right = fullTree[len(fullTree) - 1]
                    rootAndLeft.append(right)
                    if len(rootAndLeft) > 2:
                        fullTree[len(fullTree) - 2] = format_root_node_as_right(rootAndLeft)
                    else:
                        fullTree[len(fullTree) - 2] = rootAndLeft
                    fullTree.remove(fullTree[len(fullTree) - 1])
                    if len(fullTree) == 1:
                        fullTree = fullTree[0]
            elif len(fullTree[len(fullTree) - 1]) == 1:  # add left child
                tree = fullTree[len(fullTree) - 1]
                tree.append(str(t))
                fullTree[len(fullTree) - 1] = tree
            else:
                fullTree.append(str(t))
        else:
            # the character is not an acceptable character, so save it and return it later to the user for feedback
            illegal_chars.append(t)
        # decrement the expression by one character
        pe = pe[1:]
        ################################################################################################################
        # RECURSION CALL
        ################################################################################################################
        prefix_to_postfix_recursive(pe, illegal_chars)
        ################################################################################################################
        ################################################################################################################
    else:
        # reached the end of the expression
        # swap the right and left children in the tree for easier conversion to postfix evaluation
        if len(fullTree) != 1:
            fullTree = format_root_node_as_right(fullTree)
        else:
            fullTree = fullTree[0]
        # the tree is formatted, so convert it to an easier-to-read string
        postfix_string = print_binary_tree_as_string(fullTree)


def prefix_to_postfix(expression) -> [str, bool]:
    """
    Takes a prefix expression as a string and facilitates the recursive call of "prefixToPostfixRecursive" to convert
        the expression to a binary tree and evaluate it. Also resets error flags and global parameters. Finally, the
        function obtains any errors and, if conversion is successful, the final postfix expression and formats these as
        a human readable string that is returned with a boolean value indicating any errors that occured.
    :param expression: an array of characters (a string) representing the prefix expression to be converted to postfix.
    :returns [str, bool]: an array containing:
                        1) a string of the evaluated postfix expresssion and (if applicable) descriptions of errors
                        2) a boolean value indicating whether or not the prefix expression contained any errors
    """
    global postfix_string
    global fullTree
    global op_flag
    postfix_string = ''
    fullTree = []
    illegal_chars = []
    op_flag = False

    # convert the prefix expression
    prefix_to_postfix_recursive(expression, illegal_chars)
    # a bit of defensive programming
    # ensure that each character in the postfix expression is found in the prefix expression
    for i in postfix_string:
        if i not in expression:
            op_flag = True
    # if the length of the expressions are different, there were too many operators/operands
    if len(expression) > len(postfix_string):
        op_flag = True

    # build the message that communicates the postfix expression to the user (if found) and any errors encountered
    if len(illegal_chars) > 0 and op_flag:
        postfix_str = f'The characters {illegal_chars} are illegal in the given prefix string.\n' \
                      f'There are also too many operands or operators in given prefix string.\n' \
                      f'Only alphabetical characters and operands of type {acceptable_operators} are acceptable.'
        return [postfix_str, True]
    elif len(illegal_chars) > 0:
        postfix_str = f'The characters {illegal_chars} are illegal in the given prefix string: {postfix_string}.\n' \
                      f'Only alphabetical characters and operands of type {acceptable_operators} are acceptable.'
        return [postfix_str, True]
    elif op_flag:
        postfix_str = f'There are too many operands or operators in given prefix string.'
        return [postfix_str, True]
    else:
        postfix_str = postfix_string
        return [postfix_str, False]




    