@echo off

rem Définir les chemins d'accès aux répertoires
set source_dir=G:\
set target_dir="E:\copie cle usb\cle 1"

rem Se déplacer dans le répertoire source
cd /d %source_dir%

rem Copier le fichier dans le répertoire cible
xcopy /Y /E /I "G:\" %target_dir%

rem Afficher un message de confirmation
echo Folder copied successfully!
