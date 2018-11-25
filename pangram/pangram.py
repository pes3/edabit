def is_pangram(sentence):
    #convert input string into lower case
    x = sentence.lower()
    #lis of al unique characters present in the sentence
    y = set(x)

    #ord(ch) returns ascii value of characfter

    a = [ch for ch in y if ord(ch) in range(ord('a'),ord('z')+1)]

    if len(a) == 26:
        return True
    else:
        return False
                                            
    
