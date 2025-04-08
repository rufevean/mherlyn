# mherlyn

**mherlyn** is a minimal CLI-based `.env` file validator written in Python.  
It checks for common formatting issues in `.env` files and can optionally enforce stricter validation rules.

---

## 🔧 Features

- Ignores comments and blank lines
- Detects malformed lines without `=`
- Flags empty keys or values
- Detects duplicate keys
- Optional strict mode:
  - Fails on **unquoted** whitespace in values

---

## 🚀 Usage

```bash
python main.py <filename> [--strict]
