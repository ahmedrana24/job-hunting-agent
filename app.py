import os
import csv
from datetime import datetime

# --- 1. CONFIGURATION (Environment) --- [cite: 123-136]
JOB_DIR = "input_jobs"
RESUME_DIR = "input_resumes"
KB_DIR = "input_kb"
OUTPUT_DIR = "outputs"
TRACKER_DIR = "tracker"

# Keywords for skill matching [cite: 131-136]
KEYWORDS = [
    "python", "machine learning", "deep learning", "sql", "git", "github",
    "api", "prompt engineering", "communication", "problem solving",
    "pandas", "numpy", "streamlit", "docker", "aws", "ci/cd", "fastapi"
]

# --- 2. CORE UTILITIES (Actions) --- [cite: 137-147]
def ensure_folders():
    """Creates the required project folders if they don't exist."""
    for folder in [JOB_DIR, RESUME_DIR, KB_DIR, OUTPUT_DIR, TRACKER_DIR]:
        os.makedirs(folder, exist_ok=True)

def read_text_files(folder):
    """Reads all .txt files in a folder and combines their content."""
    combined_text = ""
    file_count = 0
    for filename in os.listdir(folder):
        if filename.lower().endswith(".txt"):
            path = os.path.join(folder, filename)
            with open(path, "r", encoding="utf-8") as file:
                combined_text += f"\n\n--- FILE: {filename} ---\n"
                combined_text += file.read()
                file_count += 1
    return combined_text, file_count

def save_text(path, content):
    """Saves generated text to a specific file path."""
    with open(path, "w", encoding="utf-8") as file:
        file.write(content)

# --- 3. ANALYSIS LOGIC (Actions & Memory) --- [cite: 148-160]
def extract_keywords(text):
    """Extracts predefined keywords from the provided text."""
    text_lower = text.lower()
    found = []
    for keyword in KEYWORDS:
        if keyword in text_lower:
            found.append(keyword)
    return found

def compare_skills(job_skills, resume_skills):
    """Matches job requirements against resume skills and calculates a score."""
    matched = [skill for skill in job_skills if skill in resume_skills]
    missing = [skill for skill in job_skills if skill not in resume_skills]
    score = 0 if not job_skills else round((len(matched) / len(job_skills)) * 100, 2)
    return matched, missing, score

# --- 4. REPORT GENERATORS --- [cite: 161-200]
def generate_job_analysis(job_text, job_skills):
    report = "Job Analysis Report\n===================\n\n"
    report += "Skills/keywords found in job posters:\n"
    for skill in job_skills:
        report += f"- {skill}\n"
    return report

def generate_skill_gap_report(job_skills, resume_skills, matched, missing, score):
    report = "Skill Gap Report\n================\n\n"
    report += f"Match Score: {score}%\n\n"
    report += "Matched Skills:\n"
    for skill in matched:
        report += f"- {skill}\n"
    report += "\nMissing Skills:\n"
    for skill in missing:
        report += f"- {skill}\n"
    return report

def generate_resume_suggestions(job_skills, missing):
    output = "Tailored Resume Suggestions\n===========================\n\n"
    output += "Suggested improvements according to job posters:\n"
    for skill in job_skills:
        output += f"- Add or improve resume evidence related to {skill}.\n"
    output += "\nSuggested resume bullets:\n"
    output += "- Developed Python-based academic projects with clear documentation.\n"
    output += "- Used GitHub for project version control and README-based documentation.\n"
    if missing:
        output += "\nSkills to improve before applying/interview:\n"
        for skill in missing:
            output += f"- {skill}\n"
    return output

def generate_interview_questions(job_skills, kb_text):
    questions = "Interview Questions\n===================\n\n"
    questions += "Technical questions based on job posters:\n"
    for skill in job_skills:
        questions += f"- Explain your understanding of {skill}.\n"
        questions += f"- How have you used {skill} in a project or course activity?\n"
    questions += "\nQuestions inspired by KB/slides:\n"
    kb_lines = [line.strip("-").strip() for line in kb_text.splitlines() if line.strip()]
    for line in kb_lines[:10]:
        questions += f"- How would you explain this point in an interview: {line}?\n"
    return questions

