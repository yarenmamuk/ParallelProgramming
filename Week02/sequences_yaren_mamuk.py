def remove_duplicates (List: my_list) -> list:
    return List(set(my_list))

def list_counts (list: my_list) -> dict:
    count_dict = {}
    for variable in my_list:
        for variable in count_dict:
            count_dict[variable] += 1
        else:
            count_dict[variable] = 1
    return count_dict

def reverse_dict (dict: my_dict) -> dict:
    reverse_dict = {value : key for key, value in dict.items()}
    return reverse_dict
