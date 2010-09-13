Customization
=============

TeXnicCenter allows you to customize nearly every aspect of the graphical user
interface (GUI). To customize the user interface of TeXnicCenter select in the
:menuselection:`Tools --> Customize...` This will open the
:dialog:`Customization` dialog.

Customizing commands
--------------------

To customize commands which are available on several toolbars and menus open the
:dialog:`Customization` dialog and select the :tab:`Commands` tab.

.. figure:: images/customizecommands.*

  :dialog:`Command customization` dialog

When this page is active you can simply drag & drop commands from one menu to
another, from one toolbar to another, from a toolbar to a menu and vice versa.
Further on, you can drag & drop commands, not already available on the toolbars
or the menus from the :control:`Commands` list on the dialog page.

You can also change the text and/or the image of menu items and toolbar buttons.
Simply select a menu item or a button, right click on it and choose button
:button:`Appearance...`

The controls of the page are having the following meaning:

**Categories**
  Choose the category of commands to display in the list :control:`Commands`. 

**Commands**
  Commands available for the selected categorie. You can drag & drop the
  commands listed here to the toolbars and menus. 

**Description**
  A short description of the currently selected command in the list :control:`Commands`. 


Customizing toolbars
--------------------

To customize the toolbars, open the dialog Customization and select the tab
:tab:`Toolbars`.

.. figure:: images/customizetoolbars.*

  :dialog:`Toolbar customization` dialog

The meanings of the controls are:

**Toolbars**
  A list of all toolbars available at the moment. The toolbars which are
  checked, are visible at the moment. 

**Reset**
  Resets the toolbar currently selected in the list :control:`Toolbars` to the
  default configuration. All the changes you have made to the toolbar since the
  installation of TeXnicCenter will be lost. 

**Reset All**
  Resets all toolbars to the default configuration. All the changes you have
  made to the toolbars since the installation of TeXnicCenter will be lost. 

**New...**
  Creates a new toolbar. You can place commands on the toolbar using the page
  :control:`Commands`. 

**Rename...**
  If you have selected a toolbar in the list :control:`Toolbars`, that has been
  created by you using the :button:`New...` command, this button allows you to
  rename the toolbar.  
  
**Delete...**
  If you have selected a toolbar in the list :control:`Toolbars`, that has been
  created by you using the :button:`New...` command, this button allows you to
  delete the toolbar.  :button:`Show text labels` If this option is enabled,
  the buttons on the bar, selected in the list :control:`Toolbars`, will be
  displayed with labels below the icons.


Customizing the tools menu
--------------------------

You can add several commands to the menu :control:`Tools`, that allow you to
invoke external tools. This is a very powerful feature. Using placeholders for
the :control:`Arguments`, this feature allows you to integrate external tools
like spell checkers and other tools which should work with the current document
or currently selected word or elements like that.

To customize the menu :control:`Tools`, open the :dialog:`Customization` dialog
and select the tab :control:`Tools`.

.. figure:: images/customizetools.*

  :dialog:`Tools menu customization` dialog

The meanings of the controls are:

**Menu contents**
  A list of the menu items to display in the menu :menuselection:`Tools`.  You
  can create a new entry by choosing the new button (rectangle), remove the
  selected entry by choosing the delete button (cross) and move the selected
  entry up or down in the menu by choosing the up or down button.  To change the
  entry name, simply select an item and press :kbd:`F2`. 

**Command**
  Specify the full path of the application to start, when the selected entry
  will be choosen. 

**Arguments**
  Specify which arguments to pass on the command line to the application. You
  can use place holders for dynamic arguments. 

**Initial directory**
  Specify the working directory for the application to start. You can use
  placeholders for dynamic directories. 


Customizing keyboard shortcuts
------------------------------

TeXnicCenter allows you to customize the key combinations (shortcuts), necessary
to invoke a command without using the mouse.

To customize the shortcuts, open the dialog Customization and select the tab
:control:`Keyboard`.

.. figure:: images/customizekeyboard.*

  :dialog:`Keyboard shortcuts customization` dialog

The meanings of the controls are:


**Category**
  The category of the commands to display in the list :control:`Commands`. 

**Commands**
  Commands available for the currently selected category. Select a command here
  to specify a shortcut for it. 

**Description**
  A short description of the selected command. 

**Set Accelerator for**
  Specifies the menu, for which to change the shortcuts. Has to be
  :control:`Default`. 

**Current Keys**
  List of shortcuts currently assigned to the command selected in the list
  :control:`Commands`. 

**Press new Shortcut Key**
  Press the key combination here, you would like to assign to the selected
  command. 

**Assign**
  Add the shortcut shown in the field :control:`Press new Shortcut Key` to the
  list of shortcuts for the selected command. 

**Remove**
  Remove the shortcut selected in the list :control:`Current Keys` from the list
  of shortcuts for the selected command. 

**Reset All**
  Reset all shortcuts to the default. All the changes that have been made to the
  shortcuts since the installation of TeXnicCenter will be lost. 


Customizing menus
-----------------


TeXnicCenter allows you to customize the main and the context menus.  To
customize the menus, open the dialog Customization and select the tab
:tab:`Menu`.

.. figure:: images/customizemenu.*

  :dialog:`Menu customization` dialog

The meanings of the controls are:

Application Frame Menus
^^^^^^^^^^^^^^^^^^^^^^^

**Show Menus for**
  List of available main window menus. Select the menu you would like to
  customize.  For TeXnicCenter only the :dialog:`Default Menu` is available.  
  
**Reset**
  Resets the selected main window menu. All the changes that have been made to
  the menu since the installation of TeXnicCenter will be lost.  
  
**Menu animations**
  Specifies, which animation to use when opening a menu. 

**Menu shadows**
  If this option is enabled, menus in TeXnicCenter will have a fading shadow,
  otherwise the menus are displayed normally.  
  
Context Menus
^^^^^^^^^^^^^

**Select context menu**
  List of available context menus. Select the menu you would like to customize.
  Context menus pop up, when you click the right mouse button.  TeXnicCenter
  uses the following context menus.
  
  **Editor**
    Shown when you right click into an editor window.
    
  **Main Window Area**
    Shown when you right click into the main window's background or on the
    editor's scrollbars.
    
  **Navigator View**
    Shown when you right click onto an item in the navigator bar. 
    
**Reset**
  Resets the selected context menu. All the changes that have been made to that
  context menu since the installation of TeXnicCenter will be lost. 


Customizing the look and feel
-----------------------------

TeXnicCenter allows you to widely customize the look and feel of the graphical
user interface including downloadable skins.

To customize the look & feel open the :dialog:`Customization` dialog and select
the :tab:`Options` tab.

.. figure:: images/customizeoptions.*

  :dialog:`Options customization` dialog

The controls of the page are having the following meanings:

**Show ScreenTips on toolbars**
  If this option is enabled, a small yellow window (ScreenTips) with a short
  description will appear when you move the mouse cursor above a toolbar icon
  and wait for a moment. 

**Show shortcut keys in ScreenTips**
  If this option is enabled, the ScreenTips will contain the shortcut for the
  specific command besides the short description of the command. 

**Large Icons**
  If this option is enabled all toolbar icons will be displayed in double size. 

