"""
EPAS - Emergency Priority Allocation System

This package contains modules for:
- defining emergency requests
- calculating priority for emergency vehicles
- sample data for testing
"""

from .models import EmergencyRequest
from .priority_engine import calculate_priority
from .sample_data import sample_requests

__all__ = ["EmergencyRequest", "calculate_priority", "sample_requests"]