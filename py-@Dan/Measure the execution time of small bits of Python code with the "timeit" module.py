import timeit

# The "timeit" module lets you measure the execution
# time of small bits of Python code

# result
# 0-1-2-3-4-5-6-7-8-9-10...-99

print(
    timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
)  # 0.8995874719998938
print(
    timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000)
)  # 0.8709785030000603
print(
    timeit.timeit('"-".join(map(str, range(100)))', number=10000)
)  # 0.8709785030000603
