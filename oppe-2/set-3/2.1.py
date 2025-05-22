def get_words_after_the(sentence: str) -> list:
    
    words = sentence.split()
    words_after_the = []
    for i in range(1, len(words)):
       if words[i - 1].lower() == 'the':
           words_after_the.append(words[i])
    return words_after_the
    
