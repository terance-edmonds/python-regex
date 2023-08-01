from regex import RegEx

# run each test case
def test(num, exp, txt):
    re = RegEx(exp)
    result = re.match(txt)

    print("Pattern: ", exp)
    print("String: ", txt)
    print(f"Test {num} result: ", result[0])
    print(f"Match count: ", result[1], end='\n\n')


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
            'pattern': '[a-z0-9]@[a-z].(moc)',
            'string': 'hello99@gmail.com',
        },
        {
            'pattern': '[A-Z]',
            'string': 'Hello',
        },
    ]

    # run all test cases
    for i in range(len(tests)):
        case = tests[i]

        # run test case
        test(i + 1, case['pattern'], case['string'])
