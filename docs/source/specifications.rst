
Specifications 
================

Overview Specifications
------------------------
   
.. needtable::
  :types: spec
  :columns: id;title;incoming;outpoing
  :style: table
   
Detailed Specifications
-------------------------

.. spec:: Use Git for version control
  :id: S_git
  :status: closed
  :links: R_version_controlled
  :style: yellow, blue_border

  Use Git for version control of the BMI calculator
  
    * Using a specific style for this need and
    * deliberately linking to a non-existing requirement
  
.. spec:: Create a command line tool for the BMI calculator
  :id: S_command_line
  :status: closed
  :links: R_user_friendly, R_cheap

  Create a command line tool for the BMI calculator as it is cheap and user friendly

  .. uml::

    User -> Tool: start tool
    Tool -> User: ask for weight
    User -> Tool: enter weight
    Tool -> User: ask for height
    User -> Tool: enter height
    Tool -> User: display BMI


.. spec:: Enter the weight and height in metric units
  :id: S_metric_units
  :status: closed
  :links: R_compute_bmi

  The BMI calculator shall only accept weight and height in metric units

.. spec:: Algorithm for computing the BMI
  :id: S_algorithm
  :status: closed
  :links: R_compute_bmi

  The BMI shall be computed using a well known algorithm

