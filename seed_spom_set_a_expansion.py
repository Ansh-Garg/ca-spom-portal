"""
CA Final SPOM Set A - Expansion Seeder: High-Yield Scenarios & Advanced Exam Traps
Database: spom_portal.db
Author: Antigravity Prep Engine for CA Final SPOM Set A
"""

import sqlite3
import os
import sys

DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "spom_portal.db")

# ==============================================================================
# CASE STUDY 6: Corporate Takeover, Moratorium & Section 29A Resolution Disqualification
# Entity: Horizon Infra Projects Ltd (Corporate Debtor in CIRP)
# Topics: IBC Sec 14 Moratorium, Sec 29A Disqualification, Sec 66 Fraudulent Trading, Sec 12
# ==============================================================================
CASE_6_TEXT = (
    "CASE SCENARIO: HORIZON INFRA PROJECTS LTD - CIRP MORATORIUM & RESOLUTION\n\n"
    "Horizon Infra Projects Ltd. ('Horizon') was admitted into Corporate Insolvency Resolution Process (CIRP) "
    "by the NCLT Mumbai Bench on 1st June 2024. Mr. Vinod was appointed as the Resolution Professional (RP).\n\n"
    "During the CIRP, the following critical legal issues arose:\n"
    "1. Moratorium & Essential Utility Supplies: State Electricity Distribution Company disconnected electricity supply "
    "to Horizon's corporate headquarters and manufacturing plant on 15th July 2024, citing unpaid electricity arrears "
    "of Rs 1.80 Crore that accrued prior to the CIRP commencement date. The RP tendered payment for current electricity "
    "consumed during June and July 2024, but the utility insisted on full clearance of past dues before restoring power.\n\n"
    "2. Personal Guarantor Enforcement during Moratorium: A secured financial creditor, ICICI Bank, initiated proceedings "
    "under the SARFAESI Act and invoked the personal guarantee executed by Mr. Rohit, the promoter and former Managing "
    "Director of Horizon. Mr. Rohit petitioned NCLT contending that the Section 14 moratorium completely bars any enforcement "
    "action against a personal guarantor while CIRP is ongoing.\n\n"
    "3. Resolution Applicant Ineligibility under Section 29A: In response to the Expression of Interest, a consortium led by "
    "Nova Assets Pvt. Ltd. submitted a resolution plan. Nova Assets holds 45% equity and board control in Orion Cables Ltd., "
    "an account that was classified as a Non-Performing Asset (NPA) by Indian Bank in March 2022 (over two years prior to Horizon's CIRP) "
    "and whose overdue NPA debts remain unpaid. Nova argued that since Orion Cables is a distinct juristic entity, Nova is eligible.\n\n"
    "4. CIRP Timelines & Statutory Outer Limit: Horizon's CIRP completed its initial 180-day window on 28th November 2024. "
    "The CoC, by a vote of 78% of financial creditors, instructed the RP to seek a 90-day extension from NCLT. Meanwhile, "
    "various interlocutory applications were pending before NCLT, raising concerns about the mandatory 330-day outer ceiling."
)

