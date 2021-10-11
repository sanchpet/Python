# Programming technologies and methods
###### Assignments for Programming technologies and methods, ITMO University, Faculty of Information Security, 2021
## TASKS:

[__1. Laboratory work 1a__](https://github.com/cyberknopa/Python/blob/main/TIMP/Lab_1.py)

Develop a program that prohibits the creation, copying or renaming of 
files with specified names in the current (the one where it is located) directory 
(you can use file masks). The list of names or their templates should be stored in the template.tbl file as text. 
This file must be protected from deletion, unauthorized viewing and modification. When installing the program, 
you can provide for disabling it using the password stored in the first line of the template.tbl file in hashed form. 
The program must enable and disable the protection mode.

[__2. Laboratory work 2__](https://github.com/cyberknopa/Python/tree/main/TIMP/Lab2)

Develop a simple program that asks for the user's name and puts this information into a text file. If there is such a name in the file, then give a message about it. After entering the information, the program should terminate and inform the user about its usage limits (time or number of runs). When the startup limit is reached, the program must prompt the user to purchase its full version or to uninstall itself. When reinstalling the program, it should report its previous presence on this computer and check the past usage limits (i.e., not let them be exceeded in total).

The installer, program and uninstaller are taken for protection (the program is registered in the system, and you know where to look and how to "crack" it).

Two versions of the program are executed (you can combine them into one):

a) Time-limited (time limit to do no more than 3 minutes, so you can track when the limit is reached at the time of delivery).

b) Start-limited (limit on the number of runs should also be clear, for example - 4-5).

