import pytest

from solver import Solver

_solver = Solver()

@pytest.fixture
def solver():
    return _solver



def test_5cd_3d3s4d6hJc(solver):
    assert solver.process("omaha-holdem 3d3d4d6hJc Js2dKd5c KsAsTcTs Jh2h3c9c Qc8dAd6c 7dQsAc5d") == "7dQsAc5d Qc8dAd6c KsAsTcTs Js2dKd8c Jh2h3c9c"



def test_5cd_4cKs4h8s7s(solver):
    assert solver.process("texas-holdem 4cKs4h8s7s Ad4s Ac4d As9s KhKd 5d6d") == "Ac4d=Ad4s 5d6d As9s KhKd"

def test_5cd_2h3h4h5d8d(solver):
    assert solver.process("texas-holdem 2h3h4h5d8d 9hJh KdKs") == "KdKs 9hJh"




def test_5cd_7h4s4h8c9h(solver):
    assert solver.process("five-card-draw 7h4s4h8c9h Tc5h6dAc5c Kd9sAs3cQs Ah9d6s2cKh 4c8h2h6c9c") == "4c8h2h6c9c Ah9d6s2cKh Kd9sAs3cQs 7h4s4h8c9h Tc5h6dAc5c"

def test_5cd_5s3s4c2h9d(solver):
    assert solver.process("five-card-draw 5s3s4c2h9d 8dKsTc6c2c 4h6s8hJd5d 5c3cQdTd9s AhQhKcQc2d KhJs9c5h9h 8c3d7h7dTs") == "5s3s4c2h9d 4h6s8hJd5d 5c3cQdTd9s 8dKsTc6c2c 8c3d7h7dTs KhJs9c5h9h AhQhKcQc2d"


