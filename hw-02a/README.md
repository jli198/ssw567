# Week 2 - Assignment 02a

*Note: you should do this assignment (02a) before you attempt assignment (02b)* </br>
</br>
The objective of this assignment is for you to (a) develop a set of tests for an existing triangle classification program, (b) use those tests to find and fix defects in that program, and (c) report on your testing results for the Triangle problem

## Description of assignment

Sometimes you will be given a program that someone else has written, and you will be asked to fix, update and enhance that program.   In this assignment you will start with an existing implementation of the classify triangle program that will be given to you.   You will also be given a starter test program that tests the classify triangle program, but those tests are not complete.

* These are the two files: Triangle.py and TestTriangle.py
  * ***[Triangle.py](Triangle.py)*** is a starter implementation of the triangle classification problem.
  * ***[TestTriangle.py](TestTriangle.py)*** contains a starter set of unittest test cases to test the `classifyTriangle()` function in the file Triangle.py file.

In order to determine if the program is correctly implemented, you will need to update the set of test cases in the test program.  You will need to update the test program until you feel that your tests adequately test all of the conditions.   Then you should run the complete set of tests against the original triangle program to see how correct the triangle program is.    Capture and then report on those results in a formal test report described below.   For this first part you should not make any changes to the classify triangle program.  You should only change the test program. </br>
</br>
Based on the results of your initial tests, you will then update the classify triangle program to fix all defects.  Continue to run the test cases as you fix defects until all of the defects have been fixed.   Run one final execution of the test program and capture and then report on those results in a formal test report described below. </br>
</br>
Note that you should NOT simply replace the logic with your logic from Assignment 1.  Test teams typically don't have the luxury of rewriting code from scratch and instead must fix what's delivered to the test team. </br>
</br>

***[Triangle.py](Triangle.py) contains an implementation of the `classifyTriangle()`*** function with a few bugs.
***[TestTriangle.py](TestTriangle.py) contains the initial set of test cases.***

### Part 0

