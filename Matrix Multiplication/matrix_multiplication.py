
# 1. Manual matrix multiplication function
def manual_matrix_multiply(A, B):
    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    return result

# 2. Example matrices
A = [[1, 2, 3],
     [4, 5, 6]]

B = [[7, 8],
     [9, 10],
     [11, 12]]

# 3. Perform manual multiplication
manual_result = manual_matrix_multiply(A, B)
print("Manual Multiplication Result:")
for row in manual_result:
    print(row)

# 4. Use NumPy to verify
import numpy as np
np_A = np.array(A)
np_B = np.array(B)
np_result = np.dot(np_A, np_B)

print("\nNumPy Multiplication Result:")
print(np_result)

# 5. Check if both results are the same
is_same = np.array_equal(np.array(manual_result), np_result)
print("\nResults Match:", is_same)
