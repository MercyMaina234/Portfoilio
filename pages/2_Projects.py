import streamlit as st

st.set_page_config(page_title="My Projects", layout="wide")

st.title("🧩 My Projects")
st.write("Here are some of the projects I’ve worked on, showcasing my skills in web development, data analysis, and application design.")
project_list = [
{
        "title": "📦 Portfolio Web App",
        "description": "A personal web portfolio built with Streamlit to showcase my skills, projects, and background.",
        "technologies": ["Python", "Streamlit", "HTML", "CSS"],
        "features": [
            "Multi-page layout",
            "Responsive UI",
            "Interactive project sections",
        ],
        "github": "https://github.com/MercyMaina234/Portfoilio_App",
    },
    {
        "title": "📦 Python Quiz app",
        "description": "A small python based project of a sample quiz app",
        "technologies": ["Python"],
        "features": [
            "Multi-page layout",
            "Responsive UI",
            "Interactive project sections",
        ],
        "github": "https://github.com/MercyMaina234/Quiz-app",
    },
    {
        "title": "Jupyter Notebook Python basics ",
        "description": "Short codes that showcase basic python functionalities and their Syntax ",
        "technologies": ["Python"],
        "features": [
            "Python Syntax",
            "Short Python projects"
        ],
        "github": "https://github.com/MercyMaina234/PythonFundamentals",
    },
    {
        "title": "📊 Titanic data Analysis",
        "description": "A data analysis project using pandas to filter, sort, and give insights about the chance of survival on the titanic.",
        "technologies": ["Python", "pandas"],
        "features": [
            "Data cleaning & filtering",
            "Survival rate analysis based on various factors",
            "Survival rate insights",
        ],
        "github": "https://github.com/MercyMaina234/Titanic-",
    },
    {
        "title": "Ronaldo Vs Messi EDA ",
        "description": "A data analysis project using pandas to filter, sort, and give insights on the who's the greatest of all time between Messi and Ronaldo.",
        "technologies": ["Python", "pandas"],
        "features": [
            "Data cleaning & filtering",
            "Total games scored analysis based on various factors",
            "Total Games Scored insights",
        ],
        "github": "https://github.com/MercyMaina234/GOAT",


    }
]
for project in project_list:
    with st.container():
        st.subheader(project["title"])
        st.write(project["description"])
        st.markdown(f"**Technologies:** {', '.join(project['technologies'])}")
        st.markdown("**Key Features:**")
        for feat in project["features"]:
            st.markdown(f"- {feat}")
        st.markdown(f"[🔗 View on GitHub]({project['github']})")
        st.markdown("---")