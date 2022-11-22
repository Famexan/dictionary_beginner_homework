def count_users_with_age(data:list, age:int) -> int:
    """
    Return the number of users with a given age

    Args:
        data (dict): A dictionary of values
        age (int): The age to search for
    Returns:
        int: The number of users with the given age
    """
    count = 0
    for i in data:
        for k,j in i.items():
            if k == 'age' and j == x:
                count += 1 
    return count
data = [
    {'name ': 'John', 'job': 'Developer', 'age': 50},
    {'name ': 'Mary', 'job': 'Developer', 'age': 50},
    {'name ': 'Bary', 'job': 'Student', 'age': 50},
    {'name ': 'Golib', 'job': 'Snayper', 'age': 60},
]
x = 60

print(count_users_with_age(data,x))
