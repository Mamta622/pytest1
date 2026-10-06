import xml.etree.ElementTree as ET
import csv
import os
from datetime import datetime

# Read the results.xml file
tree = ET.parse("results.xml")
root = tree.getroot()

# Find the testsuite section
testsuite = root.find(".//testsuite")

# Get test counts
total = int(testsuite.attrib.get("tests", 0))
failed = int(testsuite.attrib.get("failures", 0)) + int(testsuite.attrib.get("errors", 0))
skipped = int(testsuite.attrib.get("skipped", 0))

# Calculate executed and passed tests
executed = total - skipped
passed = executed - failed

# Calculate metrics
pass_rate = (passed / executed) * 100 if executed else 0
execution_progress = (executed / total) * 100 if total else 0

# Display results
print("===== Test Metrics =====")
print(f"Total Tests: {total}")
print(f"Executed Tests: {executed}")
print(f"Passed Tests: {passed}")
print(f"Failed Tests: {failed}")
print(f"Skipped Tests: {skipped}")
print(f"Pass Rate: {pass_rate:.2f}%")
print(f"Execution Progress: {execution_progress:.2f}%")

# Save metrics to CSV history
history_file = "metrics_history.csv"

file_exists = os.path.exists(history_file)

with open(history_file, "a", newline="") as file:
    writer = csv.writer(file)

    # Add column headings only for the first run
    if not file_exists:
        writer.writerow([
            "Timestamp",
            "Total",
            "Executed",
            "Passed",
            "Failed",
            "Skipped",
            "Pass Rate",
            "Execution Progress"
        ])

    # Add current test run
    writer.writerow([
        datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        total,
        executed,
        passed,
        failed,
        skipped,
        round(pass_rate, 2),
        round(execution_progress, 2)
    ])

print(f"\nMetrics saved to {history_file}")