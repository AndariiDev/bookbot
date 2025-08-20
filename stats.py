def get_num_words(text):
    num_words = text.split()
    return len(num_words)
    # print("{len(num_words)} words found in the document")

def get_num_chars(text):
    num_chars = {}
    text = text.lower()
    for i in text:
        if i.isalpha():
            if i in num_chars:
                num_chars[i] += 1
            else:
                num_chars[i] = 1
    return num_chars

def sorted_report(num_chars):
    num_chars.sort()
    print(num_chars)
