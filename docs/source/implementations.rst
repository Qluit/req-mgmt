
Implementations 
================

Overview Implementations
------------------------
   
.. needtable::
  :types: impl
  :columns: id;title;incoming;outpoing
  :style: table
   
Detailed Implementations
-------------------------

.. impl:: Use GitHub for version control
  :id: I_github
  :tags: system
  :status: closed
  :links: S_git, R_cheap

.. impl:: Use English prompts for the BMI calculator
  :id: I_english
  :tags: system
  :status: closed
  :links: S_command_line, R_user_friendly

  Use English prompts for the BMI calculator

.. impl:: Use Python for the BMI calculator
  :id: I_python
  :tags: system
  :status: closed
  :links: S_command_line, R_compute_bmi

  Use Python 3 for the BMI calculator

  .. uml::
    
     class BMI {
         + float calculate(float weight, float height)
     }

.. impl:: Use a meters and kilograms for the BMI calculator
  :id: I_meter_kilogram
  :tags: system
  :status: closed
  :links: S_metric_units, R_compute_bmi

  Use meters and kilograms for the BMI calculator
  
.. impl:: Use algorithm from Wikipedia for the BMI calculator
  :id: I_wikipedia_algorithm
  :tags: system
  :status: closed
  :links: S_algorithm, R_compute_bmi

  Use the algorithm from Wikipedia for the BMI calculator: :math:`bmi = weight/height^2`



