<div align="center">

# 🌤️ RAj Weather App

### *A Modern Python Weather Application with Real-Time Data*

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)
![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20Windows%20%7C%20macOS-lightgrey)

</div>

---

## 📋 Table of Contents
- [Overview](#-overview)
- [Features](#-features)
- [Screenshots](#-screenshots)
- [Technology Stack](#-technology-stack)
- [Installation](#-installation)
- [Usage](#-usage)
- [API Reference](#-api-reference)
- [Project Structure](#-project-structure)
- [Error Handling](#-error-handling)
- [Future Enhancements](#-future-enhancements)
- [Author](#-author)
- [License](#-license)

---

## 🎯 Overview

**RAj Weather App** is a feature-rich desktop application built with Python Tkinter that provides real-time weather information for cities worldwide. It leverages the OpenWeatherMap API to deliver accurate and up-to-date weather data with an intuitive user interface.

### 🎨 Problem Statement
Traditional weather checking methods require opening browsers or mobile apps. This application provides a lightweight, dedicated desktop solution with a clean interface for quick weather lookups.

### 🌟 Objectives
- Provide instant weather information
- User-friendly graphical interface
- Real-time data fetching
- Cross-platform compatibility

---

## ✨ Features

| Category | Features |
|----------|----------|
| **🌡️ Weather Data** | • Current Temperature (°C) • Weather Description • "Feels Like" Temperature |
| **📊 Additional Metrics** | • Humidity Percentage • Wind Speed (km/h) • Atmospheric Pressure (hPa) • Visibility Distance |
| **🎨 User Interface** | • Modern Dark Theme • Responsive Card Layout • Weather-Based Background Colors • Real-time Date & Time |
| **⚡ Functionality** | • City Search • Enter Key Support • Loading States • Error Handling • Internet Connection Detection |
| **🛡️ Error Management** | • Invalid City Names • Network Issues • API Timeouts • Graceful Fallbacks |

---

## 📸 Screenshots

<div align="center">

### Main Interface
┌─────────────────────────────────────────┐
│ 🌤️ RAj Weather │
│ │
│ [Enter city name...] [🔍 Search] │
│ │
│ ┌─────────────────────────────────────┐│
│ │ 📍 Mumbai ││
│ │ Friday, March 21, 2026 | 3:30 PM││
│ │ ││
│ │ 28.5°C ││
│ │ Clear Sky ││
│ │ ││
│ │ 💧 65% 💨 12km/h 📊 1013hPa ││
│ └─────────────────────────────────────┘│
└─────────────────────────────────────────┘


### Weather Variations

| Weather Type | Background Color |
|--------------|------------------|
| ☀️ Clear | Dark Blue |
| ☁️ Clouds | Dark Gray |
| 🌧️ Rain | Deep Blue |
| ❄️ Snow | Light Blue |
| ⛈️ Thunderstorm | Very Dark Blue |

</div>

---

## 🛠️ Technology Stack

| Technology | Purpose | Version |
|------------|---------|---------|
| **Python** | Core Programming Language | 3.8+ |
| **Tkinter** | GUI Framework | Built-in |
| **Requests** | HTTP API Calls | 2.28+ |
| **OpenWeatherMap API** | Weather Data Source | 2.5 |
| **Git** | Version Control | Latest |

---

## 💻 Installation

### Prerequisites

```bash
# Python 3.8 or higher
python3 --version

# pip package manager
pip3 --version