# --- 5. TRACKER & REMINDERS --- [cite: 201-241]
def create_or_update_tracker():
    path = os.path.join(TRACKER_DIR, "applications.csv")
    if not os.path.exists(path):
        with open(path, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([
                "application_id", "company", "role", "source", "status",
                "applied_date", "interview_date", "follow_up_date", "next_action", "notes"
            ])
            writer.writerow([
                "APP-001", "Tech-Vision Corp", "Junior AI Engineer", "LinkedIn",
                "Not Applied", "2026-04-28", "", "", "Tailor resume and apply", "Sample entry"
            ])
    return path

def generate_reminders():
    tracker_path = os.path.join(TRACKER_DIR, "applications.csv")
    reminders = "Application Reminders\n=====================\n\n"
    if not os.path.exists(tracker_path): return "No tracker file found."
    with open(tracker_path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            status = row.get("status", "").lower()
            if status == "not applied":
                reminders += f"- {row['application_id']}: Tailor resume for {row['role']} at {row['company']}.\n"
            elif status == "interview scheduled":
                reminders += f"- {row['application_id']}: Interview at {row['company']} on {row['interview_date']}.\n"
    return reminders

 # --- UNIQUE FEATURE: LinkedIn Outreach Generator --- [cite: 308, 338]
def generate_linkedin_message(company, role):
    message = "LinkedIn Outreach Message\n=========================\n\n"
    message += f"Hi [Recruiter Name],\n\n"
    message += f"I recently applied for the {role} position at {company} and am very excited about the opportunity. "
    message += f"With my background in AI/ML engineering and MLOps, I am confident I can contribute effectively to your team.\n\n"
    message += "I've attached my tailored resume for your review. Looking forward to hearing from you!\n\n"
    message += "Best regards,\nRana Muhammad Ahmed"
    return message

# --- 6. MAIN EXECUTION (The Brain of the Agent) ---
def run_agent():
    # A. Ensure all folders exist [cite: 243]
    ensure_folders()
    
    # B. Read inputs from folders [cite: 244-246]
    job_text, job_count = read_text_files(JOB_DIR)
    resume_text, resume_count = read_text_files(RESUME_DIR)
    kb_text, kb_count = read_text_files(KB_DIR)
    
    # C. Safety Check: If folders are empty, stop and warn the user [cite: 247-248]
    if job_count == 0 or resume_count == 0 or kb_count == 0:
        print("\n[!] ERROR: Please add .txt files in input_jobs, input_resumes, and input_kb folders.")
        return

    # D. Process data using keyword extraction [cite: 249-252]
    job_skills = extract_keywords(job_text)
    resume_skills = extract_keywords(resume_text)
    matched, missing, score = compare_skills(job_skills, resume_skills)
    
    # E. Generate individual reports [cite: 253-256]
    job_report = generate_job_analysis(job_text, job_skills)
    gap_report = generate_skill_gap_report(job_skills, resume_skills, matched, missing, score)
    resume_suggestions = generate_resume_suggestions(job_skills, missing)
    interview_questions = generate_interview_questions(job_skills, kb_text)
    
    # F. UNIQUE FEATURE: LinkedIn Outreach Generator [cite: 299, 308]
    # We use 'Tech-Vision Corp' as a placeholder; in a real app, this would be dynamic
    outreach_msg = generate_linkedin_message("Tech-Vision Corp", "Junior AI Engineer")
    
    # G. Update the tracker and reminders [cite: 257-258]
    create_or_update_tracker()
    reminders = generate_reminders()
    
    # H. Create the Final Master Report [cite: 259-266]
    final_report = "CareerPrep Job-Hunting Agent Report\n"
    final_report += f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
    final_report += "====================================\n\n"
    final_report += job_report + "\n"
    final_report += gap_report + "\n"
    final_report += resume_suggestions + "\n"
    final_report += interview_questions + "\n"
    final_report += outreach_msg + "\n" # Adding the LinkedIn message to final report
    final_report += reminders + "\n"
    
    # I. Save all outputs to their respective folders [cite: 267-271]
    save_text(os.path.join(OUTPUT_DIR, "job_analysis_report.txt"), job_report)
    save_text(os.path.join(OUTPUT_DIR, "skill_gap_report.txt"), gap_report)
    save_text(os.path.join(OUTPUT_DIR, "tailored_resume_suggestions.txt"), resume_suggestions)
    save_text(os.path.join(OUTPUT_DIR, "interview_questions.txt"), interview_questions)
    save_text(os.path.join(OUTPUT_DIR, "linkedin_outreach.txt"), outreach_msg)
    save_text(os.path.join(OUTPUT_DIR, "final_agent_report.txt"), final_report)
    save_text(os.path.join(TRACKER_DIR, "reminders.txt"), reminders)
    
    # J. Console Success Message with Visual Score Gauge (Unique Idea) [cite: 272-277, 299]
    print("\n" + "="*40)
    print("      AGENT COMPLETED SUCCESSFULLY")
    print("="*40)
    
    # Create a visual text-based progress bar for the Match Score
    bar_length = 20
    filled_length = int(bar_length * score // 100)
    gauge = '█' * filled_length + '-' * (bar_length - filled_length)
    
    print(f"Match Score: |{gauge}| {score}%")
    print(f"Files Processed: Jobs({job_count}), Resumes({resume_count}), KB({kb_count})")
    print("Check the 'outputs/' and 'tracker/' folders for your reports!")
    print("="*40)

if __name__ == "__main__":
    run_agent()