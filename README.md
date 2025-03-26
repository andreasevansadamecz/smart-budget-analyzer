# Smart Budget Analyzer

Smart Budget Analyzer is a web-based personal finance tool that helps you understand and manage your spending by analyzing your bank transaction CSV files.

## 🚀 Features

- Upload CSV bank statements directly from the web interface
- AI-powered transaction categorization using OpenAI's GPT API
- Automatic caching to reduce API usage and cost
- Interactive pie chart showing spending by category
- Monthly income/expense summaries
- Clean and intuitive interface built with Flask

## 🛠 Tech Stack

- Python, Flask
- Pandas for data processing
- Matplotlib for data visualization
- OpenAI API for intelligent transaction categorization
- HTML/CSS (vanilla) for frontend

## 🧠 AI Categorization

The app uses GPT to assign each transaction a category from a predefined set:
```
Food, Entertainment, Transport, Housing, Subscriptions,
Utilities, Retail, Clothing, Fitness, Pet Supplies,
Donations, Postage & Shipping, Home Services, Auto Services,
Finance, Wellness, Education, Income, Other
```

The category is cached to avoid redundant API calls and reduce costs.

## 🧪 Usage

1. Clone the repo:
   ```
   git clone https://github.com/andreasevansadamecz/smart-budget-analyzer.git
   cd smart-budget-analyzer
   ```

2. Set up your virtual environment and install dependencies:
   ```
   python -m venv .venv
   .venv\Scripts\activate     # On Windows
   pip install -r requirements.txt
   ```

3. Add your OpenAI API key in a `.env` file:
   ```
   OPENAI_API_KEY=your_key_here
   ```

4. Run the app:
   ```
   python app.py
   ```

5. Open your browser to `http://127.0.0.1:5000` and upload a CSV file!

## 📁 Project Structure

```
smart-budget-analyzer/
│
├── app.py                # Flask app
├── requirements.txt
├── templates/            # HTML templates
├── src/                  # Python modules (categorizer, parser, summary, visualizer)
├── static/               # Pie chart output
├── uploads/              # Uploaded CSVs
├── data/                 # Cached categories
└── .env                  # API key (not tracked)
```

## 📌 Note

Make sure to **exclude sensitive files** from version control using `.gitignore`. This includes:
- `.env`
- `/data/`
- `/uploads/`
- `/static/`
- `.venv/`

## 🧑‍💻 Author

Andreas Evans-Adamecz  
Computer Programming and Analysis student  
[GitHub](https://github.com/andreasevansadamecz)
