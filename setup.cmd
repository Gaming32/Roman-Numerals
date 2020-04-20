del /q dist\*
python setup.py sdist bdist_wheel

twine check dist\*
if %ERRORLEVEL%==0 (
    twine upload dist\*
)