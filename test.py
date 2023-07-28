from regex import RegEx

# run each test case
def test(num, exp, txt):
    re = RegEx(exp)
    print("Pattern: ", exp)
    print("String: ", txt)
    print(f"Test {num} result: ", re.match(txt), end='\n\n')


if __name__ == '__main__':
    # test cases
    tests = [
        {
            'pattern': 'John',
            'string': 'Hello John how are you John?',
        },
        {
            'pattern': '[a-zA-Z0-9]',
            'string': 'Hello77',
        },
        {
            'pattern': '[0-9]',
            'string': 'Hello77',
        },
        {
            'pattern': '[a-z]',
            'string': 'simple',
        },
        {
            'pattern': '[a-z0-9]@[a-z].(com|net|org)',
            'string': 'hello99@gmail.com',
        },
        {
            'pattern': '[A-Z]',
            'string': 'Hello',
        },
    ]
    
    tests_1 = [
        {
            'pattern': '[a-z0-9]@[a-z].(com|net|org)',
            'string': 'hello99@mail.net',
        },
    ]

    # run all test cases
    for i in range(len(tests)):
        case = tests[i]

        # run test case
        test(i + 1, case['pattern'], case['string'])
