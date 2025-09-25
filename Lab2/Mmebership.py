import time
import random

# Generate 1 million integers
N = 1_000_000
data = list(range(N))

# Create a list and a set from the same data
data_list = data
data_set = set(data)

# Pick some random values to test membership
to_find = [random.randint(0, N-1) for _ in range(10_000)]  # 10k lookups


print("=== Membership Test in List vs Set ===")

# Test membership in list (O(n) on average)
start = time.time()
for x in to_find:
    _ = x in data_list
end = time.time()
print(f"List membership: {end - start:.4f} sec")

# Test membership in set (O(1) on average, uses hashing)
start = time.time()
for x in to_find:
    _ = x in data_set
end = time.time()
print(f"Set membership:  {end - start:.4f} sec")


print("\n=== Methodology & Complexity Explanation ===")
print("""
List:
- Implemented as a dynamic array.
- Membership check (x in list) scans elements one by one.
- Time complexity: O(n).

Set:
- Implemented as a hash table.
- Membership check (x in set) uses hash(x) to directly locate bucket.
- Time complexity: O(1) on average, O(n) in worst-case with hash collisions.
""")
