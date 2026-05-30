-----------------Structure-------------
Project_Root/
│
├── Backend/
│   ├── app.py                # Backend API (handles MongoDB connections)
│   ├── .env                  # Environment variables (MONGO_URI)
│   └── requirements.txt      # Python dependencies
│
└── Frontend/
    ├── app.py                # Frontend web server (serves HTML & sends requests)
    └── templates/
        └── index.html        # Styled HTML form