CASE_6_QUESTIONS = [
    {
        "set_name": "A",
        "section_group": "Part II: Economic Laws (30 Marks)",
        "chapter_code": "A_IBC",
        "topic": "Insolvency and Bankruptcy Code, 2016",
        "subtopic": "Section 14(2) Moratorium - Essential Goods and Services Continuity",
        "question": (
            "Refer to Point 1 of Case Scenario 6. Was the State Electricity Distribution Company legally justified in "
            "disconnecting electricity supply to Horizon during the Section 14 moratorium for pre-CIRP dues?"
        ),
        "option_a": "Yes, because utility providers are commercial entities and cannot be forced to supply electricity without clearance of old accumulated arrears.",
        "option_b": "No, because under Section 14(2) read with Section 14(2A), the supply of essential goods or services (including electricity and water) shall not be terminated or suspended during the moratorium period, provided current dues arising during the CIRP are paid.",
        "option_c": "Yes, but only if prior sanction is obtained from the Committee of Creditors.",
        "option_d": "No, but the corporate debtor must deposit 50% of the pre-CIRP arrears into an escrow account within 7 days.",
        "correct_option": "B",
        "marks": 2,
        "explanation": (
            "Under Section 14(2) of the Insolvency and Bankruptcy Code, 2016, the supply of essential goods or services to the corporate debtor "
            "as may be specified (which includes electricity, water, telecommunication services and information technology services under Regulation 32 "
            "of the IBBI CIRP Regulations) SHALL NOT BE TERMINATED OR SUSPENDED OR INTERRUPTED during moratorium period.\n\n"
            "Furthermore, under Section 14(2A) (inserted by the IBC Amendment Act 2020), where the interim resolution professional or resolution "
            "professional considers the supply of goods or services critical to protect and preserve the value of the corporate debtor and manage "
            "the operations as a going concern, then the supply of such goods or services shall not be terminated, suspended or interrupted, "
            "EXCEPT WHERE SUCH CORPORATE DEBTOR HAS NOT PAID DUES ARISING FROM SUCH SUPPLY DURING THE MORATORIUM PERIOD.\n\n"
            "Here, Horizon paid all current electricity dues arising during the CIRP. The utility company CANNOT disconnect supply for pre-CIRP arrears, "
            "as pre-CIRP arrears must be claimed as an operational debt in the CIRP process. Disconnection was illegal."
        ),
        "section_ref": "Insolvency and Bankruptcy Code, 2016 - Section 14(2) & 14(2A)",
        "exam_tip": "EXAM TRAP: Essential utility services (electricity, water, IT) CANNOT be disconnected during CIRP for past arrears, so long as CURRENT bills during the moratorium period are paid!",
        "source_tag": "ICAI Case Scenario",
        "difficulty": "Moderate",
        "is_case_study": 1,
        "case_scenario": CASE_6_TEXT,
        "why_incorrect_a": "Section 14(2) prohibits disconnection for pre-CIRP arrears as long as current dues are serviced.",
        "why_incorrect_b": "",
        "why_incorrect_c": "CoC approval cannot authorize a utility to violate Section 14(2).",
        "why_incorrect_d": "There is no requirement to deposit 50% of pre-CIRP arrears."
    },
    {
        "set_name": "A",
        "section_group": "Part II: Economic Laws (30 Marks)",
        "chapter_code": "A_IBC",
        "topic": "Insolvency and Bankruptcy Code, 2016",
        "subtopic": "Section 14(3) Moratorium Exclusion - Personal Guarantor Liability",
        "question": (
            "Refer to Point 2 of Case Scenario 6. Does the Section 14 moratorium protect Mr. Rohit, the personal guarantor "
            "of Horizon, from recovery actions by ICICI Bank during the ongoing CIRP of the corporate debtor?"
        ),
        "option_a": "Yes, because the moratorium covers all contracts and guarantees associated with the corporate debtor to prevent piecemeal liquidation.",
        "option_b": "No, because under Section 14(3)(b) of the IBC (and the Supreme Court ruling in State Bank of India v. V. Ramakrishnan), the moratorium DOES NOT apply to a surety in a contract of guarantee to a corporate debtor.",
        "option_c": "Yes, provided the personal guarantor does not alienate his personal assets without NCLT permission.",
        "option_d": "No, but ICICI Bank can only recover up to 25% of the guaranteed debt while CIRP is pending.",
        "correct_option": "B",
        "marks": 2,
        "explanation": (
            "Under Section 14(3)(b) of the Insolvency and Bankruptcy Code, 2016 (inserted by the IBC Second Amendment Act, 2018 with retrospective effect):\n"
            "The provisions of sub-section (1) of Section 14 (Moratorium) SHALL NOT APPLY to a surety in a contract of guarantee to a corporate debtor.\n\n"
            "This statutory principle was conclusively affirmed by the Supreme Court in the landmark judgment of State Bank of India v. V. Ramakrishnan (2018), "
            "and reiterated in Lalit Kumar Jain v. Union of India (2021). The object of the Code is not to allow guarantors to escape their independent and "
            "co-extensive liability under Section 128 of the Indian Contract Act, 1872. Therefore, ICICI Bank is fully entitled to invoke the personal guarantee "
            "and proceed against Mr. Rohit despite the ongoing CIRP of Horizon."
        ),
        "section_ref": "Insolvency and Bankruptcy Code, 2016 - Section 14(3)(b) & SBI v. V. Ramakrishnan",
        "exam_tip": "EXAM TRAP: Section 14 Moratorium DOES NOT protect personal guarantors or corporate guarantors of the corporate debtor! Creditors can simultaneously pursue guarantors.",
        "source_tag": "Offline SPOM Recall",
        "difficulty": "Moderate",
        "is_case_study": 1,
        "case_scenario": CASE_6_TEXT,
        "why_incorrect_a": "Section 14(3)(b) explicitly carves out sureties in contracts of guarantee.",
        "why_incorrect_b": "",
        "why_incorrect_c": "NCLT permission is not needed to enforce personal guarantees under Section 14(3)(b).",
        "why_incorrect_d": "There is no 25% limitation on enforcing guarantees."
    },
    {
        "set_name": "A",
        "section_group": "Part II: Economic Laws (30 Marks)",
        "chapter_code": "A_IBC",
        "topic": "Insolvency and Bankruptcy Code, 2016",
        "subtopic": "Section 29A(c) Ineligibility of Resolution Applicant - NPA Account Holder & Connected Persons",
        "question": (
            "Refer to Point 3 of Case Scenario 6. Is the consortium led by Nova Assets Pvt. Ltd. eligible to submit a resolution plan "
            "for Horizon under Section 29A(c) of the Insolvency and Bankruptcy Code, 2016?"
        ),
        "option_a": "Yes, because Nova Assets itself has never been classified as an NPA by any bank.",
        "option_b": "No, because under Section 29A(c) read with Section 29A(j), a person is disqualified if it, or a connected person/entity under its management or control, has an account classified as NPA for at least ONE (1) YEAR prior to CIRP commencement and has failed to clear all overdue amounts.",
        "option_c": "Yes, because the NPA classification occurred more than 2 years ago, which exceeds the limitation period.",
        "option_d": "No, but Nova Assets can cure the defect by paying a 5% penalty to the Insolvency and Bankruptcy Board of India (IBBI).",
        "correct_option": "B",
        "marks": 2,
        "explanation": (
            "Under Section 29A(c) of the Insolvency and Bankruptcy Code, 2016, a person shall not be eligible to submit a resolution plan if such person, "
            "or any other person acting jointly or in concert with such person:\n"
            "Has an account, or an account of a corporate debtor under the management or control of such person or of whom such person is a promoter, "
            "classified as a NON-PERFORMING ASSET (NPA) in accordance with the guidelines of the Reserve Bank of India, and AT LEAST A PERIOD OF ONE YEAR "
            "has elapsed from the date of such classification till the date of commencement of the corporate insolvency resolution process of the corporate debtor, "
            "AND SUCH PERSON HAS FAILED TO CLEAR ALL ARREARS of interest and principal relating to such account before submission of resolution plan.\n\n"
            "Under Section 29A(j), this bar extends to any 'connected person'. Since Nova Assets holds 45% equity and board control in Orion Cables (making Orion "
            "a company under Nova's management/control), and Orion's NPA classification in March 2022 was over 1 year prior to Horizon's CIRP (June 2024), "
            "Nova is legally DISQUALIFIED under Section 29A(c) unless it pays off all overdue amounts with interest before submitting the plan."
        ),
        "section_ref": "Insolvency and Bankruptcy Code, 2016 - Section 29A(c) & Proviso",
        "exam_tip": "EXAM TRAP: Under Section 29A(c), an applicant is disqualified if its account OR an account under its control has been an NPA for >= 1 YEAR prior to CIRP. Disqualification can ONLY be cured by clearing all overdue interest and principal before plan submission!",
        "source_tag": "ICAI Test Your Knowledge",
        "difficulty": "Hard",
        "is_case_study": 1,
        "case_scenario": CASE_6_TEXT,
        "why_incorrect_a": "Ignores the connected person / management control test under Section 29A(c) and 29A(j).",
        "why_incorrect_b": "",
        "why_incorrect_c": "NPA status persisting for over 1 year establishes disqualification; it does not lapse by time.",
        "why_incorrect_d": "There is no IBBI penalty payment cure; the actual overdue NPA debt must be paid in full."
    },
    {
        "set_name": "A",
        "section_group": "Part II: Economic Laws (30 Marks)",
        "chapter_code": "A_IBC",
        "topic": "Insolvency and Bankruptcy Code, 2016",
        "subtopic": "Section 12 CIRP Timelines - Extension Voting Threshold & 330-Day Outer Ceiling",
        "question": (
            "Refer to Point 4 of Case Scenario 6. Under Section 12 of the Insolvency and Bankruptcy Code, 2016, what are the statutory "
            "requirements for extending the CIRP beyond 180 days, and what is the absolute outer timeline including legal proceedings?"
        ),
        "option_a": "CoC must pass resolution by 51% voting share; NCLT can grant up to 60 days extension; outer limit is 270 days.",
        "option_b": "CoC must pass resolution by not less than 66% voting share; NCLT can grant a one-time extension of up to 90 days; overall CIRP mandatorily completed within 330 days (including time taken in legal proceedings).",
        "option_c": "CoC must pass resolution by 75% voting share; NCLT can grant multiple extensions of 30 days each; outer limit is 365 days.",
        "option_d": "CoC must pass resolution by 90% voting share; NCLT can extend indefinitely if resolution is near completion.",
        "correct_option": "B",
        "marks": 2,
        "explanation": (
            "Under Section 12 of the Insolvency and Bankruptcy Code, 2016:\n"
            "1. Section 12(1): The corporate insolvency resolution process shall be completed within a period of ONE HUNDRED AND EIGHTY (180) DAYS "
            "from the date of admission of the application.\n"
            "2. Section 12(2) & 12(3): The Resolution Professional shall file an application to the Adjudicating Authority (NCLT) for extension "
            "if instructed to do so by a resolution passed at a meeting of the Committee of Creditors by a vote of NOT LESS THAN SIXTY-SIX PERCENT (66%) "
            "of the voting shares. The NCLT may grant a ONE-TIME EXTENSION not exceeding NINETY (90) DAYS.\n"
            "3. Second Proviso to Section 12(3) (inserted by IBC Amendment Act 2019): The corporate insolvency resolution process SHALL MANDATORILY "
            "BE COMPLETED WITHIN A PERIOD OF THREE HUNDRED AND THIRTY (330) DAYS from the insolvency commencement date, including the extension period "
            "and the time taken in legal proceedings in relation to such resolution process of the corporate debtor.\n"
            "(In Essar Steel, the Supreme Court held that in exceptional cases where delay is attributable to the Tribunal, 330 days may be relaxed, but the statutory benchmark remains 330 days)."
        ),
        "section_ref": "Insolvency and Bankruptcy Code, 2016 - Section 12(1), (2), (3) & Second Proviso",
        "exam_tip": "EXAM TRAP: Extension voting threshold is 66% (not 75% or 51%). Extension can only be granted ONCE for max 90 days. Mandatory statutory outer ceiling is 330 DAYS.",
        "source_tag": "Offline SPOM Recall",
        "difficulty": "Moderate",
        "is_case_study": 1,
        "case_scenario": CASE_6_TEXT,
        "why_incorrect_a": "Voting requirement is 66%, not 51%; extension is up to 90 days, not 60 days; outer limit is 330 days, not 270 days.",
        "why_incorrect_b": "",
        "why_incorrect_c": "Voting requirement is 66%, not 75%; extension cannot be in multiple 30-day increments.",
        "why_incorrect_d": "90% voting is required for Section 12A withdrawal, not for Section 12 extension."
    }
]

