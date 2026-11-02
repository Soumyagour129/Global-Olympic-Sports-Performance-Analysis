# Global Olympic Sports Performance Analysis

A web-based project portal for exploring Olympic sports performance through an interactive Tableau Public dashboard.

## Live links

- **Website:** Add your deployed Render URL here.
- **Tableau Dashboard:** [Open the interactive dashboard](https://public.tableau.com/app/profile/soumya.gour8185/viz/smartbridge_project/Dashboard2?publish=yes)

## Overview

Global Olympic Sports Performance Analysis presents Olympic-related data through interactive visual analytics. The project website provides an introduction to the analysis and an embedded Tableau dashboard for exploration.

The analysis can be used to investigate patterns across countries, sports, athletes and medal outcomes, depending on the dimensions available in the published Tableau workbook. The website includes a guided Story page that frames these as exploration questions; it does not invent results or assume fields that have not been verified.

## Features

- Responsive project landing page
- Dedicated project Story page with a five-chapter narrative walkthrough
- Dedicated dashboard page
- Embedded Tableau Public visualization
- Direct link to open the dashboard on Tableau
- Sections describing the project focus and technology

## Technology

- Python and Flask
- HTML5 and CSS3
- Tableau Public
- Gunicorn
- GitHub
- Render

## Run locally

1. Install Python 3.10 or later.
2. Clone or download this repository.
3. Open a terminal in the project directory.
4. Create and activate a virtual environment (recommended).

### Windows PowerShell

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python app.py
```

Open <http://127.0.0.1:5000>.

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python app.py
```

## Deploy on Render

1. Push this project to a GitHub repository.
2. In Render, choose **New → Web Service** and connect the repository.
3. Use these settings:

| Setting | Value |
|---|---|
| Runtime | Python |
| Build command | `pip install -r requirements.txt` |
| Start command | `gunicorn app:app` |
| Root directory | Leave blank |

4. Deploy the service. Render will provide a public URL.

## Project structure

```text
global-olympic-sports-performance/
├── app.py
├── config.py
├── requirements.txt
├── Procfile
├── render.yaml
├── README.md
├── templates/
│   ├── base.html
│   ├── index.html
│   └── dashboard.html
└── static/
    └── css/
        └── style.css
```

## Data documentation

Add the source dataset name, time period, row count, field descriptions, cleaning steps and data-source attribution here after confirming them from the Tableau workbook and original dataset. Do not assume these values.

## Screenshots

Add screenshots of the homepage and embedded Tableau dashboard here.

## Notes

The Tableau visualization is hosted by Tableau Public. An internet connection is required to load the embedded dashboard. If embedding is unavailable, use the direct Tableau link above. The Story page is a website-based narrative walkthrough because the supplied Tableau link points to a dashboard; a separate Tableau Story URL was not supplied.

## Author

Add your name, institution and project acknowledgements here.


## Tableau views

- Dashboard: https://public.tableau.com/app/profile/soumya.gour8185/viz/smartbridge_project/Dashboard2?publish=yes
- Tableau Story: https://public.tableau.com/app/profile/soumya.gour8185/viz/smartbridge_project/Story1?publish=yes

The website provides separate `/dashboard` and `/story` pages, each embedding its corresponding Tableau Public view.
