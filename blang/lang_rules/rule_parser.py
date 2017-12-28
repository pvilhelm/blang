import re

class rule_parser(object):
    """description of class"""

    def __init__(self):
        self.text = ""
        

    def load(self, path):
        self.text += "# File {}".format(path) + open(path).read()
        
    def parse(self):
        self.text_no_comments = ""
        # Remove comments
        for line in self.text.splitlines(keepends = False):
            if line.isspace():
                continue
            i = 0
            in_quote = False
            escape = False
            for c in line:
                if c == "\"" and not in_quote:
                    in_quote = True
                elif c == "\"" and in_quote and not escape:
                    in_quote = False
                elif c == "\\" and in_quote and not escape:
                    escape = True
                elif c == "#" and not in_quote:
                    break
                elif escape and in_quote:
                    escape = False
                elif escape and not in_quote:
                    raise RuntimeError("Parse error")
                i += 1

            self.text_no_comments += line[0:i] + '\n'

if __name__ == "__main__":
    p = rule_parser()
    p.load(r"C:\Users\fisksoppa\Documents\blang\bläng spec.txt")
    p.parse()
    print(p.text_no_comments)
