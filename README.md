# 📞 Choji Food Shop USSD Application 🍲

Welcome to **Choji Food Shop**, a food ordering platform accessible via USSD!  

This project is an open-source application built using **Django**, allowing users to order food through their mobile phones. Simple and convenient, especially for those without internet access!

## 🚀 Features

- 🍴 Order food, drinks, and special combos via USSD
- 📦 View order summary and checkout directly from your mobile phone
- 🔄 Continue shopping or checkout based on user selections
- 🛠️ Built with Django for a robust backend

---

## ⚙️ Installation and Setup

Follow these steps to clone and run the **Choji Food Shop USSD** application locally.

### 1. Clone the Repository

```bash
git clone https://github.com/HarunaDev/chopchop-ussd.git && cd chopchop-ussd/
```

### 2. Create and Activate a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv/Scripts/activate
```

### 3. Install Backend Requirements

```bash
pip install -r requirements.txt
```

### 4. Apply Migrations

```bash
python manage.py migrate
```

### 5. Run the Django Development Server

```bash
python manage.py runserver
```

## 🛠️ Testing the USSD Logic

To test the USSD application, use the following guide to run it in your browser.

The Django project is named ussd and the app handling the USSD functionality is called subscription. You can pass commands in the browser's URL to simulate user inputs via USSD.

### Example Test -

Once the server is running, open your browser and use the following pattern to test different USSD commands:

```browser
http://127.0.0.1:8000/ussd/?text=1
```

This simulates a user sending 1. command via USSD.

### Continue with the next option -

For example, if your next selection is 2, enter -

```chrome
http://127.0.0.1:8000/ussd/?text=1*2
```

## 🖖 Contributing to Choji Food Shop USSD

We welcome contributions from the community! 🎉 If you'd like to contribute, follow these steps:

### 1. Fork the Project

- Click the `Fork` button at the top of this repository to create your own copy.

### 2. Create a Branch

- Create a new branch for your feature or bug fix:

```bash
git checkout -b feature/new-feature
```

### 3. Make Your Changes

- Implement your changes and commit them with a meaningful message:

```bash
git commit -m "Added new feature: ..."
```

### 4. Push to Your Branch

- Push your changes to your forked repository:

```bash
git push origin feature/new-feature
```

### 5. Create a Pull Request

- Open a Pull Request (PR) to the main repository. Ensure your PR clearly describes the changes and improvements you've made.

---

## 🙌 Community and Support

Join our growing community! Feel free to open issues for bugs, feature requests, or general questions. We also encourage you to engage in discussions to help improve the platform.

---

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## ❤️ Show Your Support

If you like this project, **give it a ⭐ on GitHub**.  
Every star helps to spread the love for Choji Food Shop USSD! ✨😊

---

**“Choji Food Shop: Bringing food to your fingertips, anytime, anywhere!”** 📲🍔🍜