# Read the number of test cases
T = int(input())

# Loop over each test case
for _ in range(T):
    # Read the votes for parties A, B, and C
    X_A, X_B, X_C = map(int, input().split())
    
    # Check for a clear majority
    if X_A > 50:
        print("A")
    elif X_B > 50:
        print("B")
    elif X_C > 50:
        print("C")
    else:
        print("NOTA")# cook your dish here
