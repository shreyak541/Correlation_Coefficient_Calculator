def correlation_coefficient(x, y):
    n = len(x)
    sum_x = sum(x)
    sum_y = sum(y)
    sum_xy = sum([x[i] * y[i] for i in range(n)])
    sum_x2 = sum([x[i] ** 2 for i in range(n)])
    sum_y2 = sum([y[i] ** 2 for i in range(n)])

    numerator = n * sum_xy - sum_x * sum_y
    denominator = ((n * sum_x2 - sum_x ** 2) * (n * sum_y2 - sum_y ** 2)) ** 0.5

    if denominator == 0:
        return None  # Avoid division by zero
    return numerator / denominator

print("             Correlation Coefficient Calculator             ")
print("------------------------------------------------------------")

try:
    n = int(input("\nEnter the number of data points: "))
    if n < 2:
        print("Need at least 2 points to calculate correlation.")
        exit()
except ValueError:
    print("Invalid input. Please enter a positive integer.")
    exit()

x = []
y = []

print("\nEnter the data points:")
for i in range(n):
    try:
        xi = float(input(f"x[{i+1}]: "))
        yi = float(input(f"y[{i+1}]: "))
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        exit()
    x.append(xi)
    y.append(yi)

r = correlation_coefficient(x, y)

if r is None:
    print("\nCannot compute correlation (division by zero).")
else:
    print(f"\nCorrelation Coefficient (r) = {r:.4f}")