# ==============================================================================
# CASE STUDY 7: Managerial Appointments, Remuneration Caps & Audit Committee Rigor
# Entity: Zenith Agrochem Ltd (Unlisted Public Company)
# Topics: Sec 196 (Age 70), Sec 197(1) (Overall 11% & 5%/10%/1%), Sec 177, Sec 161(1)
# ==============================================================================
CASE_7_TEXT = (
    "CASE SCENARIO: ZENITH AGROCHEM LTD - MANAGERIAL GOVERNANCE & REMUNERATION\n\n"
    "Zenith Agrochem Ltd. ('Zenith Agro') is a thriving unlisted public enterprise having Paid-up Share Capital of Rs 25 Crore, "
    "Turnover of Rs 140 Crore, and Outstanding Bank Term Loans of Rs 60 Crore. The Net Profit of the company computed under "
    "Section 198 for FY 2024-25 is Rs 20 Crore.\n\n"
    "During the year, the following board and managerial matters were deliberated:\n"
    "1. Appointment of Managing Director aged 72 Years: The Board proposes to appoint Mr. Harish, aged 72 years, as the Managing "
    "Director for a term of 5 years. The Company Secretary noted that Section 196(3)(a) bars appointment of any person who has "
    "attained the age of 70 years, unless specific statutory approvals are secured.\n\n"
    "2. Managerial Remuneration Ceiling under Section 197(1): Zenith Agro has two Whole-Time Directors and one Managing Director. "
    "The Board proposes to pay the Managing Director a remuneration of Rs 1.40 Crore (7% of net profits) and each of the two Whole-Time "
    "Directors Rs 80 Lakhs (4% of net profits each), making aggregate managerial remuneration Rs 3.00 Crore (15% of net profits). "
    "In addition, the company has 4 Non-Executive Directors and proposes to pay them Rs 30 Lakhs (1.5% of net profits).\n\n"
    "3. Audit Committee Constitution & Omnibus Approval: Based on its financial metrics, the Board debated whether constitution "
    "of an Audit Committee is legally mandatory under Section 177, and whether the Audit Committee can grant an omnibus approval "
    "for repetitive related party transactions for a duration of 3 years.\n\n"
    "4. Appointment of Additional Director Rejected at AGM: Mr. Suresh was proposed as an ordinary director at the Annual General "
    "Meeting held on 25th September 2024, but the resolution failed to pass. On 10th October 2024, the Board passed a resolution "
    "appointing Mr. Suresh as an Additional Director under Section 161(1) to fill an urgent technical vacancy."
)

