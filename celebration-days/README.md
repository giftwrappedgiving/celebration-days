# Celebration Days Project

This project provides an interface to celebrate various special days throughout the year. It allows users to query the next upcoming celebration day and retrieve specific celebration details in JSON format.

## Project Structure

```
celebration-days
├── src
│   ├── __init__.py
│   ├── main.py
│   ├── celebration_interface.py
│   └── utils.py
├── data
│   ├── celebration-day.csv
│   └── historical-figure.csv
├── requirements.txt
└── README.md
```

## Setup Instructions

1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd celebration-days
   ```

2. **Install dependencies**:
   It is recommended to use a virtual environment. You can create one using:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
   Then install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. **Run the application**:
   Execute the main script to start the application:
   ```
   python src/main.py
   ```

2. **Querying Celebration Days**:
   - To get the next celebration day, the application will automatically determine and display it.
   - To retrieve details of a specific celebration day, you can input the reference name (e.g., `world-book-day-uk`) and receive the information in JSON format.

## Dependencies

- `pandas`: For data manipulation and processing.
- Additional dependencies can be added to `requirements.txt` as needed.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
