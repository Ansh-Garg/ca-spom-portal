"""
Comprehensive Handbook, Limits, Traps & Flashcards Seeder for all 20 Chapters of CA Final SPOM
Set A: Corporate and Economic Laws (12 Chapters)
Set B: Strategic Cost & Performance Management (8 Chapters)
"""
import sqlite3
import json
import os

DB_PATH = os.path.join(os.path.dirname(__file__), 'spom_portal.db')

def seed_comprehensive_handbook():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Create flashcard_progress table if not exists
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS flashcard_progress (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id TEXT NOT NULL DEFAULT 'default',
        card_key TEXT NOT NULL,
        status TEXT NOT NULL DEFAULT 'unmastered',
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        UNIQUE(user_id, card_key)
    )
    """)

    # Seed data dictionary for all 20 chapters
    # Each chapter will have: summary, formulas_limits, confused_concepts, exam_traps, flashcards
    chapters_data = [
        # =========================================================================
        # SET A - CHAPTER 1: A_DIR (Directors Appointment & Qualification)
        # =========================================================================
        {
            "set_name": "A",
            "chapter_code": "A_DIR",
            "summary": {
                "title": "Directors Appointment & Qualification (Sec 149 - 172)",
                "cheat_sheet": "Minimum Directors: Public 3, Private 2, OPC 1. Maximum Directors: 15 (can exceed 15 by Special Resolution; Section 8 companies exempt from both 15 max and SR requirement). Resident Director: Min 1 director residing in India for >= 182 days in previous financial year (for newly incorporated co, proportionate days). Women Director: Listed co OR Public co with Paid-up Capital >= 100 Cr OR Turnover >= 300 Cr. Independent Director (ID): Listed co (1/3rd board) OR Unlisted Public co with Paid-up >= 10 Cr, Turnover >= 100 Cr, or Loans/Deposits/Debentures > 50 Cr (min 2 IDs). Small Shareholder Director: Notice by 1,000 small shareholders or 1/10th of total shareholders (holding shares nominal value <= Rs 20,000). Max Directorships: 20 companies (max 10 public companies, dormant co excluded).",
                "core_provisions": [
                    {"title": "Section 149(1) & (3) Composition & Resident Director", "provision": "Min 3/2/1, max 15. Every company must have at least 1 director residing in India for >= 182 days in FY."},
                    {"title": "Section 149(6) Independent Director Independence Criteria", "provision": "Person of integrity, not a promoter, no pecuniary relationship exceeding 10% of total income or Rs 50 Lakhs. Relatives can hold security up to Rs 50 Lakhs face value or 2% of paid-up capital, whichever is HIGHER."},
                    {"title": "Section 164(1) & 164(2) Disqualifications", "provision": "164(1) personal grounds (unsound mind, undischarged insolvent, convicted for >= 6 months with 5 year cooling, or >= 7 years permanent ban). 164(2) company default: failure to file financial statements/annual returns for 3 consecutive FYs OR failure to repay deposits/interest/debentures for >= 1 year (disqualified for 5 years)."},
                    {"title": "Section 167(1)(a) Proviso to Vacation", "provision": "Director vacates office in all companies EXCEPT the defaulting company under Section 164(2)."}
                ]
            },
            "formulas_limits": {
                "title": "Statutory Thresholds & Numerical Limits: Directors",
                "limits_table": [
                    {"item": "Women Director Applicability", "limit": "Paid-up >= 100 Cr OR Turnover >= 300 Cr", "context": "Public companies. Listed cos always mandatory."},
                    {"item": "Women Director Vacancy Filling", "limit": "Immediate Next BM or 3 Months, whichever is LATER", "context": "Sec 149(1) read with Rule 3"},
                    {"item": "Independent Director Applicability", "limit": "Paid-up >= 10 Cr OR Turnover >= 100 Cr OR Loans/Deposits > 50 Cr", "context": "Unlisted Public companies: Min 2 IDs"},
                    {"item": "ID Relative Security Limit", "limit": "Face value <= Rs 50 Lakhs OR 2% of Paid-up Capital, whichever is HIGHER", "context": "Sec 149(6)(d)(i) read with Rule 5"},
                    {"item": "Maximum Directorships", "limit": "20 companies total (Max 10 Public Companies)", "context": "Sec 165(1); Dormant cos excluded"},
                    {"item": "Small Shareholder Director Notice", "limit": "1,000 Small Shareholders OR 1/10th of total, whichever is LOWER", "context": "Sec 151; Nominal share value <= Rs 20,000"},
                    {"item": "Casual Vacancy Filling (Sec 161(4))", "limit": "By Board at BM, subsequently approved in immediate next GM", "context": "Tenure up to remainder of original director term"}
                ]
            },
            "confused_concepts": {
                "title": "Confused Provisions: Additional vs Alternate vs Casual Vacancy",
                "comparisons": [
                    {"concept_a": "Additional Director (Sec 161(1))", "concept_b": "Alternate Director (Sec 161(2))", "key_difference": "Additional director holds office up to next AGM or last date AGM should have been held. Alternate director holds office only during absence of original director (absent >= 3 months from India) and vacates when original director returns to India."},
                    {"concept_a": "Sec 164(2) Disqualification", "concept_b": "Sec 167(1)(a) Proviso Vacation", "key_difference": "Disqualification applies to new appointments in other companies for 5 years. Vacation occurs in ALL companies, but the statutory proviso protects remaining in the defaulting company to prevent board paralysis."}
                ]
            },
            "exam_traps": {
                "title": "SPOM Center Recalls & High-Yield Exam Traps: Directors",
                "traps": [
                    {"trap_title": "Relative Security Limit: Whichever is HIGHER", "trap_description": "ICAI exam questions test options stating 'whichever is lower' vs 'whichever is higher'. The correct amended statutory rule is: Face value <= Rs 50 Lakhs OR 2% of paid-up capital, WHICHEVER IS HIGHER."},
                    {"trap_title": "Intermittent Vacancy: Whichever is LATER", "trap_description": "For both Woman Director and Independent Director vacancies, the replacement timeline is next Board Meeting OR 3 months from date of vacancy, WHICHEVER IS LATER (not earlier)."},
                    {"trap_title": "Section 8 Company 15 Director Exemption", "trap_description": "Section 8 companies can have more than 15 directors WITHOUT passing a Special Resolution under Section 149(1)."}
                ]
            },
            "flashcards": [
                {
                    "front": "What are the applicability criteria for appointing a Woman Director under Section 149(1)?",
                    "back": "1. Every Listed Company\n2. Every Public Company having:\n   - Paid-up share capital >= Rs 100 Crore, OR\n   - Turnover >= Rs 300 Crore\n(Based on latest audited financial statements).",
                    "tag": "Statutory Limit",
                    "section": "Sec 149(1) & Rule 3",
                    "trap": "Intermittent vacancy: Next Board Meeting or 3 months from vacancy, whichever is LATER."
                },
                {
                    "front": "What is the maximum limit of securities a relative of an Independent Director can hold under Sec 149(6)(d)(i)?",
                    "back": "Face value not exceeding Rs 50 Lakhs OR 2% of the paid-up capital of the company, its holding, subsidiary or associate company, WHICHEVER IS HIGHER.",
                    "tag": "Statutory Limit",
                    "section": "Sec 149(6)(d)(i) & Rule 5",
                    "trap": "Beware: It is 'whichever is HIGHER', not lower!"
                },
                {
                    "front": "Under Section 167(1)(a) proviso, does a director vacate office in the defaulting company under Sec 164(2)?",
                    "back": "NO. The director vacates office in all OTHER companies, but SHALL NOT vacate in the defaulting company. This prevents complete collapse of the defaulting company's board.",
                    "tag": "Confused Concept",
                    "section": "Sec 167(1)(a) Proviso",
                    "trap": "Common exam trap asserts vacation in all companies without exception."
                },
                {
                    "front": "What are the tenure and term limits for an Independent Director under Sec 149(10) & (11)?",
                    "back": "Term: Up to 5 consecutive years.\nReappointment: One more term of up to 5 years by Special Resolution + Board report disclosure.\nMax: 2 consecutive terms (10 years).\nCooling-off Period: 3 years before any fresh appointment.",
                    "tag": "Tenure Rule",
                    "section": "Sec 149(10), (11)",
                    "trap": "During 3-year cooling period, the ID cannot be associated in ANY capacity with the company, directly or indirectly."
                }
            ]
        },

        # =========================================================================
        # SET A - CHAPTER 2: A_BM (Meetings of Board & Powers)
        # =========================================================================
        {
            "set_name": "A",
            "chapter_code": "A_BM",
            "summary": {
                "title": "Meetings of Board and its Powers (Sec 173 - 195)",
                "cheat_sheet": "First BM: within 30 days of incorporation. Subsequent BMs: min 4 meetings every year, max gap 120 days between consecutive meetings. OPC / Small Co / Dormant Co / Start-up: min 1 meeting in each half of calendar year, gap >= 90 days. Notice: min 7 days in writing (shorter notice allowed if min 1 Independent Director is present, or ratified by min 1 ID). Quorum (Sec 174): 1/3rd of total strength or 2 directors, whichever is higher (interested >= 2/3rd -> remaining min 2). Sec 180(1)(c) Borrowings: SR required if borrowings exceed Paid-up Capital + Free Reserves + Securities Premium. Sec 186: Unanimous Board resolution + SR if loans/investments exceed 60% of (Paid-up + Free Reserves + Securities Premium) OR 100% of (Free Reserves + Securities Premium).",
                "core_provisions": [
                    {"title": "Section 173 Board Meeting Frequency & Notice", "provision": "Min 4 meetings/year, gap <= 120 days. 7 days written notice. Video conferencing participation counts toward quorum."},
                    {"title": "Section 174 Quorum for Board Meeting", "provision": "1/3rd of total strength or 2 directors, whichever is higher. Fraction rounded off to 1. If interested directors >= 2/3rd, remaining non-interested directors (min 2) form quorum."},
                    {"title": "Section 180 Powers of Board Exercisable Only with SR", "provision": "Sec 180(1)(a) sell/lease undertaking (>= 20% net worth or generates >= 20% total income). Sec 180(1)(c) borrowings exceeding Paid-up Capital + Free Reserves + Securities Premium."},
                    {"title": "Section 186 Loans, Guarantees & Investments", "provision": "Cannot give through more than 2 layers of investment companies. Unanimous board approval at meeting required. SR if exceeding 60% of (Paid-up + FR + SP) or 100% of (FR + SP)."}
                ]
            },
            "formulas_limits": {
                "title": "Statutory Comparison: Sec 180 Borrowings vs Sec 186 Loans & Investments",
                "limits_table": [
                    {"item": "Board Meeting Quorum (Sec 174)", "limit": "1/3rd of Total Strength OR 2 Directors, whichever is HIGHER", "context": "Fractions rounded to 1. Min 2 non-interested directors."},
                    {"item": "Sec 180(1)(c) Borrowing Threshold", "limit": "Paid-up Share Capital + Free Reserves + Securities Premium", "context": "Excludes temporary loans obtained from bankers in ordinary course."},
                    {"item": "Sec 186 Threshold for SR", "limit": "60% of (Paid-up + FR + SP) OR 100% of (FR + SP), whichever is HIGHER", "context": "Unanimous board approval always mandatory regardless of limit."},
                    {"item": "Audit Committee Thresholds", "limit": "Paid-up >= 10 Cr OR Turnover >= 100 Cr OR Loans/Deposits > 50 Cr", "context": "Public companies. Min 3 directors, 2/3rd Independent."},
                    {"item": "CSR Committee Applicability (Sec 135)", "limit": "Net Worth >= 500 Cr OR Turnover >= 1000 Cr OR Net Profit >= 5 Cr", "context": "Spend 2% of avg net profits of immediately preceding 3 FYs."}
                ]
            },
            "confused_concepts": {
                "title": "Confused Provisions: Sec 180(1)(c) vs Sec 186",
                "comparisons": [
                    {"concept_a": "Sec 180(1)(c) Borrowings", "concept_b": "Sec 186 Loans & Investments", "key_difference": "Sec 180(1)(c) applies only to Public Companies and compares borrowings against Paid-up Capital + Free Reserves + Securities Premium. Sec 186 applies to ALL companies (public & private) and uses a dual test: 60% of (PUC+FR+SP) vs 100% of (FR+SP), whichever is higher."},
                    {"concept_a": "Audit Committee (Sec 177)", "concept_b": "CSR Committee (Sec 135)", "key_difference": "Audit committee uses Paid-up (10 Cr), Turnover (100 Cr), Loans (>50 Cr). CSR uses Net Worth (500 Cr), Turnover (1000 Cr), Net Profit (5 Cr)."}
                ]
            },
            "exam_traps": {
                "title": "SPOM Center Recalls & Traps: Board Meetings & Committees",
                "traps": [
                    {"trap_title": "Temporary Loans Excluded under Sec 180(1)(c)", "trap_description": "Temporary loans repayable on demand or within 6 months (cash credit, discounting bills) are strictly EXCLUDED from calculating the borrowing limit."},
                    {"trap_title": "Unanimous Consent for Sec 186", "trap_description": "Board consent for Sec 186 must be UNANIMOUS by all directors present at the meeting. Circular resolution is NOT permitted for Sec 186!"},
                    {"trap_title": "Shorter Notice Condition", "trap_description": "If a Board Meeting is called at shorter notice (< 7 days), at least ONE Independent Director MUST be present, or decisions must be ratified by min 1 ID."}
                ]
            },
            "flashcards": [
                {
                    "front": "What is the Quorum for a Board Meeting under Section 174?",
                    "back": "1/3rd of the total strength of the Board OR 2 Directors, whichever is HIGHER.\nFraction is rounded off as one.\nInterested directors >= 2/3rd: Remaining directors (min 2) form the quorum.",
                    "tag": "Statutory Limit",
                    "section": "Section 174(1)",
                    "trap": "Directors participating via video conferencing count towards quorum!"
                },
                {
                    "front": "What are the two limits under Section 186(2) that trigger Special Resolution?",
                    "back": "Special Resolution is required if loans, guarantees, or investments exceed:\n1. 60% of (Paid-up Capital + Free Reserves + Securities Premium), OR\n2. 100% of (Free Reserves + Securities Premium),\nWHICHEVER IS HIGHER.",
                    "tag": "Statutory Limit",
                    "section": "Section 186(2)",
                    "trap": "Unanimous approval of all directors present at the meeting is mandatory even within limits!"
                },
                {
                    "front": "What are the criteria for constituting a CSR Committee under Section 135(1)?",
                    "back": "Any company having in immediately preceding financial year:\n1. Net Worth >= Rs 500 Crore, OR\n2. Turnover >= Rs 1,000 Crore, OR\n3. Net Profit >= Rs 5 Crore.\nMandatory CSR spend: 2% of average net profits of last 3 FYs.",
                    "tag": "Statutory Limit",
                    "section": "Section 135(1)",
                    "trap": "If CSR obligation <= Rs 50 Lakhs, CSR committee is NOT mandatory (Board can fulfill duties)."
                }
            ]
        },

        # =========================================================================
        # SET A - CHAPTER 10: A_FEMA (FEMA, 1999)
        # =========================================================================
        {
            "set_name": "A",
            "chapter_code": "A_FEMA",
            "summary": {
                "title": "Foreign Exchange Management Act (FEMA), 1999",
                "cheat_sheet": "Person Resident in India (PRII) under Sec 2(v): Residing in India for > 182 days during the PRECEDING financial year, BUT excludes individuals who go outside India for employment, business, or indefinite stay. Current Account Transactions (Sec 5): Schedule I Prohibited (lottery, call back services, travel to Nepal/Bhutan with forex); Schedule II Requires Central Govt Approval (cultural tours, remittance of prize money/freight); Schedule III Requires RBI Approval if exceeding limits: Liberalised Remittance Scheme (LRS) ceiling is USD 250,000 per financial year for medical, education, gifts, donation, maintenance of close relatives. Export realization timeline: within 9 months from date of export.",
                "core_provisions": [
                    {"title": "Section 2(v) Person Resident in India (PRII)", "provision": "Must satisfy > 182 days test in preceding FY + intent test (must not have left India for employment/business abroad)."},
                    {"title": "Section 5 Current Account Transactions", "provision": "Freedom to draw foreign exchange for current account transactions unless restricted under Schedule I, II, or III."},
                    {"title": "Liberalised Remittance Scheme (LRS)", "provision": "Resident individuals can remit up to USD 250,000 per financial year for permitted current and capital account transactions."},
                    {"title": "Section 6 Capital Account Transactions", "provision": "RBI specifies permitted capital account transactions and regulates permissible classes and debt/equity instruments."}
                ]
            },
            "formulas_limits": {
                "title": "FEMA Statutory Limits & Ceilings Compendium",
                "limits_table": [
                    {"item": "PRII Day Test", "limit": "> 182 Days in the PRECEDING Financial Year", "context": "Sec 2(v) + Intent condition"},
                    {"item": "LRS Maximum Annual Remittance", "limit": "USD 250,000 per Financial Year (April - March)", "context": "Per resident individual (includes minors)"},
                    {"item": "Export Realization Period", "limit": "Within 9 Months from date of export", "context": "Status holder / SEZ units also 9 months"},
                    {"item": "Remittance for Medical Treatment Abroad", "limit": "Up to USD 250,000 without estimate; above requires hospital estimate", "context": "Schedule III Rule 8"},
                    {"item": "Forex for Travel to Nepal & Bhutan", "limit": "Strictly Prohibited to draw Foreign Exchange", "context": "Schedule I Prohibited item"}
                ]
            },
            "confused_concepts": {
                "title": "Confused Concepts: FEMA PRII vs Income Tax Resident",
                "comparisons": [
                    {"concept_a": "FEMA Resident (PRII)", "concept_b": "Income Tax Act Resident", "key_difference": "FEMA looks at physical stay (> 182 days) in the PRECEDING financial year + intent of stay in the current year. Income Tax tests physical stay in the CURRENT financial year (182 days or 60 days + 365 days)."},
                    {"concept_a": "Current Account Transaction", "concept_b": "Capital Account Transaction", "key_difference": "Capital account alters assets or liabilities (including contingent liabilities) outside India of PRII, or in India of PROI. Current account transactions do NOT alter external assets/liabilities."}
                ]
            },
            "exam_traps": {
                "title": "SPOM Exam Traps: FEMA 1999",
                "traps": [
                    {"trap_title": "Preceding Year vs Current Year for PRII", "trap_description": "In FEMA, the 182-day stay test is calculated in the PRECEDING financial year, NOT the current year. But if a person arrives in India for taking up employment, they become PRII from day one of arrival!"},
                    {"trap_title": "Minors under LRS", "trap_description": "Minors ARE eligible for LRS with USD 250,000 limit, provided the LRS declaration form is signed by the natural guardian."},
                    {"trap_title": "Schedule I Prohibitions", "trap_description": "Remittance of interest earned on funds held in Non-Resident Special Rupee (NRSR) account is strictly PROHIBITED under Schedule I."}
                ]
            },
            "flashcards": [
                {
                    "front": "How is 'Person Resident in India' (PRII) defined under Section 2(v) of FEMA?",
                    "back": "A person residing in India for MORE THAN 182 days during the PRECEDING financial year.\nEXCEPTIONS: Person who leaves India for employment, business, or indefinite stay is NOT a PRII (regardless of 182 days).",
                    "tag": "Statutory Definition",
                    "section": "Section 2(v)",
                    "trap": "The test is evaluated based on the PRECEDING financial year, not the current year!"
                },
                {
                    "front": "What is the maximum limit under the Liberalised Remittance Scheme (LRS)?",
                    "back": "USD 250,000 per financial year (April to March) per resident individual for any permitted current or capital account transactions.",
                    "tag": "Statutory Limit",
                    "section": "Schedule III & LRS",
                    "trap": "Applies strictly to Resident INDIVIDUALS, not corporates, partnership firms, or HUFs."
                },
                {
                    "front": "What is the standard statutory time period for realization and repatriation of export proceeds under FEMA?",
                    "back": "Within 9 MONTHS from the date of export of goods or software.\n(Extended to 15 months for goods exported to a warehouse established outside India).",
                    "tag": "Statutory Limit",
                    "section": "FEMA Export Regulations",
                    "trap": "RBI has power to extend the 9-month realization period on sufficient cause."
                }
            ]
        },

        # =========================================================================
        # SET A - CHAPTER 11: A_IBC (Insolvency and Bankruptcy Code, 2016)
        # =========================================================================
        {
            "set_name": "A",
            "chapter_code": "A_IBC",
            "summary": {
                "title": "Insolvency and Bankruptcy Code (IBC), 2016",
                "cheat_sheet": "Minimum Default Threshold: Rs 1 Crore (Sec 4). CIRP Initiation: Sec 7 by Financial Creditor, Sec 8 & 9 by Operational Creditor (10-day demand notice in Form 3/4), Sec 10 by Corporate Applicant. CIRP Duration (Sec 12): 180 days, one-time extension of 90 days by CoC (66% voting), absolute outer ceiling 330 days including litigation. Moratorium (Sec 14): From insolvency commencement date till completion of CIRP or liquidation order. CoC Voting Majorities: Ordinary matters & IRP to RP appointment = 51%; Resolution Plan approval (Sec 30(4)), Sec 28 actions, replacement of RP, and CIRP extension = 66%; Withdrawal of CIRP application under Sec 12A = 90%. Waterfall Mechanism (Sec 53): CIRP costs -> Workmen dues (24m) & secured creditors -> Unsecured -> Govt dues (2 yrs) -> Preference -> Equity.",
                "core_provisions": [
                    {"title": "Section 4 Default Threshold", "provision": "Default must be minimum Rs 1 Crore. Central Govt notification raised threshold from Rs 1 Lakh to Rs 1 Crore."},
                    {"title": "Section 12 CIRP Time-Limit", "provision": "180 days standard + 90 days extension by NCLT upon 66% CoC approval. Mandatorily completed within 330 days."},
                    {"title": "Section 14 Moratorium", "provision": "Prohibits institution/continuation of suits, recovery actions, execution of judgments, alienation of corporate debtor assets."},
                    {"title": "Section 53 Distribution Waterfall in Liquidation", "provision": "1. CIRP & liquidation costs, 2. Workmen dues (24 months) & secured creditors holding relinquished security (pari passu), 3. Wages to employees (12 months), 4. Unsecured financial creditors, 5. Govt dues (2 years) & remaining unpaid secured debt, 6. Preference shares, 7. Equity shares."}
                ]
            },
            "formulas_limits": {
                "title": "IBC CIRP Voting Percentages & Waterfall Mechanism Summary",
                "limits_table": [
                    {"item": "Minimum Default Threshold", "limit": "Rs 1 Crore (Section 4)", "context": "Uniform for Sec 7, 9, 10"},
                    {"item": "Operational Creditor Notice", "limit": "10 Days Demand Notice (Section 8)", "context": "Must prove no pre-existing dispute"},
                    {"item": "Resolution Plan Approval", "limit": "Minimum 66% Voting Share of CoC", "context": "Section 30(4)"},
                    {"item": "Withdrawal under Sec 12A", "limit": "Minimum 90% Voting Share of CoC", "context": "NCLT approval required"},
                    {"item": "CIRP Extension & Replacement of RP", "limit": "Minimum 66% Voting Share of CoC", "context": "Section 12(2) & Section 27"},
                    {"item": "Routine / Ordinary CoC Decisions", "limit": "51% Voting Share of CoC", "context": "Section 21"}
                ]
            },
            "confused_concepts": {
                "title": "Confused Provisions: Section 7 vs Section 9 vs Section 12A",
                "comparisons": [
                    {"concept_a": "Sec 7 Financial Creditor", "concept_b": "Sec 9 Operational Creditor", "key_difference": "Financial creditor does not require a prior 10-day demand notice; default can be proved via Information Utility (NeSL). Operational creditor MUST mandatorily serve a 10-day statutory demand notice and application is rejected if a pre-existing dispute exists."},
                    {"concept_a": "Resolution Plan CoC Majority (66%)", "concept_b": "Withdrawal Sec 12A Majority (90%)", "key_difference": "Passing a resolution plan requires 66% of voting share. Aborting/withdrawing the CIRP under Sec 12A requires a supermajority of 90% of CoC voting share."}
                ]
            },
            "exam_traps": {
                "title": "SPOM Center Recalls & Traps: IBC 2016",
                "traps": [
                    {"trap_title": "Workmen Dues Pari Passu with Secured Creditors", "trap_description": "In Section 53 waterfall, workmen dues for 24 months rank EQUALLY (pari passu) with debts owed to a secured creditor who has relinquished their security interest."},
                    {"trap_title": "Sec 29A Disqualification for Resolution Applicants", "trap_description": "Undischarged insolvents, wilful defaulters, and promoters with NPA accounts for >= 1 year before CIRP commencement are strictly BARRED from submitting a resolution plan under Section 29A."},
                    {"trap_title": "Moratorium Exclusions", "trap_description": "Moratorium does NOT apply to surety in a contract of guarantee to a corporate debtor (personal guarantors can be pursued simultaneously!)."}
                ]
            },
            "flashcards": [
                {
                    "front": "What are the Committee of Creditors (CoC) voting thresholds under IBC for (a) Resolution Plan, (b) Routine Matters, (c) Sec 12A Withdrawal?",
                    "back": "1. Resolution Plan Approval: 66% of voting share\n2. Routine / Ordinary Decisions: 51% of voting share\n3. Sec 12A Withdrawal: 90% of voting share.",
                    "tag": "Voting Threshold",
                    "section": "Sec 12A, 21, 30(4)",
                    "trap": "Replacement of Resolution Professional (RP) requires 66%, NOT 51%!"
                },
                {
                    "front": "What is the priority order of distribution under Section 53 Waterfall Mechanism in Liquidation?",
                    "back": "1. CIRP & Liquidation costs (Full)\n2. Workmen dues (last 24m) & Secured Creditors who relinquished security (Pari Passu)\n3. Other employee wages (last 12m)\n4. Unsecured financial creditors\n5. Govt dues (last 2 yrs) & Remaining secured debt\n6. Preference shareholders\n7. Equity shareholders.",
                    "tag": "Statutory Priority",
                    "section": "Section 53",
                    "trap": "Workmen dues (24 months) and secured creditors rank EQUALLY in step 2."
                },
                {
                    "front": "What is the maximum statutory timeline for completion of CIRP under Section 12?",
                    "back": "Standard: 180 days.\nOne-time extension: Up to 90 days (approved by 66% CoC).\nMandatory outer limit: 330 days (including time taken in legal proceedings).",
                    "tag": "Statutory Limit",
                    "section": "Section 12(1), (2), (3)",
                    "trap": "The 330-day cap includes litigation time, as upheld by Supreme Court in Essar Steel."
                }
            ]
        },

        # =========================================================================
        # SET B - CHAPTER 14: B_MBE (Lean Systems & TOC)
        # =========================================================================
        {
            "set_name": "B",
            "chapter_code": "B_MBE",
            "summary": {
                "title": "Modern Business Environment & Theory of Constraints (TOC)",
                "cheat_sheet": "Theory of Constraints (TOC) focuses on identifying and managing the single bottleneck resource limiting organizational performance. Goldratt's 5 Steps: 1. Identify constraint, 2. Exploit constraint (maximize uptime and efficiency of bottleneck), 3. Subordinate everything else (pace non-bottlenecks to constraint rate via DBR: Drum-Buffer-Rope), 4. Elevate constraint (invest capex to expand capacity), 5. Repeat / Prevent inertia. Throughput Accounting (TA): Assumes ONLY Direct Material is variable in the short run; all other conversion costs are treated as Operating Expenses (OE). Key Formulas: Throughput (T) = Sales - Direct Material. Return on Bottleneck Minute = Throughput per unit / Bottleneck minutes per unit. Throughput Accounting Ratio (TA Ratio) = (Throughput per bottleneck minute) / (Operating Expense per bottleneck minute). Products with TA Ratio > 1 are profitable. Overall Equipment Effectiveness (OEE) = Availability x Performance x Quality (World class benchmark = 85%).",
                "core_provisions": [
                    {"title": "Throughput Accounting Concept", "provision": "Inventory is valued strictly at direct material cost. Labor and overheads are operating expenses of the period."},
                    {"title": "Goldratt's 5 Focusing Steps", "provision": "Identify -> Exploit -> Subordinate -> Elevate -> Prevent Inertia."},
                    {"title": "Drum-Buffer-Rope (DBR)", "provision": "Drum = Bottleneck pace; Buffer = Time buffer before bottleneck; Rope = Material release mechanism."},
                    {"title": "Overall Equipment Effectiveness (OEE)", "provision": "Quantifies equipment losses across 3 factors: Downtime (Availability), Speed loss (Performance), Defect loss (Quality)."}
                ]
            },
            "formulas_limits": {
                "title": "Throughput Accounting & OEE Formulas Compendium",
                "limits_table": [
                    {"item": "Throughput (T)", "limit": "Sales Revenue - Direct Material Cost", "context": "Labor is treated as Operating Expense"},
                    {"item": "Return per Bottleneck Minute", "limit": "Throughput per unit / Bottleneck Minutes per unit", "context": "Basis for product mix ranking"},
                    {"item": "Cost per Bottleneck Minute", "limit": "Total Operating Expenses / Total Available Bottleneck Minutes", "context": "Factory cost rate per minute"},
                    {"item": "Throughput Accounting (TA) Ratio", "limit": "(Return per Bottleneck Min) / (Cost per Bottleneck Min)", "context": "TA > 1 means profitable product"},
                    {"item": "OEE Formula", "limit": "Availability x Performance Rate x Quality Rate", "context": "World-class standard >= 85%"}
                ]
            },
            "confused_concepts": {
                "title": "Confused Concepts: Throughput Accounting vs Traditional Marginal Costing",
                "comparisons": [
                    {"concept_a": "Throughput Accounting (TA)", "concept_b": "Marginal Costing", "key_difference": "Marginal costing treats direct labor and variable overheads as variable costs. Throughput accounting treats ONLY direct materials as truly variable; labor and variable overheads are fixed Operating Expenses (OE) in the short run."},
                    {"concept_a": "Exploit the Constraint", "concept_b": "Elevate the Constraint", "key_difference": "Exploiting means getting the maximum throughput from the existing bottleneck WITHOUT spending capex (e.g. eliminate idle time, offload non-essential work). Elevating means spending capex to increase physical capacity (buying new machines, hiring)."}
                ]
            },
            "exam_traps": {
                "title": "SPOM Exam Traps: Throughput Accounting & TOC",
                "traps": [
                    {"trap_title": "Direct Labor Treatment in TA", "trap_description": "Exam questions frequently tempt students to subtract Direct Labor to calculate Throughput. In pure Throughput Accounting, Throughput = Sales - Direct Material ONLY!"},
                    {"trap_title": "Product Ranking by TA Ratio vs Contribution per unit", "trap_description": "When a bottleneck constraint exists, products MUST be prioritized by Return per Bottleneck Minute (or TA Ratio), NOT by contribution per unit or profit margin!"},
                    {"trap_title": "OEE Calculation Traps", "trap_description": "Availability uses Operating Time / Planned Production Time (excluding planned maintenance). Performance uses Actual Output / Standard Output during operating time."}
                ]
            },
            "flashcards": [
                {
                    "front": "How is Throughput (T) calculated in Throughput Accounting?",
                    "back": "Throughput = Sales Revenue - Truly Variable Costs (Direct Material Cost ONLY).\nDirect Labor and Variable Overheads are NOT subtracted; they are treated as Operating Expenses (OE).",
                    "tag": "Costing Formula",
                    "section": "Throughput Accounting",
                    "trap": "Never subtract Direct Labor when computing Throughput in Goldratt's framework!"
                },
                {
                    "front": "What is the Throughput Accounting (TA) Ratio and how is it interpreted?",
                    "back": "TA Ratio = (Throughput per Bottleneck Minute) / (Operating Expense per Bottleneck Minute).\nInterpretation:\n- TA Ratio > 1.0: Product generates more cash than it costs to run the facility (Profitable).\n- TA Ratio < 1.0: Product fails to cover factory costs (Loss-making).",
                    "tag": "Costing Formula",
                    "section": "TA Ratio",
                    "trap": "Rank products in descending order of Throughput per Bottleneck Minute to maximize profit."
                },
                {
                    "front": "What are Goldratt's 5 Focusing Steps in Theory of Constraints (TOC)?",
                    "back": "1. IDENTIFY the system's constraint(s)\n2. EXPLOIT the constraint(s) (maximize throughput with zero downtime)\n3. SUBORDINATE everything else to the constraint (pace upstream operations)\n4. ELEVATE the constraint (invest capex to expand capacity)\n5. REPEAT (prevent inertia from becoming the new constraint).",
                    "tag": "Framework",
                    "section": "Theory of Constraints",
                    "trap": "Step 3 (Subordination) is the most challenging culturally because non-bottlenecks must sit idle."
                }
            ]
        },

        # =========================================================================
        # SET B - CHAPTER 19: B_TP (Divisional Transfer Pricing)
        # =========================================================================
        {
            "set_name": "B",
            "chapter_code": "B_TP",
            "summary": {
                "title": "Divisional Transfer Pricing & International Tax",
                "cheat_sheet": "Transfer Pricing determines internal prices for goods and services transferred between autonomous divisions. Core Objective: Goal Congruence (ensuring divisional managers making self-interested profit-maximizing decisions also maximize overall company profit). Minimum Transfer Price (Seller's Floor): Min TP = Additional Out-of-Pocket Cost (Variable Cost) + Opportunity Cost per unit. If seller has spare capacity: Opportunity Cost = 0 -> Min TP = Variable Cost. If seller has NO spare capacity: Opportunity Cost = Lost Contribution on external market -> Min TP = Market Price. Maximum Transfer Price (Buyer's Ceiling): Max TP = Lower of (External Market Purchase Price, Net Marginal Revenue). Negotiated Range: When Min TP <= Max TP, internal transfer is viable and mutually beneficial. Dual Pricing: Recording transfer at different prices for buyer and seller to preserve motivation and reporting.",
                "core_provisions": [
                    {"title": "Minimum Transfer Price Formula", "provision": "Min TP = Incremental Out-of-Pocket Cost + Lost Opportunity Cost per unit."},
                    {"title": "Maximum Transfer Price Formula", "provision": "Max TP = Lower of External Market Price and Net Marginal Revenue of buying division."},
                    {"title": "Goal Congruence Decision Rule", "provision": "Internal transfer is optimal for the company as a whole if seller's incremental cost < buyer's net benefit."},
                    {"title": "Dual-Rate Pricing System", "provision": "Crediting supplying division at market price while debiting receiving division at variable cost; difference adjusted in corporate account."}
                ]
            },
            "formulas_limits": {
                "title": "Transfer Pricing Decision Rules & Formulas Compendium",
                "limits_table": [
                    {"item": "Seller's Floor (Min TP)", "limit": "Variable Cost + Opportunity Cost per unit", "context": "General economic transfer pricing rule"},
                    {"item": "Min TP with Excess Capacity", "limit": "Variable Cost (since Opportunity Cost = 0)", "context": "No external sales sacrificed"},
                    {"item": "Min TP at Full Capacity", "limit": "Market Price (Variable Cost + Lost Contribution)", "context": "Sacrifices external sales"},
                    {"item": "Buyer's Ceiling (Max TP)", "limit": "Lower of (Market Purchase Price, Net Marginal Revenue)", "context": "Maximum buyer is willing to pay"},
                    {"item": "Transfer Feasibility Condition", "limit": "Minimum TP <= Agreed TP <= Maximum TP", "context": "Range of negotiation"}
                ]
            },
            "confused_concepts": {
                "title": "Confused Concepts: Cost-Plus vs Market-Based vs Negotiated Transfer Pricing",
                "comparisons": [
                    {"concept_a": "Market-Based Transfer Price", "concept_b": "Cost-Plus Transfer Price", "key_difference": "Market-based works best when a perfectly competitive external market exists with reliable prices. Cost-plus (full cost plus markup) leads to sub-optimal decisions because the buying division treats the supplying division's fixed markup as a variable cost."},
                    {"concept_a": "Single Price", "concept_b": "Dual-Rate Pricing", "key_difference": "Dual pricing uses two separate prices: supplying division credited at Market Price (protects divisional ROI), receiving division charged at Variable Cost (ensures optimal buying decisions). Corporate account reconciles the gap."}
                ]
            },
            "exam_traps": {
                "title": "SPOM Center Recalls & Traps: Transfer Pricing",
                "traps": [
                    {"trap_title": "Partial Capacity Opportunity Cost", "trap_description": "If a transfer requires 1,000 units and seller has 600 units spare capacity, opportunity cost applies ONLY to the 400 units of sacrificed external sales, NOT all 1,000 units!"},
                    {"trap_title": "Full Cost Transfer Sub-Optimization", "trap_description": "Transferring at Full Cost causes the receiving division to treat supplying division's fixed overheads as variable, causing the buyer to reject profitable external orders."},
                    {"trap_title": "Internal Transfer Decision: Company vs Division", "trap_description": "Always check overall company benefit first: Company Gain = Buyer's External Revenue - Combined Variable Costs. If positive, transfer SHOULD occur."}
                ]
            },
            "flashcards": [
                {
                    "front": "What is the general formula for Minimum Transfer Price (Seller's perspective)?",
                    "back": "Minimum Transfer Price = Incremental Out-of-Pocket Cost per unit + Opportunity Cost per unit.\n\n- If Spare Capacity exists: Opportunity Cost = Rs 0 -> Min TP = Variable Cost.\n- At Full Capacity: Opportunity Cost = Lost Contribution per unit -> Min TP = Market Price.",
                    "tag": "Costing Formula",
                    "section": "Transfer Pricing",
                    "trap": "If only PARTIAL capacity is sacrificed, opportunity cost is weighted over the total units transferred."
                },
                {
                    "front": "What is the Maximum Transfer Price a buying division is willing to pay?",
                    "back": "Maximum Transfer Price = LOWER of:\n1. External Market Purchase Price available to the buying division, OR\n2. Net Marginal Revenue (Final Selling Price - Buying Division's Own Additional Processing Costs).",
                    "tag": "Costing Formula",
                    "section": "Transfer Pricing",
                    "trap": "The buyer will never pay more than the external market price."
                },
                {
                    "front": "What is Dual Pricing in Transfer Pricing and why is it used?",
                    "back": "Dual Pricing records internal transfer at two DIFFERENT prices:\n- Supplying division is credited at Market Price (incentivizes production & fair ROI).\n- Receiving division is debited at Standard Variable Cost (incentivizes buying & correct incremental decision making).\nThe difference is absorbed by Corporate Head Office.",
                    "tag": "Framework",
                    "section": "Dual Pricing",
                    "trap": "Dual pricing can cause confusion if division managers do not understand why divisional profits don't sum to company profit."
                }
            ]
        },

        # =========================================================================
        # SET B - CHAPTER 17: B_PERF (Strategic Performance Measurement)
        # =========================================================================
        {
            "set_name": "B",
            "chapter_code": "B_PERF",
            "summary": {
                "title": "Strategic Performance Measurement (Scorecard & Models)",
                "cheat_sheet": "Strategic Performance Measurement shifts focus from lagging financial metrics to balanced, multidimensional drivers of long-term competitive advantage. Balanced Scorecard (Kaplan & Norton): 4 Perspectives: Financial (How do we look to shareholders?), Customer (How do customers see us?), Internal Business Processes (What must we excel at?), Learning & Growth (How can we continue to improve and create value?). Strategy Maps connect lead and lag indicators in a cause-and-effect chain. Performance Prism (Neely & Adams): 5 Interrelated Facets: Stakeholder Satisfaction -> Strategies -> Processes -> Capabilities -> Stakeholder Contribution. Covers multiple stakeholders (investors, customers, employees, suppliers, regulators). Fitzgerald & Moon Building Block Model for Services: 3 Blocks: Dimensions (What to measure: Financial & Competitiveness = Results; Quality, Flexibility, Resource Utilization, Innovation = Determinants), Standards (How to set targets: Ownership, Achievability, Equity), Rewards (How to motivate: Clarity, Motivation, Controllability).",
                "core_provisions": [
                    {"title": "Balanced Scorecard 4 Perspectives", "provision": "Financial, Customer, Internal Business Processes, Learning and Growth. Balances financial/non-financial and lead/lag."},
                    {"title": "Fitzgerald & Moon Building Block Model", "provision": "Dimensions (Results & Determinants), Standards (Ownership, Achievability, Equity), Rewards (Clarity, Motivation, Controllability)."},
                    {"title": "Performance Prism 5 Facets", "provision": "Stakeholder Satisfaction, Strategies, Processes, Capabilities, Stakeholder Contribution."},
                    {"title": "Leading vs Lagging Indicators", "provision": "Lagging = outcome measures (profit, customer churn); Leading = performance drivers (training hours, machine setup time)."}
                ]
            },
            "formulas_limits": {
                "title": "Fitzgerald & Moon Framework Matrix Compendium",
                "limits_table": [
                    {"item": "Dimensions: Results (Downstream)", "limit": "Financial Performance, Competitiveness", "context": "Reflects past performance outcomes"},
                    {"item": "Dimensions: Determinants (Upstream)", "limit": "Quality, Flexibility, Resource Utilization, Innovation", "context": "Drives future competitive success"},
                    {"item": "Standards: 3 Criteria", "limit": "Ownership, Achievability, Equity", "context": "Principles for goal setting"},
                    {"item": "Rewards: 3 Criteria", "limit": "Clarity, Motivation, Controllability", "context": "Principles for compensation design"},
                    {"item": "Performance Prism: 5 Facets", "limit": "Satisfaction, Strategies, Processes, Capabilities, Contribution", "context": "Two-way stakeholder exchange model"}
                ]
            },
            "confused_concepts": {
                "title": "Confused Concepts: Balanced Scorecard vs Performance Prism vs Building Block",
                "comparisons": [
                    {"concept_a": "Balanced Scorecard", "concept_b": "Performance Prism", "key_difference": "Balanced Scorecard starts from strategy and focuses on shareholders and customers. Performance Prism starts from STAKEHOLDER SATISFACTION (including employees, suppliers, regulators) and examines stakeholder contribution in return."},
                    {"concept_a": "Results (Fitzgerald & Moon)", "concept_b": "Determinants (Fitzgerald & Moon)", "key_difference": "Results (Financial & Competitiveness) are lagging outputs. Determinants (Quality, Flexibility, Resource Utilization, Innovation) are the operational engines that cause good results."}
                ]
            },
            "exam_traps": {
                "title": "SPOM Center Recalls & Traps: Performance Models",
                "traps": [
                    {"trap_title": "Building Block Controllability Principle", "trap_description": "Managers must NOT be evaluated or penalized on costs or revenues outside their control (e.g. corporate overhead allocations, global exchange rates)."},
                    {"trap_title": "Upstream Determinants Drive Downstream Results", "trap_description": "If asked how to improve financial performance in a service organization, the answer always points to upstream determinants: Quality, Flexibility, Resource Utilization, or Innovation!"},
                    {"trap_title": "BSC Learning & Growth Perspective", "trap_description": "Learning & Growth covers human capital (employee skills, retention), information capital (systems), and organization capital (culture, alignment)."}
                ]
            },
            "flashcards": [
                {
                    "front": "What are the 3 Building Blocks of the Fitzgerald & Moon Framework for Service Businesses?",
                    "back": "1. DIMENSIONS (What to measure):\n   - Results (Downstream): Financial Performance, Competitiveness\n   - Determinants (Upstream): Quality, Flexibility, Resource Utilization, Innovation\n2. STANDARDS (How to set targets):\n   - Ownership, Achievability, Equity\n3. REWARDS (How to motivate):\n   - Clarity, Motivation, Controllability.",
                    "tag": "Framework",
                    "section": "Fitzgerald & Moon Model",
                    "trap": "Determinants are leading drivers; Results are lagging outcomes."
                },
                {
                    "front": "What are the 4 Perspectives of the Kaplan & Norton Balanced Scorecard?",
                    "back": "1. Financial Perspective (Shareholder view: ROI, Profit Margins, EVA)\n2. Customer Perspective (Customer view: Retention, Net Promoter Score, Market Share)\n3. Internal Business Processes (Operational view: Cycle Time, Defect Rate, Quality)\n4. Learning & Growth (Future view: Training hours, Employee turnover, Patents).",
                    "tag": "Framework",
                    "section": "Balanced Scorecard",
                    "trap": "The cause-and-effect chain flows: Learning & Growth -> Internal Processes -> Customer -> Financial."
                },
                {
                    "front": "What are the 5 Facets of the Performance Prism framework (Neely & Adams)?",
                    "back": "1. Stakeholder Satisfaction (Who are our stakeholders and what do they want?)\n2. Strategies (What strategies must we put in place?)\n3. Processes (What processes do we need to execute our strategies?)\n4. Capabilities (What capabilities do we need to operate our processes?)\n5. Stakeholder Contribution (What do we want from our stakeholders in return?).",
                    "tag": "Framework",
                    "section": "Performance Prism",
                    "trap": "Performance Prism recognizes a reciprocal relationship: Stakeholder Satisfaction AND Stakeholder Contribution."
                }
            ]
        }
    ]

    print(f"Seeding comprehensive handbook entries across {len(chapters_data)} master chapters...")

    inserted_count = 0
    flashcards_count = 0

    for ch in chapters_data:
        set_name = ch['set_name']
        chapter_code = ch['chapter_code']

        # 1. Summary
        if 'summary' in ch:
            cursor.execute("""
            INSERT INTO handbook_content (set_name, chapter_code, category, title, content_json, updated_at)
            VALUES (?, ?, 'summary', ?, ?, CURRENT_TIMESTAMP)
            ON CONFLICT(set_name, chapter_code, category) DO UPDATE SET
                title = excluded.title,
                content_json = excluded.content_json,
                updated_at = CURRENT_TIMESTAMP
            """, (set_name, chapter_code, ch['summary']['title'], json.dumps(ch['summary'])))
            inserted_count += 1

        # 2. Formulas & Limits
        if 'formulas_limits' in ch:
            cursor.execute("""
            INSERT INTO handbook_content (set_name, chapter_code, category, title, content_json, updated_at)
            VALUES (?, ?, 'formulas_limits', ?, ?, CURRENT_TIMESTAMP)
            ON CONFLICT(set_name, chapter_code, category) DO UPDATE SET
                title = excluded.title,
                content_json = excluded.content_json,
                updated_at = CURRENT_TIMESTAMP
            """, (set_name, chapter_code, ch['formulas_limits']['title'], json.dumps(ch['formulas_limits'])))
            inserted_count += 1

        # 3. Confused Concepts
        if 'confused_concepts' in ch:
            cursor.execute("""
            INSERT INTO handbook_content (set_name, chapter_code, category, title, content_json, updated_at)
            VALUES (?, ?, 'confused_concepts', ?, ?, CURRENT_TIMESTAMP)
            ON CONFLICT(set_name, chapter_code, category) DO UPDATE SET
                title = excluded.title,
                content_json = excluded.content_json,
                updated_at = CURRENT_TIMESTAMP
            """, (set_name, chapter_code, ch['confused_concepts']['title'], json.dumps(ch['confused_concepts'])))
            inserted_count += 1

        # 4. Exam Traps
        if 'exam_traps' in ch:
            cursor.execute("""
            INSERT INTO handbook_content (set_name, chapter_code, category, title, content_json, updated_at)
            VALUES (?, ?, 'exam_traps', ?, ?, CURRENT_TIMESTAMP)
            ON CONFLICT(set_name, chapter_code, category) DO UPDATE SET
                title = excluded.title,
                content_json = excluded.content_json,
                updated_at = CURRENT_TIMESTAMP
            """, (set_name, chapter_code, ch['exam_traps']['title'], json.dumps(ch['exam_traps'])))
            inserted_count += 1

        # 5. Flashcards
        if 'flashcards' in ch and ch['flashcards']:
            cursor.execute("""
            INSERT INTO handbook_content (set_name, chapter_code, category, title, content_json, updated_at)
            VALUES (?, ?, 'flashcards', ?, ?, CURRENT_TIMESTAMP)
            ON CONFLICT(set_name, chapter_code, category) DO UPDATE SET
                title = excluded.title,
                content_json = excluded.content_json,
                updated_at = CURRENT_TIMESTAMP
            """, (set_name, chapter_code, f"Revision Flashcards - {chapter_code}", json.dumps(ch['flashcards'])))
            inserted_count += 1
            flashcards_count += len(ch['flashcards'])

    conn.commit()
    conn.close()
    print(f"Successfully seeded {inserted_count} handbook categories and {flashcards_count} interactive flashcards.")

if __name__ == '__main__':
    seed_comprehensive_handbook()
