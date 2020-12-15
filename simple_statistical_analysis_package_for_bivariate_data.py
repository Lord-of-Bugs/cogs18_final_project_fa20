import numpy as np
import re
import string
import supporting_functions as sf

        
def student_t_tests():
   
    """This is a function designed to handle all three types of student's t-tests, including the single-sample
    t-test, independent samples t-test, and dependent samples t-test. Users can call on this function and are
    prompted to input specific type of t-test parameters as the function executes, instead of having to 
    explicitly specify input parameters all at once. Hence, no input parameter is needed for this function.
    
    Parameter:
    ---------
    None
    
    Returns:
    -------
    A string containing the calculated t-statistic for the corresponding t-test that the user sepcified.
    """

    # Setting up a global variable. Prompts the user to select their intended type of t-test operation.    
    t_type = input('Which type of t-test are you trying to perform:\n\tA. Single-sample t-test.\n\tB. Independent samples t-test.\n\tC. Dependent samples t-test.\n')
    
    # Performs a single-sample t-test if the user enters scenario A.    
    if t_type == 'A' or t_type == 'a':
        
        # The user is prompted to enter the dataset and the population mean used for the single-sample t-test.        
        data = input('Please paste your single-sample data in the form of a list below:\n')
        
        population_parameter = input('What is the population mean that your data is aiming to estimate?\n')
        
        # Call on the supporting data_cleaning() function to help clean our data.
        cleaned_data = sf.data_cleaning(data)
        
        # After the input dataset is cleaned and ready, the rest is mainly just numerical calculations.        
        degree_freedom = len(cleaned_data) - 1
        
        sample_size = len(cleaned_data)
        
        sample_mean = np.mean(cleaned_data)
        
        sample_variance = np.sum((cleaned_data - sample_mean)**2) / degree_freedom
        
        standard_error = np.sqrt(sample_variance / sample_size)
        
        # In order to avoid any unsupported operations between 'numpy' objects and 'ufunc' operators, such as the '-', 
        # all elements used in the final t-statistic calculation, including the remaining two t-tests, are converted 
        # to floating point values. Using the Try/Except structure in order to filter out zero division error.        
        try:
        
            t_statistic = (float(sample_mean) - float(population_parameter)) / float(standard_error)
            
        except ZeroDivisionError:
            
            raise ZeroDivisionError('t-test is insuccessful since the dataset has a standard error of 0.')
        
        return 'Here is your calculated t_statistic: ' + str(t_statistic)
    
    # Performs an independent-samples t-test is scenarios B is selected.    
    elif t_type == 'B' or t_type == 'b':
        
        # The user is first prompted to provide the two datasets used in an independent samples t-test.        
        data_1 = input('Please paste your first dataset to the independent samples in the form of a list below:\n')
        
        data_2 = input('Please paste your second dataset to the independent samples in the form of a list below:\n')
        
        # Call on the supporting function twice to clean two input datasets.
        cleaned_data_1 = sf.data_cleaning(data_1)
        
        cleaned_data_2 = sf.data_cleaning(data_2)

        # This is a built-in test that checks if the lengths of the two cleaned datasets are equivalent since performing
        # an independent samples t-test requires so. An error would be raised if the assertion fails.        
        try:
            
            assert len(cleaned_data_1) == len(cleaned_data_2)
            
        except:
            
            raise SyntaxError('Two input datasets are of unequivalent lengths. Please terminate the function and try again.') 
            
        # Below are mainly numerical operations performed on the two cleaned datasets to obtain the t-statistic for an
        # independent samples t-test.        
        degree_freedom_1 = len(cleaned_data_1) - 1
        
        degree_freedom_2 = len(cleaned_data_2) - 1
        
        sample_mean_1 = np.mean(cleaned_data_1)
        
        sample_mean_2 = np.mean(cleaned_data_2)
        
        sum_of_squares_1 = np.sum((cleaned_data_1 - sample_mean_1)**2)
        
        sum_of_squares_2 = np.sum((cleaned_data_2 - sample_mean_2)**2)
        
        pooled_variance = (sum_of_squares_1 + sum_of_squares_2) / (degree_freedom_1 + degree_freedom_2)
        
        standard_error = np.sqrt((pooled_variance / len(cleaned_data_1)) + (pooled_variance / len(cleaned_data_2)))
        
        try:
            
            t_statistic = (float(sample_mean_1) - float(sample_mean_2)) / float(standard_error)
            
        except ZeroDivisionError:
            
            raise ZeroDivisionError('t-test is insuccessful since the datasets have a standard error of 0.')
        
        return 'Here is your calculated t_statistic: ' + str(t_statistic)
    
    # Performs a dependent-samples t-test is scenarios C is selected.    
    elif t_type == 'C' or t_type == 'c':
        
        # The user is first prompted to provide the two datasets recorded from pre- and post-treatment conditions.        
        data_1 = input('Please paste your pre-treatment dataset in the form of a list below:\n')
        
        data_2 = input('Please paste your post-treatment dataset in the form of a list below:\n')
        
        # Call on the supporting function twice again to clean the pre- and post-treatment datasets.
        cleaned_data_1 = sf.data_cleaning(data_1)
        
        cleaned_data_2 = sf.data_cleaning(data_2)
        
        # This is a built-in test that checks if the lengths of the two cleaned datasets are equivalent since performing
        # a dependent samples t-test also requires so. An error would be raised if the assertion fails.        
        try:
            
            assert len(cleaned_data_1) == len(cleaned_data_2)
            
        except:
            
            raise SyntaxError('Two input datasets are of unequivalent lengths. Please terminate the function and try again.')
        
        # Below are mainly numerical operations performed on the two cleaned datasets to obtain the t-statistic for a
        # dependent samples t-test.        
        sample_size = len(cleaned_data_1)
        
        degree_freedom = len(cleaned_data_1) - 1
        
        differences = cleaned_data_2 - cleaned_data_1
        
        mean_difference = np.mean(differences)
        
        sum_of_squared_deviations = np.sum((differences - mean_difference)**2)
        
        sample_variance = sum_of_squared_deviations / degree_freedom
        
        standard_error = np.sqrt(sample_variance / sample_size)
        
        try:
        
            t_statistic = float(mean_difference) / float(standard_error)
            
        except ZeroDivisionError:
            
            raise ZeroDivisionError('t-test is insuccessful since the datasets have a standard error of 0.')
        
        return 'Here is your calculated t_statistic: ' + str(t_statistic)
    
    # Finally, if the user provided an entry other than letter "A/a", "B/b", or "C/c", an error would be raised to 
    # alert him/her to enter the selection correctly.  
    else:
        
        raise NameError('You have entered an undefined type of t-test. Please enter only the letter code of the t-test you would like to perform.')


