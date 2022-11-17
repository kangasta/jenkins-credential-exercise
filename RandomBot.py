import random

RESULTS = ['PASS', 'FAIL', 'ERROR']

def random_test_result():
    result = random.choice(RESULTS)

    if result == 'PASS':
        return
    elif result == 'FAIL':
        raise RuntimeError()
    elif result == 'ERROR':
        raise KeyboardInterrupt()

if __name__ == '__main__':
    random_test_result()
