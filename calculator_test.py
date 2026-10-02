import allure
from calculator import add, sub
@allure.title("verify Addition")
@allure.description("verify that two numbers are added correctly.")
def test_add():
    assert add(2,3)==5
    
@allure.title("verify subtraction")
@allure.description("verify that two numbers are subtracted correctly.")
    
def test_sub():
    assert sub(5,4)==1
    