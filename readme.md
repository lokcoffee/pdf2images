```bash
pyinstaller.exe --onefile pdf2images.py 
# exclude module to minimize the target exe
pyinstaller --onefile --exclude-module tkinter --exclude-module numpy pdf2images.py
```