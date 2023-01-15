import pytest


@pytest.mark.parametrize("ingredient,sum", [(5, 10), (2, 4)])
def test_addition(ingredient, sum):                  #name must start with test_
    assert ingredient + ingredient == sum, "The expected sum is " + str(ingredient+ingredient) #text after comma  is displayed
                                                                                                # only when test fail
