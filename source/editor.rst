Editor
======

TeXnicCenter comes with an advanced editor that supports the following features:

    * syntax highlighting
    * fixed-width fonts
    * proportional fonts
    * font antialiasing
    * rectangular selections
    * multiple selections
    * code folding
    * bookmarks

.. TODO write some more stuff about multiple selection and other advanced,
   unusual stuff. Provide images for that.


.. index::
  editor

Editor keyboard shortcuts
-------------------------


.. index::
  editor keyboard shortcuts
  shortcuts

The following table lists the editor commands that are accessible via the
keyboard. Some of these shortcuts can be :ref:`customized
<customization-shortcuts>`, others are built-in. User-defined shortcuts take
precedence over built-in shortcuts.

.. list-table:: Editor keyboard shortcuts
    :header-rows: 1

    * - Command
      - Keyboard shortcut
    * - Magnify text size
      - :shortcut:`Ctrl+Keypad +`
    * - Reduce text size
      - :shortcut:`Ctrl+Keypad -`
    * - Restore text size to normal
      - :shortcut:`Ctrl+Keypad /`
    * - Cycle through recent files
      - :shortcut:`Ctrl+Tab`
    * - Cycle through recent files in reverse order
      - :shortcut:`Ctrl+shift+Tab`
    * - Indent block
      - :shortcut:`Tab`
    * - Dedent block
      - :shortcut:`shift+Tab`
    * - Delete to start of word
      - :shortcut:`Ctrl+Backspace`
    * - Delete to end of word
      - :shortcut:`Ctrl+Delete`
    * - Delete to start of line
      - :shortcut:`Ctrl+shift+Backspace`
    * - Delete to end of line
      - :shortcut:`Ctrl+shift+Delete`
    * - Go to start of document
      - :shortcut:`Ctrl+Home`
    * - Extend selection to start of document
      - :shortcut:`Ctrl+shift+Home`
    * - Go to start of display line
      - :shortcut:`Home` (pressed once) or :shortcut:`Alt+Home`
    * - Go to start of line
      - :shortcut:`Home` (pressed twice)
    * - Go to end of document
      - :shortcut:`Ctrl+End`
    * - Extend selection to end of document
      - :shortcut:`Ctrl+shift+End`
    * - Go to end of display line
      - :shortcut:`End` (pressed once) or :shortcut:`Alt+End`
    * - Go to end of line
      - :shortcut:`End` (pressed twice)
    * - Create or delete a bookmark
      - :shortcut:`Ctrl+F2`
    * - Go to next bookmark
      - :shortcut:`F2`
    * - Find selection
      - :shortcut:`Ctrl+F3`
    * - Find selection backwards
      - :shortcut:`Ctrl+shift+F3`
    * - Scroll up
      - :shortcut:`Ctrl+Up`
    * - Scroll down
      - :shortcut:`Ctrl+Down`
    * - Line cut
      - :shortcut:`Ctrl+L`
    * - Line copy
      - :shortcut:`Ctrl+shift+T`
    * - Line delete
      - :shortcut:`Ctrl+shift+L`
    * - Line transpose with previous
      - :shortcut:`Ctrl+T`
    * - Selection duplicate
      - :shortcut:`Ctrl+D`
    * - Previous paragraph. shift extends selection
      - :shortcut:`Ctrl+[`
    * - Next paragraph. shift extends selection
      - :shortcut:`Ctrl+]`
    * - Select paragraph. Press several times to extended selection
      - :shortcut:`Ctrl+P`
    * - Select brace block. Press several times to extended selection
      - :shortcut:`Ctrl+M`
    * - Previous word. shift extends selection
      - :shortcut:`Ctrl+Left`
    * - Next word. shift extends selection
      - :shortcut:`Ctrl+Right`
    * - Rectangular block selection
      - :shortcut:`Alt+shift+|Movement|`
    * - Extend rectangular selection to start of line
      - :shortcut:`Alt+shift+Home`
    * - Extend rectangular selection to end of line
      - :shortcut:`Alt+shift+End`
    * - Abort selection (select nothing)
      - :shortcut:`Esc`

.. Does not work or we do not have this in TXC:
    * - Expand or contract a fold point
      - :shortcut:`Ctrl+Keypad*`
    * - Select to next bookmark
      - :shortcut:`Alt+F2`
    * - Find matching preprocessor conditional, skipping nested ones
      - :shortcut:`Ctrl+K`
    * - Select to matching preprocessor conditional
      - :shortcut:`Ctrl+shift+K`
    * - Find matching preprocessor conditional backwards, skipping nested ones
      - :shortcut:`Ctrl+J`
    * - Select to matching preprocessor conditional backwards
      - :shortcut:`Ctrl+shift+J`

.. Do not advocate this, since it doesn't make sense for LaTeX:
    * - Previous word part. shift extends selection
      - :shortcut:`Ctrl+/`
    * - Next word part. shift extends selection
      - :shortcut:`Ctrl+\\`


Editor mouse shortcuts
----------------------

.. index::
  editor mouse shortcuts
  shortcuts

The following table lists the editor commands that are accessible via the mouse.

.. list-table:: Editor mouse shortcuts
    :header-rows: 1

    * - Command
      - Mouse shortcut
    * - Magnify text size
      - :shortcut:`Ctrl+|Mouse Wheel Up|`
    * - Reduce text size
      - :shortcut:`Ctrl+|Mouse Wheel Down|`
    * - Create or delete a bookmark
      - Click on the left-most margin.
    * - Expand or contract a fold point
      - Click on the fold margin.
    * - Scroll up
      - :shortcut:`|Mouse Wheel Up|`
    * - Scroll down
      - :shortcut:`|Mouse Wheel Down|`
    * - Extend regular selection
      - :shortcut:`shift+|Left Click|`
    * - Rectangular block selection
      - :shortcut:`Alt+|Left Mouse Button|`
    * - Multiple selections
      - :shortcut:`Ctrl+|Left Mouse Button|`
    * - Abort selection (select nothing)
      - Left Click
    * - Move text
      - Drag&Drop selected text
    * - Copy text
      - Drag&Drop selected text while holding :shortcut:`Ctrl`
