import time
import random
import threading





# Simple matrix multiplication function
def simple_matrix_multiply(A, B):
    

    """   Multiply two matrices A and B together.

    Args:
        A: a 2D list of size MxN
        B: a 2D list of size NxP

    Returns:
        a 2D list of size MxP
    """

    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    return result

# Helper function to generate a random matrix of given size
def generate_matrix(rows, cols):
    
    return [[random.randint(1, 10) for _ in range(cols)] for _ in range(rows)]

# Measure performance of simple matrix multiplication
def measure_simple_multiplication(A, B):
    start_time = time.time()
    result = simple_matrix_multiply(A, B)
    end_time = time.time()
    print(f"Time taken for simple matrix multiplication: {end_time - start_time:.6f} seconds")
    return result










# Multithreaded matrix multiplication (one thread per row)
def multithreaded_matrix_multiply_row(A, B):

    """
    Multiply two matrices A and B together using multiple threads.

    Each thread is responsible for computing one row of the result matrix.

    Args:
        A: a 2D list of size MxN
        B: a 2D list of size NxP

    Returns:
        a 2D list of size MxP
    """


    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]

    def multiply_row(i):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]

    threads = []
    for i in range(len(A)):
        thread = threading.Thread(target=multiply_row, args=(i,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return result

# Measure performance of multithreaded matrix multiplication
def measure_multithreaded_multiplication_row(A, B):
    start_time = time.time()
    result = multithreaded_matrix_multiply_row(A, B)
    end_time = time.time()
    print(f"Time taken for multithreaded matrix multiplication (row-based): {end_time - start_time:.6f} seconds")
    return result







# Multithreaded matrix multiplication (one thread per cell)
def multithreaded_matrix_multiply_cell(A, B):
    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]

    def multiply_cell(i, j):
        result[i][j] = sum(A[i][k] * B[k][j] for k in range(len(B)))

    threads = []
    for i in range(len(A)):
        for j in range(len(B[0])):
            thread = threading.Thread(target=multiply_cell, args=(i, j))
            threads.append(thread)
            thread.start()

    for thread in threads:
        thread.join()

    return result

# Measure performance of multithreaded matrix multiplication (cell-based)
def measure_multithreaded_multiplication_cell(A, B):
    
    start_time = time.time()
    result = multithreaded_matrix_multiply_cell(A, B)
    end_time = time.time()
    print(f"Time taken for multithreaded matrix multiplication (cell-based): {end_time - start_time:.6f} seconds")
    return result


if __name__ == "__main__":
    # Define matrix dimensions
    rows_A, cols_A = 100, 100
    rows_B, cols_B = 100, 100

    # Generate random matrices A and B
    A = generate_matrix(rows_A, cols_A)
    B = generate_matrix(rows_B, cols_B)

    print("Measuring simple matrix multiplication performance:")
    simple_result = measure_simple_multiplication(A, B)

    print("\nMeasuring multithreaded matrix multiplication (one thread per row):")
    multithreaded_row_result = measure_multithreaded_multiplication_row(A, B)

    print("\nMeasuring multithreaded matrix multiplication (one thread per cell):")
    multithreaded_cell_result = measure_multithreaded_multiplication_cell(A, B)
