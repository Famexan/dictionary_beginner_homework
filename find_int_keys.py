def find_int_keys(data: dict) -> list:
    """
    Return a list of all keys in a dictionary that are integers.
    Args:
        data (dict): A dictionary of values
    Returns:
        list: A list of all keys in the dictionary that are integers.
    """
    count = []
    for i in data:
        for j in i:
            if type(j) == int:
                count.append(j)
                
    return count      
    
data = [
    {'name ': 'John', 'job': 'Developer', 50: 'age'},
    {'name ': 'Mary', 'job': 'Developer', 5.0: 'age'},
    {'name ': 'Bary', 'job': 'Student', 50: 'age'},
    {'name ': 'Golib', 'job': 'Snayper', 50: 'age'},
]

print(find_int_keys(data))