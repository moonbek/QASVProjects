# QASVProjects – Selenium UI Tests

This repository contains automated UI tests written in **Python** using **Selenium WebDriver** and **unittest**.

The project is created for learning and practicing QA Automation skills:
- writing UI tests
- working with Selenium WebDriver
- using Git and GitHub
- structuring test projects
- applying basic Page Object Model (POM) principles

---

## 🧪 Test Coverage

The tests cover different UI scenarios from a demo web application, including:

- Add / Remove Elements
- Basic Authentication
- Checkboxes
- Context Menu
- Disappearing Elements
- Drag and Drop
- Dropdown
- Login functionality

Each test file is located in the `tests/` directory and follows the naming convention `test_*.py`.

---

## 🛠 Technologies Used

- **Python 3**
- **Selenium WebDriver**
- **unittest** (Python built-in testing framework)
- **ChromeDriver**
- **Git & GitHub**
- **PyCharm**

---

## 📁 Project Structure


---

## 🧩 Design Pattern (Page Object Model)

Basic **Page Object Model (POM)** principles are used in this project to:
- separate test logic from page interaction logic
- reduce code duplication
- improve test readability and maintainability

Common actions, locators, and helper methods are stored in `utils.py` and reused across test cases.

---

## ▶️ How to Run Tests

### 1. Clone the repository
```bash
git clone https://github.com/moonbek/QASVProjects.git
cd QASVProjects

Make sure Python is installed, then install Selenium:
pip install selenium
