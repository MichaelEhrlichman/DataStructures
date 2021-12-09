# python3

from collections import namedtuple
import os

Bracket = namedtuple("Bracket", ["ch", "pos"])

def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]

def find_mismatch(text):
    stack = []
    for i, next in enumerate(text):
        if next in "([{":
            stack.append(Bracket(next,i))
        if next in ")]}":
            if not stack:
                return str(i+1)
            top = stack.pop()
            if not are_matching(top.ch,next):
                return str(i+1)
    return 'Success' if stack == [] else str(stack[-1].pos+1)

def main():
    text = input()
    mismatch = find_mismatch(text)
    print(mismatch)

def test_main():
    for i in range(1,55):
        test = '{:02}'.format(i)
        answer = '{:02}.a'.format(i)
        with open('tests/'+test,'r') as tf, open('tests/'+answer,'r') as af:
            teststr = tf.read().strip()
            ansstr = af.read().strip()
            print( find_mismatch(teststr) == ansstr )

if __name__ == "__main__":
    main()
    #test_main()
