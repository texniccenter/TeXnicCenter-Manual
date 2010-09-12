Options
=======

TeXnicCenter provides many options to configure the application, making usage
easier. To change these options, open the dialog :dialog:`Options` by choosing
the menu item :menuselection:`Tools --> Options...`.

.. index::
  options

General options
---------------

.. index::
  options; general

The :tab:`General` options page in the :dialog:`Options` dialog allows to modify
general options for TeXnicCenter.

.. figure:: images/optionsgeneral.*

  :tab:`General` option page

The meaning of the controls is:

**Restore last session on start up**
  If enabled TeXnicCenter will reload the project and all files that were open
  before TeXnicCenter was closed the last time. 

**Replace quotation marks**
  If this option is enabled, TeXnicCenter will do two related things:
  
  * Replace opening quotation marks with the string specified by *Opening
    quotation mark*
  * Replace closing quotation marks with the string specified by *Closing
    quotation mark*
  
  when the user types the quotation mark (") character. 
  
**Language**
  The choices are English and Deutsch (German).

**Optimize user interface for visually handicapped users**
  Improves the visibility of some of the features of TeXnicCenter.


.. _file-options:

Files options 
-------------

.. index::
  options; files

The :tab:`Files` options page in the dialog :dialog:`Options` allows to modify
the file handling of TeXnicCenter.

.. figure:: images/optionsfiles.*

  :tab:`Files` option page

The meaning of the controls is:

**Save new document immediately**
  If this option is enabled, then as soon as a new document has been created it
  will be saved without delay. 

**Save all before compilation**
  If this option is enabled, TeXnicCenter will save all modified files before
  the build process is started. 

**Save automatic every x minutes**
  If enabled, TeXnicCenter will save all modified files at the specified
  interval. 

**Default**
  Allows to specify the default end-of-line format:

  * Windows (``\r\n``)
  * Unix (``\n``)
  * Macintosh (``\r``)

  The format for each file can be changed in the dialog :menuselection:`File -->
  Save As...` individually. 


Directories options
-------------------

.. index::
  options; directories

The :tab:`Directories` options page in the :dialog:`Options` dialog allows to
modify the directory paths used by TeXnicCenter.

.. figure:: images/optionsdirectories.*

  :tab:`Directories` option page

The meaning of the controls is:

**Project template directories**
  The directory where project templates are stored.  Typically these directories
  contain further subdirectories with collections of related templates.  When
  you create a new project, you can select a template from any of these
  collections. 

**Document template directories**
  The files in the directories listed here will be provided as document
  templates when a new document is created. 

**Default working directory**
  The directory specified here will be used as the default directory for new
  projects and new files. If this path is left empty, the default directory for
  the Windows user is used. If a project is still open, the project's  directory
  is used. 


Spelling options
----------------

.. index::
  options; spelling

The :tab:`Spelling` options page in the :dialog:`Options` dialog allows users to
set spelling and language options for TeXnicCenter. See Advanced configuration
for more information and settings about languages and spelling.

.. figure:: images/optionsspelling.*

  :tab:`Spelling` option page

The meaning of the controls is:

**Language**
  This drop down list shows all languages of the installed dictionaries. The
  language setting only affects the spell checking functionality of
  TeXnicCenter. It does not affect the language of the TeXnicCenter user
  interface. Changing the language does require a restart of TeXnicCenter to
  became effective.  The choices are English (en) and German (de). 

**Dialect**
  This drop down list shows all dialects available for the selected language.
  The dialect setting only affects the spell checking functionality of
  TeXnicCenter. It does not affect the language of the TeXnicCenter user
  interface. Changing the dialect does require a restart of TeXnicCenter to
  become effective. 

**Check spelling while typing**
  When selected, TeXnicCenter performs spell checking during data input. Words
  not found in the spell checker dictionary are highlighted. 

**Suggest from main dictionary only**
  When selected, TeXnicCenter suggests only words from the main dictionary.
  Words from the personal dictionary will not be included in the suggestion
  list. 

**Ignore comments**
  When selected, TeXnicCenter does not check the spelling of comments. 

**Ignore LaTeX tags**
  When selected, TeXnicCenter does not check the spelling of LaTeX tags. This
  setting does not affect spell checking LaTeX command arguments. For example,
  the argument of the LaTeX command ::

    \caption{This is a caption} 
    
  ``This is a caption`` is always spell-checked. This option only determines
  whether ``\caption`` is spell-checked. 

**Ignore words with numbers**
  When selected, TeXnicCenter does not check the spelling of words containing
  numbers. 

**Ignore UPPERCASE words**
  When selected, TeXnicCenter does not check the spelling of words in uppercase
  letters. 

**Personal Dictionary**
  Contains the path to and the name of the file containing the personal
  dictionary. The personal dictionary contains words not found in the main
  dictionary. It is loaded once during application startup and written once
  during application shutdown. Clearing the personal dictionary text field
  disables the personal dictionary. Changes to the personal dictionary control
  do not cause the personal dictionary to be reloaded until TeXnicCenter is
  started next time. 

  
After spell checking has finished, TeXnicCenter saves the words you added to the
dictionary or those you marked as *ignore* in the project directory. These words
will be considered in future sessions, so that you don't have to mark them
again. 

.. note::

  There is a file for each language. For instance, German files have the suffix
  ``German``. If the language is changed, the words will be lost.

If you want to reset or change these dictionaries, just delete or edit them. The
first row contains the number of entries, followed by the number of lines. Each
line contains exactly one word. For example, a file with 3 words has the
following content::

  3
  first
  second
  third


Clean options
-------------

.. index::
  options; clean

The :tab:`Clean` options page in the :dialog:`Options` dialog allows to modify
file protection and file deletion options when :menuselection:`Build --> Clean
Project` is invoked.

.. figure:: images/optionsclean.*

  :tab:`Clean` option page

.. note::

  Please be carefull when configuring this command. Deleting the wrong files may
  cause loss of important data. While TeXnicCenter tries its best to prevent
  deletion of essential files, you are responsible for this, too.

The meaning of the controls is:

**File groups**
  The entries in the list box below define the files to be deleted or protected.
  Scroll through this list and select an entry to edit or remove it.
  
  There are two entries at the end of the list, which can not be edited or
  removed. These two entries are used to protect all files of the project and
  all files that are currently opened within the editor. Files recognized by
  TeXnicCenter as a part of the project are shown on the tab Files in the
  Navigation window. The listed set may not include all files of the current
  project.  You may add any not already recognized by TeXnicCenter. 

**New**
  Pressing this button adds a new entry to the list. 

**Remove**
  Pressing this button removes the selected entry from the list. 

**Sort**
  Pressing this button sorts the list of entries for a better overview. 

**Description**
  This edit box is used to change the description text of the selected entry.
  This text does not mean anything to TeXnicCenter -- type here whatever would
  be helpful in understanding the selected entry. 

**Pattern**
  The text in this control defines a file or a set of files to act on for the
  selected entry. 

  It is permissible to use the same wildcards (``*`` and ``?``) permitted in a
  Windows command line. Additionally, you may use placeholders for single files
  and placeholders for sets of files here. The combination of wildcards with
  placeholders for single files is supported, but no other combination is
  permitted.
  
  Use the button on the right of the edit box to select a placeholder from a
  list.  Alternatively, you may type it in manually. 

**Action**
  This control selects the action to be performed on the file(s) defined by
  **Pattern** for the selected entry. The following actions are available:
  
  **none**
    The selected entry will not be used to build up the lists for deletion or
    protection. Use this action to deactivate an entry without removing it
    altogether.
    
  **delete**
    The files defined by **Pattern** will be deleted unless they are protected
    by another entry in the list. 

  **protect**
    The files defined by **Pattern** will be protected from deletion. If an
    entry defines a file to be protected and another entry defines the same file
    to be deleted, the file will be protected, i.e., the deletion entry will be
    ignored. 

**Include subdirectories**
  If selected, TeXnicCenter searches the subdirectories of the active project
  for matching files defined by **Pattern**, too. The choice can differ for
  different file groups. 

**Confirm before delete**
  If selected, TeXnicCenter will show a dialog before deleting files. This
  dialog lists all the files to be deleted and protected. 

  This entry refers to all entries in the table, not just the one currently
  selected.

Clicking on the :button:`Cancel` button will dismiss any changes without
applying them. 


Text format options
-------------------

.. index::
  options; text format

TeXnicCenter allows to customize the font family, style and size for the
navigator bar, the output bar and the editor window. Additionally, editor colors
used for syntax highlighting can be modified as well.

To customize the text format open the :dialog:`Customization` dialog and select
the :tab:`Text Format` option page.

.. figure:: images/optionstextformat.*

  :tab:`Text Format` option page

The meanings of the controls are:

**Window**
  Select the window for which you would like to change the text format.
  Available window types are:
  
  **Editor**
    The editor window used to edit the (La)TeX documents.
    
  **Navigator**
    The window normally docked at the left side of the main window, which
    displays the document structure. 

  **Output**
    The window normally docked at the bottom of the main window, which displays
    the output generated by the (La)TeX compiler. 
  
**Font**
  Displays an example of the currently selected font for the selected window
  type. 

**Change...**
  Allows you to select the font family, style and size to use for the selected
  window type. If the current window type is 'Editor', only fonts with a fixed
  width per character are available.

**Item** (only available for window type `Editor`) 
  Allows to specify the editor item whose appearance should be modified.

  **Selection Margin**
    The margin displayed at the left side of an editor window. 
  
  **Whitespaces**
    Invisible characters like space and tabulator. 
  
  **Background**
    Background of the text.
    
    .. note::
      This option will not change the background of the editor window but only
      the areas where text is placed.

  **Normal Text**
    Normal text.

  **Background (selected)**
    Same as `Background`, but for selected text. 
  
  **Normal Text (selected)**
    Selected text.

  **Keyword**
    A (La)TeX keyword.
  
  **Comment**
    A (La)TeX comment.
  
  **Operator**
    A (La)TeX operator.
  
  **Text in \verbatim**
    Text inside a verbatim environment.
  
  **Normal text in equation ($$)**
    Text inside inline math mode. 
  
  **Keyword in equation ($$)**
    A (La)TeX keyword inside inline math mode.
  
  **Matched brace background**
    The background of matched brace.
  
  **Matched brace text**
    The text of matched brace.
  
  **Matched brace background (at cursor)**
    The background of brace at cursor.
  
  **Matched brace text (at cursor)**
    The text of brace at cursor.
    
  **Block background between braces**
    The background of text between brace at cursor and matched brace.

  **Unmatched brace background**
    The background of brace that have no pair.
  
  **Unmatched brace text**
    The text of brace that have no pair.

  **Digits**
    The appearance of single digits.  

  **Units**
    The appearance of unit specifiers ``em``, ``ex``, ``pt``, ``pc``, ``in``,
    ``bp``, ``cm``, ``mm``, ``dd``, ``cc``, ``sp``.

**Color Picker** (only available for window type `Editor`)
  Choose the color for the selected element here. The color ``Automatic`` is the
  default value for the selected element. 

**Tabulator width** (only available for window type `Editor`)
  Specifies the width of a tabulator in characters. 

