# GLOBAL-OLYMPIC-SPORTS-PERFORMANCE-ANALYSIS

A Tableau and Flask project that analyses global Olympic sports performance through interactive visualizations and a structured Tableau Story. The project explores country-wise performance, medal achievements, athlete accomplishments and sports-related trends. The published Tableau Dashboard and Story are integrated into a Flask website, providing a single platform to explore the analysis.

The project is designed for three types of users:

- Sports Analyst: Explores country-wise Olympic performance, medal achievements and trends across sporting disciplines to understand global sports performance.
- Sports Broadcaster: Uses visual insights about countries, athletes and sports to communicate Olympic achievements and highlight notable performances.
- Sports Researcher: Examines patterns in Olympic participation and achievements to understand performance differences across countries and sporting events.

## Project links

|             |                                                                                                                                                                              |
| ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Demo Link   |  https://drive.google.com/file/d/1A4Ew_tG_LI6hgBGwZXlZkrINMqqUESwt/view?usp=sharing                                                                                                                                          |
| GitHub Link |                                                                                                                                            |
| Dashboard   | https://public.tableau.com/app/profile/soumya.gour8185/viz/smartbridge_project/Dashboard2?publish=yes                                      |
| Story Link  | https://public.tableau.com/app/profile/soumya.gour8185/viz/smartbridge_project/Story1?publish=yes                                          |

## Repository structure

```
GLOBAL-OLYMPIC-SPORTS-PERFORMANCE-ANALYSIS/
│
├── app.py
├── config.py
├── requirements.txt
├── Procfile
├── render.yaml
├── README.md
├── .gitignore
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── dashboard.html
│   └── story.html
│
└── static/
    └── css/
        └── style.css
```

## Project Components

| Part                   | What was built                                                                                                    | Where                     |
| ---------------------- | ----------------------------------------------------------------------------------------------------------------- | ------------------------- |
| 1. Project Planning    | Defined the objectives and analytical focus of Global Olympic Sports Performance Analysis.                        | Project documentation     |
| 2. Data Visualization  | Developed interactive Tableau visualizations to explore Olympic performance and related insights.                 | Tableau Public            |
| 3. Dashboard           | Created the Global Olympic Sports Performance Dashboard for exploring the published visual analytics.             | Tableau Public            |
| 4. Story               | Created the Global Olympic Sports Performance Story to present the analysis through a sequence of visualizations. | Tableau Public            |
| 5. Web Development     | Developed a Flask-based website with a landing page and dedicated dashboard and story pages.                      | `templates/`, `app.py`    |
| 6. Tableau Integration | Embedded the published Tableau Dashboard and Story into the Flask website.                                        | `config.py`, `templates/` |
| 7. Deployment          | Prepared the application for public deployment using Gunicorn and Render.                                         | `Procfile`, `render.yaml` |

## Published views on Tableau Public

The project includes two published Tableau views:

- Dashboard: https://public.tableau.com/app/profile/soumya.gour8185/viz/smartbridge_project/Dashboard2?publish=yes
- Story: https://public.tableau.com/app/profile/soumya.gour8185/viz/smartbridge_project/Story1?publish=yes

Both visualizations are embedded into the Flask application, allowing visitors to explore the dashboard and story without navigating away from the website.

## Website features

- Home Page: Introduces the project, its objectives and analytical focus.
- Dashboard Page: Embeds the interactive Tableau dashboard.
- Story Page: Embeds the published Tableau Story.
- Navigation: Provides access to all three website sections.
- Responsive Design: Supports different screen sizes and devices.
- Tableau Integration: Loads published visualizations directly from Tableau Public.

## Technologies used

| Technology     | Purpose                                |
| -------------- | -------------------------------------- |
| Python         | Backend programming                    |
| Flask          | Web application framework              |
| Tableau Public | Data visualization and analysis        |
| HTML5          | Website structure                      |
| CSS3           | Website styling                        |
| JavaScript     | Frontend interactions                  |
| Gunicorn       | Production application server          |
| Render         | Cloud deployment                       |
| Git and GitHub | Version control and repository hosting |

## Run the web app locally

### 1. Clone the repository

```
git clone https://github.com/Soumyagour129/Global-Olympic-Sports-Performance-Analysis.git
```

### 2. Navigate to the project directory

```
cd GLOBAL-OLYMPIC-SPORTS-PERFORMANCE-ANALYSIS
```

### 3. Create a virtual environment

```
python -m venv venv
```

### 4. Activate the virtual environment

Windows:

```
venv\Scripts\activate
```

macOS/Linux:

```
source venv/bin/activate
```

### 5. Install dependencies

```
pip install -r requirements.txt
```

### 6. Run the Flask application

```
python app.py
```

### 7. Open the website

Visit:

```
http://127.0.0.1:5000/
```

## Deploy the application on Render

1. Push the project repository to GitHub.
2. Log in to https://render.com
3. Select New → Web Service.
4. Connect the GitHub repository.
5. Configure the deployment settings:

| Setting       | Value                             |
| ------------- | --------------------------------- |
| Runtime       | Python                            |
| Build Command | `pip install -r requirements.txt` |
| Start Command | `gunicorn app:app`                |

6. Click Deploy Web Service.
7. After successful deployment, Render will provide a public URL for the website.

## Run the web app

Open https://global-olympic-sports-performance-2he8.onrender.com

The embedded views load from Tableau Public, so the computer needs internet access and the workbook must be public (not hidden) on the Tableau Public profile.

## Tableau integration notes

The Flask application embeds the Tableau views using their published URLs.

For the embedded visualizations to work correctly:

- The Tableau workbook and views must be published to Tableau Public.
- The published views must be publicly accessible.
- The dashboard and story URLs must be correctly configured in `config.py`.
- An active internet connection is required to load Tableau visualizations.

## Future enhancements

- Add more Olympic performance comparisons and analytical insights.
- Introduce additional interactive visualizations.
- Expand country-wise and sport-wise performance analysis.
- Improve dashboard filtering and exploration capabilities.
- Add more detailed analytical summaries to the website.

## Author

Soumya Gour

Project: Global Olympic Sports Performance Analysis

Visualization Platform: Tableau Public

Web Framework: Python Flask

This project combines data visualization and web development to make global Olympic sports performance insights accessible through an interactive web platform.

Important: This README follows the structure and professional project-documentation style of your F1 reference. I have intentionally avoided inventing dataset row counts, season coverage, calculated fields, validation results or specific chart types because those details have not been verified from your Olympic workbook.

- Tableau Dashboard: https://public.tableau.com/app/profile/soumya.gour8185/viz/smartbridge_project/Dashboard2?publish=yes
- Tableau Story: https://public.tableau.com/app/profile/soumya.gour8185/viz/smartbridge_project/Story1?publish=yes
