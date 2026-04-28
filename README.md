# 🤖 CareerPrep: File-Driven Job-Hunting Agent

## 📌 Project Overview
The **CareerPrep Job-Hunting Agent** is an intelligent career assistant built as part of an **Agentic AI** lab. It automates the tedious parts of the job search—analyzing job posters, identifying skill gaps, tailoring resumes, and tracking applications. 

Instead of using hard-coded strings, this agent is **file-driven**, meaning it dynamically reads data from designated folders to provide real-time career insights.

## 🏗️ GAME Framework Design
This project follows the **GAME Framework** for AI Agents:
* **Goal:** Help students convert scattered job-search material into a structured, automated workflow.
* **Actions:** File reading, keyword extraction, resume matching, and report generation.
* **Memory:** Persistence via `applications.csv` and `reminders.txt` to track history and upcoming tasks.
* **Environment:** A structured local file system utilizing specific input/output directories.

## 📂 Repository Structure
* `input_jobs/`: Place target job descriptions (.txt) here.
* `input_resumes/`: Place your current resume (.txt) here.
* `input_kb/`: Place interview notes or course slides (.txt) here.
* `outputs/`: Where generated reports are saved.
* `tracker/`: Contains the application log and reminders.

## 🚀 Getting Started
1. Clone this repository.
2. Ensure your folders contain your resume and at least one job poster in `.txt` format.
3. Run the agent: `python app.py`.
4. Review the results in the `outputs/` folder.

## 👤 Author
* **Name:** Rana Muhammad Ahmed
* **University:** FAST NUCES , CFD
* **Focus:** AI/ML Engineer

---

## 🌟 Step 9: The "Unique Feature" (Extra 10 Marks)

To make sure you get those 10 marks for "Uniqueness and Creativity," let's add a **LinkedIn Outreach Generator**. This function will create a professional message you can send to recruiters.
---

ready for submission. Do you need help with anything else?**
