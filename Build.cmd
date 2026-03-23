@echo off

REM ~ Make the directory current where this batch file is from
cd %~p0

set NO_COLOR=1

make html
REM ~ make htmlhelp
