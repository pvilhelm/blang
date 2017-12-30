
import re

def __tokenize_rule(self, text):
                               
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
                                token = self.__tokenize(text[i_start_par + 1:ii]) # Recursive tokenize contents of parantheses
                                token_list.append(token)
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
    
def __tokenize_code(self, text):
    char_is_a_token_list = [";"]
                
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
                                token = self.__tokenize(text[i_start_par + 1:ii]) # Recursive tokenize contents of parantheses
                                token_list.append(token)
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
    def text_is_this_rule(self, text, dict_of_rules):
        i = 0
        
        #Split text into tokens
        
        
        
        for rulepoint in self.rulepoint_list:
            token_list = __tokenize_rule(rulepoint)
            
    
    def __init__(self, text):
        self.text = text

        self.__parse_text()
        
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
    s = 'function-expression (e::fnc):\n    name "(" p::l ")"\n    name "(" ")"\n'
    r = rule(s)
    print(r.to_string())  
    print(r.text_is_this_rule("int var = 3;\nif(var == 3) exit();\n",{}))
        
if __name__ == "__main__":
    main()