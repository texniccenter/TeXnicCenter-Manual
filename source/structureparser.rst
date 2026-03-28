Structure Parser
================

The Structure Parser scans the LaTeX project files and extracts meaningful document structure.
It builds a coherent outline that helps to understand large projects quickly.
This includes not only standard LaTeX commands,
but also selected custom command patterns,
as well as practical diagnostics such as missing referenced files.
As a result, the parser supports both authoring and project maintenance
by making structure, dependencies, and common issues
visible in the :dialog:`Outline` and :dialog:`Files` tool windows.
The messages of the structure parser can be found in the :dialog:`Parse` tool window.

The following aspects are supported.

* Included TeX files

  * Built-in: \input, \include
  * User-defined include-like commands via % TXCUserCommand: InputFileTeXParse
  * Missing included files are also tracked

* Headings/sections

  * Built-in: \part, \chapter, \section, \subsection, \subsubsection (including variants like addsec/addchap)
  * \appendix handling
  * User-defined heading commands via % TXCUserCommand: Heading

* Graphics

  * \includegraphics and \graphicspath
  * Missing graphic files are tracked

* Figures, tables, equations (environments)

  * figure, table (including starred/sideways variants), equation-family environments (equation, eqnarray, gather, multline, align, alignat, flalign)
  * Captions and labels are parsed and attached

* Unknown environments
  
  * Any \begin{...} / \end{...} not covered by known environment rules

* Bibliography

  * \bibliography / \nobibliography forms
  * bib files and BibTeX entries (BibItem)
  * Missing bibliography files are tracked

* Index / glossary markers

  * \printindex
  * \printnomenclature, \printglossary, \printglossaries



User-defined Parser Commands
----------------------------

The Structure Parser can be extended directly from within your LaTeX source by reading specially formatted comment blocks that describe additional parsing rules. This lets you teach the editor how to recognize your own commands, so custom macros can appear in the structure view just like built-in LaTeX commands. In practical terms, you define a command type, provide metadata, and supply a regular expression that captures the part of interest, such as a file name or a heading title. The parser then applies this rule while scanning the document.


.. _basic_command_definition_block:

Basic Rules
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following block shows the basic syntax for user-defined commands:

.. admonition:: Basic Command Definition Block

  | :command:`% TXCUserCommand:` *<command type>*
  | :command:`% Name:` *<any name you choose>*
  | :command:`% Description:` *<any description you choose>*
  | :command:`%` *<regular expression for parsing a single line looking for the command>*
  | :command:`% Capture Group ID:` *<capture group number in the regular expression>*
  | :command:`%` *<possible further lines depending on the command type>*

The definition block must start with :command:`% TXCUserCommand:`
and the following definition lines must also be comment lines
that begin with :command:`%`.
The formatting is strict,
and lines with leading spaces before the :command:`%`-sign
are not treated as valid.
TeXnicCenter will only consider fully valid, uninterrupted command definition blocks.

The mandatory starting string :command:`% TXCUserCommand:` must be followed by a known command type:

* `InputFileTeXParse`_
* `Heading`_

The next two lines define the :command:`% Name:` and provide a :command:`% Description:`
for the command. These lines have no functional impact other than providing a form of documentation.

The fourth line of the definition block is of high importance.
It defines a **regular expression**
that is used to search for the command in the LaTeX project.
Note how this line starts only with a :command:`%`-sign and no other text.
Indeed, the entire line is devoted to the regular expression.

.. highlight:: latex

