import re



def tokenize_rule(text):                         
    if type(text) is not str:
        RuntimeError("Parameter not a string")
    elif len(text) == 0:
        return []
    
    token_list = list()
    is_in_quote = False
    is_escaped = False
    parentheses_count = 0
    is_in_token = False
    
    i_start = 0
    i = 0
    while True:
        c = text[i]
        
        if c == "t":
            1
            
        if c == '"':
            if is_in_quote and not is_escaped:
                is_in_quote = False
                is_in_token = False
                token_list.append(text[i_start:i + 1])
                i_start = i + 1
            elif is_in_quote and is_escaped:
                is_escaped = False
            elif not is_in_quote:
                is_in_quote = True
                is_in_token = True
            else:
                raise RuntimeError("Invalid parse:\nChar:{}\nText:\n{}".format(i, text))
        elif c.isspace():
            if is_in_token and not is_in_quote:
                is_in_token = False
                token_list.append(text[i_start:i])
                i_start = i + 1
            elif is_in_token and is_in_quote:
                pass
            elif not is_in_token:
                i_start = i + 1
            else:
                raise RuntimeError("Invalid parse:\nChar:{}\nText:\n{}".format(i, text))
        elif c == "(":
            if is_in_quote:
                pass
            elif not is_in_quote:
                if is_in_token:
                    token_list.append(text[i_start:i])
                    is_in_token = False
                elif not is_in_token:
                    pass
                
                #find ending parantheses
                parentheses_count = 1
                i_start_par = i
                in_quote_par = False
                is_escaped_par = False
                 
                for ii in range(i + 1,len(text)):
                    c = text[ii]
                    if c == ")" and not in_quote_par:
                        parentheses_count -= 1
                        if parentheses_count == 0:
                            token = tokenize_rule(text[i_start_par + 1:ii]) # Recursive tokenize contents of parantheses
                            token_list.append("(")
                            token_list.append(token)
                            token_list.append(")")
                            i_start = ii + 1
                            i = ii
                            break
                    elif c == ")" and in_quote_par:
                        pass
                    elif c == "(" and not in_quote_par:
                        parentheses_count += 1
                    elif c == "(" and in_quote_par:
                        pass                            
                    elif c == '"' and not in_quote_par:
                        in_quote_par = True
                    elif c == '"' and in_quote_par and not is_escaped_par:
                        in_quote_par = False   
                    elif c == '"' and in_quote_par and is_escaped_par:
                        pass
                    elif c == "\\" and in_quote_par and not is_escaped_par:
                        is_escaped = True
                    elif c == "\\" and in_quote_par and is_escaped_par:
                        pass
                    elif c == "\\" and not in_quote_par:
                        pass
                     
                    
                    if ii + 1 == len(text):
                        raise RuntimeError("Invalid parse (no end parantheses) :\nChar:{}\nText:\n{}".format(i_start_par, text))
                
                i_start = ii + 1
                
        elif not is_in_quote and (c.isalnum() or c == "_" or c == ":"):
            is_in_token = True
        elif not is_in_quote: 
            if is_in_token:
                token_list.append(text[i_start:i])
                is_in_token = False
            token_list.append(text[i:i+1])
            i_start = i + 1
        else:
            pass
        
        i += 1
        if i == len(text):
            break 
    
    return token_list
    
