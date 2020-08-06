import sys
import os

# This will include algeabra utitlities as a search directory
__from_actual_to_dir__ = ""
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__from_actual_to_dir__),
                                 os.path.pardir)))
