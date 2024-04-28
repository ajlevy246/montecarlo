"""
Unit and regression test for the montecarlo package.
"""

# Import package, test suite, and other packages as needed
import sys

import pytest

import montecarlo


J = [[(1, 1), (2, 1)], [(0, 1), (2, 1)], [(0, 1), (1, 1)]]
test = montecarlo.IsingHamiltonian(J, [1, 1, 1])

def test_montecarlo_imported():
    """Sample test, will always pass so long as import statement worked."""
    assert "montecarlo" in sys.modules

def test_compute_average_values():
    assert test.compute_average_values(50) == (-0.11528297636533837, -0.05764148818266907, 0.002213033723299384, 0.05762788964949499)
    assert test.compute_average_values(1) == (-1.6935445861227463, -0.846772293061373, 0.5235423995768027, 0.5894320975808381)
    

def test_get_lowest_energy_config():
    assert test.get_lowest_energy_config() == (-2, "001")

    test.mus[0] == 5
    assert test.get_lowest_energy_config() == (-2, "001")