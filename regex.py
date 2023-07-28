# is the character a starting character of a set
def is_start_set(char):
    return char == '[' or char == '('

def match_star(start, end, txt):
    # for i in range(len(txt) + 1):
    return [True]


# extract set from expression
def extract_set(char, exp):
    end_pos = 0

    if(char == '['):
        end_pos = exp.find(']') + 1
    if(char == '('):
        end_pos = exp.find(')') + 1
    
    return [exp[:end_pos], end_pos]

# match range set
def match_range(exp, txt, pos = 0):
    if(len(txt) == 0):
        return [True, pos]
    
    # if string contains lowercase letters
    if('a-z' in exp):
        if(txt[0] >= 'a' and txt[0] <= 'z'):
            return match_range(exp, txt[1:], pos + 1)
        
    # if string contains uppercase letters
    if('A-Z' in exp):
        if(txt[0] >= 'A' and txt[0] <= 'Z'):
            return match_range(exp, txt[1:], pos + 1)
    
    # if string contains integers
    if('0-9' in exp):
        if(txt[0] >= '0' and txt[0] <= '9'):
            return match_range(exp, txt[1:], pos + 1)
    
    return [False, pos]

# match options set
def match_set(exp, txt):
    arr = exp.replace('(', '').replace(')', '').split('|')
    return [txt in arr]


# find match of the expression in the text
def match_exp(exp, txt, txt_pos = 0, exp_pos = 0):
    # if expression is empty - we have checked all
    if (len(exp) == 0):
        return True
    
    # if match set of characters
    if(is_start_set(exp[exp_pos])):
        [set_exp, exp_pos] = extract_set(exp[exp_pos], exp)
        
        if(exp[0] == '['):
            [matched, txt_pos] = match_range(set_exp, txt)
            if(matched):
                return True
            
        elif(exp[0] == '('):
            [matched] = match_set(set_exp, txt)
            if(matched):
                return True
    
    # if character matches
    if(len(exp) > exp_pos and len(txt) > txt_pos):
        if (exp[exp_pos] == txt[txt_pos]):
            if(match_exp(exp[(exp_pos + 1):], txt[(txt_pos + 1):])):
                return True

    # if nothing matches
    return False

# if valid to start
def is_valid(exp, txt):
    return len(txt) >= len(exp) or is_start_set(exp[0])

# start matching
def init_match(exp, txt):
    matched_count = 0
    txt_pos = 0

    # if the text length is greater than the expression proceed
    if (is_valid(exp, txt)):
        # naive algorithm
        while txt_pos < len(txt) - 1:
            if (match_exp(exp, txt[txt_pos:])):
                matched_count += 1
            
            elif(is_start_set(exp[0])):
                break
            
            txt_pos += 1

    # if the matched count is greater than zero
    if (matched_count > 0):
        return True

    return False


class RegEx:
    def __init__(self, pattern):
        self.pattern = pattern

    def match(self, text):
        return init_match(self.pattern, text)
