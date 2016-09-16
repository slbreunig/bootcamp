import pytest

import l35_tdd

#goes hand-in-hand with design specification
#first write design specification, then run test so that it fails
#use pytest.raises(RuntimeError, "statement") to do this

#write test function
def test_n_neg():
#if assert statement is true, nothing happens
#if false, throws an AssertionError
    assert l35_tdd.n_neg('E') == 1
    assert l35_tdd.n_neg('D') == 1
    assert l35_tdd.n_neg('') == 0
    assert l35_tdd.n_neg('ACKLWTTAE') == 1
    assert l35_tdd.n_neg('DEDEDDEE') == 8
    assert l35_tdd.n_neg('acklwttae') == 1
    #only allow natural amino acids

    pytest.raises(RuntimeError, "l35_tdd.n_neg('Z')")

    return None
