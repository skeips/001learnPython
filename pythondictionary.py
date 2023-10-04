python_definitions = {
    "definition": "/nPython is a general-purpose, high-level programming language. Its design philosophy emphasizes code readability with its notable use of significant whitespace. Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects.",
    "string": "Python string is a sequence of characters. It can be used to represent any type of text, such as names, addresses, or sentences. Strings are immutable, meaning that once they are created, they cannot be changed.",
    "list": "A Python list is a sequence of data types. It is one of the most important data structures in Python, and it can be used to store any type of data, including numbers, strings, booleans, and other lists.",
    "condition": "A Python condition is a statement that evaluates to either True or False. Conditions are used to control the flow of a program, by determining whether or not certain statements should be executed.",
    "function": "A Python function is a block of code that can be reused. Functions can take arguments and return values.",
    "module": "A Python module is a file that contains Python code. Modules can be imported into other Python programs to make use of their functions and other variables.",
}

# Add examples to the Python topics.
python_definitions["string"] += (" Here are some examples of Python strings: \n"
                                  "'Hello, world!' \n"
                                  '''"This is a string." \n'''
                                  "'' \n"
                                  "'''This is a multi-line string.'''")
python_definitions["list"] += (" Here are some examples of Python lists: \n"
                                  "[1, 2, 3, 4, 5] \n"
                                  '''["one", "two", "three"] \n'''
                                  "[] \n"
                                  "[1, 2, 3, [4, 5, 6]]")
python_definitions["function"] += (" Here are some examples of Python functions: \n"
                                  "def greet(): \n"
                                  "    print('Hello, world!') \n"
                                  "greet()\n"
                                  "\n"
                                  "def add_numbers(a, b): \n"
                                  "    return a + b \n"
                                  "result = add_numbers(1, 2) \n"
                                  "print(result)")
python_definitions["module"] += (" Here are some examples of Python modules: \n"
                                  "import math \n"
                                  "print(math.pi) \n"
                                  "\n"
                                  "import random \n"
                                  "print(random.randint(1, 10))")

user_ask = input("Ask me anything about Python: ")
user_ask = user_ask.split(" ")

valid_topics = ["definition", "string", "list", "condition", "function", "module"]

if any(topic in user_ask for topic in valid_topics):
    # Get the topic that the user is asking about.
    topic = next(topic for topic in user_ask if topic in valid_topics)

    # Print the definition of the topic, along with any examples.
    print(python_definitions[topic])
else:
    print("Invalid Input!! Write something like, 'what is string' etc")
