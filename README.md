# popcat-clicker

Click that popcat with no effort.

### How to run

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

- Or if you want to build manually, run)
	```sh
	pyinstaller --onefile -w main.py --add-binary "drivers/chromedriver.exe:drivers" --add-binary "drivers/chromedriver_macos:drivers" --add-binary "drivers/chromedriver_linux:drivers"
	```
	side note: for windows, change `:` to `;`


