import sympy
import sys

def helpargv():
    """help command line
    """
    if len(sys.argv)==5:
        pass
    else:
        print("Usage: python statisticstest.py <sensitivity> <specificity> <real positive> <real negative>")
        sys.exit()

helpargv()
x, y = float(sys.argv[1]), float(sys.argv[2])
a, b = int(sys.argv[3]), int(sys.argv[4])

TP = sympy.Symbol('TP')
TN = sympy.Symbol('TN')
FP = sympy.Symbol('FP')
FN = sympy.Symbol('FN')
AC = sympy.Symbol('AC')

equation1 = TP/(TP + FN) - x
equation2 = TN/(TN + FP) - y
equation3 = TP + FN - a
equation4 = FP + TN - b
equation5 = (TP + TN)/(TP + FP + TN + FN) - AC

print(sympy.solve([equation1, equation2, equation3, equation4, equation5]))