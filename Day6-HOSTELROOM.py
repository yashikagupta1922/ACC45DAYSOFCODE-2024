def max_people_in_room(test_cases):
    results = []
    for case in test_cases:
        N, X, A = case
        current_people = X
        max_people = X
        
        for change in A:
            current_people += change
            if current_people > max_people:
                max_people = current_people
                
        results.append(max_people)
        
    return results

# Input processing
T = int(input())
test_cases = []

for _ in range(T):
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    test_cases.append((N, X, A))

# Getting results
results = max_people_in_room(test_cases)

# Output results
for result in results:
    print(result)
