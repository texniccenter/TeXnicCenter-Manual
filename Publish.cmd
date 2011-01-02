@echo off

REM ~ Make the directory current where this batch file is from
cd %~p0
REM ~ And then step into the build dir
cd build/html


REM ~ Which user is going to push the changes?
set idUser=1
echo Who are you?
echo 1 - Tino
echo 2 - Sergiu
set /p idUser="Enter your number: "

REM ~ Default: Tino
set UserName="niteria"
if %idUser% == 2 (set UserName="sergiudotenco")


REM ~ Create a list for review
rsync --verbose --rsh=ssh --checksum --archive --recursive --dry-run --exclude=/_sources/** --exclude=/.buildinfo --exclude=/objects.inv ./ %UserName%,texniccenter@web.sourceforge.net:htdocs/ | grep -v ".*/$"

echo.
echo Is the list of files ok?
echo.
timeout /T 30


REM ~ Do the actual sync
echo.
rsync --verbose --rsh=ssh --checksum --archive --recursive --exclude=/_sources/** --exclude=/.buildinfo --exclude=/objects.inv ./ %UserName%,texniccenter@web.sourceforge.net:htdocs/ | grep -v ".*/$"
echo.


timeout /T 30
