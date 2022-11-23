def find_max_key(data: dict) -> int:
    """
    Return the maximum key in a dictionary.
    Args:
        data (dict): A dictionary of values
    Returns:
        int: The maximum key in the dictionary.
    """
    count = 0
    for i in data:
        for j in i.keys():
            if type(j) == int and j > count:
                count = j

    return count
    
data = [
    {'name ': 'John', 'job': 'Developer', 50: 'age'},
    {'name ': 'Mary', 'job': 'Developer', 5.0: 'age'},
    {'name ': 'Bary', 'job': 'Student', 60: 'age'},
    {'name ': 'Golib', 'job': 'Snayper', 50: 'age'},
]
print(find_max_key(data))
