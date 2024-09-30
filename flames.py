def remove_common_letters(name1, name2):
    name1 = list(name1)
    name2 = list(name2)
    for letter in name1[:]:
        if letter in name2:
            name1.remove(letter)
            name2.remove(letter)
    return len(name1) + len(name2)

def flames_game(count):
    result = ['Friends', 'Love', 'Affection', 'Marriage', 'Enemy', 'Siblings']
    while len(result) > 1:
        split_index = (count % len(result)) - 1
        if split_index >= 0:
            result = result[split_index+1:] + result[:split_index]
        else:
            result = result[:len(result)-1]
    return result[0]
name1 = input("Enter first person name: ").lower().replace(" ", "")
name2 = input("Enter second person name: ").lower().replace(" ", "")
remaining_count = remove_common_letters(name1, name2)
relationship = flames_game(remaining_count)
print("The relationship is:", relationship)
