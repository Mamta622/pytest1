import csv
import matplotlib.pyplot as plt

# Read metrics history from CSV
timestamps = []
passed = []
failed = []
skipped = []
pass_rates = []

with open("metrics_history.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        timestamps.append(row["Timestamp"])
        passed.append(int(row["Passed"]))
        failed.append(int(row["Failed"]))
        skipped.append(int(row["Skipped"]))
        pass_rates.append(float(row["Pass Rate"]))


# -----------------------------
# Chart 1: Latest Test Run
# -----------------------------

latest_passed = passed[-1]
latest_failed = failed[-1]
latest_skipped = skipped[-1]

labels = ["Passed", "Failed", "Skipped"]
values = [latest_passed, latest_failed, latest_skipped]

plt.figure(figsize=(8, 5))
plt.bar(labels, values)
plt.title("Latest Test Run")
plt.xlabel("Test Result")
plt.ylabel("Number of Tests")
plt.tight_layout()


# -----------------------------
# Chart 2: Pass Rate Over Time
# -----------------------------

plt.figure(figsize=(8, 5))
plt.plot(range(1, len(pass_rates) + 1), pass_rates, marker="o")
plt.title("Pass Rate Over Time")
plt.xlabel("Test Run")
plt.ylabel("Pass Rate (%)")
plt.ylim(0, 100)
plt.tight_layout()

# Save the dashboard
plt.savefig("dashboard.png")

print("Dashboard created successfully: dashboard.png")