del /q dist\*
py -3 setup.py sdist bdist_wheel
py -2 setup.py sdist bdist_wheel

twine check dist\*
if %ERRORLEVEL%==0 (
    twine upload dist\*
)