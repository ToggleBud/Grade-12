import re
def q1():
    def allowed_char(string):
        charRe = re.compile(r'[^a-zA-Z0-9]')
        string = charRe.search(string)
        return not bool(string)

    print(allowed_char("ABCabc123"))
    print(allowed_char("&*%^$#@!>>?"))

def q2():
    def string_match(string):
        patterns = "ab*"
        if re.search(patterns, string):
            return "Found a Match"
        else:
            return "Not a Match"
    
    print(string_match("ac"))
    print(string_match("abc"))
    print(string_match("abbc"))

def q3():
    def string_match(string):
        patterns = "ab+"
        if re.search(patterns, string):
            return "Found a Match"
        else:
            return "Not a Match"
    
    print(string_match("ac"))
    print(string_match("abc"))
    print(string_match("abbc"))

def q4():
    def string_match(string):
        patterns = "ab?"
        if re.search(patterns, string):
            return "Found a Match"
        else:
            return "Not a Match"
    
    print(string_match("ac"))
    print(string_match("abc"))
    print(string_match("abbc"))

def q5():
    def string_match(string):
        patterns = "ab{3}"
        if re.search(patterns, string):
            return "Found a Match"
        else:
            return "Not a Match"
    
    print(string_match("ac"))
    print(string_match("abc"))
    print(string_match("abbbc"))

q5()