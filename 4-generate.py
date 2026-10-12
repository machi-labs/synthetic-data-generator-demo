"""Demo: generate synthetic customers and orders. All data is fictitious."""
import csv
import random
import sys
from datetime import date, timedelta

FIRST = ["Ana", "Luis", "Marta", "Pablo", "Lucia", "Jorge", "Elena", "Pau"]
LAST = ["Garcia", "Lopez", "Martin", "Sanz", "Vidal", "Ferrer", "Soler", "Gil"]
CITIES = ["Valencia", "Madrid", "Sevilla", "Bilbao", "Murcia"]


def main(n, customers_path, orders_path, seed=42):
    rnd = random.Random(seed)
    with open(customers_path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["id", "name", "email", "city"])
        for i in range(1, n + 1):
            first, last = rnd.choice(FIRST), rnd.choice(LAST)
            w.writerow([i, f"{first} {last}", f"{first}.{last}{i}@example.com".lower(), rnd.choice(CITIES)])
    start = date(2026, 1, 1)
    with open(orders_path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["order_id", "customer_id", "date", "amount_eur"])
        for o in range(1, n * 3 + 1):
            w.writerow([o, rnd.randint(1, n), start + timedelta(days=rnd.randint(0, 270)),
                        round(rnd.uniform(5, 250), 2)])


if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit("usage: python generate.py N customers.csv orders.csv")
    main(int(sys.argv[1]), sys.argv[2], sys.argv[3])
