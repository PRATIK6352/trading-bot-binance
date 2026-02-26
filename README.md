# 📈 Binance Futures Trading Bot (Testnet)

A lightweight Python trading bot with a Streamlit-based web UI that allows users to place **Market and Limit orders** on **Binance Futures Testnet**, monitor open positions, view order history, and check account balance in real time.

This project demonstrates **API integration, trading order execution, validation, logging, and UI development** using Python.

---

## 🚀 Features

* Market and Limit order execution (BUY / SELL)
* Trade BTCUSDT perpetual futures (Testnet)
* Real-time order execution using Binance Futures API
* Interactive Streamlit UI
* View current open position (Long / Short)
* View recent order history
* Account balance monitoring (USDT)
* Minimum notional validation (Binance rule)
* Quantity precision handling based on symbol step size
* Error handling with user-friendly UI messages
* Secure API key management using `.env`
* Logging for debugging and tracking order execution

---

## 🧠 Trading Concepts Demonstrated

* Market vs Limit orders
* Long vs Short positions
* Futures contracts (BTCUSDT perpetual)
* Notional value validation
* Exchange precision & lot size constraints
* Order vs Position difference

---

## 🛠 Tech Stack

* Python 3.x
* Streamlit (UI)
* Binance Futures API (Testnet)
* Pandas
* python-binance
* python-dotenv

---

## 📂 Project Structure

```
trading_bot/
│
├── bot/
│   ├── client.py            # Binance API client
│   ├── orders.py            # Order execution & exchange logic
│   ├── validators.py        # Input validation
│   └── logging_config.py    # Logging setup
│
├── app.py                   # Streamlit UI (main dashboard)
├── cli.py                   # CLI-based trading interface
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Setup Instructions

### 1. Clone Repository

```bash
git clone https://github.com/PRATIK6352/trading-bot-binance.git
cd trading-bot-binance
```

---

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3. Create Binance Futures Testnet Account

Go to:

https://testnet.binancefuture.com

* Login using GitHub/Google
* Generate **API Key** and **Secret Key**
* Use **Testnet only (no real money required)**

---

### 4. Configure Environment Variables

Create a `.env` file in project root:

```
API_KEY=your_testnet_api_key
API_SECRET=your_testnet_api_secret
```

⚠️ Never commit `.env` to GitHub.

---

### 5. Run Streamlit UI

```bash
streamlit run app.py
```

Open in browser:

```
http://localhost:8501
```

---

## 🧭 How the System Works

### Market Order

Executes instantly at the best available market price.

### Limit Order

Executes only when the market reaches the specified price.

### Dashboard Displays

* Order execution details
* Current open position (Long / Short)
* Recent order history
* Account balance (USDT)

---

## 📊 Example Usage

* Place BUY Market order → Opens LONG position
* Place SELL Market order → Opens SHORT or closes LONG
* Place LIMIT order → Waits until price is matched
* Monitor order status & execution
* Track open position and unrealized PnL

---

## 🔐 Security Notes

* Uses **Binance Futures Testnet only**
* No real funds involved
* API keys stored securely in `.env`
* `.env` excluded using `.gitignore`

---

## 🧪 Common Errors Handled

* Minimum notional (< 100 USDT)
* Quantity precision issues
* Invalid symbol / side / order type
* Exchange API errors
* Position fetching failures

---

## 📈 Possible Future Improvements

* Stop-loss / Take-profit orders
* Cancel open order feature
* Live BTC price ticker
* Auto-refresh dashboard
* Strategy-based trading logic
* Docker containerization
* Deployment on Streamlit Cloud

---

## 🎓 Learning Outcomes

This project demonstrates:

* REST API integration
* Real-time trading system basics
* Futures trading concepts
* Error handling & validation
* Secure credential handling
* UI development with Streamlit
* Clean modular Python architecture

---

## 👨‍💻 Author

**Pratik Patil**
Python Developer | API Integration | Trading Systems

---

## ⭐ If you found this useful

Feel free to star ⭐ the repository.
