# Challenge:

Write a Python program that reads in a CSV file containing student names and their corresponding test scores. The program should calculate the average score for each student and print out a report showing the student's name and average score, sorted by highest average score first.

Your program should be able to handle errors gracefully. Specifically, it should:
* gracefully handle a missing or incorrectly formatted input file
* gracefully handle invalid test scores (e.g. negative scores, scores greater than 100)

To debug your program, use Python's built-in logging module to log error messages at appropriate levels.

Hint: You may want to use the csv module in Python to read in the CSV file.

Sample input:
```
student,score
Alice,90
Bob,80
Charlie,70
Dave,60
Eve,50
Frank,40
```

Sample output:
```
Alice: 90.0
Bob: 80.0
Charlie: 70.0
Dave: 60.0
Eve: 50.0
Frank: 40.0
```

Note: The output should be sorted by highest average score first.

Challenge Requirements:

Use Python 3.x
Use the logging module to log error messages at appropriate levels.
Handle errors gracefully as specified above.
Write clean, well-organized code with appropriate comments and docstrings.
Good luck!

## Tools

```
# Basic message levels format

logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')

```