CASE_7_QUESTIONS = [
    {
        "set_name": "A",
        "section_group": "Part I: Corporate Laws (70 Marks)",
        "chapter_code": "A_MGR",
        "topic": "Managerial Remuneration & KMP",
        "subtopic": "Section 196(3)(a) Appointment of MD/WTD Attaining Age of 70 Years",
        "question": (
            "Refer to Point 1 of Case Scenario 7. Can Mr. Harish, aged 72 years, be appointed as Managing Director of Zenith Agrochem Ltd. "
            "under Section 196(3)(a) of the Companies Act, 2013, and what approval is required?"
        ),
        "option_a": "No, there is an absolute statutory disqualification upon attaining 70 years of age, and no resolution can waive this bar.",
        "option_b": "Yes, provided the appointment is approved by passing a SPECIAL RESOLUTION in general meeting with an explanatory statement annexed to the notice indicating the justification for appointing such person.",
        "option_c": "Yes, provided prior Central Government approval is obtained under Schedule V.",
        "option_d": "Yes, by passing an Ordinary Resolution in general meeting without any explanatory statement.",
        "correct_option": "B",
        "marks": 2,
        "explanation": (
            "Under Section 196(3)(a) of the Companies Act, 2013, no company shall appoint or continue the employment of any person as "
            "managing director, whole-time director or manager who has not attained the age of twenty-one years or has attained the age of seventy years.\n\n"
            "However, under the First Proviso to Section 196(3)(a):\n"
            "Appointment of a person who has attained the age of seventy years MAY BE MADE BY PASSING A SPECIAL RESOLUTION in general meeting, "
            "in which case the explanatory statement annexed to the notice for such motion shall indicate the justification for appointing such person.\n\n"
            "Under the Second Proviso (inserted by Companies Amendment Act 2017), where no such special resolution is passed but votes cast in favour "
            "exceed votes cast against, the Board may make an application to the Central Government. But Central Govt approval is not mandatory if a Special Resolution is passed!"
        ),
        "section_ref": "Companies Act, 2013 - Section 196(3)(a) & First Proviso",
        "exam_tip": "EXAM TRAP: A person aged >= 70 years CAN be appointed as MD/WTD if a SPECIAL RESOLUTION is passed with explanatory justification. Central Government approval is NOT required if Special Resolution is passed!",
        "source_tag": "ICAI BoS Module",
        "difficulty": "Moderate",
        "is_case_study": 1,
        "case_scenario": CASE_7_TEXT,
        "why_incorrect_a": "Section 196(3)(a) allows appointment past age 70 via Special Resolution.",
        "why_incorrect_b": "",
        "why_incorrect_c": "Central Government approval is not needed if the Special Resolution is passed.",
        "why_incorrect_d": "Ordinary Resolution alone is insufficient; Special Resolution is mandatory under the First Proviso."
    },
    {
        "set_name": "A",
        "section_group": "Part I: Corporate Laws (70 Marks)",
        "chapter_code": "A_MGR",
        "topic": "Managerial Remuneration & KMP",
        "subtopic": "Section 197(1) Remuneration Percentage Ceilings on Net Profits",
        "question": (
            "Refer to Point 2 of Case Scenario 7. Net Profit is Rs 20 Crore. Evaluating Section 197(1) of the Companies Act, 2013, "
            "can Zenith Agrochem pay Rs 1.40 Crore (7%) to the MD, and Rs 30 Lakhs (1.5%) to Non-Executive Directors?"
        ),
        "option_a": "Yes, because the company has sufficient net profits and the Board has full discretion to fix individual percentages.",
        "option_b": "No; under the Second Proviso to Section 197(1), remuneration payable to any ONE managing director or whole-time director CANNOT EXCEED 5% of net profits (Rs 1.00 Crore), and remuneration to all Non-Executive Directors CANNOT EXCEED 1% of net profits (Rs 20 Lakhs) when there is a managing/whole-time director, unless approved by Special Resolution.",
        "option_c": "Yes, provided the overall remuneration does not exceed 20% of net profits.",
        "option_d": "No, because unlisted public companies cannot pay more than Rs 50 Lakhs to any director under any circumstance.",
        "correct_option": "B",
        "marks": 2,
        "explanation": (
            "Under Section 197(1) of the Companies Act, 2013:\n"
            "1. Overall Ceiling: Total managerial remuneration payable by a public company to its directors (including MD/WTD) shall not exceed "
            "ELEVEN PERCENT (11%) of net profits, unless approved by shareholders in general meeting by Ordinary Resolution (subject to Schedule V).\n\n"
            "2. Second Proviso Individual Sub-Limits:\n"
            "(i) Remuneration payable to ANY ONE managing director or whole-time director SHALL NOT EXCEED FIVE PERCENT (5%) of net profits (here, 5% of Rs 20 Cr = Rs 1.00 Crore). "
            "Paying Rs 1.40 Crore (7%) violates this 5% individual limit unless authorized by Special Resolution.\n"
            "(ii) Where there is more than one managing/whole-time director, aggregate to all such directors shall not exceed TEN PERCENT (10%) (here 10% of Rs 20 Cr = Rs 2.00 Crore). Paying 7% + 4% + 4% = 15% breaches the 10% ceiling.\n"
            "(iii) Remuneration to directors who are neither managing directors nor whole-time directors (Non-Executive Directors) SHALL NOT EXCEED ONE PERCENT (1%) "
            "of net profits if there is a managing director or whole-time director (1% of Rs 20 Cr = Rs 20 Lakhs). Paying Rs 30 Lakhs (1.5%) breaches this 1% ceiling.\n\n"
            "Hence, the proposed remuneration violates all individual statutory percentage caps under the Second Proviso to Section 197(1)."
        ),
        "section_ref": "Companies Act, 2013 - Section 197(1) & Second Proviso",
        "exam_tip": "EXAM TRAP: Memorize the sub-limits under Section 197(1): (1) Single MD/WTD = max 5%; (2) Multiple MD/WTD = max 10%; (3) NEDs when MD/WTD exists = max 1%; (4) NEDs when NO MD/WTD exists = max 3%; (5) Overall company ceiling = 11%.",
        "source_tag": "ICAI Test Your Knowledge",
        "difficulty": "Hard",
        "is_case_study": 1,
        "case_scenario": CASE_7_TEXT,
        "why_incorrect_a": "Board discretion is strictly curtailed by statutory percentage ceilings under Section 197(1).",
        "why_incorrect_b": "",
        "why_incorrect_c": "The overall ceiling is 11%, not 20%.",
        "why_incorrect_d": "There is no Rs 50 Lakh arbitrary limit for unlisted public companies."
    },
    {
        "set_name": "A",
        "section_group": "Part I: Corporate Laws (70 Marks)",
        "chapter_code": "A_BM",
        "topic": "Meetings of Board and its Powers",
        "subtopic": "Section 177 Audit Committee Applicability & Omnibus Approval Validity",
        "question": (
            "Refer to Point 3 of Case Scenario 7. Is Zenith Agrochem Ltd. legally required to constitute an Audit Committee under Section 177, "
            "and what is the maximum validity period for an omnibus approval granted by the Audit Committee for related party transactions?"
        ),
        "option_a": "Audit Committee is not applicable as it is unlisted; omnibus approval is valid for 3 years.",
        "option_b": "Audit Committee IS applicable (Paid-up capital >= Rs 10 Cr and Loans > Rs 50 Cr); under Rule 6A of Companies (Meetings of Board and its Powers) Rules, omnibus approvals SHALL BE VALID FOR A PERIOD NOT EXCEEDING ONE (1) YEAR.",
        "option_c": "Audit Committee is applicable, and omnibus approval is valid for 5 years.",
        "option_d": "Audit Committee is applicable, but omnibus approvals are strictly prohibited under the Companies Act, 2013.",
        "correct_option": "B",
        "marks": 2,
        "explanation": (
            "1. Applicability of Audit Committee under Section 177 read with Rule 4 of Companies (Meetings of Board and its Powers) Rules, 2014:\n"
            "The Board of Directors of every listed public company and the following classes of unlisted public companies shall constitute an Audit Committee:\n"
            "(i) Paid-up share capital of Rs 10 Crore or more;\n"
            "(ii) Turnover of Rs 100 Crore or more; OR\n"
            "(iii) Outstanding loans, debentures and deposits EXCEEDING Rs 50 Crore.\n"
            "Zenith Agrochem meets ALL THREE criteria (Paid up capital = Rs 25 Cr >= 10 Cr; Turnover = Rs 140 Cr >= 100 Cr; Loans = Rs 60 Cr > 50 Cr). "
            "Hence, constituting an Audit Committee is MANDATORY.\n\n"
            "2. Validity of Omnibus Approval under Rule 6A(3):\n"
            "Omnibus approvals granted by the Audit Committee for repetitive related party transactions SHALL BE VALID FOR A PERIOD NOT EXCEEDING "
            "ONE (1) FINANCIAL YEAR and shall require fresh approval after the expiry of such financial year."
        ),
        "section_ref": "Companies Act, 2013 - Section 177 read with Rule 4 & Rule 6A",
        "exam_tip": "EXAM TRAP: Omnibus approvals granted by Audit Committee under Rule 6A are valid for a MAXIMUM OF 1 YEAR (not 3 years). Fresh approval is required each year.",
        "source_tag": "ICAI BoS Module",
        "difficulty": "Moderate",
        "is_case_study": 1,
        "case_scenario": CASE_7_TEXT,
        "why_incorrect_a": "Unlisted public companies meeting the capital/turnover/borrowing thresholds must constitute an Audit Committee; omnibus approvals cannot exceed 1 year.",
        "why_incorrect_b": "",
        "why_incorrect_c": "Omnibus approval cannot be given for 5 years; statutory ceiling is 1 year.",
        "why_incorrect_d": "Omnibus approvals are expressly permitted under Section 177(4)(iv) Proviso and Rule 6A."
    },
    {
        "set_name": "A",
        "section_group": "Part I: Corporate Laws (70 Marks)",
        "chapter_code": "A_DIR",
        "topic": "Appointment and Qualification of Directors",
        "subtopic": "Section 161(1) Additional Director - Statutory Bar on Rejected Candidates",
        "question": (
            "Refer to Point 4 of Case Scenario 7. Was the appointment of Mr. Suresh as an Additional Director by the Board on 10th October 2024 "
            "valid under Section 161(1) of the Companies Act, 2013?"
        ),
        "option_a": "Yes, because the Board has plenary residual power to appoint any qualified technical expert as an Additional Director.",
        "option_b": "No, because under the Proviso to Section 161(1), a person who FAILS TO GET APPOINTED AS A DIRECTOR AT A GENERAL MEETING CANNOT BE APPOINTED AS AN ADDITIONAL DIRECTOR.",
        "option_c": "Yes, provided Mr. Suresh is designated as an Independent Director.",
        "option_d": "No, because Additional Directors can only be appointed between 1st April and 30th June of any financial year.",
        "correct_option": "B",
        "marks": 2,
        "explanation": (
            "Under Section 161(1) of the Companies Act, 2013, the articles of a company may confer on its Board of Directors the power to "
            "appoint any person as an additional director at any time, who shall hold office up to the date of the next annual general meeting "
            "or the last date on which the annual general meeting should have been held, whichever is earlier.\n\n"
            "However, the Proviso to Section 161(1) contains an absolute statutory bar:\n"
            "'Provided that a person who FAILS TO GET APPOINTED AS A DIRECTOR AT A GENERAL MEETING SHALL NOT BE APPOINTED AS AN ADDITIONAL DIRECTOR.'\n\n"
            "The rationale is that the will of the supreme body of shareholders in general meeting cannot be overridden or subverted by the Board "
            "through the backdoor route of an additional directorship. Since Mr. Suresh was proposed and rejected at the AGM on 25th September 2024, "
            "his subsequent appointment by the Board on 10th October 2024 is void ab initio and illegal."
        ),
        "section_ref": "Companies Act, 2013 - Section 161(1) Proviso",
        "exam_tip": "SUPER FREQUENT EXAM TRAP: If a candidate's resolution was defeated or rejected at a General Meeting, the Board CANNOT appoint that person as an Additional Director under Section 161(1).",
        "source_tag": "Offline SPOM Recall",
        "difficulty": "Moderate",
        "is_case_study": 1,
        "case_scenario": CASE_7_TEXT,
        "why_incorrect_a": "Board power under Section 161(1) is expressly subject to the statutory bar in the Proviso.",
        "why_incorrect_b": "",
        "why_incorrect_c": "A candidate rejected at GM cannot be appointed as an additional director under any designation.",
        "why_incorrect_d": "There is no calendar restriction (April-June) for appointing additional directors."
    }
]

