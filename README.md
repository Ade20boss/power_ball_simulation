# 🎰 Powerball Lottery Simulator

A Python-based simulation tool to demonstrate the mechanics and odds of the U.S. Powerball lottery. Enter your lucky numbers and see the aggregated results of playing those numbers across thousands, or even a million, simulated draws!

## ✨ Features

* **Interactive Input:** Easily enter your 5 white ball numbers (1-69) and 1 Powerball number (1-26).
* **Mass Simulation:** Run up to **1,000,000** simulated draws per run to quickly analyze the long-term expected returns.
* **Accurate Prize Mapping:** Uses the official Powerball prize tiers to calculate winnings based on matches.
* **Total Winnings Calculation:** Calculates the total cost, total winnings, and net gain/loss over the entire simulation period.
* **Robust Validation:** Features reliable input validation to ensure numbers are unique, within range, and numeric.

## 🚀 Getting Started

### Prerequisites

You only need Python 3 installed on your system.

```bash
python --version
```

---
## Installation
Clone the repository:
```
git clone [https://github.com/YourUsername/your-repository-name.git](https://github.com/YourUsername/your-repository-name.git)
cd powerball-simulator
```

---
##How to Run
Execute the script directly from your terminal:
```
python powerball_simulator.py
```
Follow the on-screen prompts to enter your numbers and the number of times you wish to play.

---
##Core Logic
The simulator uses the following Powerball rules:

| White Balls Matched | Powerball Matched | Prize Amount |
| :-----------------: | :---------------: | :----------: |
| 5                   | Yes               | Jackpot      |
| 5                   | No                | $1,000,000   |
| 4                   | Yes               | $50,000      |
| 4                   | No                | $100         |
| 3                   | Yes               | $100         |
| 3                   | No                | $7           |
| 2                   | Yes               | $7           |
| 1                   | Yes               | $4           |
| 0                   | Yes               | $4           |

Note: For the purpose of calculation, the Jackpot prize is set to a fixed value of $400,000,000.

----

🤝 Contribution
Feel free to fork the repository and submit pull requests! Ideas for improvement include:

Tracking and printing detailed Prize Breakdown statistics.

Allowing the Jackpot value to be configured by the user.

Adding command-line arguments for non-interactive simulation.

---

⚖️ License
This project is licensed under the MIT License - see the LICENSE.md file for details.

