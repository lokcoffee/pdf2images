```bash
pyinstaller.exe --onefile pdf2images.py 
# exclude module to minimize the target exe
pyinstaller --onefile --exclude-module tkinter --exclude-module numpy pdf2images.py
```


`fitz` package is in the package of `PyMuPDF`
```angular2html
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple PyMuPDF
```



```bash
$ pdf2images.exe c:\Users\fernando\Desktop\example.pdf c:\Users\fernando\Desktop\out

$ pdf2images.exe c:\Users\fernando\Desktop\example.pdf c:\Users\fernando\Desktop\out -f jpg -r 200 -n example
```