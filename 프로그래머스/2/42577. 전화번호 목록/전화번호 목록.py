from typing import List

def solution(phone_book: List[str]) -> bool:
    phone_hash = {}
    
    for number in phone_book:
        phone_hash[number] = True
    
    for number in phone_book:
        temp = ""
        for char in number[:-1]:
            temp += char
            if temp in phone_hash:
                return False
        
    return True
