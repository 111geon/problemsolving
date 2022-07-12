def solution(phone_book):
    answer = True
    phone_book.sort(key=lambda x: len(x))
    lengths = {len(i) for i in phone_book}
    
    for length in lengths:
        check = set()
        for phone_number in phone_book:
            if phone_number[:length] in check: return False
            if len(phone_number) == length: check.add(phone_number[:length])
        
    return answer

# def solution(phoneBook):
#     phoneBook = sorted(phoneBook)

#     for p1, p2 in zip(phoneBook, phoneBook[1:]):
#         if p2.startswith(p1):
#             return False
#     return True
