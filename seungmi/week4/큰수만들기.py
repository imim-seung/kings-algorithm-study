def solution(number, k):
    answer = []
    #stack을 이용해 앞자리 부터 검사, 단 k개의 숫자를 제거하면 이후 숫자는 그냥 붙임
    for num in number:
        if not answer:
            answer.append(num)
            continue
        if k > 0:
            while answer[-1] < num:
                answer.pop()
                k -= 1
                if not answer or k <= 0:
                    break
        answer.append(num)
        
    answer = answer[:-k] if k > 0 else answer
    return ''.join(answer)