## Note:
- This project is using Python 3.11.8
- The commands worked on Windows PowerShell

## Development Setup
```bash
# Create virtual environment (Development only)
python -m venv .venv
.\.venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Run Locally
```bash
cd dashboard
streamlit run dashboard.py
```

## Deployment
This app is deployed on Streamlit Cloud:
1. Ensure data file is in the dashboard folder
2. Push changes to GitHub:
   ```bash
   git add .
   git commit -m "Update for deployment"
   git push origin main
   ```
3. Deploy on [Streamlit Cloud](https://streamlit.io/cloud)
   - Select dashboard/dashboard.py as the main file
   - No need to set up virtual environment (handled by Streamlit Cloud)

## Features
- Analisis pola polutan apda setiap musim
- Korelasi antara kondisi cuaca dengan udara tingkat PM2.5
- Visualisasi yang interaktif

## Author
- **Name:** Faturrachman
- **Email:** faturrachman6773@gmail.com
- **Dicoding ID:** Faturrachman 