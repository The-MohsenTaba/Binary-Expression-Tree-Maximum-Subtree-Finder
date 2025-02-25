# Binary Expression Tree Maximum Subtree Finder
This project is a Python program designed to find the subtree with the maximum value in a binary expression tree. The binary expression tree consists of numbers and operators  for addition (+) and for subtraction(-). The goal is to find the subtree whose sum of values is the maximum possible.
# How to Run
**To run this project, follow these steps:**

**1.Python:** Ensure that Python is installed on your system. This project has been tested with Python 3.

**2.Code:** Save the project code in a Python file, for example, binary_tree.py.

**3.Execution:** Run the Python file:
```
python binary_tree.py
```
# Code Explanation
### Tree Structure
The binary expression tree is defined as a string where numbers and operators are separated by spaces. For example:
```
tree = "5 2 -1 + + 21 1 -3 + -1 + + + *"
```
In this string, * indicates the end of the tree.

### Algorithm
**1.String Parsing:** The tree string is converted into a list, and its elements are processed.

**2.Finding the Maximum Subtree:**

- The subtree function recursively examines the left and right subtrees.

- The sum of values for each subtree is calculated and compared with the current maximum value.

- If the sum of a new subtree is greater than the current maximum, the maximum value and its corresponding path are updated.

**3.Output:** The program prints the maximum value and its corresponding path.

### Example Output
For the example tree provided, the program output will be:
```
maximum subtree is :  24
the path is :  10
```
This output indicates that the subtree with the maximum value has a sum of 24, and its path is 10.


## Contribution
If you would like to contribute to this project, please create an Issue or submit a Pull Request. Any suggestions or improvements are welcome.