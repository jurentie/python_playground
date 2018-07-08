# Notes on Python3 #
This page is dedicated to recording small pieces of information learned from
working through the book [Python Playground](https://www.amazon.com/Python-Playground-Projects-Curious-Programmer/dp/1593276044)
written by [Mahesh Venkitachalam](https://in.linkedin.com/in/mkvenkit).  
The following are in no particular order, simply organized by when I discovered them.

* [Main Function](#main-function)
* [Handling arguments](#handling-arguments)
   * [import sys](#import-sys)
* [String Formatting](#string-formatting)
   * [Conversion Operators](#conversion-operators)

## Main Function ##
```python
def main():
	#myCodeHere

if __name__ == "__main__":
	main()
```

## Handling Arguments ##
If trying to allow arguments to be passed after the script call.  
Example: `python3 myProgram.py -arg`
```python
import sys

def main():
	arg1 = sys.argv[1]
```

### import sys ###
** System-specific parameters and functions ** :  
This module provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter. It is always available.

Read more about `sys` [here](https://docs.python.org/2/library/sys.html).

## String Formatting ##
It is possible to format strings in Python with the help of the `%` operator followed by
a conversion operator:
```python
name = "John"
age = 22
print("Hello, my name is %s, and I am %d years old." % (name, age))
```
Output:  
`Hello, my name is John.`

### Conversion Operators: ###
| Conversion | Meaning |
| --- | --- |
| d | Signed integer decimal. |
| i | Signed integer decimal. |
| o | Unsigned octal. |
| u | Unsigned decimal. |
| x | Unsigned hexadecimal (lowercase). |
| X | Unsigned hexadecimal (uppercase). |
| e | Floating point exponential format (lowercase) |
| E | Floating point exponential format (uppercase). |
| f | Floating point decimal format. |
| F | Floating point decimal format. |
| g | Same as `e` if exponent is greater than -4 or less than precision, `f` otherwise. |
| G | Same as `E` if exponent is greater than -4 or less than precision, `F` otherwise. |
| c | Single character (accepts integer or single character string). |
| r | String (converts any python object using `repr()``). |
| s | String (converts any python object using `str()`). |
| % | No argument is converted, results in a `%` character in result. |

Read more about string formatting [here](https://docs.python.org/2.4/lib/typesseq-strings.html).
