Usage
=====

.. _installation:

Installation
------------

Clone the archive on GitHub or another RTD supported version control system
If you do not want to use RTD, building just locally might be an option

To buid the documentation on RTD, read the 
`Read the Docs tutorial <https://docs.readthedocs.io/en/stable/tutorial/>`_ 


Building locally
------------------

Activate the environment for your platform first

.. tabs::

   .. tab:: UX

      .. code-block:: console

         cd docs
         source activate.sh

   .. tab:: Windows

      .. code-block:: console

         cd docs
         activate.bat

Then build the documentation locally by entering ``make html``. 
Documentation can be viewed by opening index.html.

Exporting and importing needs
------------------------------

If you would like to use separate archives for say requirements and specifications,
needs can be exported from the requirements project in json format and then imported 
into the specification project to reference to them without modifying them.

To use this scheme, create two archives as a copy from this one:

   * Requirements
   * Specifications

Strip these archives to have only requirements and specifications respectively.
The needs from this project are exported in the same folder as the 
html files as `needs.json <needs.json>`_

The json file can be imported in the specification project by a `needs_import` directive.
The requirement R_cheap is imported from a local file called cheap.json. 
Once the Requirements are built on RTD, they can even be imported in the Specification 
document by using the url on RTD for `needs_import`.

Dirty links
------------

When updating requirements (any need actually), the links to other needs might become dirty.
To be able to detect dirty links, needs have an id that is to be postfixed with a version number.
When the need is updated, the version number is to be increased. 
All link errors are converted into todo items in the documentation.
Link errors can be solved by mentioning the right need id (with the new id) in the need.
If the need itself needs adaptation due to the updated need it points to, 
the version number of that need is to be increased as well.
This way, the dirtiness propagates until everything is updated accordingly.
The format of the version number can be enforced in conf.py.
A working format is: R_version_controlled^42.

Issue management on GitHub
----------------------------

Issues on GitHub can be used using 
`create-issue-branch <https://github.com/marketplace/actions/create-issue-branch>`_  
in such a way that branches are automatically created for an issue if you type 
``/createissuebranch`` or just ``/cib`` in a comment of the issue. 

Furthermore, when the branch is merged using a pull request, the issue is automatically
closed. You need a default branch called ``develop`` to make this work. 
Behavior can be modified in ``issue-branch.yml``.
