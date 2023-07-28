# Simple Regular Expression Algorithm (RegEx)

This is a simple regular expression (RegEx) algorithm developed with python.

It supports:
  - Literals ( abc )
  - Ranges ( [a-z], [A-Z], [0-9], [a-zA-Z0-9] )
  - Alternatives ( a|b )
  - Matching in the middle of a string

## Usage

To run a string against the regular expression, create a new object of `RegEx` with the expression or the pattern as its parameter.

Then by using the `match` function of the `RegEx` object pass the string as its parameter and get the result.

```python
    from regex import RegEx

    re = RegEx("[a-z0-9]@[a-z].(com|net|org)")
    
    result = re.match("hello99@gmail.com") 
    # output: True

    result = re.match("Hello99@gmail.com") 
    # output: False

    result = re.match("Hello99@gmailcom") 
    # output: False
```

There are some test cases in `tests.py` file. Use the below code to run the test cases.

```bash
python tests.py
```