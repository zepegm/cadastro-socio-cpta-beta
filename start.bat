	@ECHO OFF

	:: %~dp0\venv\Scripts\activate.bat

	set FLASK_APP=main.py
	set FLASK_DEBUG=1
	flask run

	PAUSE