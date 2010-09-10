Configuration
=============

TeXnicCenter can be configured and customized in many different ways to suit the
needs of the user. The following configuration categories are available:

* Output profiles define how the printable output is generated from the LaTeX
  files.  The output can be in several formats, including device-independent
  (DVI), PostScript (PS), and portable document format (PDF).
* Options allow you to modify the behaviour of TeXnicCenter. 
* Customization allows you to modify the graphical user interface, including the
  menu structure, the toolbar, the short cuts, the editor and the general look
  and feel.
* Advanced configuration provides instructions for configuration changes not
  available directly from within TeXnicCenter.

Output profiles 
---------------

The LaTeX files are just simple text files. To get a printable output they have
to be compiled. Current TeX distributions support several formats like the
TeX-specific DVI-format, PostScript or the very widely used PDF-format.

Where other editors can only produce one format as output, TeXnicCenter allows
the user to select any of these output formats.  It  can even be extended to
include other formats available in other TeX distributions or through the use of
additional filters.

For each output format used an output profile has to be defined first.  You can
add as many profiles as you want. Output profiles specify answers to a number of
questions:

* Is a (La)TeX compiler necessary to generate the output?  If so, what is the
  path to it? What are the command line arguments to pass to the compiler? 
* Is a BibTeX compiler available for the specified format?  If it is, what is
  the path to it?  What are the command line arguments to pass to the compiler? 
* Is a MakeIndex compiler available for the specified format?  If so, what is
  the path to it?  What are the command line arguments to pass to the compiler. 
* Which additional tools (postprocessors) have to be started after or instead of
  the TeX compiler to generate the desired output? 
* Which application is used to view files in the desired format?  What are the
  commands needed to display an output file?  What are the commands needed to
  perform a forward search?  Is it necessary to close the output before the
  compilation starts? If it is, what is the command to do so?


Output wizard 
-----------------

The Output Wizard leads through the configuration of some basic output profiles
step by step. If the MiKTeX distribution is installed, the Output Wizard can
perform the configuration almost without user interaction.

Invoking the output wizard 
^^^^^^^^^^^^^^^^^^^^^^^^^^

After TeXnicCenter has started, it checks to see whether output profiles are
already defined. If this is not the case, TeXnicCenter will then start the
Output Wizard automatically.

To start the Output Wizard manually, please select the menu item
:menuselection:`Build --> Define Output Profiles...` and click on the button
:button:`Wizard` in the next dialog.

Using the output wizard 
^^^^^^^^^^^^^^^^^^^^^^^

At first the Wizard will look for an installed MiKTeX distribution. If MiKTeX is
found on the system, the Wizard asks for permission to configure TeXnicCenter
accordingly or to use another distribution.

To configure TeXnicCenter to use MiKTeX, the Wizard will perform the following
steps:

1. It will look for the TeX compiler. If no compiler can be found, the path to
   the compiler can be entered in a dialog. 

2. Afterwards the Wizard will look for the registered DVI-viewer. If the
   registered viewer is YAP, TeXnicCenter will be configured to YAP as default
   viewer. If another viewer is found, command line parameters to start the
   viewer, to view documents and to perform a forward search, can be entered 
   in a dialog.  
  
3. Now the wizard will test if :program:`dvips` (a tool that convert DVI
   documents into PostScript files) is installed. If :program:`dvips` is found,
   the path for command-line arguments can be entered in a dialog. 

4. Finally the Wizard will test if PDFLaTeX is installed. If this test is
   successful, the Wizard will look for the viewer registered for PDF files. If
   the viewer is the Adobe Acrobat Reader, the wizard will do the configuration,
   otherwise the path and the command line arguments for a different PDF viewer
   can be entered in a dialog. 

5. Now TeXnicCenter will create the following output profiles: 

  * LaTeX --> DVI (only if :program:`latex` has been found)
  * LaTeX --> DVI --> PDF (only if :program:`latex` and :program:`dvipdfm`
    have been found)
  * LaTeX --> PDF (only if :program:`pdflatex` has been found).
  * LaTeX --> PS (only if :program:`dvips` and :program:`latex` have been
    found)
  * LaTeX --> PS --> PDF (only if :program:`dvips` and :program:`latex`
    have been found)
  * LuaLaTeX --> PDF (only if :program:`lualatex` has been found)
  * XeLaTeX --> PDF (only if :program:`xelatex` has been found)

  If one of the above output profiles already exists, the wizard will ask
  permission to overwrite or to keep the existing one. 

To check what the wizard has created open the dialog
:ref:`manual-configuration`.

.. _manual-configuration:

Manual configuration
--------------------

To create new output profiles or to edit existing ones, choose the menu item
:menuselection:`Build --> Define Output Profiles...` The dialog
:dialog:`Profiles` is displayed:

.. figure:: images/defineprofiles.*
  
  :dialog:`Profiles` dialog

The :control:`Profiles` list shows all profiles already defined. The four
buttons at the bottom of the list provide the following actions:

**Add**
  Adds a new output profile to the list.

**Copy**
  Copies the selected output profile to a new profile. 

**Rename**
  Changes the name of the selected output profile. 

**Remove**
  Removes the selected output profile from the list. 

Use the other buttons to perform these actions:

**Wizard**
  Starts the Profile Wizard that will help generating new output profiles. 

**OK**
  Stores the changes and closes the dialog.

**Cancel**
  Ignores the changes and closes the dialog. 

To edit an output profile select a profile in the list and modify the settings
on the three tabs.


(La)TeX tab
^^^^^^^^^^^

The tab '(La)TeX' allows to define:

