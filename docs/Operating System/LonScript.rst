LonScript
~~~~~~~~~

-  Utilizing ANTLR Parsing
-  Allows for Multi-State Machinery
-  Truly built for Scientific Computing 
and so much more…. 

|N|lonscript| 

Lonero CLI
--------------
The Lonero CLI is currently under construction, but once it is build should integrate all its core features.
| Install via: ``npm install lonero-cli``

Commands list:

| ``lonero-cli decent-test [FILE]``
| ``lonero-cli dev [FILE]``
| ``lonero-cli hello [FILE]``
| ``lonero-cli help [COMMAND]``
| ``lonero-cli inquirer``
| ``lonero-cli lon [FILE]``
| ``lonero-cli lon-matrix [FILE]``
| ``lonero-cli lon-multi [FILE]``
| ``lonero-cli plugin [FILE]``
| ``lonero-cli produce [FILE]``
| ``lonero-cli stage [FILE]``
| ``lonero-cli test-compile [FILE]``

Lonero IDE
--------------
The Lonero IDE is also actively being built.

Install via ``npm install lonero-ide`` 

This is the official IDE for Lonero. In order to start, make sure you have yarn installed and NVM as well as Node version 10.  
| Run the following:
```
$ nvm install 10
$ nvm use 10
$ npm install
$ yarn build
$ yarn theia start
```
| In order to shut down, run: `kill $(lsof -t -i:3000)`  
| The default port this uses is 3000.

Syntax Charts
--------------
*Quads*
|N|Quad|

*Strings*
|N|Strings|

*Integers*: |N|Integers|

*Comments*
|N|Comments|

*Hex Digits*
|N|Hex Digit|

*Characters*
|N|Characters|

*Identifiers*
|N|Identifiers|

*Hex Unicode*
|N|UnicodeHex|

*Whitespaces*: |N|Whitespaces|

*Escape Sequences*
|N|EscapeSeq|

*Floating Exponents*
|N|FloatingExp|

*Octal Escape Sequences*
|N|OctalSeq|

*Unicode Escpape Sequences*
|N|UnicodeSeq|

.. |N|lonscript| image:: https://raw.githubusercontent.com/Mentors4EDU/Images/master/lscript_chart.png
   :target: https://www.starkdrones.org/home/lonscript
.. |N|Quad| image:: https://raw.githubusercontent.com/Mentors4EDU/Images/master/Quad.png
.. |N|Integers| image:: https://raw.githubusercontent.com/Mentors4EDU/Images/master/Integers.png
.. |N|Strings| image:: https://raw.githubusercontent.com/Mentors4EDU/Images/master/Strings.png
.. |N|Comments| image:: https://raw.githubusercontent.com/Mentors4EDU/Images/master/Comments.png
.. |N|Hex Digit| image:: https://raw.githubusercontent.com/Mentors4EDU/Images/master/Hex%20Digit.png
.. |N|Characters| image:: https://raw.githubusercontent.com/Mentors4EDU/Images/master/Characters.png
.. |N|Identifiers| image:: https://raw.githubusercontent.com/Mentors4EDU/Images/master/Identifiers.png
.. |N|UnicodeHex| image:: https://raw.githubusercontent.com/Mentors4EDU/Images/master/UnicodetoHex.png 
.. |N|Whitespaces| image:: https://raw.githubusercontent.com/Mentors4EDU/Images/master/Whitespaces.png
.. |N|EscapeSeq| image:: https://raw.githubusercontent.com/Mentors4EDU/Images/master/Escape%20Sequences.png
.. |N|FloatingExp| image:: https://raw.githubusercontent.com/Mentors4EDU/Images/master/Floating%20Exponents.png
.. _here: https://puppet.com/docs/pe/2019.2/managing_puppet_code.html
.. |N|OctalSeq| image:: https://raw.githubusercontent.com/Mentors4EDU/Images/master/Octal%20Escape.png
.. |N|UnicodeSeq| image:: https://raw.githubusercontent.com/Mentors4EDU/Images/master/Unicode%20Escape.png
