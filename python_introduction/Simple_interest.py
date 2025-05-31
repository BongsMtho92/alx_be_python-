def calculate_simple_interest(principal, rate, time):
    try:
        simple_interest = (principal * rate * time) / 100
        return simple_interest
    except Exception as e:
        print("Error occurred:", e)
        return None

# Example usage
p = 1000
r = 5
t = 2

si = calculate_simple_interest(p, r, t)
if si is not None:
    print(f"Simple Interest: {si}")
