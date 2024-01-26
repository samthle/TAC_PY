import numpy as np

def read_matrices(file_path):
    with open(file_path, 'r') as file:
        n, m = map(int, file.readline().split())
        matrices = [np.array([list(map(int, file.readline().split())) for _ in range(m)]) for _ in range(n)]
    return n, matrices

def calculate_max_det_matrices(n, matrices):
    max_det = -1
    max_pair = None
    for i in range(n):
        for j in range(i + 1, n):
            det_ij = np.linalg.det(np.dot(matrices[i], matrices[j]))
            if det_ij > max_det:
                max_det = det_ij
                max_pair = (i, j)
    return max_pair

def calculate_code_matrix(matrices, max_pair):
    result_matrix = np.dot(matrices[max_pair[0]], matrices[max_pair[1]])

    if np.linalg.det(matrices[max_pair[0]]) > np.linalg.det(matrices[max_pair[1]]):
        return np.linalg.inv(result_matrix)
    else:
        return np.linalg.inv(np.dot(matrices[max_pair[1]], matrices[max_pair[0]]))

def main():
    file_path = 'my_file.txt'
    n, matrices = read_matrices(file_path)
    
    max_pair = calculate_max_det_matrices(n, matrices)
    code_matrix = calculate_code_matrix(matrices, max_pair)

    for row in code_matrix:
        print(' '.join(f'{val:.3f}' for val in row))

if __name__ == "__main__":
    main()
