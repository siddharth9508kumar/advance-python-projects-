#50. WAP to print Pythagorean Triplets  
def pythagorean_triplets(n):
    triplets = []
    for a in range(1, n + 1):
        for b in range(a, n + 1):
            c = (a**2 + b**2)**0.5
            if c.is_integer() and c <= n:
                triplets.append((a, b, int(c)))
    return triplets
limit = int(input("Enter the limit for Pythagorean triplets: "))
triplets = pythagorean_triplets(limit)
print(f"Pythagorean triplets up to {limit}: {triplets}")
