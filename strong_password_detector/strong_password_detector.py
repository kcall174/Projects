#! python3
#! strong_pw_detector.py - detects if a password is strong 

import re
import sys


def check_pw_strength(password):
    """
    Determines if the argument satisfies the requirements of a strong
    password (uppercase, lowercase, digit, special character, and length >= 8)
    :param str password: password to evaluate
    :return: bool indicating whether or not the password is strong
    """
    pw_regex = re.compile(r'''
        ^(?=.*?[A-Z])                   # at least 1 capital letter
        (?=.*?[a-z])                    # at least 1 lower case letter
        (?=.*?[0-9])                    # at least 1 digit
        (?=.*?[#?!@$%^&*()\-_=+./\\])   # at least 1 special character
        .{8,}$                          # at least 8 characters long
    ''', re.VERBOSE)

    if pw_regex.search(password):
        return True
    return False


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('Usage: python strong_pw_detector.py [password] - determines if password is strong')
        exit()

    if check_pw_strength(password=str(sys.argv[1])):
        print('The tested password is strong!')
    else:
        print('The tested password is not strong!'
              '\nA strong password satisfies all of the following requirements:'
              '\n\tcontains at least one lowercase character'
              '\n\tcontains at least one uppercase character'
              '\n\tcontains at least one digit'
              '\n\tcontains at least one special character'
              '\n\tis at least 8 digits in length')
