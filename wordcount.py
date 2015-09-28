def word_count(file_path):
    log_file = open(file_path)
    unique_words = {}
    for line in log_file:
        line = line.strip()
        line = line.replace("--", " ")
        line = line.split(" ")
        
        for word in line:
            word = word.lower()
            word = word.strip()
            word = word.strip("?.,:;!'\"_()-__")
            
            if word in unique_words:
                unique_words[word] += 1
            else:
                unique_words[word] = 1
    return unique_words


print word_count("twain.txt")