Create a new folder under your GitHub repository for SSW567 that you have created and shared with the instructor and TA. When creating the new folder, you should include a README file under it. Give your new folder a meaningful name. In our example here we will name our folder for this homework as "hw-02a" but you can name it anything (as long as it makes sense for this assignment). </br>
</br>
Of course, you should have git installed on your laptop, but if you do not then you will need to do that first. You can download git from [here](https://git-scm.com/downloads) </br>
</br>
Next you should upload and commit both of these files, Triangle.py and TestTriangle.py in their original form to the new folder in your GitHub repo. Then any changes you make to these programs will also be committed to the same GitHub repo. </br>
</br>

**Here are the steps to do this:** </br>
</br>

* Copy your two Triangle source files to your local repository folder,
* then add and commit them to git,
* and then push those files up to your repository on GitHub.

a. Copy Triangle.py and TestTriangle.py to the Triangle567 folder. </br>
b. Next you should run these commands to add and commit the changes to your local repository on your laptop:

```bash
git add TestTriangle.py Triangle.py
git commit -m "add triangle code"
```

c. Finally, you should run this command to push the changes to GitHub:

```bash
git push
```

### Part 1

1. Review the [Triangle.py](Triangle.py) file which includes the `classifyTriangle()` function implemented in Python.  
2. Enhance the set of test cases for the Triangle problem that adequately tests the `classifyTriangle()` function to find problems. The test cases will be in a separate test program file called [TestTriangle.py](TestTriangle.py). You should not fix any bugs in Triangle.py at this time, just make changes to TestTriangle.py
3. Run your test set against the classifyTriangle() function by running:

```bash
python -m unittest TestTriangle
```

4. Create a test report in the format specified below.  This report shows the results of testing the initial `classifyTriangle()` implementation.
5. Commit and push your changes to the TestTriangle.py program to GitHub

### Part 2

1. After you've completed part 1 that defines your test set and after running it against the buggy `classifyTriangle()` function, update the logic in `classifytTriangle()` to fix all of the logic bugs you found by code inspection and with your test cases.
2. Run the same test set on your improved `classifyTriangle()` function and create a test report on your improved logic
3. Commit and push your changes to the Triangle.py program to GitHub

Deliverables:

1. Include a written test report in your assignment summary with the results of running your test set against the initial buggy implementation of classifyTriangle in the origianl Triangle.py using  the following format:

Test ID | Input | Expected Results | Actual Result | Pass or Fail
--- | --- | --- | --- | ---
testRightTriangleA | 3,4,5 | Right | InvalidInput | Fail
testRightTriangleB | 5,3,4 | Right | InvalidInput | Fail
testRightTriangleC | 4,5,3 | Right | InvalidInput | Fail
testEquilateralTriangles | 33,33,33 | Equilateral | InvalidInput | Fail
testIsoscelesTriangles | 5,6,6 | Isosceles | InvalidInput | Fail
testScaeleneTriangles | 8,9,10 | Scalene | InvalidInput | Fail
testNotATriangle | 12,57,15 | NotATriangle | InvalidInput | Fail
testInvalidInputA | 43,37,0 | InvalidInput | IvalidInput | Pass
testInvalidInputB | 1,1,305 | InvalidInput | IvalidInput | Pass
testInvalidInputC | 25,50,-1 | InvalidInput | IvalidInput | Pass
testInvalidInputD | 89,76,0.45 | InvalidInput | IvalidInput | Pass

2. Upload a copy of your source code for your improved classifyTriangle  (file named Triangle.py)
3. Upload a copy of your test set.  Your test set should be in a separate file (file named TestTriangle.py)
4. Upload a screen dump or output file of running your test set on the improved classifyTriangle() function
5. Include a written test report in your assignment summary with the results of running your test set against the improved implementation of classifyTriangle using  the following format:

Test ID | Input | Expected Results | Actual Result | Pass or Fail
--- | --- | --- | --- | ---
testRightTriangleA | 3,4,5 | Right | Right | Pass
testRightTriangleB | 5,3,4 | Right | Right | Pass
testRightTriangleC | 4,5,3 | Right | Right | Pass
testEquilateralTriangles | 33,33,33 | Equilateral | Equilateral | Pass
testIsoscelesTriangles | 5,6,6 | Isosceles | Isosceles | Pass
testScaeleneTriangles | 8,9,10 | Scalene | Scalene | Pass
testNotATriangle | 12,57,15 | NotATriangle | NotATriangle | Pass
testInvalidInputA | 43,37,0 | InvalidInput | IvalidInput | Pass
testInvalidInputB | 1,1,305 | InvalidInput | IvalidInput | Pass
testInvalidInputC | 25,50,-1 | InvalidInput | IvalidInput | Pass
testInvalidInputD | 89,76,0.45 | InvalidInput | IvalidInput | Pass

6. Your assignment summary should include a matrix as shown below in the summary results along with a description of the strategy you used to decide when you had a sufficient number of test cases.

Test Summary | Test Run 1 | Test Run 2
--- | --- | ---
Tests Planned | 11 | 11
Tests Executed | 11 | 11
Tests Passed | 4 | 11
Defects Found | 7 | 0
Defects Fixed | 0 | 7

7. Submit the name of the repo containing all of the code for this assignment

***All assignments should be written up in the following format:*** </br>
All project reports should include the following standard information in the following order:

1. Assignment Description: write it out! (cut and paste is fine)
2. Author: jli198
3. Summary: at the top, include

* a summary of your results
* reflection -- this is where you actually think about the assignment after it is over -- what did you learn? What worked, what didn't?

4. Honor pledge: "I Pledge my Honor that I have abided by the Stevens Honor System." ~jli198

5. Detailed results, if any:

* A careful description of techniques you used (In this case, this item may not apply)
* Details of any assumptions or constraints made
  * I had to make sure the legacy code was not massively rewritten to ensure that the reusability for the modules can be facilitated to other teams and up to the code standard of the organization. I also assumed that isosceles was misspelled within the triangle.py code.
* A description of whatever data inputs you used
  * I decided to make another test case to test the triangle is indeed right. I also added test cases for scalene and isosceles was right. Equilateral I tested with low thirty values that were all the same, isosceles had 2 data inputs that were the same, scalene had no data inputs that were the same. NotATriangle test case was implemented by putting values where the two lowest values were less than or equal to the biggest value. InvalidInput test cases A, B, C, and D each had a 0 value, a value greater than 200, a value that was negative, and a value that is a decimal.
* An explanation of the results of your work. In this case, upload copies of the code, the sanity tests, and the results,  plus any other relevant results about the tools selection/installation/usage.
  * To change the Triangle program to pass all tests, I changed line 33 to make b <= 0 instead of b <= b which is a bug. If b <= b, this would always be true making the data inputs Invalid.
  * I removed the semicolon in line 39 to make the Python program consistent. It is fine to have a semicolon at the end of a statement in Python, but it is best practice to not have it if nowhere else there is a semicolon.
  * I changed line 45 to say b +c and a + c instead of b-c and a-c. This does not make sense subtracting those values.
  * Line 51 I added more cases to test the Pythagorean Theorem for right triangles as this new version would count the different permutations of a, b, and c to test if it is a right triangle.
  * Line 53 I changed a != b to a!= c. This is a bug and programming mishap as both conditions would be in the statement. a != c checks for all relevant permutations.
  * Line 56 I changed the spelling of Isoseles to Isosceles.
