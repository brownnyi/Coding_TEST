def solution(phone_book):
    phone_book.sort() #문자열을 정리하면 숫자의 크기대로 정렬을 하는 것이 아닌 자리수마다 숫자를 비교하여 정렬
    for i in range(len(phone_book)-1): #len(phone_book) - 1 하는 이유는 phone_book[i+1]을 확인하고 싶을때 phone_book[len(phone_book)]은 오류가 발생하기 때문
        if phone_book[i+1].startswith(phone_book[i]):
            return False
    return True
    