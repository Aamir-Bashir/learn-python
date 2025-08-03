s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}

# Union of two sets
s_union = s1.union(s2)  # or s1 | s2
print("Union:", s_union)  # Output: {1, 2, 3, 4, 5, 6, 7, 8}

# Intersection of two sets
s_intersection = s1.intersection(s2)  # or s1 & s2
print("Intersection:", s_intersection)  # Output: {4, 5}