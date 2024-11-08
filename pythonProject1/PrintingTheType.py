import sys, re, traceback
from unittest import TestCase

words = ["Good Morning", "Good Afternoon", "Good Evening"]


class Evaluate(TestCase):

    def test_exercise(self):
        import words

        def check_variable():
            """For code that contains variables which should be checked if they exist and what they contain"""

            # Check if user has declared the variable
            if not hasattr(check_variable, "words"):
                sys.exit("You must define a 'words' variable")

            # Check if variable is assigned the correct value
            if type(check_variable.words) != list:
                sys.exit('"words" variable should have a list assigned. \nCheck the type of the value.')

        def check_list_content():
            # Check the content of the list
            # Check if the person list contains exactly 4 elements
            if len(check_variable.words) != 3:
                sys.exit("The 'person' list must contain exactly 4 elements.")

            # Check if each element in person corresponds to the respective variables
            if type(check_variable.words[0]) != str:
                sys.exit("The first item in the 'words' list should be the a string.")

            if type(check_variable.words[1]) != str:
                sys.exit("The second item in the 'words' list should be the a string.")

            if type(check_variable.words[2]) != str:
                sys.exit("The third item in the 'words' list should be the a string.")

        def check_print_missing():
            """For code that contain print function to check if the user forgots to include print() """
            with open("exercise.py") as file:
                content = file.read()
            check1 = re.compile("print\(.*").search(content)  # check number print(15.56)

            if check1:
                pass
            else:
                sys.exit(
                    "It looks like there is no print() function in your code. \nDid you forget to print out the output?")

        def check_print_output():
            """Compare expected output with user's printed output for exercises that require print()"""

            try:
                user_output = sys.stdout.getvalue().strip("\n")
            except Exception:
                extracted_exception = traceback.format_exc().splitlines()[3:]
                traceback_string = ''
                for line in extracted_exception:
                    if r'/eval/' in line:
                        line = line.replace(r'/eval/', '')
                    traceback_string = traceback_string + line + "\n"
                sys.exit(traceback_string)

            correct_output = str(check_variable.words)

            message_output = f"Your code generates this output:\n→{user_output}←\nBut, the expected output is:\n→{correct_output}←"

            if correct_output == user_output:
                pass
            else:
                sys.exit(
                    message_output + "\n\nPlease compare the two outputs carefully. \nSometimes you might be missing a space in your text, \nor using a lowercase letter instead of uppercase or vice-versa.")

        check_variable()
        check_list_content()
        check_print_missing()
        check_print_output()