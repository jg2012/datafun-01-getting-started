# ----------------- INSTRUCTOR GENERATED CODE -----------------

# Use this handy logger to document your work automatically

# import setup_logger function from instructor-generated module
from util_logger import setup_logger

# setup the logger using the current file name (a built-in variable)
logger, logname = setup_logger(__file__)

# ----------------- END INSTRUCTOR GENERATED CODE -----------------

# Import from Python Standard Library
import statistics
from functools import reduce

#Variables 
number1 = input("Please choose a number:")
number2 = input("Please choose a second number:")
number3 = input("Please choose one last number:")

int1 =int(number1)
int2 = int(number2)
int3 = int(number3)

sum = sum([int1, int2, int3])
average = statistics.mean([int1, int2, int3])
product = reduce(lambda x, y: x*y, [int1, int2, int3])
min = min(int1, int2, int3)
max = max(int1, int2, int3)

logger.info(f"sum   = {sum}")
logger.info(f"mean   = {average:.2f}")
logger.info(f"product   = {product:.2f}")
logger.info(f"min   = {min}")
logger.info(f"max   = {max}")