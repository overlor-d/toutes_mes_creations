@echo off

rem Définir les chemins d'accès aux répertoires
set source_dir=E:\
set target_dir="I:\PC fixe\cours 22, 23"

rem Se déplacer dans le répertoire source
cd /d %source_dir%

rem Copier le fichier dans le répertoire cible
xcopy /Y /E /I "cours 22;23" %target_dir%

rem Afficher un message de confirmation
echo Folder copied successfully!
