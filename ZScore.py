def gate_and(input1, input2):
    """ an AND gate (input1 ^ input2) """
    gate1 = input1 and input2
    return bool(gate1)
                

# Homework 3: Z-Score Python Script (Group Homework)

#################
#  SAMPLE DATA  #
#################
# First data set: a list of positive integers (not a normal distribution)
population1 = [14, 28, 96, 97, 21, 29, 29, 4, 58, 
               42, 25, 97, 49, 33, 75, 53, 14, 53, 
               45, 87, 75, 66, 62, 55, 57, 44, 44, 
               94, 19, 96, 12, 59, 86, 88, 61, 68, 
               37, 64, 19, 46, 68, 98, 19, 54, 65, 
               30, 1, 82, 76, 3]

# Second data set: a list of negative and positive integers (normal distribution)
population2 = [-16, 10, -15, -6, -5, -20, -11, 9, -9,
               -7, 5, -14, 6, -10, -22, -19, 21, 11, 
               -18, -13, -24, -21, 14, 19, 20, 13, 16, 
               8, 4, 3, 18, 22, 17, 7, -12, -3, 
               23, -8, 2, -2, -4, 1, 12, -25, -1,
               15, 0, -23, -17, 24]

# Third data set: a list of positive integers (normal distribution)
population3 = [125, 475, 275, 550, 350, 325, 575, 
               25, 225, 150, 425, 75, 175, 650, 
               600, 625, 675, 250, 100, 0, 375, 
               500, 400, 450, 300, 525, 50, 200]

# Third data set: a list of same integers (not normal distribution)
population4 = [125, 125, 125, 125, 125, 125, 125, 
               125, 125, 125, 125, 125, 125, 125, 
               125, 125, 125, 125, 125, 125, 125, 
               125, 125, 125, 125, 125, 125, 125]

#################
#  FUNCTIONS    #
#################

def mean(data_set):
    """
    This function will return the mean of the data_set(population)
    **Do not change this function**
    """
    return sum(data_set)/len(data_set)

def stdev(data_set, avg):
    """
    This function will return the standard deviation of the data_set(population), given the mean of the data_set (avg)
    **Do not change this function**
    """
    variance = sum([(integer - avg) ** 2 for integer in data_set])/len(data_set)
    # return the square root of the variance calculation 
    return variance ** .5
	
def least(data_set):
    """
    Returns the least value in the data_set(population)
    **Do not change this function**
    """
    return min(data_set)
	
def greatest(data_set):
    """
    Returns the greatest value in the data_set(population)
    **Do not change this function**
    """
    return max(data_set)

# Your grader will use this function to help them verify your code
def test_z_score_function():
    pop1_avg = mean(population1)
    pop1_sd = stdev(population1, pop1_avg)
    
    mean_z_score_p1 = z_score(pop1_avg, pop1_avg, pop1_sd)
    
    pop2_greatest = greatest(population2)
    pop2_avg = mean(population2)
    pop2_sd = stdev(population2, pop2_avg)
    
    greatest_z_score_p2 = z_score(pop2_greatest, pop2_avg, pop2_sd)
    
    print("The z-score of the mean of population1 is", mean_z_score_p1)
    print("The z-score of the greatest value of population2 is", greatest_z_score_p2)
  

###########################################################
# My CODE GOES BELOW THIS BOX.                            #
#                                                         #
# Complete the following z_score function.                #
# I may call the functions above,	                      #
#   but I will not define any others (except for testing) #
# I may use arithmetic operators                          #
#  (i.e., +, -, *, **, /) but not Python Boolean          #
#  (call the provided functions instead)                  #
#                                                         #
# Be sure to include names of the group members that      #
# participated in the group assignment work               #
###########################################################

def z_score(x, mu, sigma):
    """
    x is the population item
    mu is the population mean
    sigma is the population standard deviation
    
    Returns the z-score of x
    """
    
    # Participating group members: Kevin Sun, Erick Moyano, Zachary Van Dyke.
    
    # Calculate the z-score for an item x using the mean of the population and the standard deviation of the population

    # Check if the standard deviation is 0 or not, if it is, raise error.
    if sigma == 0:
        raise ValueError("Error: Standard Deviation can't be 0.")
    
    #If not, calculate by subtracting the value by mean and devide by standard deviation
    z_value = (x - mu) / sigma

    return z_value # Return the calculated z-score result by the z_score function


# We will use this function to help verify our code
def my_test_z_score(population):
    """
    population is the data set which is a list of numbers
    No return value
    This function will print out the mean, stdev of the data set
    It will also print out the z-score of the greatest, the smallest, the mean of the population and their z-score
    """

    pop_avg = mean(population)
    pop_sd = stdev(population, pop_avg)
    pop_greatest = greatest(population) 
    pop_smallest = least(population)
    
    # print out the mean, standard deviation, greatest, and smallest of population data set
    print("The mean of population is", pop_avg)
    print("The standard deviation of population is", pop_sd)
    print("The greatest value of population is", pop_greatest)
    print("The smallest value of population is", pop_smallest)
    print("")

    # test the mean of population
    mean_z_score_p = z_score(pop_avg, pop_avg, pop_sd)  
    print("The z-score of the mean of population is", mean_z_score_p) 

    # test the least value of population
    greatest_z_score_p = z_score(pop_greatest, pop_avg, pop_sd)   
    print("The z-score of the greatest value of population is", greatest_z_score_p)

    # test the smallest value of population1
    smallest_z_score_p = z_score(pop_smallest, pop_avg, pop_sd) 
    print("The z-score of the smallest value of population is", smallest_z_score_p)


# test population1 data set, which is not a normal distribution set
print("=========== Test population1 ===========")
my_test_z_score(population1)

# test population2 data set, which is a normal distribution set
print("=========== Test population2 ===========")
my_test_z_score(population2)

# test population3 data set, which is a normal distribution set
print("=========== Test population3 ===========")
my_test_z_score(population3)

# test population4 data set, which is not a normal distribution set, standard deviation is 0, z-score should error out because we can't divide by 0
print("=========== Test population4 ===========")
my_test_z_score(population4)