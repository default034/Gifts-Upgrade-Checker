# ⭐ Userbot Upgrade Checker

[![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Telethon](https://img.shields.io/badge/Telethon-1.28+-blue?logo=telegram)](https://docs.telethon.dev/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A lightweight Python bot built with Telethon that automatically monitors and notifies about new gift upgrades available in Telegram. Perfect for staying updated with the latest gift enhancement opportunities.

---

## 🚀 Features

*   **Automatic Upgrade Detection**: Continuously monitors for new gift upgrades in Telegram.
*   **Smart Filtering**: Tracks only relevant gift upgrades based on your configuration.
*   **Real-time Notifications**: Sends instant alerts to your specified channel when new upgrades are detected.
*   **Persistent Memory**: Remembers processed gifts to avoid duplicate notifications.
*   **Detailed Logging**: Provides comprehensive logs both in console and to your Telegram chat.
*   **Error Resilient**: Handles network issues and continues monitoring automatically.

---

## 🛠️ Installation

Follow these steps to set up the monitoring bot:

1.  **Clone the repository:**
    ```sh
    git clone https://github.com/default034/Gifts-Upgrade-Checker.git
    cd Upgrade-Checker
    ```

2.  **Install dependencies:**
    It's recommended to use a virtual environment.
    ```sh
    pip install -r requirements.txt
    ```

3.  **Configuration:**
    Rename `config.py.example` to `config.py` and update with your credentials:
    *   `API_ID` and `API_HASH`: Obtain from [my.telegram.org](https://my.telegram.org/)
    *   `SESSION`: Your session name (e.g., `"my_account"`)
    *   `TARGET_CHANNEL`: Channel username or ID where upgrade notifications will be sent
    *   `LOG_CHAT`: Chat for receiving bot logs and status updates
    *   `CHECK_INTERVAL_SECONDS`: How often to check for new upgrades

---
## 🤝 Contributing

This project was created for personal use, but I am open to suggestions and contributions. If you have ideas for improvement or find a bug, feel free to create an Issue or a Pull Request.

---

## 📜 License

This project is distributed under the MIT License. See the `LICENSE` file for more information.

---
<p align="center">
  <a href="https://t.me/mlnwstudio">
    <img src="https://img.shields.io/badge/Telegram-Contact_Me-28A8EA?style=for-the-badge&logo=telegram&logoColor=white" alt="Telegram Contact"/>
  </a>
</p>
