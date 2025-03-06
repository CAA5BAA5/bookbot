def sort_on(dict):
    return dict["count"]

def nr_of_words(text):
    return len(text.split())
 
def char_count(text):
    return_dict = {}
    for char in text:
        if char == " ":
            continue
        char = char.lower()
        if char in return_dict:
            return_dict[char] +=1
        else:
            return_dict[char] = 1  
    return return_dict

def sort_list(dictionary):
    return_list = []
    for key in dictionary:
        return_list.append({"character":key, "count": dictionary[key]})

    return_list.sort(key=sort_on, reverse=True)
    return return_list

