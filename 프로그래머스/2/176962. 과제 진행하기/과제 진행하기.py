def solution(plans):
    plans = sorted(map(lambda x: [x[0], int(x[1][:2]) * 60 + int(x[1][3:]), int(x[2])], plans), key=lambda x: x[1])
    answer = []
    stack = []
    
    for i in range(len(plans) - 1):
        remaining_time = 0
        
        subject, time, duration = plans[i]
        next_subject, next_time, next_duration = plans[i + 1]
        
        if time + duration <= next_time:
            answer.append(subject)
            remaining_time += next_time - (time + duration)
            
            while remaining_time > 0 and stack:
                if stack[-1][1] > remaining_time:
                    stack[-1][1] -= remaining_time 
                    break
                else:
                    remaining_time -= stack[-1][1]
                    answer.append(stack.pop()[0])
        else:
            stack.append([subject, duration - (next_time - time)])
            
    answer.append(plans[-1][0])
                
    while stack:
        answer.append(stack.pop()[0])
            
    return answer
