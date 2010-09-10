Spelling dictionaries
=====================

Additional dictionaries
-----------------------

TeXnicCenter is distributed with English, German and French dictionaries.
Dictionaries for several other languages are provided by the OpenOffice.org
project http://wiki.services.openoffice.org/wiki/Dictionaries.

Installing dictionaries
-----------------------

Each Hunspell dictionary consist of two main files. Copy both the affix file,
``language-dialect.aff``, and the dictionary file, ``language-dialect.dic`` into
the Language directory of your TeXnicCenter installation. The new dictionary
will appear in the :tab:`Spelling` option page immediately, but your new
selection will not take affect until after you restarted TeXnicCenter.

Personal dictionaries format
----------------------------

The personal dictionary format is a simple text file with one case-sensitive
word per line. The first line contains the approximate number of words in the
dictionary. If the first line doesn't contain a valid number, then TeXnicCenter
guesses the size of the word list. Failing to place a blank line or a number as
the first line in the personal dictionary file will cause the first word in the
dictionary to be lost.

Using a word list from another application as personal dictionary
-----------------------------------------------------------------

You may use any word list that is in the format accepted by the personal
dictionary. You will also need read and write access to the personal dictionary
file.

Correcting spelling errors in the dictionary
--------------------------------------------

If the spelling error is in your personal dictionary open your personal
dictionary file in any text editor and remove or correct the incorrect word. If
you believe you have found a spelling error in the main dictionary, ensure that
the mis-spelling really is an error. First, ensure you have the correct language
and dialect. The dialect determines which spelling of words with multiple
spellings to use. Next, review your language and spelling option settings. If
you still believe that you have found a spelling error in a main dictionary, you
should contact the author or maintainer of the dictionary directly.