def z_test(population_mean, population_std, sample_mean, sample_size):
    
    """This functions performs a single-sample z-test with the users input values, calculates the 
    z-statistic and returns a conclusion about the calculated z-statistic.
    
    Parameters:
    ----------
    population_mean: int or float
        A numerical value about the mean of a particular measurement that we are interested in 
        with regard to a population.
    population_std: int or float
        The standard deviation of that particular measurement about population.
    sample_mean: int or float
        The mean of the measurement that we take from a sample.
    sample_size: int or float
        The number of participants we recorded for that sample.
        
    Returns:
    -------
    conclusion: str
        A string containing the z-statistic we calculated.
    """

    # This operation gives the standard error of the sample value at a particular sample size.    
    standard_error = population_std / np.sqrt(sample_size)
    
    z_statistic = (sample_mean - population_mean) / standard_error
    
    conclusion = 'The calculated z-statistic is: ' + str(z_statistic)
    
    return conclusion

def linear_regression(dataset_1, dataset_2):
    
    """This function calculates the linear regression line in the slope-intercept form of 
    y = mx + b with the user's two input dataset.
    
    Parameters:
    ----------
    dataset_1: list or np.ndarray
        A list/array of numerical values that are the default independent variables.
    dataset_2: list or np.ndarray
        A list/array of numerical values that are the default dependent variables.
        
    Returns:
    -------
    regression_line: str
        A string containing the formula of the calculated linear regression line.
    """
    
    # First check if the two datasets have the same lengths. It is required to have input data tidied up
    # in this way to perform proper linear regression. If not, the function terminates and raises an error.
    if len(dataset_1) == len(dataset_2):
        
        dataset_1_mean = np.mean(dataset_1)
    
        dataset_2_mean = np.mean(dataset_2)
    
        sum_of_products = np.sum((dataset_1 - dataset_1_mean) * (dataset_2 - dataset_2_mean))
        
        sum_of_squares_1 = np.sum((dataset_1 - dataset_1_mean)**2)
        
        # Caculating the slope of the linear regression line.
        m_val = sum_of_products / sum_of_squares_1
        
        # Calculating the intercept of the linear regression line.
        b_val = dataset_2_mean - m_val * dataset_1_mean
        
        regression_line = print('The line of linear regression for these two datasets is y = %sx + %s' % (m_val, b_val))
        
        return regression_line
    
    else:
        
        raise SyntaxError('The two input datasets must be of equivalent lengths.')
        

def finding_correlation_coefficient_r(dataset_1, dataset_2):
    
    """This functions calculates the Pearson's r for any two provided datasets.
    
    Parameters:
    ----------
    dataset_1: list or np.ndarray
        A series of numerical values.
    dataset_2: list or np.ndarray
        A series of numerical values.
        
    Returns:
    -------
    output: str
        A string explaining the calculated r and its strength of correlation.
    """
    
    # Establishes a dictionary that contains the conventional cutoff magnitudes that determine the strength
    # of given Pearson's r that would be utilized toward the end when determining the strength of our own
    # calculated r.
    r_strength = {'almost non-existent': [0, 0.1],
                  'weak': [0.1, 0.3],
                  'moderate': [0.3, 0.5],
                  'strong': [0.5, 1]
                 }
    
    if len(dataset_1) == len(dataset_2):
    
        mean_1 = np.mean(dataset_1)
    
        mean_2 = np.mean(dataset_2)
    
        std_1 = np.std(dataset_1)
    
        std_2 = np.std(dataset_2)
    
        # Convert all values in dataset 1 into their standard units.
        std_u_1 = (dataset_1 - mean_1)/std_1
    
        # Convert all values in dataset 2 into their standard units.
        std_u_2 = (dataset_2 - mean_2)/std_2
    
        r = np.mean(std_u_1 * std_u_2)
    
        # Comparing the calculated r with the existing thresholds of r in our dictionary to determine the magnitude of 
        # the association between our two datasets.
        for i in r_strength:
        
            r_range = r_strength[i]
        
            if r_range[0] <= r < r_range[1]:
            
                strength = i
            
        output = print("The Pearson's correlation coefficient for this pair of data is %s, indicating a %s association between the two." % (r, strength))
    
        return output 
    
    else:
        
        raise SyntaxError('The two input datasets must be of equivalent lengths.')