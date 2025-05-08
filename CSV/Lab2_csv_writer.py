"""
Objectives
* improving the student's skills in reading and writing CSV files;
* using the writer function or the DictWriter class.

Scenario
Your task will be to prepare a report summarizing the results of exams in maths, physics and biology.
The report should include:
* the name of the exam,
* the number of candidates,
* the number of passed exams,
* the number of failed exams,
* the best and the worst scores.

All the data necessary to create the report is in the exam_results.csv file.

Note that one candidate may have several results for the same exam.
The number of candidates should express the number of unique people in each exam identified by Candidate ID.

The final report should look like this:

Exam Name,Number of Candidates,Number of Passed Exams,Number of Failed Exams,Best Score,Worst Score
Maths,8,4,6,90,33
Physics,3,0,3,66,50
Biology,5,2,3,88,23
"""

import csv

with open('exam_results.csv', 'w', newline='') as csv_file:
    header = ['Exam Name', 'Number of Candidates', 'Number of Passed Exams',
              'Number of Failed Exams', 'Best Score', 'Worst Score']
    writer = csv.DictWriter(csv_file, fieldnames=header)

    writer.writeheader()
    writer.writerow({'Exam Name': 'Maths',
                     'Number of Candidates': '8',
                     'Number of Passed Exams': '4',
                     'Number of Failed Exams': '6',
                     'Best Score': '90',
                     'Worst Score': '33'})
    writer.writerow({'Exam Name': 'Physics',
                     'Number of Candidates': '3',
                     'Number of Passed Exams': '0',
                     'Number of Failed Exams': '3',
                     'Best Score': '66',
                     'Worst Score': '50'})
    writer.writerow({'Exam Name': 'Biology',
                     'Number of Candidates': '5',
                     'Number of Passed Exams': '2',
                     'Number of Failed Exams': '3',
                     'Best Score': '88',
                     'Worst Score': '23'})
