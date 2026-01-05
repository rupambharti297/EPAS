def calculate_priority(request):
    score = 0
    reasons = []

    # urgency
    score += request.urgency_level * 3
    reasons.append("High urgency" if request.urgency_level >= 4 else "Moderate urgency")

    # traffic
    score += request.traffic_density * 2
    reasons.append("Heavy traffic" if request.traffic_density >= 4 else "Manageable traffic")

    # distance
    if request.distance_km > 5:
        score += 2
        reasons.append("Long distance to hospital")

    # multiple emergencies
    if request.multiple_emergencies:
        score -= 2
        reasons.append("Multiple emergencies active")

    # decision
    if score >= 18:
        priority = "FULL PRIORITY (Green Corridor)"
    elif score >= 12:
        priority = "PARTIAL PRIORITY (Signal Support)"
    else:
        priority = "LOW PRIORITY (Monitor Only)"

    explanation = ", ".join(reasons)
    return priority, explanation