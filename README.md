# Playwright Automation Framework

## 📌 Overview
This is a **Playwright-based UI test automation framework** designed to test web applications efficiently. It supports multiple browsers and integrates with **Python**, **Pytest**, and **GitHub Actions**.

## 🛠️ Features
- **Cross-Browser Testing** (Chromium, Firefox, WebKit)
- **Headless & Headed Mode Execution**
- **Parallel Test Execution**
- **Custom Reporting with Allure Reports**
- **CI/CD Integration with GitHub Actions**

---

## 🚀 Installation & Setup

### **1. Clone the Repository**
Run the following command in PowerShell:
```sh
 git clone https://github.com/YOUR_GITHUB_USERNAME/Playwright-Automation-Framework.git
 cd Playwright-Automation-Framework
```

### **2. Create & Activate Virtual Environment**
```sh
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

### **3. Install Dependencies**
```sh
pip install -r requirements.txt
```

### **4. Install Playwright Browsers**
```sh
playwright install
```

---

## 🎯 Running Tests

### **Run All Tests**
```sh
pytest tests/
```

### **Run Tests in Headless Mode**
```sh
pytest --headed
```

### **Generate Allure Report**
```sh
pytest --alluredir=reports/
allure serve reports/
```

---

## 🌍 Committing & Pushing Changes Using PowerShell

### **1. Add All Files**
```sh
git add .
```

### **2. Commit Changes**
```sh
git commit -m "Updated Playwright automation tests"
```

### **3. Push to GitHub**
```sh
git push origin main
```

If pushing for the first time, you might need to set the upstream branch:
```sh
git push --set-upstream origin main
```


