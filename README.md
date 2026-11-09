# CA Final SPOM Intelligence-Driven Testing Portal
### Comprehensive Exam Intelligence, 10 Practice Modes, Quick Revision Handbook & 100M CBT Simulator
**Set A: Corporate and Economic Laws** (Part I: 70M | Part II: 30M)  
**Set B: Strategic Cost & Performance Management** (Part I: 50M | Part II: 50M)

---

## 🌟 Executive Overview
This portal is an **examination intelligence system** built specifically to help CA Final students clear the mandatory **ICAI Self-Paced Online Modules (SPOM)** with zero wasted study time and maximum conceptual retention.

Engineered strictly in compliance with the **Master Design Specification** (`SPOM Portal.txt`):
1. **Official ICAI Weightage Structure**: Strict 70/30 split for Set A and 50/50 split for Set B.
2. **Explainable 0–100 Priority Scoring**: Topic ranking model based on 5 weighted pillars.
3. **"What Should I Study Today?" Recommender**: Algorithmic daily focus generator.
4. **Important Topics & Quick Revision Handbook**: Ultra-short revision sheets, statutory limits, formulas, and head-to-head comparison tables.
5. **Intelligent Practice Engine (10 Modes)**: Instant conceptual feedback with why every option A/B/C/D is right or wrong, statutory citations, and exam trap alerts.
6. **TCS iON CBT 100M Simulator**: 50 questions x 2 marks = 100 marks, 180m countdown, 5-state palette, Section tabs, dynamic option shuffling, and 50% passing cutoff.
7. **My Mistakes Book**: Automated error logging with spaced revision status (`Unrevised` ➔ `Reviewed` ➔ `Mastered`) and revision notes.
8. **Research Ingestion & Audit Log**: Source provenance tracking for ICAI BoS, Reddit `r/CharteredAccountants` student recalls, and YouTube faculty lectures.
9. **Syllabus & Amendment Control**: Version tracking for ICAI New Education & Training Scheme 2024–2025.

---

## 🏗️ Architectural Overview & Core Modules

### 1. 🎯 Exam Intelligence Centre
- **0–100 Explainable Priority Scoring Model**:
  - **ICAI BoS Study Material Relevance (25%)**
  - **Student Examination Recall Frequency (25%)**
  - **Faculty Recommendations (20%)**
  - **ICAI Case Scenarios & MTPs (15%)**
  - **Conceptual Traps / Difficulty (15%)**
- **Priority Classifications**:
  - `Very High Priority` (85–100)
  - `High Priority` (70–84)
  - `Moderate Priority` (50–69)
  - `Standard Coverage` (<50)
- **Interactive Multi-Segment Score Bars**: Every topic card visualizes exact score contributions from all 5 pillars.
- **Revision Toggle**: Students can mark individual topics as revised/pending.

### 2. 💡 "What Should I Study Today?" Recommender
- Dynamically recommends the top unrevised high-priority topics across the syllabus.
- Analyzes weak chapters identified by actual errors recorded in **My Mistakes Book**.
- Provides 1-click launch to drill practice questions for those specific chapters.

### 3. 📖 Important Topics & Quick Revision Handbook
Eliminates rereading hundreds of module pages with 5 targeted views:
- **Chapter Summary**: Core section ranges and essentials.
- **Statutory Limits & Formulas Compendium**:
  - *Set A*: Women Director thresholds (100 Cr / 300 Cr), Audit Committee limits, Sec 180 vs Sec 186 borrowings, CIRP voting majorities (51%, 66%, 90%), FEMA LRS limits (USD 250,000), FCRA 20% admin cap.
  - *Set B*: Throughput Accounting ratios, Fitzgerald & Moon Building Block (OAE Standards & CMC Rewards), Transfer Pricing decision rules, Economic Value Added (EVA) brand-building adjustments, OEE.
- **Confused Concepts Comparison Matrix**: Head-to-head comparison of frequently confused legal and costing provisions.
- **High-Yield Exam Traps**: Detailed pitfalls recalled in past TCS iON exams.

### 4. ⚡ Intelligent Practice Engine (10 Modes)
1. **Important Questions Practice**: Only high-priority topics (85–100 score).
2. **ICAI Official Practice**: Official ICAI BoS Module, TYK, and Case Booklet questions.
3. **Student Recall Practice**: Questions recalled by actual test-takers at test centers.
4. **Faculty Picks Practice**: Questions recommended in faculty marathons.
5. **Chapter-Wise Practice**: Single chapter drill-down.
6. **Mixed Syllabus Practice**: Multi-chapter randomized practice.
7. **Weak Area Practice**: Automatically targets chapters where you have logged mistakes.
8. **Rapid Revision Blitz**: Fast 10-question sprint.
9. **Case Scenario Practice**: Integrated multi-question scenario problems.
10. **Adaptive Practice**: Performance-tuned selection giving higher weight to failed questions.

**Immediate Answer Feedback**:
- Shows why the correct option is legally/conceptually sound.
- Breaks down **Why Option A/B/C/D is wrong** individually.
- Displays Bare Act Section Reference / Costing Framework.
- Displays SPOM Exam Trap Alert.

### 5. 🖥️ TCS iON CBT 100M Simulator
- **Total Marks**: 100 Marks (50 Questions x 2 Marks).
- **Time Limit**: 180 Minutes (45 Minutes for Power Blitz).
- **Negative Marking**: Zero (exact ICAI rule).
- **Passing Standard**: Mandatory 50% cutoff (50/100).
- **Section Tabs**: Direct switching between **Part I** and **Part II**.
- **Dynamic Option Shuffling**: Options A, B, C, D are randomized per attempt to prevent position memorization.
- **5-State Question Palette**:
  - 🟢 Answered
  - 🔴 Not Answered
  - 🟣 Marked for Review
  - 🔵 Answered & Marked for Review
  - ⚪ Not Visited
- **Keyboard Shortcuts**: Keys `1–4` or `A–D` to select options, `Enter` to Save & Next, `Left Arrow` for Previous.

### 6. 📕 My Mistakes Book & Spaced Revision
- Every wrong answer submitted in mocks or practice is **automatically logged** in the SQLite database.
- Tracks **how many times** a question was answered incorrectly.
- Tracks your last selected option vs the true correct answer.
- Spaced revision workflow: `Unrevised` ➔ `Reviewed` ➔ `Mastered`.
- Editable personal study notes per mistake.

### 7. 📤 MCQ Studio & Research Ingestion Audit Log
- **Bulk Upload**: Import CSV and JSON files with schema validation.
- **Single MCQ Creator**: Add individual questions with section references and trap tips.
- **Research Source Ingestion**: Log URLs, titles, and summaries from Reddit, YouTube, or ICAI.
- **Audit Log Table**: Comprehensive verifiable provenance tracking.

---

## 🚀 How to Run the Portal

### Option 1: Double-Click Batch File (Windows)
Double-click `start_server.bat` in `C:\Users\Ansh\Desktop\Coding\ca-spom-portal`. It starts the Python backend and opens `http://localhost:8080` in your default browser.

### Option 2: Command Line
```powershell
cd C:\Users\Ansh\Desktop\Coding\ca-spom-portal
python server.py 8080
```
Open `http://localhost:8080` in your web browser.

---

## 🔒 Data Preservation & Integrity
- **Database**: SQLite at `spom_portal.db`.
- **Pre-Migration Backups**: Stored at `backups/spom_portal_backup_*.db`.
- **Zero Loss Guarantee**: All historical attempts, bookmarks, and user questions are preserved across all updates.
- **100% Offline Capability**: Runs entirely locally on standard Python 3.12 without external npm or pip package requirements.
