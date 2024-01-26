import numpy as np

file_path = 'my_file.txt' 
with open(file_path, 'r') as file:
    n, m = map(int, file.readline().split())
    matrices = [np.array([list(map(int, file.readline().split())) for _ in range(m)]) for _ in range(n)]

max_det = -1
max_pair = None
for i in range(n):
    for j in range(i+1, n):
        det_ij = np.linalg.det(np.dot(matrices[i], matrices[j]))
        if det_ij > max_det:
            max_det = det_ij
            max_pair = (i, j)

result_matrix = np.dot(matrices[max_pair[0]], matrices[max_pair[1]])

if np.linalg.det(matrices[max_pair[0]]) > np.linalg.det(matrices[max_pair[1]]):
    code_matrix = np.linalg.inv(result_matrix)
else:
    code_matrix = np.linalg.inv(np.dot(matrices[max_pair[1]], matrices[max_pair[0]]))

for row in code_matrix:
    print(' '.join(f'{val:.3f}' for val in row))
