
Test Cases 
================

Overview Test Cases 
------------------------
   
.. needtable::
  :types: test, Test-Case
  :columns: id;title;result;incoming;outpoing
  :style: table
   
Test Cases not passed or not covered by automatic test
--------------------------------------------------------

.. needtable::
  :types: test, Test-Case
  :columns: id;title;result;status
  :style: table
  :filter: result != 'passed' and links_back == []
   
Detailed Test Cases 
-------------------------

.. test:: Test if version controlled
  :id: T_version_controlled
  :tags: system
  :status: closed
  :links: S_git, I_github

  .. uml::

    start
    if (GitHub used?) then (yes)
      :test passes;
    else (no)
      :test fails;
    endif
    stop

.. test:: Test if user friendly
  :id: T_user_friendly
  :tags: system
  :status: open
  :links: I_english, R_user_friendly, S_metric_units

.. test:: Test if BMI is computed
  :id: T_compute_bmi
  :tags: system
  :status: closed
  :links: I_wikipedia_algorithm, I_meter_kilogram, I_wikipedia_algorithm

.. test:: Test if overweight
  :id: T_overweight
  :tags: system
  :status: closed
  :links: I_wikipedia_algorithm

  A test to check if the BMI is overweight.

.. test:: Test if underweight
  :id: T_underweight
  :tags: system
  :status: closed
  :links: I_wikipedia_algorithm

  A test to check if the BMI is underweight.

.. test:: Test if valid height
  :id: T_valid_height
  :tags: system
  :status: closed
  :links: I_wikipedia_algorithm, I_meter_kilogram

  A test to check if the height is valid.

Automated Test Cases with link to results
-----------------------------------------

.. test-case:: Overweight BMI
   :id: A_overweight
   :file: ../../software/bmi/report.xml
   :suite: pytest
   :classname: test_bmi_calculator.TestBMICalculator
   :case: test_bmi_overweight
   :links: T_overweight

   A pytest test case to test underweight.

.. test-case:: Underweight BMI
    :id: A_underweight
    :file: ../../software/bmi/report.xml
    :suite: pytest
    :classname: test_bmi_calculator.TestBMICalculator
    :case: test_bmi_underweight
    :links: T_underweight
  
    A pytest test case to test underweight.

.. test-case:: Normal BMI
   :id: A_normal
   :file: ../../software/bmi/report.xml
   :suite: pytest
   :classname: test_bmi_calculator.TestBMICalculator
   :case: test_bmi_normal
   :links: T_compute_bmi

   A pytest test case to test normal BMI.

.. test-case:: Non-zero height
    :id: A_non_zero_height
    :file: ../../software/bmi/report.xml
    :suite: pytest
    :classname: test_bmi_calculator.TestBMICalculator
    :case: test_zero_height
    :links: T_valid_height
  
    A pytest test case to test non-zero height.

.. test-case:: Non-negative height
    :id: A_non_negative_height
    :file: ../../software/bmi/report.xml
    :suite: pytest
    :classname: test_bmi_calculator.TestBMICalculator
    :case: test_negative_height
    :links: T_valid_height

    A pytest test case to test non-negative height.

Test Results of automated tests
--------------------------------------

.. test-results:: ../../software/bmi/report.xml

.. Test Results of automated tests from C++ version
.. --------------------------------------------------

.. These results are not used in the documentation

.. .. test-results:: ../../software/bmi_cpp/report.xml

.. Test Results of automated tests from Java version
.. --------------------------------------------------

.. These results are not used in the documentation

.. .. test-results:: ../../software/bmi_java/target/surefire-reports/TEST-BMICalculatorTest.xml