* which LaTeX or TeX compiler to use; 
* which BibTeX compiler to use; 
* which MakeIndex compiler to use. 

.. figure:: images/defineprofilelatex.*

  :tab:`(La)TeX` tab page

The meaning of the different controls:

**Run (La)TeX in this profile**
  Choose this option, if the specified (La)TeX compiler should be called when
  building output with this output profile. 

**Path to the (La)TeX compiler**
  Specify the full path of the (La)TeX compiler to use in this profile. 
  
**Command line arguments to pass to the compiler**
  Specify the command line to pass to the (La)TeX compiler. Use place holders
  for dynamic arguments. 

**Do not use BibTeX in this profile**
  Choose this option, to prevent BibTeX from being started, when using this
  profile. If this option is not checked, BibTeX will start or not depending on
  the project settings. 

**Path to the BibTeX compiler**
  Specify the full path of the BibTeX compiler to use in this profile.

**Command line arguments to pass to the compiler**
  Specify the command line arguments to pass to the BibTeX compiler. Use place
  holders for dynamic arguments. 

**Do not use MakeIndex in this profile**
  Choose this option, to prevent MakeIndex from being started, when using this
  profile. If this option is not checked, MakeIndex will started or not
  depending on the project settings. 

**Path to the MakeIndex compiler**
  Specify the full path of the MakeIndex compiler to use in this profile. 

**Command line arguments to pass to the compiler**
  Specify the command line arguments to pass to the MakeIndex compiler. Use
  place holders for dynamic arguments. 


Postprocessor tab
^^^^^^^^^^^^^^^^^

The :tab:`Postprocessor` tab page allows to define tools, which should be run
after the (La)TeX compiler, i.e. to convert the file generated by the compiler
to another format.


.. figure:: images/defineprofilepostprocessor.*

  :tab:`Postprocessor` tab page


The meaning of the different controls:


**Postprocessors to run after the (La)TeX compiler**
  Lists all tools to run after the compiler has been executed. The tools are
  listed in the order of the execution.

  * Use the button New at the top of the list to add a new tool.
  * Use the button Remove to remove the selected tool from the list.
  * Use the buttons Up or Down to change the execution order. 

**Executable**
  Specifies the full path of the currently selected tool's executable file. 


**Arguments**
  Specifies the command line arguments to pass to the tool. Use place holders
  for dynamic arguments. 

**Input redirection**

  Specifies where the selected tool retrieves its input data from.  If nothing
  is specified here, the tool will retrieve its input data from the standard
  input device (normally the keyboard). Otherwise it will retrieve its input
  from the specified file.

  Use place holders for dynamic arguments.

**Output redirection**
  Specifies where the selected tool should write its data output to.  If nothing
  is specified here, the tool will write its output to the standard output
  device, which normally is the console, the tool has been started from (i.e. a
  DOS box) or if TeXnicCenter started the tool the output window.  Use place
  holders for dynamic arguments. 

Using input and output redirection allow to use tools, which do not interpret
command line arguments, but retrieve their data input from the tool's input
device and/or write their data output to the tools output device.

An example of such a tool is :program:`tth`, which is used to convert LaTeX
documents into HTML documents. To start up :program:`tth` use ::

  tth < file.tex > file.html

When using this tool with TeXnicCenter, use :file:`file.tex` as input and
:file:`file.html` as output redirection. The command line of this tool has to be
empty.


Viewer tab
^^^^^^^^^^

The :tab:`Viewer` tab page allows to define the applications used to view the
files generated by this profile. 


.. figure:: images/defineprofileviewer.*

  :tab:`Viewer` tab page


The meanings of the different controls:

**Executable path**
  The full path of the application used to view the files generated by this
  profile. 

**View project's output**
  Command executed to view the project's output.  This command will be executed,
  if the menu item :menuselection:`Build --> View Output` is chosen and no open
  document in TeXnicCenter.  This command can be either a command line or a
  DDE-command (see below). 

**Forward Search**
  Command executed to view output file, corresponding to the paragraph in the
  source file the text cursor of the editor is currently placed on.  This
  command will be executed, if the menu item :menuselection:`Build --> View
  Output` chosen and is no open document in TeXnicCenter.  This command can be
  either a command line or a DDE-command (see below). 

**Close document before running (La)TeX**
  Specifies the command executed to close a previously generated output file
  open in the viewer before generating it a new one.  This command will be
  executed, if the menu item :menuselection:`Build --> Build Output` is chosen
  directly before the build process starts. Specify this command only if the
  viewer used opens files exclusively, so that no other application can access
  the output file with write access, while opened in the viewer (e.g.  Adobe
  Acrobat Reader works that way). If the compiler tries to generate a new output
  file, it will fail because the file can not be overwritten.  Specify a command
  here to close the file in the viewer before the compiler is executed.  This
  command can be either a command-line option or a DDE-command. 

All the commands can be either command-line options or DDE commands. Command-line options will be passed to the application during its start.

The meanings of the fields for a command are:

**Command line argument**
  Choose to specify a normal command line. 

**DDE command**
  Choose to specify a DDE command. 

**Command**
  Enter the command line to pass to the executable here, if the option 'Command
  line argument' was chosen or enter the DDE command to send to the viewer, if
  the option 'DDE command' was choosen.  You can use place holders to specify
  dynamic arguments.

**Server** (only available for 'DDE command') 
  Specify the server name used to connect to the DDE server (the viewer). For
  more information please refer to the manual of the viewer.  
  
**Topic** (only available for 'DDE command') 
  Specify the DDE topic the DDE command belongs to.  For more information please
  refer to the manual of the viewer.  Most applications are expecting the topic
  "System" here. 


