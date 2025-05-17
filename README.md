# MITPA Bot Watchdog — Auto-Restart & Multilingual Status Monitoring

> 🛰️ Automatic bot monitoring and recovery system for MIT Preparation Academy's beta bot.
## Overview

**MITPA Bot Watchdog** is a local monitoring utility built to ensure that the MITPA beta bot, hosted on **Discloud**, stays online.  
If the bot goes offline while the Discord API is operational, this system automatically restarts the bot locally and notifies the admin — all while supporting multilingual status messages for global accessibility.

---

## 🌟 Purpose

- Automatically detect if the MITPA beta bot is offline.
- Distinguish between bot failure and Discord API outages.
- Restart the bot locally via Node.js in a separate desktop workspace.
- Send real-time notifications to Discord for transparency.
- Allow each user to set their preferred language for status messages.

---

## Features

### ⚙️ Auto-Restart System
- Verifies if the Discord API is operational.
- Checks bot availability on Discloud.
- Starts the bot locally using `node index.js` if offline.

### 🔔 Admin Notifications
- Windows desktop toast notifications to alert the system admin when the bot goes down and is restarted.

### 🌐 Multilingual Interface
- Users can change the language of status messages with an interactive button.
- Language selection only affects the user who clicked the button (not everyone).

### ✅ Built-in Testing
- Pytest-powered test suite to verify system components.
- GitHub Actions CI workflow for test automation.

---

## 🛠️ Tech Stack

- **Python (.pyw)** — Silent local monitoring with GUI-less execution.
- **Node.js** — Runtime environment for the Discord bot.
- **Discord.py** — Communication with Discord API.
- **Googletrans** — Language translation.
- **PyWin32 / win10toast** — Desktop notifications (Windows only).
- **GitHub Actions** — CI for testing.
