
Data Wrangling
===============

Overview
---------------

This homework focuses on the first steps of getting data into a usable form to start asking very simple questions.  We'll start asking more complicated questions very soon!

This homework should not be very difficult if you can program in Python.  If this homework is particularly challenging, you may not have enough of a programming background for the course and need to quickly get up to speed or consider another course.

This program will be autograded.  That means that it's important to not change function names and to not add additional functionality that may improve the program but produce different results.  Make sure that your unit tests pass.  This what a successful set of unit tests will look like:

    $ python3 tests.py
    .....
    ----------------------------------------------------------------------
    Ran 5 tests in 0.002s
    
    OK

If you do not get this result from running the tests, you will not get a good grade.

District Margins
----------------------------

In the US, our legislature is made up of representatives of individual
*districts* (unlike proportional representation systems).  Some of
these districts are competitive, meaning that the winner of the
election is not a "sure thing" based on the voters in the districts.
However, for a variety of reasons, many of these districts are not
very competitive.  We're going to look at the 2014 election and see
which districts are competitive.

You will output to a file with the districts sorted by how competitive
they are (with the most competitive districts first).  If an election
is uncontested, the margin should be "100", in that the percentage
difference between the first place candidate and the second is 100.  

  $ python districts.py
  $ head district_totals.csv
  STATE,DISTRICT,MARGIN
  Arizona,2,0.07000000000000028
  California,7,0.7999999999999972
  Florida,2,1.1299999999999955
  Minnesota,8,1.3999999999999986
  Maryland,6,1.4500000000000028
  California,16,1.4599999999999937
  Washington,4,1.6200000000000045
  Texas,23,2.1000000000000014
  Iowa,1,2.280000000000001
  $ tail district_totals.csv
  Georgia,3,100.0
  Georgia,14,100.0
  Florida,25,100
  Georgia,5,100.0
  Florida,14,100
  Georgia,11,100.0
  Pennsylvania,18,100.0
  West Virginia,5,100.0
  West Virginia,4,100.0
  Florida,27,100