def tokenize_code(text):
    char_is_a_token_list = [";"]
    char_is_paranthesisish = ["[","{","("]
    char_is_paranthesisish_end = ["]","}",")"]
         
    if type(text) is not str:
        RuntimeError("Parameter not a string")
    elif len(text) == 0:
        return []
    
    token_list = list()
    is_in_quote = False
    is_escaped = False
    parentheses_count = 0
    is_in_token = False
    
    i_start = 0
    i = 0
    while True:
        c = text[i]
        
        if c == "t":
            1
            
        if c == '"':
            if is_in_quote and not is_escaped:
                is_in_quote = False
                token_list.append(text[i_start:i + 1])
                i_start = i + 1
            elif is_in_quote and is_escaped:
                is_escaped = False
            elif not is_in_quote:
                is_in_quote = True
                is_in_token = True
            else:
                raise RuntimeError("Invalid parse:\nChar:{}\nText:\n{}".format(i, text))
        elif c.isspace():
            if is_in_token and not is_in_quote:
                is_in_token = False
                token_list.append(text[i_start:i])
                i_start = i + 1
            elif is_in_token and is_in_quote:
                pass
            elif not is_in_token:
                i_start = i + 1
            else:
                raise RuntimeError("Invalid parse:\nChar:{}\nText:\n{}".format(i, text))
        elif c in char_is_paranthesisish:
            if is_in_quote:
                pass
            elif not is_in_quote:
                if is_in_token:
                    token_list.append(text[i_start:i])
                    is_in_token = False
                elif not is_in_token:
                    pass
                
                #find ending parantheses
                parentheses_count = 1
                i_start_par = i
                in_quote_par = False
                is_escaped_par = False
                
                matching_end = ""
                if c == "(":
                    matching_end = ")"
                elif c == "[":
                    matching_end = "]"
                elif c == "{":
                    matching_end = "}"
                 
                for ii in range(i + 1,len(text)):
                    cc = text[ii]
                    if cc == matching_end and not in_quote_par:
                        parentheses_count -= 1
                        if parentheses_count == 0:
                            token = tokenize_code(text[i_start_par + 1:ii]) # Recursive tokenize contents of parantheses
                            token_list.append(c)
                            token_list.append(token)
                            token_list.append(matching_end)
                            i_start = ii + 1
                            i = ii
                            break
                    elif cc in char_is_paranthesisish_end and in_quote_par:
                        pass
                    elif cc == c and not in_quote_par:
                        parentheses_count += 1
                    elif c == cc and in_quote_par:
                        pass                            
                    elif cc == '"' and not in_quote_par:
                        in_quote_par = True
                    elif cc == '"' and in_quote_par and not is_escaped_par:
                        in_quote_par = False   
                    elif cc == '"' and in_quote_par and is_escaped_par:
                        pass
                    elif cc == "\\" and in_quote_par and not is_escaped_par:
                        is_escaped = True
                    elif cc == "\\" and in_quote_par and is_escaped_par:
                        pass
                    elif cc == "\\" and not in_quote_par:
                        pass
                     
                    
                    if ii + 1 == len(text):
                        raise RuntimeError("Invalid parse (no end parantheses) :\nChar:{}\nText:\n{}".format(i_start_par, text))
                    
                i_start = ii + 1
        elif not is_in_quote and (c.isalnum() or c == "_"):
            is_in_token = True
        elif not is_in_quote: 
            if is_in_token:
                token_list.append(text[i_start:i])
                is_in_token = False
            token_list.append(text[i:i+1])
            i_start = i + 1
        else:
            pass
        
        i += 1
        if i == len(text):
            break 
    
    return token_list

class rule():

    def __init__(self, text):
        self.text = text

        self.__parse_text()
        
    def text_is_this_rule(self, text, dict_of_rules):
        i = 0
        
        #Split text into tokens

        for rulepoint in self.rulepoint_list:
            rule_token_list = tokenize_rule(rulepoint)
            code_token_list = tokenize_code(text)
            1 
            
    def __match_code_and_rule_tokens(self, code_tokens, rule_tokens, dict_of_rules):
        for token in rule_tokens:
        
        
        
        
    
    def __parse_text(self):
        m = re.search(r"\(([\w\:]*)\)\:", self.text)
        if(m is None):
            raise RuntimeError("Couln't parse short-name: {}".format(self.text))
        
        self.short_name = m[1]
        
        m = re.search(r"^([\w\-]*) \([^\)]*\):", self.text)
        if(m is None):
            raise RuntimeError("Couln't parse long-name: {}".format(self.text))
        self.long_name = m[1]
        
        self.rulepoint_list = list()
        for line in self.text.splitlines():
            m = re.match(r"    (.*)", line)            
            if m is None:
                continue
            elif m[0].isspace():
                continue
            self.rulepoint_list.append(m[1])
        
    def to_string(self):
        s_out = ""
        s_out += "Short name: {} \n".format(self.short_name)
        s_out += "Long name: {} \n".format(self.long_name)
        for rule in self.rulepoint_list:
            s_out += "Rulepoint: {}\n".format(rule)
        s_out += "Backing text: \n{}\n".format(self.text)
        
        return s_out
        
        
        
def main():
    from blang.lang_rules.rule_parser import rule_parser
    
    p = rule_parser()
    p.load(r"C:\repos\blang\blang\blang\bläng spec.txt")
    dict_of_rules = p.parse()
    
    s = 'function-expression (e::fnc):\n    name "(" p::l ")"\n    name "(" ")"\n'
    r = rule(s)
    print(r.to_string())  
    print(r.text_is_this_rule("int var = 3;\nif(var == 3) exit();\n",dict_of_rules))
        
if __name__ == "__main__":
    main()