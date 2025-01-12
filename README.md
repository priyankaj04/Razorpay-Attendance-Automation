# Razorpay Attendance Automation

This project automates the process of logging into the Razorpay attendance system and performing check-in/check-out actions based on the current time and day. It uses Selenium WebDriver to interact with the web elements.

## Prerequisites

- Python 3.13
- Google Chrome or Brave browser
- Selenium WebDriver

## Setup

1. Clone the repository:

```sh
git clone https://github.com/yourusername/razorpay-attendance-automation.git
cd razorpay-attendance-automation
```

2. Create a virtual environment and activate it:

```sh
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. Install the required packages:

```sh
pip install -r requirements.txt
```

4. Install the required packages:

```sh
brave_path = "/Applications/Brave Browser.app"  # Update this path
```

## Usage

1. Run the script:

```sh
python main.py
```

2. The script will open the Razorpay attendance website, log in using the provided credentials, and perform the check-in/check-out actions based on the current time and day.

## Configuration

* Update the email and password in ```py main.py``` with your Razorpay login credentials.
* Ensure the locators for the web elements (e.g., ```By.ID```, ```By.XPATH```) are correct and update them if necessary.

## License

This project is licensed under the MIT License.

### Thankyou, Hope this was helpful.