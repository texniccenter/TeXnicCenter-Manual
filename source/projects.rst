Project management
==================

TeXnicCenter provides a project management tool that helps to keep the files of
one document together and to generate output for a document.  It is especially
useful when working on large documents.

A project file will be generated for each project containing the project's
properties. The stored information is:

* The path to the main file of the project relative to the directory the
  project file is placed in.  This file will be passed to the LaTeX compiler.
* A flag that specifies whether the current project uses BibTeX. 
* A flag that specifies whether the current project uses MakeIndex. 

Some features are only available if a project is opened.  Examples of these are
Structure View (the navigator bar on the left side of the main window) and the
automatic invocation of BibTeX and MakeIndex 

Using projects is very simple. Just create a new project before starting to work
on a new document. If the requirements for the project have changed, it is easy
to simply modify project's properties.

.. _create-new-project:

Creating a new project
----------------------

To create a new project, simply choose the menu item :menuselection:`File --> New --> Project...`


.. figure:: images/newproject.*

  :dialog:`New Project` dialog


Choose one of the document templates from the list on the left side. The tabs
are representing the available categories of the available templates.

The other controls have the following meanings:

**Project Name**
  Name of the new project. This will also be the title of the project file and
  of the project's main file. 

**Project path**
  The directory, where the new project is located. If the directory does not
  exist, it will be created automatically. 

**File format**
  Choose which line delimiter should be used for the newly generated files.
  Refer to the section :ref:`file-options` for detailed information. 

**Uses BibTeX**
  Enable this option, if TeXnicCenter should run BibTeX, when generating output
  for this project. 

**Uses MakeIndex**
  Enable this option, if TeXnicCenter should run MakeIndex, when generating
  output for this project. 

**Template**
  The text displayed here is a description for the currently selected document
  template. 

Press the :button:`OK` button to generate the new project. TeXnicCenter will
create the project file and the project's main file, based on the chosen
template.  Afterwards the newly created project will be opened in TeXnicCenter.


Modifying project settings
--------------------------

All project settings can be changed afterwards, by choosing the menu item
:menuselection:`Project --> Properties...` Refer to the section
:ref:`create-new-project` for more information.

.. figure:: images/projectproperties.*

  :dialog:`Project properties` dialog


The controls have the following meanings:

**Main file**
  This is the path of the project's main file, that will be passed to the
  (La)TeX compiler, when generating output.  The path has to be specified
  relatively to the directory, the project file is placed in. 

**Uses BibTeX**
  Enable this option, if TeXnicCenter should run BibTeX, when generating output
  for this project. 

**Uses MakeIndex**
  Enable this option, if TeXnicCenter should run MakeIndex, when generating
  output for this project. 

