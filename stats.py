def word_count(text):
    return len(text.split()) 

#function to take text and return number of times each character appears
def char_count(text):
    count = {}
    lowercase_text = text.lower() 
    for char in lowercase_text:
        if char not in count:
            count[char] = 1
        else:
            count[char] += 1
    return count

#returns char_count as sorted list of dictionaries
def sort_on(dict):
    return dict["num"]

def char_dict_to_list(char_count):
    result = []
    for char, count in char_count.items():
        result.append({"char": char, "num": count})
    result.sort(reverse=True, key=sort_on)
    return result