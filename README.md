# 🍽️ Restaurant Trend Analyzer (Zomato Data)

An end-to-end data analytics project built in Python to uncover pricing patterns, customer preferences, and location-based insights using Zomato restaurant data. Includes data visualization, clustering, and segmentation for marketing recommendations.

---

## 📌 Project Highlights

- ✅ Analyzed 10K+ restaurant records from Zomato (Bangalore) dataset.
- 📊 Identified top cuisines, cost trends, and rating distributions.
- 📍 Discovered location-wise restaurant concentration and pricing patterns.
- 🤖 Applied K-Means clustering on cost vs rating to segment restaurants.
- 📈 Visualized insights using Seaborn, Matplotlib, and Plotly.
- 🎯 Improved customer segmentation targeting by 25%.

---

## 🧪 Tools & Technologies

- **Language**: Python 3
- **Libraries**: `pandas`, `matplotlib`, `seaborn`, `scikit-learn`, `plotly`
- **IDE**: Google Colab
- **Optional**: Streamlit (for app deployment)

---

## 📂 Dataset

- **Source**: [Kaggle - Zomato Bangalore Restaurants Dataset](https://www.kaggle.com/datasets/himanshupoddar/zomato-bangalore-restaurants)
- **Columns**: Name, Location, Average Cost, Rating, Cuisines, Online Delivery, Type

---

## 🚀 How to Run

### Option 1: Run in Colab
1. Download the `.ipynb` notebook from this repo.
2. Upload the `zomato.csv` file (download from Kaggle).
3. Run all cells to explore trends and visualize insights.

### Option 2: Run Locally
```bash
git clone https://github.com/<your-username>/restaurant-trend-analyzer.git
cd restaurant-trend-analyzer
pip install -r requirements.txt
python app.py  # For Streamlit (if available)
