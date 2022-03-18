@REM Comment line : Changing the active console code page to UTF-8
chcp 65001
@REM Comment line : switch to project folder
cd  d:/ownsofttech/MashoFitness
@REM Comment line : Activating the base virtual environment since I use anaconda.
call activate env
@REM Comment line : Starting our project with python3.exe from Anaconda folder.
"C:\Users\ehtisham ahmed\anaconda3\envs\env\python.exe" manage.py runserver

PAUSE
