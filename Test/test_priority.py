import unittest
from epas.models import EmergencyRequest
from epas.priority_engine import calculate_priority

class TestPriorityEngine(unittest.TestCase):

    def test_full_priority(self):
        req = EmergencyRequest(5, 5, 10.0, False)
        self.assertEqual(calculate_priority(req), "FULL PRIORITY (Green Corridor)")

    def test_partial_priority(self):
        req = EmergencyRequest(3, 3, 4.0, False)
        self.assertEqual(calculate_priority(req), "PARTIAL PRIORITY (Signal Support)")

    def test_low_priority(self):
        req = EmergencyRequest(1, 1, 2.0, True)
        self.assertEqual(calculate_priority(req), "LOW PRIORITY (Monitor Only)")

if __name__ == "__main__":
    unittest.main()