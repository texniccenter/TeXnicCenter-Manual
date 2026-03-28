User Interface
==============

Overview
--------

The main window of the application is designed to support focused writing in the editor while giving quick access to supporting information in dockable tool windows. These windows can be shown, hidden, and arranged around the editor, so you can adapt the workspace to the way you write, review, and compile your documents. Each tool window serves a distinct purpose, and together they provide a complete workflow for navigation, bibliography work, diagnostics, previewing, and search.


Menu
----

Refer to customization

Toolbars
--------

Refer to customization

Editor
------

Refer to the editor page.

Tool Windows
------------


.. dialog:: Outline

Outline
^^^^^^^

The **Outline** window gives you a structural map of your document and helps you understand the logical shape of your project at a glance. It is especially useful in long or multi-file projects, where sections, figures, tables, equations, and bibliography-related entries are spread across many source files. By browsing this view, you can quickly orient yourself and keep track of where major content blocks are located.

Interaction with the Outline is designed to be fast and direct. When you select an entry, the application synchronizes context to that item, and when you activate an entry, the editor jumps to the corresponding source location. This makes the window ideal for navigating large documents without manually searching through text. The Outline also supports context actions and drag-based workflows for reference insertion, which helps when drafting cross-references and labels.

Environments
^^^^^^^^^^^^

The **Environments** window focuses on environment-like content and presents it in a grouped, readable form so that semantically similar elements are easy to inspect together. This helps when you want to review only specific categories of content, such as equations or figures, without the noise of unrelated document structure.

As you interact with this window, selecting entries updates the project context, and activating them takes you to the corresponding place in the source. This makes it an excellent companion when polishing technical documents and verifying that environment-heavy content is complete and consistent. It is particularly useful during editing and review passes where you need to quickly jump among specialized content types.

.. dialog:: Files

Files
^^^^^

The **Files** window presents your project’s file and folder hierarchy so you can understand how source files, bibliography files, graphics, and related assets are organized. It provides a practical project-centric view of the document’s physical layout on disk, which is very helpful in larger projects with many included files and resources.

This window supports rich interaction in everyday authoring. You can navigate through directories, invoke context actions for files, and quickly inspect whether expected resources are present. Missing resources are visually distinguishable, which helps you diagnose broken includes or unavailable assets early. The Files window also supports drag-oriented insertion workflows, so bringing file references into your writing is efficient and natural.

Bibliography
^^^^^^^^^^^^

The **Bibliography** window is dedicated to citation data and gives you a searchable, sortable catalog of bibliography entries. It is designed to make citation work practical even in large bibliographic databases by presenting key fields in a tabular layout and allowing focused filtering over author, title, key, year, publication type, and publisher information.

The interaction model is built around rapid discovery. As you type in the search field, filtering narrows the result list, and search options let you control exactly where matches are evaluated. You can sort columns to reorganize entries by the field that matters to your current task, and you can activate an entry to jump to its source context. Citation insertion workflows are also supported from this window, which allows you to move from search to writing with minimal interruption.

Bookmarks
^^^^^^^^^

The **Bookmarks** window collects all bookmarks from your project in one place so that temporary and long-term navigation points remain easy to access. This is useful when writing complex material over multiple sessions, because you can mark sections that need revision, verification, or completion and return to them immediately later.

The window supports efficient maintenance as your work evolves. You can open a bookmarked location directly, rename bookmarks to improve clarity, and remove bookmarks that are no longer needed. Because bookmarks are listed with file and line context, the window functions as a practical task and navigation board while you draft and edit your document.

Preview Image
^^^^^^^^^^^^^

The **Preview Image** window shows rendered preview output and provides controls to manage how preview content is generated and displayed. Its purpose is to give immediate visual feedback so you can assess layout, diagrams, and rendered output without leaving the writing environment.

Interaction in this window is intentionally rich. You can trigger refreshes, control preview automation behavior, switch operational modes, and cancel running preview operations when needed. The view supports zooming and fit-to-window behavior, and it allows intuitive panning and wheel-based navigation so you can inspect details or quickly return to a full-page perspective. Template and resolution controls provide additional flexibility, making this window a strong tool for iterative visual refinement.

Compilation Results
^^^^^^^^^^^^^^^^^^^

The **Compilation Results** window summarizes actionable diagnostics from your build process, including errors, warnings, and layout-related notices. Its purpose is to help you triage issues quickly and move from problem discovery to correction with as little friction as possible.

This window is designed for focused troubleshooting. You can filter which diagnostic categories are visible, sort entries according to what matters most in the moment, and activate a message to jump directly toward the relevant source location. Because diagnostics are presented in a structured list with source context, this window is central to efficient correction cycles during drafting and final polishing.

Build Output
^^^^^^^^^^^^

The **Build Output** window displays the chronological text output generated during standard build operations. It gives you a detailed narrative of what the build pipeline is doing, which can be valuable when understanding progress, identifying command flow, or interpreting messages that may not appear in summarized diagnostic views.

As you use this window, you can follow output as it grows and inspect specific lines in context. Activating relevant lines helps connect textual output to editor context, supporting a tighter feedback loop between compilation events and source editing decisions. This window is particularly useful when you need the full build story rather than only extracted problems.

Preview Build Output
^^^^^^^^^^^^^^^^^^^^

The **Preview Build Output** window provides a dedicated output stream for preview-related build activity. Its purpose is to separate preview diagnostics and progress from normal build output so that each workflow remains easier to read and reason about.

This separation makes interaction clearer during intensive preview work. You can observe preview-specific messages without mixing them with unrelated compile output, and you can inspect the preview pipeline independently while adjusting preview settings or source content. The result is a cleaner troubleshooting path when your immediate goal is visual preview quality and responsiveness.

Find 1
^^^^^^

The **Find 1** window displays one channel of search results and is intended for scenarios where you want to preserve a result set while continuing other searches. This allows you to treat a result list as a working context rather than a temporary query artifact.

Interaction is optimized for investigation and navigation. You can review matching lines, activate entries to move to relevant source locations, and keep this result list visible as you continue editing. This is especially helpful when conducting thematic revisions or when checking repeated terminology and patterns across a project.

Find 2
^^^^^^

The **Find 2** window mirrors the behavior of the first find window but provides a second independent result channel. Its purpose is to let you compare, alternate, or stage multiple search tasks without losing the results of the previous one.

In practical use, this means you can keep one query result set intact while building another in parallel. This supports advanced editing workflows such as side-by-side term normalization, cross-checking references, or tracking two categories of findings during a revision pass.


.. dialog:: Parse

Parse
^^^^^

The **Parse** window presents parser-related messages and informational feedback produced during structural analysis of your project. It helps you understand how the document is being interpreted and whether structural analysis produced expected results.

This window is valuable when refining document organization or investigating structure-sensitive behavior. By reviewing parser messages, you can quickly spot where interpretation may differ from intent and then navigate back into the source to correct it. During iterative editing, the Parse window acts as a useful companion for maintaining a clean and coherent document structure.
