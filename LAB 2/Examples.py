import time
def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

start_time = time.time()
n = 996
ans = factorial(n)
end_time = time.time()

runtime = end_time - start_time

print("Runtime of factorial at", n, "is", runtime, "seconds")