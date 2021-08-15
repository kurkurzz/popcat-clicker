# popcat-clicker

Click that popcat with no effort using python and selenium.

Note that the api limit is only 800 clicks per 30 seconds. So the script will pause on every 799 clicks

### How to run

1. Go to https://github.com/kurkurzz/popcat-clicker/releases
2. Choose latest release
3. Download `main.app.zip` for macos user, `main.exe` for windows user.
4. Run!

	Note: you might need to wait a few seconds until the script running.

Don't worry about any security issue because the code is free from any malware.


### How to rebuild the binary package
- Run 
	```sh
	pip install -r requirements.txt
	```

- Run 
	```sh
	pyinstaller main.spec
	```

	Something to take note, you might want to change paths in `datas` to `binaries` if you run on windows.

- Or if you want to build manually, run
	```sh
	pyinstaller --onefile -w main.py --add-binary "drivers/chromedriver.exe:drivers" --add-binary "drivers/chromedriver_macos:drivers" --add-binary "drivers/chromedriver_linux:drivers"
	```
	side note: for windows, change `:` to `;`


