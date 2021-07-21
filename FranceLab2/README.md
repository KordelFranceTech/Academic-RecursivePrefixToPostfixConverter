# FranceLab 2 - Kordel K. France

This project was constructed for the Data Structures class, 605.202 section 85, at Johns Hopkins University. The project 
converts mathematical prefix expressions into postfix expressions using recursion. The program was built for educational
purposes only.

The file `conversion.py` contains the recursion calls and recursive function. In this file, the function
`prefix_to_postfix_recursive` is the recursive function.

## Running FranceLab2
1. **Ensure Python 3.7 is installed on your computer.**
2. **Configure a `.txt` file with prefix expressions.** This file will be used as input data. You may name it whatever you 
wish, but ensure this file is located in the `io_files` subdirectory.
3. **Configure a blank `.txt` file.** This file will host the logged output with postfix expressions corresponding to each 
associated prefix expression. You may name it whatever you wish, but ensure this file is located in the `io_files`
subdirectory.
4. **Navigate to the Lab1 directory.** For example, `cd User\Documents\PythonProjects\Lab2`.
Do NOT `cd` into the `Lab2` module.
5. **Run the program as a module: `python -m Lab2 -h`.** This will print the help message.
6. **Run the program as a module (with real inputs): `python -m Lab2 <some_input_file> <some_output_file>`.** For example,
run the program with the command: `python -m Lab2 input.txt output.txt`.
7. **Open output file `output.txt`.** The resultant processed expressions and a duplication of the console output is located here.

**Note: If you do not supply an output file, one will be created for you automatically called 'output.txt' under the 
`io_files` subdirectory. If you put your `input.txt` file in the incorrect location, the program will scan for it and move
it to the correct folder. However, for best results, it is advised that all I/O data be placed in the `io_files`
subdirectory.**

### Lab2 Usage

```commandline
usage: python -m Lab2 input_file output_file

positional arguments:
  in_file     name of input file
  out_file    name of output file

optional arguments:
  -h, --help  show this help message and exit
```

### Project Layout

Here is how the project is structured and organized.

* FranceLab2: `The parent folder of the project. This should be the last subdirectory you navigate to to run the
project.`
    * README.md:
      `A guide on what the project does, how to run the project,`
    * Lab2: 
      `This is the module of the entire program package. It is not a directory. Do not navigate into it.`
      * __init__.py 
        `As the name suggests, this file initializes the program and gives access to the file processing capabilities
        to other programs.`
      * __main__.py 
        `This file governs the command line arguments, processes the I/O files, and begins the general program.`
      * **CharStack.py** 
        `This file defines the specification for a stack containing single-string characters. CharStack is designed to
        act as a string of characters. While the intent is for this stack to only contain characters as elements, Python 
        does not support the 'char' class so single-character strings were used instead. The effect is the same.`
      * **conversion.py**
        `This file contains functions for converting a prefix string to a postfix string. Note that the recursive 
        function used for evaluation is titled 'prefixToPostfixRecursive'.`
      * **file_processing.py**
        `This file contains I/O methods for processing the input and output .txt files you specify in the command line 
        args.`
      * **constants.py**
        `Arrays of constants that specify what characters are allowed are defined here. Specifically, the allowed
        allowed operators and operands allowed for the prefix-to-postfix expression conversion process are specified
        here. Any other character is considered as "illegal" and will throw an error.`

###References
The following items were used as references for the construction of this project. 
1) Almes, Scott. (2021). Stacks Office Hours, JHU Course 605.202 Section 81. Accessed through Blackboard on JHU student account 4 February and 8 February 2021.
2) Almes, Scott. (2021). Stacks Office Hours, JHU Course 605.202 Section 81. Accessed through Blackboard on JHU student account 12 February 2021.
3) Almes, Scott. (2021). Queues and Lists Office Hours, JHU Course 605.202 Section 81. Accessed through Blackboard on JHU student account 19 February 2021.
4) Almes, Scott. (2021). Lab 1 Office Hours, JHU Course 605.202 Section 81. Accessed through Blackboard on JHU student account 25 February 2021.
5) Almes, Scott; et al. (2021). Lab 0 Sample Project, JHU Course 605.202 Section 81. Accessed through Blackboard on JHU student account 26 February 2021. Web. URL: https://blackboard.jhu.edu/bbcswebdav/pid-9469422-dt-content-rid-100642966_2/xid-100642966_2
6) Almes, Scott. (2021). Lab 1 Office Hours, JHU Course 605.202 Section 81. Accessed through Blackboard on JHU student account 1 March 2021.
7) Chlan, Eleanor; et al. (2021). ADT and Complexity Notes, JHU Course 605.202 Section 81. Accessed through Blackboard on JHU student account 28 January – 2 February 2021.
8) Chlan, Eleanor; et al. (2021). ADT and Complexity Notes, JHU Course 605.202 Section 81. Accessed through Blackboard on JHU student account 2 February– 9 February 2021.
9) Chlan, Eleanor. (2021). Stacks Office Hours, JHU Course 605.202 Section 81. Accessed through Blackboard on JHU student account 14 February 2021.
10) Chlan, Eleanor; et al. (2021). ADT and Complexity Notes, JHU Course 605.202 Section 81. Accessed through Blackboard on JHU student account 10 February– 16 February 2021.
11) Chlan, Eleanor; et al. (2021). Queues Notes, JHU Course 605.202 Section 81. Accessed through Blackboard on JHU student account 17 February – 18 February 2021.
12) Chlan, Eleanor; et al. (2021). Lists Notes, JHU Course 605.202 Section 81. Accessed through Blackboard on JHU student account 17 February – 18 February 2021.
13) Chlan, Eleanor; et al. (2021). Queues and Lists Office Hours, JHU Course 605.202 Section 81. Accessed through Blackboard on JHU student account 21 February 2021.
14) Chlan, Eleanor; et al. (2021). Queues and Lists Office Hours, JHU Course 605.202 Section 81. Accessed through Blackboard on JHU student account 28 February 2021.
15) Miller, B. N., & Ranum, D. L. (2014). Problem solving with algorithms and data structures using Python (2nd ed.). Decorah, IA: Brad Miller, David Ranum.
16) Chlan, Eleanor; et al. (2021). Graphs Notes, JHU Course 605.202 Section 81. Accessed through Blackboard on JHU student account 10 March– 15 March 2021.
17) Chlan, Eleanor; et al. (2021). List Notes, JHU Course 605.202 Section 81. Accessed through Blackboard on JHU student account 10 March– 15 March 2021.
18) Almes, Scott. (2021). Homework 7 Office Hours, JHU Course 605.202 Section 81. Accessed through Blackboard on JHU student account 11 March 2021.
19) Chlan, Eleanor. (2021). Homework 7 Office Hours, JHU Course 605.202 Section 81. Accessed through Blackboard on JHU student account 14 March 2021.
20) Almes, Scott. (2021). Lab 2 Office Hours, JHU Course 605.202 Section 81. Accessed through Blackboard on JHU student account 19 March 2021.
21) Chlan, Eleanor. (2021). Lab 2 Office Hours, JHU Course 605.202 Section 81. Accessed through Blackboard on JHU student account 21 March 2021.