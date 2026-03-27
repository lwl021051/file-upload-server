# 🐍 Build Python Flask App to .exe (with PyInstaller + venv)

## 📌 Overview

This guide shows how to package a Python Flask app into a standalone `.exe` file that runs **without requiring Python installed**.

---

## ✅ 1. Create Virtual Environment

```bash
python -m venv venv
```

Activate it:

**Windows:**

```bash
venv\Scripts\activate
```

**Mac/Linux:**

```bash
source venv/bin/activate
```

---

## ✅ 2. Install Dependencies

```bash
pip install flask pyinstaller
```

(Optional: install other dependencies your app needs)

---

## ✅ 3. Verify Installation

```bash
pip list
```

Make sure you see:

* flask
* pyinstaller

---

## ✅ 4. Test Your App

Before building, confirm it runs:

```bash
python app.py
```

---

## ✅ 5. Build the .exe

### 🔹 Basic build

```bash
pyinstaller --onefile app.py
```

---

### 🔹 Recommended (Flask apps)

```bash
pyinstaller --onefile ^
  --hidden-import=flask ^
  --hidden-import=jinja2 ^
  --hidden-import=werkzeug ^
  --add-data "templates;templates" ^
  --add-data "static;static" ^
  app.py
```

---

## 📂 Output

After build:

```
dist/
   app.exe
```

---

## ⚠️ 6. Clean Old Builds (if errors occur)

```bash
rmdir /s /q build
rmdir /s /q dist
del app.spec
```

---

## ❗ Common Errors & Fixes

### 🔴 Error:

```
ModuleNotFoundError: No module named 'flask'
```

### ✅ Fix:

* Ensure venv is activated
* Run:

```bash
pip install flask
```

* Rebuild the executable

---

## 🧠 Important Notes

* PyInstaller does NOT include your venv directly
* It bundles:

  * Python interpreter
  * Installed packages
  * Your script

👉 So always build **inside the venv**

---

## 🚀 Optional: Folder Mode (Easier Debugging)

```bash
pyinstaller --onedir app.py
```

Output:

```
dist/
   app/
      app.exe
      (all dependencies)
```

---

## 🛠 Tips

* Use `--clean` to avoid cache issues:

```bash
pyinstaller --clean --onefile app.py
```

* If your app uses more packages, add them via:

```bash
--hidden-import=<module_name>
```

---

## ✅ Final Result

You now have a standalone `.exe` that:

* Runs without Python installed
* Includes Flask and dependencies
* Can be shared to other machines

---
