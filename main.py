from timeit import default_timer

# ===========================================================
# PROBLEM 15 -- Lattice Paths
# ===========================================================
#
#  Starting in the top left corner of a 2x2 grid, and only
#  being able to move right and down, there are exactly 6 routes
#  to the bottom right corner.
#
#  How many such routes are there through a 20x20 grid?
#
# ===========================================================
# ALGORITHM:
#   It is seen that this is a "choose" problem, whose solution
#   is 40 choose 20, so the number of solutions is equal to
#       40! / [ (40-20)! 20! ]
#       = 40 * 39 * ... * 21 / 20!
#
#
# There are x right steps and x down steps
# the number of total paths is  (x*x) choose 2
#
# For choose 2, it's:
# (x+x)! / ((x+x-2)!*2!)
#
# Example: 2x2 grid
# 4 choose 2
# 4!/(2!*2!) = (4*3*2*1) / (2*1*2*1) = 24/4 = 6
#
# For a 20x20 grid:
# 40 choose 20
#  40*39*...*21 / (20!)
#
# ===========================================================
def problem_15( ):
    # Print Problem Context
    print( "Project Euler 15 -- Lattice Paths" )

    # Set Up Variables
    start_time   =  default_timer( )
    numerator    =  1
    denominator  =  1
    choices      =  20  #down or right
    length       =  20
    width        =  20

    # Numerator (40*39*...*22*21)
    temp  =  length + width
    for x in range( choices ):
        numerator  *=  ( temp - x )

    # Denominator (20!)
    for y in range( 1 , choices + 1 ):
        denominator  *=  y

    # Compute Result
    result  =  numerator / denominator

    # Calculate Execution Time
    end_time = default_timer()
    execution_time = (end_time - start_time) * 1000

    # Display Results
    print( "   Total Paths:        %d" % result )
    print( "   Computation Time:   %.3fms" % execution_time)
    return

if __name__ == '__main__':
    problem_15( )
