Command-line arguments
======================

TeXnicCenter supports the following command-line options:

.. cmd:: filename

  Start up and open the specified file. If the file is a project file, the
  project will be opened, otherwise the file will be opened in the editor.

.. cmd:: /l linenumber filename

  Start up and open the specified file in the editor and place the cursor at the
  specified line. 

.. cmd:: /p file

  Prints the specified file to the default printer.

.. cmd:: /pt filename printer driver port

  Prints the specified file to the specified printer. 

.. cmd:: /dde

  Start up and await a DDE command.

.. cmd:: /ddecmd DDE-commands

  If there is already a running instance of TeXnicCenter, then forward the
  specified DDE commands to this instance, otherwise start up and execute the
  given DDE-commands. 

.. cmd:: /nosplash

  Start TeXnicCenter without displaying the splash screen. 


.. note::

  * If you want to influence a running instance of TeXnicCenter you should send
    DDE-commands directly to the running instance or use the :cmd:`/ddecmd`
    switch.

  * Use single quotes ``'`` inside the DDE-commands instead of double quotes
    ``"``. 

Open a file in TeXnicCenter using another application or the command line
-------------------------------------------------------------------------

The DVI-viewer YAP shipped together with the MiKTeX distribution supports a
feature called *inverse search*. If a DVI file opened in the viewer has been
generated using source specials, a double click on a paragraph in the viewer
will place the LaTeX editor caret in the appropriate line of the source
paragraph.

To do so, your favorite LaTeX editor has to support the feature to go to a line
and a source file, specified on the command-line.

TeXnicCenter supports these features with the command-line arguments listed
here.


Multiple instance support 
^^^^^^^^^^^^^^^^^^^^^^^^^

Specifying the command line ::

  /l linenumber file

in viewer's inverse search settings each time an inverse search is performed a
new instance of TeXnicCenter will be started and the new instance will open the
specified *file* and place the cursor at the specified *linenumber*.


Single instance support
^^^^^^^^^^^^^^^^^^^^^^^^

If you would like to run only one instance of TeXnicCenter (and this is what
makes sense most) you can specify the following command-line in your viewers
inverse search settings::

  /ddecmd "[goto('file', 'linenumber')]"

If you perform an inverse search now, the system will check, if there is already
a running instance of TeXnicCenter. In this case the specified DDE command will
be send to this running instance, which will open the specified *file* and place
the cursor at the specified *linenumber*.  If there is no running instance, a
new instance will be started and this new instance will open the specified file
at the specified line.

DDE commands
------------

DDE is an acronym for Dynamic Data Exchange, which is Windows' mechanism for
inter-process communication (IPC). Applications can communicate via DDE. Though
DDE is a very old mechanism, nearly all windows applications support its
commands.

Normally it is not possible to send DDE commands to an application manually
(i.e. from a command-line), but TeXnicCenter supports a special command-line
switch :cmd:`/ddecmd` which sends the specified DDE commands to an already
running instance of TeXnicCenter or if there is no instance running, starts up a
new instance and execute the DDE commands for that new instance.

The following DDE commands are available:

:command:`[open("filename")]`
  Opens the specified file. If *filename* is a project file, the
  project will be opened, otherwise the file will be opened in the editor. 

:command:`[goto("filename", "linenumber")]`
  Opens the file specified in the editor and places the cursor at the specified
  *linenumber*.

:command:`[print("filename")]`
  Prints the file specified to the default printer.

:command:`[printto("filename", "printer", "driver", "port")]`
  Prints the file specified to the printer specified. 

