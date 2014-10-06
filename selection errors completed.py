#test grading program

test_score = int(input("Please enter your percentage test score out of 100: "))
if test_score > 40 and test_score <= 50:
    print("E grade")
elif test_score > 50 and test_score <= 60:
    print("D grade")
elif test_score > 60 and test_score <= 70:
    print("C grade")
elif test_score > 70 and test_score <= 80:
    print("B grade")
elif test_score > 80 and test_score <= 90:
    print("A grade")
elif test_score > 90:
    print("You got the highest grade, well done")
else:
    print("you have failed")
