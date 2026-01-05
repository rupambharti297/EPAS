from epas.sample_data import sample_requests
from epas.priority_engine import calculate_priority

print("EPAS – Emergency Priority Allocation System\n")

results = []

# Step 1: Show all requests
for i, request in enumerate(sample_requests, start=1):
    priority, reason = calculate_priority(request)
    results.append((request, priority, reason))

    print(f"Request {i}")
    print(f"Input → Urgency:{request.urgency_level}, Traffic:{request.traffic_density}, Distance:{request.distance_km}km")
    print(f"Recommended Priority → {priority}")
    print(f"Reason → {reason}\n")

# Step 2: Authority chooses which request to act on
choice = int(input("Select request number to act on (1/2/3/4/5): "))

selected = results[choice - 1]

# Step 3: Approve or override
decision = input("Approve recommendation? (y/n): ")

if decision.lower() == "y":
    print(f"\nRequest {choice} approved with priority: {selected[1]}")
else:
    print(f"\nRequest {choice} overridden by authority")

print("\nDecision cycle complete.")