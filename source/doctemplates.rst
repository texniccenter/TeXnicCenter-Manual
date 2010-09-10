Document templates
==================

TeXnicCenter provides a powerful feature called document templates.

A document template is a simple file or a wizard that generates a frame for a
new document. When using document frames over and over again (i.e. a letter),
then using document templates will be a big help.

TeXnicCenter provides support for two types of document templates:

* File based document templates
* Document wizards

Several directories that contain document templates can be specified in the path
options. The specified directories should contain sub-directories which
represent the categories of the templates.

When a new project is created TeXnicCenter provides the document templates found
on the left side of the dialog :dialog:`New Project`.

.. TODO: image

The tabs represent the sub-directories of the directories specified in the path
options. If one or more directories contain the same sub-directory TeXnicCenter
will display the files found in those sub-directories together in one merged
list.

Example
-------

Lets assume that in the path options two template directories were specified:

#. local directory that keeps private templates and
#. directory on the companies network, that contains company specific templates.


The local directory contains the following sub-directories:

* Letters 
* University 

Whereby the directory "Letters" contains the following templates:

* :file:`Love Letter.tex`

The company's directory contains the following sub-directories:

* General 
* Articles 
* Letters 

Whereby the directory "Letters" contains the following templates:

* :file:`Order.tex`
* :file:`Notice.tex`

When creating a new project, TeXnicCenter will analyse the directories specified
in the path options. The sub folders of the template directories listed there
will become categories, which are represented by the tabs on the left side of
the dialog :dialog:`Project New` and the files contained in the sub folders will
be listed, when choosing the according tab.

In our example, these tabs would be available:

* Articles 
* General 
* Letters 
* University 

The categories `Articles` and `General` would contain the templates from the
company's directory. The category `University` would contain the templates from
the local drive. The category `Letters` would contain the templates from the
company's directory merged with the one's from the local drive:

* Order (:file:`company/Letters/Order.tex`) 
* Notice (:file:`company/Letters/Order.tex`) 
* Love Letter (:file:`local/Letters/Love Letter.tex`) 

File based document templates
-----------------------------

File based document templates are document templates created most easily.
Templates of this type will be marked with this icon in the dialog
:dialog:`Project New`:

.. TODO: TXC logo

A file based document template is a simple text file with the extension
:file:`.tex`, placed in one of the template directories, specified on the tab
Path options.

Such a file can contain an optional description, that will be displayed in the
field template description of the dialog :dialog:`Project New`, when the
template has been selected by the user. To create such a description simply
place a line starting with ``%description:`` followed by a space as the first
line of the template.

When creating a project based on a file based document template, TeXnicCenter
will copy the selected template file to the project's directory, rename it to
the project's name, remove the description line (if there is any) and replace
the line delimiters with the ones, specified in the dialog 'Project New'.

Example
^^^^^^^

This is a very simple example for a document template:

.. literalinclude:: examples/template.tex
  :language: tex

Document wizards
----------------

Document wizards are a special form of the document templates. Document
templates of this type will be marked with this icon in the dialog
:dialog:`Project New`:

.. TODO: image

A document wizard helps to create a new document by guiding step by step through
the creation process. Document wizards are provided as Windows-DLLs (dynamic
link library - file extension :file:`.dll`) located in the template directories,
specified on the tab Path options.

Such wizards are provided on the TeXnicCenter homepage.

Document wizards work together with TeXnicCenter using the COM interface by
Microsoft. This enables every one, to create document wizards, using a
programming language, that supports the implementation of COM interfaces in a
DLL. Some important languages which are providing the necessary features, are:

* Microsoft Visual Basic 
* Microsoft Visual C++ 
* Microsoft Visual Java 
* Borland Delphi 

To learn more about how to write document wizards, take a look at the
TeXnicCenter homepage.

