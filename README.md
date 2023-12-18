# SpeedComplaintBot
SpeedComplaintBot is a Python-based automated tool that tests internet speed using Speedtest.net and tweets at the service provider if the speeds are lower than the promised thresholds.

## Features

- **Automated Internet Speed Test:** Uses Speedtest.net to measure the current download and upload speeds of your internet connection.
- **Twitter Integration:** Automatically logs into Twitter and tweets at your internet service provider if your internet speeds don't match the promised speeds.
- **Customizable Speed Thresholds:** Set your expected download and upload speeds in the script.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed on your system
- Selenium WebDriver for Python
- A Twitter account with credentials
- Chrome browser and ChromeDriver installed

## Installation

Clone the repository to your local machine:

```bash
git clone https://github.com/pserdarakin/SpeedComplaintBot.git

cd SpeedComplaintBot

pip install selenium python-dotenv
```

## Configuration

- Rename .env.example to .env.
- Update the .env file with your Twitter email and password.
- Modify the PROMISED_DOWN and PROMISED_UP values in the script to reflect the download and upload speeds promised by your ISP.

## Usage

Run the script with:
```
python internet_speed_twitter_bot.py
```

## Contributing

Contributions to the project are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (git checkout -b feature/YourFeature).
3. Make your changes.
4. Commit your changes (git commit -am 'Add some feature').
5. Push to the branch (git push origin feature/YourFeature).
6. Open a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.