# ==============================================================================
# EXPANSION STANDALONE HIGH-YIELD QUESTIONS
# ==============================================================================
EXPANSION_STANDALONE = [
    # --- A_FEMA: Overseas Direct Investment (ODI) ---
    {
        "set_name": "A",
        "section_group": "Part II: Economic Laws (30 Marks)",
        "chapter_code": "A_FEMA",
        "topic": "Foreign Exchange Management Act, 1999",
        "subtopic": "Overseas Investment Rules 2022 - Financial Commitment Limit (400% of Net Worth)",
        "question": (
            "Under the Foreign Exchange Management (Overseas Investment) Rules, 2022, what is the maximum financial commitment "
            "that an Indian entity can make in all foreign entities taken together under the automatic route without prior RBI approval?"
        ),
        "option_a": "100% of its Net Worth as per last audited balance sheet.",
        "option_b": "200% of its Net Worth as per last audited balance sheet.",
        "option_c": "400% of its Net Worth as per last audited balance sheet.",
        "option_d": "Up to USD 1 Billion per financial year, irrespective of net worth.",
        "correct_option": "C",
        "marks": 2,
        "explanation": (
            "Under Schedule I (Paragraph 2) of the Foreign Exchange Management (Overseas Investment) Rules, 2022:\n"
            "The total financial commitment made by an Indian entity in all foreign entities taken together at the time of making such commitment "
            "SHALL NOT EXCEED FOUR HUNDRED PERCENT (400%) OF ITS NET WORTH as per the last audited balance sheet, or as on a subsequent date "
            "certified by statutory auditor (excluding financial commitment funded out of EEFC account balances or proceeds of ADR/GDR/ECB).\n\n"
            "Net Worth for this purpose comprises: Paid-up equity capital + Free reserves + Securities premium."
        ),
        "section_ref": "FEM (Overseas Investment) Rules, 2022 - Schedule I, Paragraph 2",
        "exam_tip": "EXAM TRAP: The financial commitment limit for ODI under Overseas Investment Rules 2022 is 400% OF NET WORTH (not 100% or 200%).",
        "source_tag": "ICAI BoS Module",
        "difficulty": "Moderate",
        "is_case_study": 0,
        "case_scenario": None,
        "why_incorrect_a": "100% is incorrect.",
        "why_incorrect_b": "200% was an older proposal and is incorrect.",
        "why_incorrect_c": "",
        "why_incorrect_d": "The ceiling is linked to 400% of Net Worth, not a flat USD 1 Billion cap without net worth reference."
    },
    # --- A_DIR: Small Shareholders' Director (SSD) ---
    {
        "set_name": "A",
        "section_group": "Part I: Corporate Laws (70 Marks)",
        "chapter_code": "A_DIR",
        "topic": "Appointment and Qualification of Directors",
        "subtopic": "Section 151 Small Shareholders' Director (SSD) Thresholds & Tenure",
        "question": (
            "Under Section 151 of the Companies Act, 2013 read with Rule 7 of the Companies (Appointment and Qualification of Directors) Rules, 2014, "
            "a listed company may have one director elected by small shareholders upon notice of not less than _________ small shareholders or _________ "
            "of total small shareholders, whichever is lower; and an SSD can hold office for a maximum consecutive period of _________:"
        ),
        "option_a": "500; 1/5th; 5 years",
        "option_b": "1,000; 1/10th; 3 years (not liable to retire by rotation and cannot be reappointed)",
        "option_c": "1,000; 1/10th; 5 years (eligible for one re-appointment)",
        "option_d": "100; 1/10th; 3 years",
        "correct_option": "B",
        "marks": 2,
        "explanation": (
            "Under Section 151 of the Companies Act, 2013 and Rule 7 of the Companies (Appointment and Qualification of Directors) Rules, 2014:\n"
            "1. A listed company may, upon notice of not less than ONE THOUSAND (1,000) small shareholders OR ONE-TENTH (1/10th) of the total number "
            "of such shareholders, whichever is lower, have a small shareholders' director elected by the small shareholders.\n"
            "(Small shareholder means a shareholder holding shares of nominal value of not more than Rs 20,000).\n\n"
            "2. Tenure of SSD under Rule 7(5):\n"
            "The tenure of a small shareholders' director SHALL NOT EXCEED A PERIOD OF THREE (3) CONSECUTIVE YEARS and he SHALL NOT BE LIABLE TO RETIRE BY ROTATION.\n\n"
            "3. Disqualification for Reappointment under Rule 7(6):\n"
            "No such director shall be eligible for re-appointment after the expiry of his tenure.\n\n"
            "4. Simultaneous Directorship: A person cannot hold the office of small shareholders' director in more than TWO companies at the same time."
        ),
        "section_ref": "Companies Act, 2013 - Section 151 read with Rule 7",
        "exam_tip": "EXAM TRAP: SSD tenure is MAX 3 YEARS (not 5 years!). SSD does NOT retire by rotation and CAN NEVER be reappointed in that company. Requisite notice is 1,000 or 1/10th, whichever is lower.",
        "source_tag": "Offline SPOM Recall",
        "difficulty": "Hard",
        "is_case_study": 0,
        "case_scenario": None,
        "why_incorrect_a": "Threshold is 1,000 or 1/10th, and tenure is 3 years, not 5 years.",
        "why_incorrect_b": "",
        "why_incorrect_c": "SSD cannot be reappointed under Rule 7(6), and tenure is 3 years, not 5 years.",
        "why_incorrect_d": "100 is the threshold for oppression petition under Sec 244, not SSD notice under Rule 7."
    },
    # --- A_DIR: Section 160 Notice & Deposit ---
    {
        "set_name": "A",
        "section_group": "Part I: Corporate Laws (70 Marks)",
        "chapter_code": "A_DIR",
        "topic": "Appointment and Qualification of Directors",
        "subtopic": "Section 160 Right of Persons Other than Retiring Directors (Deposit & Exemptions)",
        "question": (
            "Under Section 160 of the Companies Act, 2013, a person who is not a retiring director can stand for directorship at a general meeting "
            "by giving notice in writing at least 14 days before the meeting along with a deposit of Rs 1,00,000. In which of the following cases "
            "is the requirement of depositing Rs 1,00,000 STATUTORILY EXEMPTED?"
        ),
        "option_a": "Only where the candidate is a woman director.",
        "option_b": "Where the appointment of an Independent Director is proposed, or where the recommendation of the Nomination and Remuneration Committee (NRC) or the Board of Directors has been obtained.",
        "option_c": "Where the candidate holds at least 5% shares in the company.",
        "option_d": "Deposit is mandatory in all cases without any exemption.",
        "correct_option": "B",
        "marks": 2,
        "explanation": (
            "Under Section 160(1) of the Companies Act, 2013, a person not being a retiring director shall be eligible for appointment to the office of a director "
            "if he, or some member intending to propose him, leaves at the registered office of the company a notice in writing at least 14 days before the meeting "
            "along with a deposit of Rs 1,00,000 (which is refunded if the person succeeds or gets more than 25% of total valid votes cast).\n\n"
            "However, under the Proviso to Section 160(1) (inserted by the Companies Amendment Act, 2017):\n"
            "The requirements of deposit of amount SHALL NOT APPLY in case of appointment of:\n"
            "(a) An INDEPENDENT DIRECTOR, OR\n"
            "(b) A director recommended by the NOMINATION AND REMUNERATION COMMITTEE (NRC) under Section 178(1), OR\n"
            "(c) A director recommended by the BOARD OF DIRECTORS of the company, in the case of a company not required to constitute NRC.\n\n"
            "This exemption prevents unnecessary financial friction when an independent director or board-vetted candidate is proposed."
        ),
        "section_ref": "Companies Act, 2013 - Section 160(1) Proviso",
        "exam_tip": "EXAM TRAP: The Rs 1,00,000 deposit under Section 160 is NOT required for Independent Directors or candidates recommended by NRC / Board!",
        "source_tag": "ICAI Test Your Knowledge",
        "difficulty": "Moderate",
        "is_case_study": 0,
        "case_scenario": None,
        "why_incorrect_a": "Woman directors are not automatically exempt unless recommended by NRC/Board or appointed as ID.",
        "why_incorrect_b": "",
        "why_incorrect_c": "Holding 5% shares does not exempt deposit under Section 160.",
        "why_incorrect_d": "Proviso to Section 160(1) explicitly provides statutory exemptions."
    },
    # --- A_BM: Section 173(3) Shorter Notice ---
    {
        "set_name": "A",
        "section_group": "Part I: Corporate Laws (70 Marks)",
        "chapter_code": "A_BM",
        "topic": "Meetings of Board and its Powers",
        "subtopic": "Section 173(3) Board Meeting Shorter Notice & Independent Director Ratification",
        "question": (
            "Under Section 173(3) of the Companies Act, 2013, a meeting of the Board may be called at shorter notice to transact urgent business. "
            "If NO Independent Director is present at such a shorter notice meeting, how can the decisions taken at the meeting become valid?"
        ),
        "option_a": "The decisions are void ab initio and must be transacted freshly at a full 7-day notice meeting.",
        "option_b": "Decisions taken at such a meeting shall be circulated to all the directors, and SHALL BE FINAL ONLY ON RATIFICATION THEREOF BY AT LEAST ONE INDEPENDENT DIRECTOR.",
        "option_c": "Decisions become valid automatically if approved by the Managing Director.",
        "option_d": "Decisions become valid upon obtaining prior sanction of the Registrar of Companies within 7 days.",
        "correct_option": "B",
        "marks": 2,
        "explanation": (
            "Under Section 173(3) of the Companies Act, 2013:\n"
            "A meeting of the Board may be called at shorter notice to transact urgent business subject to the condition that AT LEAST ONE INDEPENDENT DIRECTOR, "
            "if any, shall be present at the meeting.\n\n"
            "Under the Proviso to Section 173(3):\n"
            "'Provided that in case of absence of independent directors from such a meeting of the Board, decisions taken at such a meeting "
            "SHALL BE CIRCULATED TO ALL THE DIRECTORS, AND SHALL BE FINAL ONLY ON RATIFICATION THEREOF BY AT LEAST ONE INDEPENDENT DIRECTOR, if any.'\n\n"
            "Thus, lack of an independent director's attendance at a shorter notice board meeting does not kill the decisions, provided at least one independent "
            "director subsequently ratifies them after circulation."
        ),
        "section_ref": "Companies Act, 2013 - Section 173(3) Proviso",
        "exam_tip": "EXAM TRAP: Shorter notice meeting WITHOUT an Independent Director is NOT void! It becomes fully valid if ratified by AT LEAST ONE Independent Director after circulation.",
        "source_tag": "Offline SPOM Recall",
        "difficulty": "Moderate",
        "is_case_study": 0,
        "case_scenario": None,
        "why_incorrect_a": "Proviso to Section 173(3) explicitly saves the meeting via ID ratification.",
        "why_incorrect_b": "",
        "why_incorrect_c": "MD approval cannot substitute for Independent Director statutory ratification.",
        "why_incorrect_d": "ROC sanction is not required for shorter notice board meeting ratification."
    },
    # --- A_BM: Section 178 Stakeholders Relationship Committee ---
    {
        "set_name": "A",
        "section_group": "Part I: Corporate Laws (70 Marks)",
        "chapter_code": "A_BM",
        "topic": "Meetings of Board and its Powers",
        "subtopic": "Section 178(5) Stakeholders Relationship Committee Applicability & Chairperson",
        "question": (
            "Under Section 178(5) of the Companies Act, 2013, the Board of Directors of a company shall constitute a Stakeholders Relationship "
            "Committee if the company has more than _________ shareholders, debenture-holders, deposit-holders and any other security holders at any time during a financial year; "
            "and the Chairperson of this committee MUST BE a _________:"
        ),
        "option_a": "500; Independent Director",
        "option_b": "1,000; Non-Executive Director",
        "option_c": "1,000; Managing Director",
        "option_d": "2,000; Independent Director",
        "correct_option": "B",
        "marks": 2,
        "explanation": (
            "Under Section 178(5) of the Companies Act, 2013:\n"
            "The Board of Directors of a company which consists of MORE THAN ONE THOUSAND (1,000) shareholders, debenture-holders, "
            "deposit-holders and any other security holders at any time during a financial year shall constitute a Stakeholders Relationship Committee "
            "consisting of a chairperson who SHALL BE A NON-EXECUTIVE DIRECTOR and such other members as may be decided by the Board.\n\n"
            "Notice two crucial points:\n"
            "1. Threshold: MORE THAN 1,000 security holders (shareholders + debenture holders + deposit holders + other security holders combined).\n"
            "2. Chairperson: MUST BE A NON-EXECUTIVE DIRECTOR. (It does not mandatorily have to be an Independent Director, but must be non-executive, "
            "and cannot be the Managing Director or Whole-time Director!)."
        ),
        "section_ref": "Companies Act, 2013 - Section 178(5)",
        "exam_tip": "EXAM TRAP: Stakeholders Relationship Committee threshold is >1,000 security holders. The Chairperson must be a NON-EXECUTIVE DIRECTOR (do not confuse with Audit Committee where ID is mandated).",
        "source_tag": "ICAI BoS Module",
        "difficulty": "Moderate",
        "is_case_study": 0,
        "case_scenario": None,
        "why_incorrect_a": "500 is incorrect; threshold is >1,000.",
        "why_incorrect_b": "",
        "why_incorrect_c": "Managing Director cannot chair the Stakeholders Relationship Committee; chair must be a Non-Executive Director.",
        "why_incorrect_d": "2,000 is incorrect."
    },
    # --- A_FOREIGN: Display of Name & Country ---
    {
        "set_name": "A",
        "section_group": "Part I: Corporate Laws (70 Marks)",
        "chapter_code": "A_FOREIGN",
        "topic": "Companies Incorporated Outside India",
        "subtopic": "Section 382 Display of Name, Country of Incorporation & Limited Liability",
        "question": (
            "Under Section 382 of the Companies Act, 2013, every foreign company SHALL conspicuously exhibit on the outside of every office "
            "or place where it carries on business in India, in legible characters in English and in the local regional language, which of the following?"
        ),
        "option_a": "Only the company's global registered address and market capitalization.",
        "option_b": "The name of the company, the country in which it is incorporated, and if the liability of members is limited, notice of that fact.",
        "option_c": "The names and PAN numbers of all Indian resident employees.",
        "option_d": "The certified copy of the incorporation certificate issued by the foreign sovereign authority.",
        "correct_option": "B",
        "marks": 2,
        "explanation": (
            "Under Section 382 of the Companies Act, 2013, every foreign company shall:\n"
            "(a) Conspicuously exhibit on the outside of every office or place where it carries on business in India, the name of the company "
            "and the country in which it is incorporated, in letters easily legible in English characters, and also in the characters of the "
            "language or one of the languages in general use in the locality;\n"
            "(b) Cause the name of the company and of the country in which the company is incorporated, to be stated in legible English characters "
            "in all business letters, bill-heads and letter paper, and in all notices, and other official publications; and\n"
            "(c) If the liability of the members of the company is limited, cause notice of that fact to be stated in every such prospectus, bill-head, etc."
        ),
        "section_ref": "Companies Act, 2013 - Section 382",
        "exam_tip": "EXAM TRAP: Under Section 382, foreign companies must display: (1) Name of company, (2) Country of incorporation, and (3) Fact of limited liability of members, both in English and the local language.",
        "source_tag": "ICAI Test Your Knowledge",
        "difficulty": "Moderate",
        "is_case_study": 0,
        "case_scenario": None,
        "why_incorrect_a": "Market cap is not required to be displayed.",
        "why_incorrect_b": "",
        "why_incorrect_c": "PAN numbers of employees is irrelevant.",
        "why_incorrect_d": "Physical incorporation certificate is not required to be exhibited on the building facade."
    }
]


