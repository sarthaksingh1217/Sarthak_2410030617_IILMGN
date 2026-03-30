# 🚆 SmartTransit - Weather-Aware Travel Reservation System

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![MySQL](https://img.shields.io/badge/MySQL-Database-orange?style=for-the-badge&logo=mysql)
![CustomTkinter](https://img.shields.io/badge/UI-CustomTkinter-brightgreen?style=for-the-badge)

## 📌 Project Overview
SmartTransit is a modern, desktop-based travel reservation application. It bridges the gap between secure backend relational data management and dynamic frontend utility. Instead of just booking a ticket, users are provided with **live, real-time weather conditions** for their destination city immediately before confirming their booking, ensuring informed travel decisions.

## ✨ Key Features
* **Modern GUI:** Built with `CustomTkinter` for a sleek, dark-themed, and responsive desktop experience.
* **Smart Weather Integration:** Uses the OpenWeatherMap API to fetch live destination weather during the checkout process.
* **Relational Database Backend:** Fully normalized MySQL database (Primary/Foreign Keys) preventing data anomalies and ensuring strict referential integrity.
* **User Authentication:** Secure registration and login system.
* **Dynamic Search:** Users can search for routes between cities and view dynamic pricing and transport types using complex SQL `JOIN` operations.

## 🛠️ Technology Stack
* **Frontend:** Python (`CustomTkinter`)
* **Backend:** Python
* **Database:** MySQL (`mysql-connector-python`)
* **External APIs:** OpenWeatherMap API (`requests` library)

## 🗄️ Database Schema
The system utilizes a 4-table normalized relational architecture:
1. **Cities:** Standardized location nodes to prevent user typos.
2. **Users:** Traveler profiles and authentication.
3. **Routes:** The transit schedule linking source and destination cities.
4. **Bookings:** The transactional ledger linking users to their selected routes.

---

## 🚀 Installation & Setup Guide

### 1. Prerequisites
You will need to have the following installed on your machine:
* Python 3.x
* MySQL Server (via XAMPP, MySQL Workbench, or Command Line)

### 2. Clone the Repository
```bash
git clone https://github.com/sarthaksingh1217/Sarthak_2410030617_IILMGN/.git
cd Sarthak_2410030617_IILMGN