from dataclasses import dataclass

@dataclass
class EmergencyRequest:
    urgency_level: int        # 1 (low) to 5 (critical)
    traffic_density: int      # 1 (free) to 5 (jammed)
    distance_km: float
    multiple_emergencies: bool