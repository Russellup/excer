def starts_w_consonant(text):
    return text.startswith('b') or text.startswith('c') or text.startswith('d') or text.startswith('f') or text.startswith('g') or text.startswith('j') or text.startswith('k') or text.startswith('l') or text.startswith('m') or text.startswith('n') or text.startswith('p') or text.startswith('q') or text.startswith('q') or text.startswith('s') or text.startswith('t') or text.startswith('v') or text.startswith('x') or text.startswith('z') or text.startswith('h') or text.startswith('r') or text.startswith('w') or text.startswith('y')       

def translate(text):
    if len(text.split()) > 1:
        ret = []
        for word in text.split():
            ret.append(translate(word))
        return ' '.join(ret)    
    if text.startswith('a') or  text.startswith('e') or                      text.startswith('i') or  text.startswith('o') or                      text.startswith('u') or text.startswith('xr') or text.startswith('yt'):
        return text + 'ay' 
    if text.startswith('qu'):
        return text[2:] + 'qu'+ 'ay'
    if starts_w_consonant(text) and text[1:].startswith('qu'):
        return text[3:] + text[0] + 'qu' + 'ay'
    if starts_w_consonant(text):
        prefix = text[0]
        
        for char in text[1:]:
            if char == 'y':
                break
            elif starts_w_consonant(char):
                prefix = prefix + char
            else:
                break
                
                
        print(prefix)     
        return text[len(prefix):] + prefix + 'ay'
        return text
    
    
   
    
    
    
    
        pass        
