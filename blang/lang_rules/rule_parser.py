import re
from blang.lang_rules.rule import rule 

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
        
        #now parse the rules    
        dict_of_rules = {}
        list_of_raw_rules = []
        in_rule = False
        s = ""
        
        for line in self.text_no_comments.splitlines(keepends = True):
            m = re.search(r"^([\w\-]*) \([^\)]*\):", line)
            if (m is not None) and not in_rule:
                in_rule = True
                s = line
            elif (m is not None) and in_rule:
                if len(s) > 0 :
                    list_of_raw_rules.append(s)
                s = line
            elif in_rule:
                m = re.match(r"    (.*)", line)
                if m is None:
                    list_of_raw_rules.append(s)
                    s = ""
                    in_rule = False
                else:
                    s += line
                    
        if len(s) > 0:
            list_of_raw_rules.append(s)
                 
        for raw_rule in list_of_raw_rules:
            r = rule(raw_rule)
            dict_of_rules[r.short_name] = r
            
        return dict_of_rules
            #r = rule(self.text_no_comments)
        

if __name__ == "__main__":
    p = rule_parser()
    p.load(r"C:\repos\blang\blang\blang\bläng spec.txt")
    p.parse()
    
    