The regular expression must define a so-called *capture group* using a pair of parenthesis ``(...)``
which identifies a piece of text
to be used for further processing such as becoming a heading or part of a filename.
As an example, assume the definition of a new LaTeX command::

  \NewDocumentCommand{\myinput}{m}{\input{#1}}

which is used like this::

  \myinput{filename}

.. highlight:: none

A simple regular expression for parsing ``\myinput`` is then::

  \\myinput\{([^\}]*)\}

where the pair of parenthesis ``([^\}]*)`` captures the filename.
A more robust regular expression for parsing ``\myinput``
considers possible white space and possible quoting of the filename::

  \\myinput\s*\{\s*\"?([^\}]*)\"?\s*\}

Regular expressions are not always easy to understand.
A good place to start testing them
is the website https://regex101.com.
TeXnicCenter uses *ECMAScript-style* regular expressions.

The fifth line defines the :command:`% Capture Group ID:`
which refers to the number of the capture group in the previously defined regular expression.
The first capture group has the ID 1.

The fifth line of the command definition block
is also the last line that all commands have in common.
Specific commands may require additional lines for their definition as can be seen below.

.. note::
  Most lines in a command definition block
  start with a word followed by a colon such as ``% Name:`` or ``% Description:``.
  If TeXnicCenter finds a colon in any such line, it ignores all text before the colon
  and uses only the text after the colon.
  Hence, the text before the colon can be freely chosen
  by the user.
  For example,
  ``% Beschreibung:``, ``% le nom:``, ``% grupo de captura:``, or ``% Filnamn:``
  are all valid.
  The only exceptions are the first and the fourth lines,
  with the start of the definition block and the regular expression, respectively.




.. _InputFileTeXParse:

Defining an InputFileTeXParse Command
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

An ``InputFileTeXParse`` command is used when you want your custom LaTeX macro to be treated like ``\input`` or ``\include``. The definition provides the parser with the command name, a description, a regular expression, the capture group that contains the target file name, and optional text to prepend or append to that file name.

This command definition block adds two lines to the :ref:`basic block <basic_command_definition_block>` from before:

.. admonition:: InputFileTeXParse Definition Block

  | :command:`% TXCUserCommand:` InputFileTeXParse
  | :command:`% Name:` *<any name you choose>*
  | :command:`% Description:` *<any description you choose>*
  | :command:`%` *<regular expression for parsing a single line looking for the command>*
  | :command:`% Filename:` *<capture group ID for the filename>*
  | :command:`% Prepend:` *<string added before filename>*
  | :command:`% Append:` *<string added after filename>*

The two last lines :command:`% Prepend:` and :command:`% Append:`
are useful when your macro defines file names without extensions
or when files are always located in a fixed subfolder.
For example, setting ``% Prepend: chapters/`` and ``% Append: .tex`` allows ``\myinput{intro}`` to resolve to :file:`chapters/intro.tex` for structure parsing.

.. highlight:: latex

.. collapse:: Example for Naming, Scaling, and Including TikZ files

  A useful example definition looks like this::

    % TXCUserCommand: InputFileTeXParse
    % Name: includetikz
    % Description: naming, scaling, and including TikZ files
    % \\includetikz\s*\{.*\}\{\s*\"?([^\}]*)\"?\s*\}
    % Filename: 1
    % Prepend: figures/
    % Append: .tikz

  With this definition in place,
  the command ``\includetikz{\linewidth}{drawing}``
  will be parsed as a file inclusion
  of a file :file:`figures/drawing.tikz`.
  This supports the following definition in LaTeX::

    \newcommand{\includetikz}[2]{%
    \tikzsetnextfilename{#2}%
    \includegraphics[width=#1]{figures/#2.tikz}%
    }

  The user would then include TikZ files using this command,
  thereby also naming them for the `external` TikZ library
  and scaling them with the package `tikzscale`,
  all in one command that TeXnicCenter can understand now as well;
  the file will appear in the :dialog:`Files` tool window
  and its structural elements will appear in the :dialog:`Outline` tool window.
  It will also be included in the :ref:`placeholder-sets` as a TeX-file.


.. _Heading:

Defining a Heading Command
^^^^^^^^^^^^^^^^^^^^^^^^^^

A ``Heading`` command is used when you want a custom macro to appear in the document outline as a section-level entry. The definition includes a regular expression that captures the heading content and a semantic level that maps the heading into the hierarchy.

A complete definition looks like this::

    % TXCUserCommand: Heading
    % Name: mysubsection
    % Description: My SubSection
    % \\mysubsection\s*\*?\s*([\[\{].*[\]\}])
    % Title: 1
    % Level: subsection

This definition can be paired with a macro such as::

    \NewDocumentCommand{\mysubsection}{m}{\subsection{#1}}
    \mysubsection{A subsection}

The valid values for ``Level`` are:

  * ``appendix``
  * ``part``
  * ``chapter``
  * ``section``
  * ``subsection``
  * ``subsubsection``

The parser uses this level to place the custom heading at the correct depth in the structure tree.

.. collapse:: Example for Exam Tasks as Section-like Elements

  As an example, suppose a document with exam tasks for a university course.
  Each task shall be numbered and the points for the task shall be written
  as well, so the default sectioning commands are not really ideal for this.
  This can be achieved like this::

    %Support for getting the highest number of a counter, \total{}
    \usepackage{totcount}

    %Command to insert exam tasks
    \NewDocumentCommand{\examtask}{O{#2}mm}{%
    \refstepcounter{Task}\bigskip%
    \noindent\textbf{Task \arabic{Task} of \total{Task}: {#2}}%
    \hfill\small\textbf{#3}\vspace{-0.5\parskip}%
    \addcontentsline{toc}{section}{\arabic{Task}: #1}}

    %Exam task heading
    \examtask{Bilinear Interpolation}{2+2+2+6 Points}
    %Exam task content comes here...

    %Another exam task heading
    \examtask[Cubic Interpolation]{Cubic Interpolation in a 2D Grid}{5 Points}
    %Exam task content comes here...

  We want the exam tasks to appear in the :dialog:`Outline` tool window of TeXnicCenter
  at the same level where we would find a ``section`` typically.
  We use this command definition block::

    % TXCUserCommand: Heading
    % Name: examtask
    % Description: Exam Tasks
    % \\examtask\s*([\[\{].*[\]\}])
    % Title: 1
    % Level: section

