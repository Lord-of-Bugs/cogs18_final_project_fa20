import string
import numpy as np
import re
        
        
def is_numeric(input_val):
    
    """Checks if a given input value is numeric.
    
    Parameter:
    ---------
    int_val: ideally an integer or float, but can be objects of any type.
    
    Returns:
    -------
    True, if int_val can be converted to a float.
    False, if the above operation is negative.
    """
    
    # First tries to convert the input value to a floating point value. If the operation goes through, return "True".
    
    try:
    
        float(input_val)
        
        return True
    
    # If the operation fails, return "False". The input then is not numeric.
    
    except ValueError:
        
        return False
    

def data_cleaning(data):
    
    """This function cleans the input dataset by removing all unnecessary punctuations and separators, and splitting
    the dataset down into individual numerical entry components.
    
    Parameter:
    ---------
    data: str only (a stringed list/array of values since inputs are accepted from an Python "input" operation.)
        A list of data points that is to be cleaned.
        
    Returns:
    -------
    cleaned_data: np.ndarray
        An array of numerical data points free of any unnecessary or inappropriate punctuation or separator, much like
        a single list of comma-separated variables.
    """
    
    # Setting up a global variable that include all punctuations, except comma, that are used as value separators.
    separators_to_remove = string.punctuation.replace('.', ' ')
    
    # Pre-define an empty array to store the cleaned data. 
    cleaned_data = np.array([])
    
    # Pre-define an empty string for storing separators that exist within the input dataset.  
    existing_separators = ''
    
    # The input dataset is first to be cleaned by removing all punctuations that are used as separation characters 
    # and keeping the numerical values. The cleaned dataset is then assigned to a new variable that is used in later
    # steps that involve actual calculation.
    try:
            
        # If a separator exists both within the global separator variable and within the data itself, it is appended 
        # to the collection of existing separators, which would later be used to split the data string into valid 
        # numerical pieces all at once.            
        for i in separators_to_remove:
                
            if i in data:
                    
                existing_separators = existing_separators + i
                                       
            else:
                    
                continue
        
        # Split the input data at all identifiable and existing punctuations.
        splitted_data = re.split('|'.join(existing_separators), data)
            
        # In this new list of splitted data entries, check if the element is numeric and store those that are numeric 
        # into our array for cleaned data.            
        for j in splitted_data:
                
            if is_numeric(j) == True:
                        
                cleaned_data = np.append(cleaned_data, float(j))
                    
            else:
                   
                cleaned_data = cleaned_data
        
        return cleaned_data
            
    except: 
            
        # If there exists any character or undetected separator in the input dataset such that we cannot convert it 
        # to a floating point numerical value, a 'Value Error' would be raised to alert the user.
        raise ValueError('Invalid or unsupported non-numeirc input. Please check your input then try again.')