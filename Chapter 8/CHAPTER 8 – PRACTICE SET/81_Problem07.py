# 7. Write a python function to remove a given word from a list ad strip it at the same time.
def remove_and_strip(lst, word):
    new_list = []
    for item in lst:
        if not(item == word):
            new_list.append(item.strip(word))
    return new_list


lst = ["apple", " banana ", "mango", " banana ", "grape"]

 
print(remove_and_strip(lst, "ana"))