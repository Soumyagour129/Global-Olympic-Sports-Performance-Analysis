# Global Olympic Sports Performance Analysis

An Interactive Data Analytics and Visualization Platform

## 1. Project Overview

Global Olympic Sports Performance Analysis is a data analytics project focused on exploring Olympic sports performance, athlete achievements, and country-wise participation and medal statistics.

The project uses Tableau Public to develop interactive visualizations that help users explore Olympic data and understand performance trends. A web application developed using Python Flask provides a centralized platform to access the Tableau Dashboard and Tableau Story.

The primary objective is to transform Olympic data into meaningful insights through interactive visual analytics and an accessible web interface.

## 2. Project Objectives

- Analyze Olympic performance across participating countries.
- Explore medal distribution and country-wise achievements.
- Examine performance across different sporting disciplines.
- Understand athlete participation and achievements.
- Identify patterns and trends in Olympic performance.
- Present analytical findings through interactive Tableau visualizations.
- Develop a web-based platform to make the analysis easily accessible.

## 3. Data Visualization

The project includes two primary Tableau visualizations.

### Tableau Dashboard

The interactive dashboard provides visual insights into Olympic sports performance and allows users to explore the available analytical information.

Dashboard: https://public.tableau.com/app/profile/soumya.gour8185/viz/smartbridge_project/Dashboard2?publish=yes

### Tableau Story

The Tableau Story presents the analysis through a sequence of visualizations, providing a structured approach to understanding the findings.

Story: https://public.tableau.com/app/profile/soumya.gour8185/viz/smartbridge_project/Story1?publish=yes

## 4. Website Features

- Home Page: Provides an introduction to the project, its objectives, and analytical focus.
- Dashboard Page: Embeds the interactive Tableau dashboard.
- Story Page: Embeds the Tableau Story to present the analysis in a narrative format.
- Responsive Interface: Supports different screen sizes and devices.
- Navigation: Provides easy access to all sections of the website.
- Tableau Integration: Allows users to interact with published Tableau visualizations directly through the website.

## 5. Technologies Used

| Technology     | Description                      |
| -------------- | -------------------------------- |
| Python         | Backend programming language     |
| Flask          | Web application framework        |
| Tableau Public | Data visualization and analytics |
| HTML5          | Website structure                |
| CSS3           | Website styling and layout       |
| JavaScript     | Frontend functionality           |
| Gunicorn       | Production WSGI server           |
| Git            | Version control                  |
| GitHub         | Source code management           |
| Render         | Cloud deployment platform        |

## 6. Project Structure

```
global-olympic-sports-performance/
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

## 7. Installation and Setup

Follow the steps below to run the application locally.

### Prerequisites

Ensure that the following software is installed:

- Python 3.x
- Git
- A code editor such as Visual Studio Code

### Step 1: Clone the Repository

```
git clone https://github.com/Soumyagour129/Global-Olympic-Sports-Performance-Analysis.git
```

### Step 2: Navigate to the Project Directory

```
cd global-olympic-sports-performance
```

### Step 3: Create a Virtual Environment

```
python -m venv venv
```

Activate the virtual environment.

Windows:

```
venv\Scripts\activate
```

macOS/Linux:

```
source venv/bin/activate
```

### Step 4: Install Dependencies

```
pip install -r requirements.txt
```

### Step 5: Run the Application

```
python app.py
```

### Step 6: Access the Website

Open the following address in your browser:

```
http://127.0.0.1:5000/
```

## 8. Deployment

The application can be deployed using Render.

### Deployment Steps

1. Upload the project to a GitHub repository.
2. Log in to https://render.com
3. Select New Web Service.
4. Connect the GitHub repository.
5. Configure the deployment settings.

| Configuration | Value                             |
| ------------- | --------------------------------- |
| Runtime       | Python                            |
| Build Command | `pip install -r requirements.txt` |
| Start Command | `gunicorn app:app`                |

6. Click Deploy Web Service.
7. After successful deployment, Render generates a public URL for accessing the application.

## 9. Expected Outcomes

- A comprehensive visual exploration of Olympic sports performance.
- Improved understanding of country-wise and sport-wise performance.
- Interactive access to Olympic data visualizations.
- A structured presentation of analytical findings through Tableau Story.
- Integration of data analytics and web development technologies.
- A publicly accessible platform for presenting the project.

## 10. Future Enhancements

- Incorporate additional Olympic datasets and performance indicators.
- Introduce advanced filtering and comparison capabilities.
- Expand the range of interactive visualizations.
- Include additional statistical analysis and insights.
- Improve website functionality and user experience.

## 11. Author

Soumya Gour

Project Title: Global Olympic Sports Performance Analysis

Visualization Platform: Tableau Public

Backend Framework: Python Flask

Project Links

- Tableau Dashboard: [https://public.tableau.com/app/profile/soumya.gour8185/viz/smartbridge_project/Dashboard2?publish=yes](https://public.tableau.com/app/profile/soumya.gour8185/viz/smartbridge_project/Dashboard2?publish=yes)
- Tableau Story: [https://public.tableau.com/app/profile/soumya.gour8185/viz/smartbridge_project/Story1?publish=yes](https://public.tableau.com/app/profile/soumya.gour8185/viz/smartbridge_project/Story1?publish=yes)
