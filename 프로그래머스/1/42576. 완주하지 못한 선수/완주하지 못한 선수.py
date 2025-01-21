def solution(participant, completion):
    participant_counter = {}
    
    for p in participant:
        participant_counter[p] = participant_counter.get(p, 0) + 1
        
    for c in completion:
        participant_counter[c] -= 1
    
    for name, count in participant_counter.items():
        if count > 0:
            return name
