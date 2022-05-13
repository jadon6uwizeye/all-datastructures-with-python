
def arrange(sentence):
    # Write your code here
    
    splitted_sentence = sentence.split(' ')
    splitted_sentence.sort(key=len)
    return_sentence = ""
    
    for i in range(len(splitted_sentence)):
        if not i == 0:
            return_sentence += " "
        
        return_sentence += splitted_sentence[i]
            
        if return_sentence.endswith("."):
            return_sentence = return_sentence[:-1]

        if(i==(len(splitted_sentence)-1)):
            return_sentence+="."
        
    return (return_sentence.capitalize())