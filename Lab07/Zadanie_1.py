import numpy as np
import time

def fileIntoMatrix(path):
    with open(path, 'r') as file:
        content = file.read()

    rows = content.split('\n')[:-1]
    size = len(rows)
    matrix = np.zeros((size, size), dtype = np.dtype('U1'))

    for i in range(size):
        for j in range(size):
            matrix[i][j] = rows[i][j]

    return matrix

def native(matrix, pattern):
    n = len(matrix)
    m = len(pattern)
    cords = []
    for i in range(n-m+1):
        for s in range(n-m+1):
            if pattern[0] == matrix[i][s] and pattern[1] == matrix[i][s+1] and pattern[2] == matrix[i][s+2]:
                if pattern[1] == matrix[i+1][s] and pattern[2] == matrix[i+2][s]:
                    cords.append((i, s))

    return cords

def KarpRabin(matrix, pattern):
    size = len(matrix)
    base = 16
    patternHash = sum(ord(c) * (base ** (len(pattern) - i - 1)) for i, c in enumerate(pattern))
    cords = []

    for i in range(size - len(pattern) + 1):
        row = matrix[i]
        rowHash = sum(ord(c) * (base ** (len(pattern) - j - 1)) for j, c in enumerate(row[:len(pattern)]))

        if rowHash == patternHash:
            if row[j] == pattern[0] and row[j+1] == pattern[1] and row[j+2] == pattern[2]:
                windowCol = [matrix[i + k][j] for k in range(len(pattern))]
                windowHashCol = sum(ord(c) * (base ** (len(pattern) - k - 1)) for k, c in enumerate(windowCol))

                if windowHashCol == patternHash:
                    if matrix[i][j] == pattern[0] and matrix[i+1][j] == pattern[1] and matrix[i+2][j] == pattern[2]:
                        cords.append((i, j))

        for j in range(1, size - len(pattern) + 1):
            rowHash = (rowHash - (ord(row[j - 1]) * (base ** (len(pattern) - 1)))) * base + ord(row[j + len(pattern) - 1])

            if rowHash == patternHash:
                if row[j] == pattern[0] and row[j+1] == pattern[1] and row[j+2] == pattern[2]:
                    windowCol = [matrix[i + k][j] for k in range(len(pattern))]
                    windowHashCol = sum(ord(c) * (base ** (len(pattern) - k - 1)) for k, c in enumerate(windowCol))

                    if windowHashCol == patternHash:
                        if matrix[i][j] == pattern[0] and matrix[i+1][j] == pattern[1] and matrix[i+2][j] == pattern[2]:
                            cords.append((i, j))

    return cords


def checkKarpRabinTime(matrix, p):
    stime = time.time()
    cords = KarpRabin(matrix, p)
    etime = time.time()
    print(f"Karp Rabin alg time: {etime - stime}")
    print(f"Number of occurrences: {len(cords)}")
    return

def checkNativeTime(matrix, p):
    stime = time.time()
    cords = native(matrix, p)
    etime = time.time()
    print(f"Native alg time: {etime - stime}")
    print(f"Number of occurrences: {len(cords)}")
    return

file1 = 'patterns/1000_pattern.txt'
file2 = 'patterns/2000_pattern.txt'
file3 = 'patterns/3000_pattern.txt'
file4 = 'patterns/4000_pattern.txt'
file5 = 'patterns/5000_pattern.txt'
file8 = 'patterns/8000_pattern.txt'

matrix = fileIntoMatrix(file8)
checkKarpRabinTime(matrix, 'ABC')
checkNativeTime(matrix, 'ABC')