import string

ALPHABET = string.ascii_uppercase
alphabet_dict = {letter: i for i, letter in enumerate(ALPHABET)}

def solution(name):
    name_length = len(name)
    total_moves = 0
    min_cursor_moves = name_length - 1  

    for i, letter in enumerate(name):
        forward_steps = alphabet_dict[letter]
        backward_steps = 26 - forward_steps
        total_moves += min(forward_steps, backward_steps)

        next_index = i + 1
        while next_index < name_length and name[next_index] == "A":
            next_index += 1

        option1 = i * 2 + (name_length - next_index)
        option2 = (name_length - next_index) * 2 + i
        option3 = min_cursor_moves  

        min_cursor_moves = min(option1, option2, option3)

    return total_moves + min_cursor_moves
