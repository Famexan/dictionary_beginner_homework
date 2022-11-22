def find_length_of_values(data: dict) -> int:
    """
    Return the sum of the length of all values in a dictionary.
    Args:
        data (dict): A dictionary of values
    Returns:
        int: The sum of the length of all values in the dictionary.
    """
    count = 0
    for i in data:
        for j in i.values():
            count += len(str(j))
    return count
data = [
    {'name ': 'John', 'job': 'Developer', 'age': 50},
    {'name ': 'Mary', 'job': 'Developer', 'age': 30},
    {'name ': 'Bary', 'job': 'Student', 'age': 50},
    {'name ': 'Golib', 'job': 'Snayper', 'age': 60},
]
print(find_length_of_values(data))
