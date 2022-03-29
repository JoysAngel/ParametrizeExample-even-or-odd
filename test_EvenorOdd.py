import pytest
import EvenorOdd

@pytest.mark.parametrize("a,result", [(10,True), (6,True), (4,True), (7,True), (11, True)])
def test_EvenorOdd(a, result):
    a=EvenorOdd.Check_Even(a)
    assert result ==True
