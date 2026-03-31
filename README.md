# 🚆 Smart Travel Reservation System

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![MySQL](https://img.shields.io/badge/MySQL-Database-orange?style=for-the-badge&logo=mysql)
![CustomTkinter](https://img.shields.io/badge/UI-CustomTkinter-brightgreen?style=for-the-badge)

## 📌 Project Overview
The Smart Travel Reservation System is a modern, desktop-based travel booking application. It bridges the gap between secure backend relational data management and dynamic frontend utility. Instead of just booking a ticket blindly, users are provided with **live, real-time weather conditions** for their destination city immediately before confirming their booking, ensuring informed travel decisions.

## ✨ Key Features
* **Smart Weather Integration:** Uses the OpenWeatherMap API to fetch live destination weather (temperature and conditions) during the checkout process.
* **Relational Database Backend:** Fully normalized MySQL database utilizing Primary and Foreign Keys to prevent data anomalies and ensure strict referential integrity.
* **Modern GUI:** Built with Python's `CustomTkinter` for a sleek, dark-themed, and responsive desktop experience.
* **User Authentication:** Secure registration and login system for travelers.
* **Dynamic Search:** Users can search for routes between cities and view dynamic pricing and transport types.

## 🛠️ Technology Stack
* **Frontend:** Python (`CustomTkinter`)
* **Backend:** Python
* **Database:** MySQL (`mysql-connector-python`)
* **External APIs:** OpenWeatherMap API (`requests` library)

## 🗄️ Database Schema
The system utilizes a 4-table normalized relational architecture:
1. **Cities:** Standardized location nodes to prevent user typos.
2. **Users:** Traveler profiles and authentication credentials.
3. **Routes:** The transit schedule linking source and destination cities with pricing.
4. **Bookings:** The transactional ledger linking users to their selected routes and travel dates.

---

## 🚀 Installation & Setup Guide

### 1. Prerequisites
You will need to have the following installed on your machine:
* Python 3.x
* MySQL Server (via XAMPP, MySQL Workbench, or Command Line)

### 2. Clone the Repository
```bash
git clone https://github.com/sarthaksingh1217/Sarthak_2410030617_IILMGN.git
cd Sarthak_2410030617_IILMGN
```
### 3\. Install Python Dependencies

Open your terminal and install the required Python libraries:
```bash
pip install customtkinter mysql-connector-python requests python-dotenv
```

### 4\. Database Setup

1.  Open your MySQL client.
    
2.  Create the SmartTransit database and tables by running the provided SQL commands.
    
3.  Open database.py and update the password="YOUR\_MYSQL\_PASSWORD" field in the create\_connection() function to match your local MySQL credentials.
    

### 5\. API Key Configuration

1.  Obtain a free API key from [OpenWeatherMap](https://openweathermap.org/).
    
2.  Open main.py and replace the placeholder API key with your actual key (or set it up securely using a .env file).
    

### 6\. Run the Application

Launch the system from your terminal:

``` bash
python main.py
```

🔮 Future Scope
---------------

*   **Cloud Database Migration:** Hosting the MySQL database on a managed cloud service (like AWS RDS) for global accessibility.
    
*   **Payment Gateway Simulation:** Integrating a sandbox API (e.g., Stripe) to simulate real financial transactions before ticket confirmation.
    
*   **Dynamic Weather Alerts:** Expanding the API integration to suggest alternate travel dates if severe weather is detected.
    
