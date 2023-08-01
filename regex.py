# is the character a starting character of a set
def is_start_set(char):
    return char == '[' or char == '('

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
    if(len(txt) == 0 or len(txt) - 1 == pos):
        if(len(txt) - 1 == pos):
            return [True, pos - 1]
        else:
            return [True, pos]

    # if string contains lowercase letters
    if('a-z' in exp):
        if(txt[pos] >= 'a' and txt[pos] <= 'z'):
            return match_range(exp, txt, pos + 1)
        
    # if string contains uppercase letters
    if('A-Z' in exp):
        if(txt[pos] >= 'A' and txt[pos] <= 'Z'):
            return match_range(exp, txt, pos + 1)
    
    # if string contains integers
    if('0-9' in exp):
        if(txt[pos] >= '0' and txt[pos] <= '9'):
            return match_range(exp, txt, pos + 1)
    
    return [False, pos]

# match options set
def match_set(exp, txt, pos = 0, end = 0):
    if(end == len(txt)):
        return [True, end]

    arr = exp.replace('(', '').replace(')', '').split('|')
    char = txt[end]

    
    if any(char in s for s in arr):
        [matched, end] =  match_set(exp, txt, pos, end + 1)
        
        if(matched):
            for item in arr:
                if(item == txt[pos:end]):
                    [matched, txt_pos] = match_exp(item, txt[pos:end], 0, 0)
                    
                    if (matched):
                        return [True, end]
                    else:
                        return [False, pos + txt_pos]
    
    return [False, pos]


# find match of the expression in the text
def match_exp(exp, txt, txt_pos = 0, exp_pos = 0):
    # if expression is empty - we have checked all
    if (len(exp) == 0):
        return [True, txt_pos]
    
    # if match set of characters
    if(is_start_set(exp[exp_pos])):
        [set_exp, exp_pos] = extract_set(exp[exp_pos], exp)
        
        if(exp[0] == '['):
            [matched, txt_pos] = match_range(set_exp, txt, txt_pos)

            if(matched):
                return [True, txt_pos]
            
        elif(exp[0] == '('):
            [matched, txt_pos] = match_set(set_exp, txt, txt_pos, txt_pos)

            if(matched):
                return [True, txt_pos]

    # if character matches
    if(len(exp) > exp_pos and len(txt) > txt_pos):
        if (exp[exp_pos] == txt[txt_pos]):
            [matched, txt_pos] = match_exp(exp[(exp_pos + 1):], txt, txt_pos + 1)
            
            if(matched):
                return [True, txt_pos]

    # if nothing matches
    return [False, txt_pos]

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
            [matched, txt_pos] = match_exp(exp, txt, txt_pos)
            
            if (matched):
                matched_count += 1
            
            elif(is_start_set(exp[0])):
                break
            
            txt_pos += 1

    # if the matched count is greater than zero
    if (matched_count > 0):
        return [True, matched_count]

    return [False, 0]


class RegEx:
    def __init__(self, pattern):
        self.pattern = pattern

    def match(self, text):
        return init_match(self.pattern, text)