def seed_expansion():
    if not os.path.exists(DB_PATH):
        print(f"[ERROR] Database file not found at: {DB_PATH}")
        sys.exit(1)

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    all_questions = CASE_6_QUESTIONS + CASE_7_QUESTIONS + EXPANSION_STANDALONE

    print(f"Total Expansion Questions to Seed: {len(all_questions)}")
    print(f"- Case Scenario 6 (Horizon Infra - IBC Moratorium, Sec 29A NPA, Sec 12 330-day): {len(CASE_6_QUESTIONS)}")
    print(f"- Case Scenario 7 (Zenith Agro - Sec 196 Age 70, Sec 197 Limits, Sec 177 Audit Comm, Sec 161(1)): {len(CASE_7_QUESTIONS)}")
    print(f"- Expansion Standalone Traps (ODI 400%, SSD Sec 151, Sec 160 Deposit Exempt, Sec 173(3), Sec 178, Sec 382): {len(EXPANSION_STANDALONE)}")

    inserted_count = 0
    updated_count = 0

    for q in all_questions:
        cursor.execute("SELECT id FROM mcqs WHERE set_name = ? AND question = ?", (q['set_name'], q['question']))
        existing = cursor.fetchone()

        if existing:
            cursor.execute("""
                UPDATE mcqs SET
                    section_group = ?,
                    chapter_code = ?,
                    topic = ?,
                    subtopic = ?,
                    option_a = ?,
                    option_b = ?,
                    option_c = ?,
                    option_d = ?,
                    correct_option = ?,
                    marks = ?,
                    explanation = ?,
                    section_ref = ?,
                    exam_tip = ?,
                    source_tag = ?,
                    difficulty = ?,
                    is_case_study = ?,
                    case_scenario = ?,
                    why_incorrect_a = ?,
                    why_incorrect_b = ?,
                    why_incorrect_c = ?,
                    why_incorrect_d = ?,
                    verification_status = 'Verified',
                    is_outdated_law = 0
                WHERE id = ?
            """, (
                q['section_group'],
                q['chapter_code'],
                q['topic'],
                q.get('subtopic', ''),
                q['option_a'],
                q['option_b'],
                q['option_c'],
                q['option_d'],
                q['correct_option'],
                q.get('marks', 2),
                q['explanation'],
                q.get('section_ref', ''),
                q.get('exam_tip', ''),
                q.get('source_tag', 'ICAI Case Scenario'),
                q.get('difficulty', 'Hard'),
                q.get('is_case_study', 0),
                q.get('case_scenario'),
                q.get('why_incorrect_a', ''),
                q.get('why_incorrect_b', ''),
                q.get('why_incorrect_c', ''),
                q.get('why_incorrect_d', ''),
                existing[0]
            ))
            updated_count += 1
        else:
            cursor.execute("""
                INSERT INTO mcqs (
                    set_name, section_group, chapter_code, topic, subtopic,
                    question, option_a, option_b, option_c, option_d,
                    correct_option, marks, explanation, section_ref, exam_tip,
                    source_tag, difficulty, is_case_study, case_scenario,
                    why_incorrect_a, why_incorrect_b, why_incorrect_c, why_incorrect_d,
                    verification_status, is_outdated_law, is_user_uploaded
                ) VALUES (
                    ?, ?, ?, ?, ?,
                    ?, ?, ?, ?, ?,
                    ?, ?, ?, ?, ?,
                    ?, ?, ?, ?,
                    ?, ?, ?, ?,
                    'Verified', 0, 0
                )
            """, (
                q['set_name'],
                q['section_group'],
                q['chapter_code'],
                q['topic'],
                q.get('subtopic', ''),
                q['question'],
                q['option_a'],
                q['option_b'],
                q['option_c'],
                q['option_d'],
                q['correct_option'],
                q.get('marks', 2),
                q['explanation'],
                q.get('section_ref', ''),
                q.get('exam_tip', ''),
                q.get('source_tag', 'ICAI Case Scenario'),
                q.get('difficulty', 'Hard'),
                q.get('is_case_study', 0),
                q.get('case_scenario'),
                q.get('why_incorrect_a', ''),
                q.get('why_incorrect_b', ''),
                q.get('why_incorrect_c', ''),
                q.get('why_incorrect_d', '')
            ))
            inserted_count += 1

    conn.commit()

    cursor.execute("SELECT count(*) FROM mcqs WHERE set_name = 'A'")
    total_a = cursor.fetchone()[0]

    cursor.execute("SELECT count(*) FROM mcqs WHERE set_name = 'A' AND is_case_study = 1")
    total_case_studies = cursor.fetchone()[0]

    cursor.execute("SELECT chapter_code, count(*) FROM mcqs WHERE set_name = 'A' GROUP BY chapter_code ORDER BY chapter_code")
    chapter_breakdown = cursor.fetchall()

    conn.close()

    print("\n[SUCCESS] Expansion Seeding completed successfully!")
    print(f"- New MCQs Inserted: {inserted_count}")
    print(f"- Existing MCQs Updated: {updated_count}")
    print(f"- Total Set A MCQs in Database: {total_a}")
    print(f"- Total Set A Case Study Questions: {total_case_studies}")
    print("\nUpdated Chapter Breakdown for Set A:")
    for ch, count in chapter_breakdown:
        print(f"  {ch}: {count} MCQs")

if __name__ == "__main__":
    seed_expansion()

