import os
import json
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Fixed list of allowed categories
CATEGORIES = [
    "Food", "Entertainment", "Transport", "Housing", "Subscriptions",
    "Utilities", "Retail", "Clothing", "Fitness", "Pet Supplies",
    "Donations", "Postage & Shipping", "Home Services", "Auto Services",
    "Finance", "Wellness", "Education", "Income", "Other"
]

# Optional: Use caching to avoid hitting OpenAI every time
CACHE_PATH = os.path.join("data", "ai_categories.json")  # updated to match web app structure
os.makedirs(os.path.dirname(CACHE_PATH), exist_ok=True)

# Load or initialize cache
if os.path.exists(CACHE_PATH):
    with open(CACHE_PATH, "r") as f:
        ai_cache = json.load(f)
else:
    ai_cache = {}

# Save cache to file
def save_cache():
    with open(CACHE_PATH, "w") as f:
        json.dump(ai_cache, f, indent=4)

# GPT categorization function
def categorize_with_ai(description):
    desc_key = description.lower().strip()

    if desc_key in ai_cache:
        print(f"Using cached category for '{description}': {ai_cache[desc_key]}")
        return ai_cache[desc_key]

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a financial assistant that classifies transactions into budget categories. "
                        "Choose only ONE of the following categories:\n" +
                        ", ".join(CATEGORIES)
                    )
                },
                {
                    "role": "user",
                    "content": f"Categorize this transaction: '{description}'"
                }
            ]
        )

        raw = response.choices[0].message.content.strip()
        category = raw.replace("Category:", "").strip()

        if category not in CATEGORIES:
            print(f"⚠️ GPT returned unknown category: '{category}', falling back to 'Other'")
            category = "Other"

        print(f"AI categorized '{description}' as: {category}")
        ai_cache[desc_key] = category
        save_cache()
        return category

    except Exception as e:
        print(f"OpenAI API Error: {e}")
        return "Other"

# Apply categorization to a DataFrame
def categorize_transactions(df):
    df["Category"] = "Uncategorized"

    for index, row in df.iterrows():
        if row["Category"] == "Uncategorized":
            category = categorize_with_ai(row["Description"])
            df.at[index, "Category"] = category

    return df
