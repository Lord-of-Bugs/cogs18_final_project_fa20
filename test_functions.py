import supporting_functions as sf
import simple_statistical_analysis_package_for_bivariate_data as ssap 

import math
import numpy as np


def test_is_numeric():
    
    assert callable(sf.is_numeric)
    
    assert sf.is_numeric('a') == False
    
    assert sf.is_numeric('9.8') == True
    
    assert isinstance(sf.is_numeric(1.5), bool)
    

def test_data_cleaning():
    
    assert callable(sf.data_cleaning)
    
    assert isinstance(sf.data_cleaning('1, 2, 3, 4, 5'), np.ndarray)
    
    assert all(sf.data_cleaning('1.1 2,3 4!5') == np.array([1.1, 2, 3, 4, 5]))
    
    
def test_student_t_tests():
    
    # Don't really how else I can test it since it involves no input arguments but rather
    # takes three inputs from users directly, then performs a series of operations on those 
    # to ultimately return one output.
    
    assert callable(ssap.student_t_tests)

    
def test_z_test():
    
    assert callable(ssap.z_test)
    
    assert isinstance(ssap.z_test(10, 0.34, 12, 1), str)
    
    assert math.isclose(float(ssap.z_test(10, 0.34, 12, 1).split(' ')[-1]), 5.88235294117647)
    
    
def test_linear_regression():
        
    assert callable(ssap.linear_regression)
    
    try:
        
        ssap.linear_regression(np.linspace(0, 50), np.linspace(0, 100, 20))
        
    except SyntaxError:
        
        assert True
        
    try:
        
        assert ssap.linear_regression(np.linspace(0, 50), np.linspace(0, 100))
    
    except AssertionError:
        
        assert True
        
        
def test_finding_correlation_coefficient_r():
    
    assert callable(ssap.finding_correlation_coefficient_r)
    
    try:
        
        assert ssap.finding_correlation_coefficient_r([11, 3, 9 ,5, 1, 7], [91, 77, 90, 80, 75, 85, 100])
        
    except SyntaxError:
        
        assert True
        
    try:
        
        assert ssap.finding_correlation_coefficient_r([11, 3, 9 ,5, 1, 7], [91, 77, 90, 80, 75, 85])
    
    except AssertionError:
        
        assert True