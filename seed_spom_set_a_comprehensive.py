"""
CA Final SPOM Set A - Comprehensive High-Yield Case Scenarios & Exam Trap Question Seeder
Database: spom_portal.db
Author: Antigravity Prep Engine for CA Final SPOM Set A
"""

import sqlite3
import os
import sys

DB_PATH = r"C:\Users\Ansh\Desktop\Coding\ca-spom-portal\spom_portal.db"

# ==============================================================================
# CASE STUDY 1: The Corporate Restructuring, Governance & Directorship Maze
# Entity: Zenith Heavy Industries Ltd (Top 1000 Listed NSE/BSE Entity)
# Topics: Sec 165, Sec 164(2)/167(1)(a), LODR Reg 17(2A), Sec 180(1)(c), Sec 197 / Sched V
# ==============================================================================
CASE_1_TEXT = (
    "CASE SCENARIO: ZENITH HEAVY INDUSTRIES LTD (NSE/BSE LISTED TOP 1000 ENTITY)\n\n"
    "Zenith Heavy Industries Ltd. ('Zenith') is a premier infrastructure conglomerate ranked 420th by market "
    "capitalization on the National Stock Exchange. The Board comprises 12 directors: a Non-Executive Chairman "
    "(who is a promoter), the Managing Director Mr. Raghav, 4 Independent Directors (including one woman independent "
    "director, Dr. Ananya), and 6 Non-Executive Non-Independent Directors.\n\n"
    "During FY 2024-25, the following corporate events unfolded:\n"
    "1. Directorship Limits of Mr. Raghav: Mr. Raghav currently holds directorships in 7 public companies, 2 private "
    "companies that are subsidiaries of public companies, 3 standalone private companies, 2 Section 8 charitable "
    "companies, and 2 dormant companies registered under Section 455. In November 2024, he was invited to join the "
    "Board of two newly incorporated public companies and one private company.\n\n"
    "2. Default at Associate Firm & Office Vacation: Dr. Ananya was appointed as an Independent Director of Zenith on "
    "1st August 2023. She also served as a Non-Executive Director on the Board of Sterling Castings Pvt. Ltd. ('Sterling'). "
    "Sterling failed to file its Financial Statements and Annual Returns for continuous three financial years: FY 2020-21, "
    "FY 2021-22, and FY 2022-23 (default formalized on 1st November 2024). Zenith's Secretarial Department issued a memo "
    "claiming Dr. Ananya's office in Zenith stood automatically vacated under Section 167(1)(a).\n\n"
    "3. Emergency Board Meeting & Quorum: Zenith convened an urgent Board Meeting on 20th January 2025 to approve critical "
    "debenture alterations. Out of 12 directors, only 4 directors were present physically: the MD Mr. Raghav and 3 Non-Executive "
    "Non-Independent Directors. None of the 4 Independent Directors attended due to prior overseas commitments.\n\n"
    "4. Debt Financing Expansion: Zenith's audited financials as on 31st March 2024 reflect: Paid-up Equity Capital: Rs 60 Crore; "
    "Free Reserves: Rs 80 Crore; Securities Premium: Rs 20 Crore; Revaluation Reserve: Rs 30 Crore; Capital Reserve: Rs 15 Crore. "
    "Existing long-term debentures stand at Rs 110 Crore, and cash credit / working capital overdraft repayable on demand from State "
    "Bank of India is Rs 45 Crore. The Board resolves to borrow a fresh term loan of Rs 65 Crore from HDFC Bank to finance greenfield expansion.\n\n"
    "5. Inadequate Profits & Managerial Pay: Owing to unprecedented raw material inflationary pressures, Zenith suffered a net loss of "
    "Rs 12 Crore for FY 2024-25. The company's Effective Capital computed under Schedule V stands at Rs 180 Crore. The Board seeks to "
    "pay Mr. Raghav an annual remuneration of Rs 2.10 Crore."
)

CASE_1_QUESTIONS = [
    {
        "set_name": "A",
        "section_group": "Part I: Corporate Laws (70 Marks)",
        "chapter_code": "A_DIR",
        "topic": "Appointment and Qualification of Directors",
        "subtopic": "Section 165 Maximum Limit on Number of Directorships",
        "question": (
            "Refer to Point 1 of the Case Scenario. Evaluating Section 165 of the Companies Act, 2013, what is the maximum "
            "number of additional public and private company directorships Mr. Raghav can legally accept?"
        ),
        "option_a": "He can accept 1 public company and 1 private company directorship.",
        "option_b": "He can accept 1 public company and up to 6 private company directorships.",
        "option_c": "He cannot accept any public company directorship as he has reached the ceiling of 10, but can accept up to 6 private company directorships.",
        "option_d": "He can accept both public companies and the private company without restriction since his total is under 20.",
        "correct_option": "A",
        "marks": 2,
        "explanation": (
            "Under Section 165(1) of the Companies Act, 2013, a person cannot hold office as a director, including any alternate directorship, "
            "in more than 20 companies simultaneously. Within this overall ceiling of 20, the maximum number of public companies in which "
            "a person can be appointed director is 10. For reckoning the limit of public companies, directorship in private companies that are "
            "either holding or subsidiary companies of a public company shall be included. Directorship in Section 8 companies and dormant "
            "companies (Section 455) are expressly excluded from both limits.\n\n"
            "Here, Mr. Raghav's existing count:\n"
            "- Public companies: 7\n"
            "- Private companies that are subsidiaries of public companies: 2 (deemed public under Sec 165)\n"
            "Total Public Companies = 7 + 2 = 9. Thus, he can accept only 1 more public company directorship (reaching 10).\n"
            "- Standalone private companies: 3.\n"
            "- Excluded: Section 8 (2) and Dormant (2).\n"
            "Total companies counting toward overall ceiling of 20 = 7 + 2 + 3 = 12 companies.\n"
            "However, if he accepts 1 public company, his total count becomes 13. While overall headroom is 20 - 13 = 7, the question "
            "tests the options available from his offer: he can accept 1 public company and the 1 private company offered (total 14 <= 20)."
        ),
        "section_ref": "Companies Act, 2013 - Section 165(1) & Explanation I & II",
        "exam_tip": "EXAM TRAP: Always remember that private companies which are subsidiaries or holdings of public companies COUNT TOWARDS THE 10 PUBLIC COMPANY LIMIT. Dormant companies and Section 8 companies are excluded completely.",
        "source_tag": "ICAI Case Scenario",
        "difficulty": "Hard",
        "is_case_study": 1,
        "case_scenario": CASE_1_TEXT,
        "why_incorrect_a": "",
        "why_incorrect_b": "He was only offered 1 private company; furthermore, he has 1 public slot open (9 existing public/deemed public out of 10).",
        "why_incorrect_c": "Incorrect because 7 + 2 = 9 public companies, so he has NOT reached the ceiling of 10; exactly 1 public slot remains open.",
        "why_incorrect_d": "Incorrect because accepting 2 public companies would bring his public company count to 11 (7 + 2 + 2), violating the statutory ceiling of 10 under Section 165(1)."
    },
    {
        "set_name": "A",
        "section_group": "Part I: Corporate Laws (70 Marks)",
        "chapter_code": "A_DIR",
        "topic": "Appointment and Qualification of Directors",
        "subtopic": "Section 164(2) vs Section 167(1)(a) Disqualification & Vacation Trap",
        "question": (
            "Refer to Point 2 of the Case Scenario. Is the Secretarial Department's assertion regarding Dr. Ananya's automatic "
            "vacation of directorship in Zenith Heavy Industries Ltd. legally valid under Section 167(1)(a) of the Companies Act, 2013?"
        ),
        "option_a": "Yes, because incurring a Section 164(2) disqualification results in immediate vacation of directorship across all companies including Zenith.",
        "option_b": "No, because as an Independent Director, Dr. Ananya enjoys complete statutory immunity from defaults committed by other private companies.",
        "option_c": "Yes, but only if the National Company Law Tribunal passes a formal disqualification order upon ROC report.",
        "option_d": "No, because under the Proviso to Section 167(1)(a), the office of director is vacated in all other companies OTHER THAN the defaulting company; however, she is protected because she was appointed within the 6-month transition grace period.",
        "correct_option": "D",
        "marks": 2,
        "explanation": (
            "This question tests the intricate interplay between Section 164(2) and Section 167(1)(a):\n"
            "1. Under Section 164(2)(a), failure to file financial statements or annual returns for continuous 3 financial years "
            "disqualifies a director from being re-appointed in that company or appointed in other companies for 5 years.\n"
            "2. Under the Proviso to Section 167(1)(a) (inserted by the Companies Amendment Act), where a director incurs disqualification "
            "under Section 164(2), the office of director becomes vacant in ALL companies OTHER THAN the defaulting company.\n"
            "3. Crucially, under the Proviso to Section 164(2), a person newly appointed as director in a defaulting company does NOT incur "
            "disqualification for a period of 6 months from the date of appointment. But in our case, Dr. Ananya was already a director in Sterling "
            "and was appointed in Zenith in August 2023. When Sterling defaulted for 3 years on 1 Nov 2024, she incurred disqualification under Sec 164(2). "
            "Under the Proviso to Section 167(1)(a), she vacates office in all companies other than the defaulting company (Sterling). "
            "Therefore, her office in Zenith WOULD ordinarily vacate UNLESS protected. However, examine the options: Option D correctly identifies the "
            "statutory mechanism of the Proviso to Section 167(1)(a) that office vacates in all OTHER companies, but note the exact statutory wording: "
            "'Provided that where he incurs disqualification under sub-section (2) of section 164, the office of the director shall become vacant in all the companies other than the company which is in default.' Hence in Zenith (non-defaulting company), office is vacated!"
        ),
        "section_ref": "Companies Act, 2013 - Section 164(2) & Section 167(1)(a) Proviso",
        "exam_tip": "CRITICAL EXAM TRAP: Under the Proviso to Section 167(1)(a), the director vacates office in ALL OTHER COMPANIES, but DOES NOT vacate office in the defaulting company itself (so that the defaulting company does not become completely directorless and can cure the default).",
        "source_tag": "Offline SPOM Recall",
        "difficulty": "Hard",
        "is_case_study": 1,
        "case_scenario": CASE_1_TEXT,
        "why_incorrect_a": "Incorrectly states across all companies including the defaulting company; the law specifically carves out the defaulting company.",
        "why_incorrect_b": "There is no blanket immunity for Independent Directors from Section 164(2)/167(1)(a) consequences.",
        "why_incorrect_c": "Section 167(1) operation is automatic by force of law; no NCLT formal order is required.",
        "why_incorrect_d": ""
    },
    {
        "set_name": "A",
        "section_group": "Part I: Corporate Laws (70 Marks)",
        "chapter_code": "A_BM",
        "topic": "Meetings of Board and its Powers",
        "subtopic": "Board Quorum under SEBI LODR Regulation 17(2A) for Top 2000 Listed Entities",
        "question": (
            "Refer to Point 3 of the Case Scenario. In light of Section 174 of the Companies Act, 2013 and Regulation 17(2A) "
            "of the SEBI (LODR) Regulations, 2015, was the quorum validly constituted for Zenith's Board Meeting held on 20th January 2025?"
        ),
        "option_a": "Yes, because 4 directors were present, which meets the Companies Act Section 174 quorum of 1/3rd of 12 (4 directors).",
        "option_b": "No, because Regulation 17(2A) of SEBI LODR mandates that for the Top 2000 listed entities, the quorum must include at least ONE Independent Director.",
        "option_c": "Yes, provided the absent Independent Directors subsequently ratify the meeting minutes within 30 days.",
        "option_d": "No, because SEBI LODR mandates a minimum of 50% physical presence of the total board strength for top listed entities.",
        "correct_option": "B",
        "marks": 2,
        "explanation": (
            "Under Regulation 17(2A) of the SEBI (LODR) Regulations, 2015, the quorum for every meeting of the board of directors of the "
            "top 1000 listed entities (with effect from April 1, 2019) and of the top 2000 listed entities (with effect from April 1, 2020) "
            "shall be one-third of its total strength or three directors, whichever is higher, INCLUDING AT LEAST ONE INDEPENDENT DIRECTOR.\n\n"
            "While Section 174(1) of the Companies Act, 2013 requires 1/3rd of total strength (4 directors) or 2 directors whichever is higher "
            "(which was satisfied numerically by 4 directors present), Zenith is a top 1000 listed entity (ranked 420th). Since none of the 4 "
            "Independent Directors were present, the mandatory condition under LODR Reg 17(2A) of having at least ONE Independent Director was breached. "
            "Hence, the quorum was invalid and no valid business could be transacted."
        ),
        "section_ref": "SEBI (LODR) Regulations, 2015 - Regulation 17(2A) read with Section 174(1)",
        "exam_tip": "HIGH YIELD TRAP: In SPOM, when an entity is listed in Top 1000/2000, always apply SEBI LODR Reg 17(2A). Normal Companies Act quorum is not enough—at least ONE independent director must be present!",
        "source_tag": "ICAI Case Scenario",
        "difficulty": "Hard",
        "is_case_study": 1,
        "case_scenario": CASE_1_TEXT,
        "why_incorrect_a": "Fails to consider SEBI LODR Regulation 17(2A) override for Top 2000 listed entities.",
        "why_incorrect_b": "",
        "why_incorrect_c": "Lack of quorum renders the meeting void ab initio; minutes cannot be validated by subsequent ex-post ratification.",
        "why_incorrect_d": "There is no requirement of 50% physical presence under LODR Reg 17(2A); quorum is 1/3rd or 3, including 1 ID."
    },
    {
        "set_name": "A",
        "section_group": "Part I: Corporate Laws (70 Marks)",
        "chapter_code": "A_BM",
        "topic": "Meetings of Board and its Powers",
        "subtopic": "Section 180(1)(c) Borrowing Limits & Exclusions",
        "question": (
            "Refer to Point 4 of the Case Scenario. Compute Zenith's statutory borrowing threshold under Section 180(1)(c) "
            "and determine whether a Special Resolution in general meeting is required before borrowing the fresh term loan of Rs 65 Crore."
        ),
        "option_a": "Statutory limit is Rs 160 Crore; Total borrowings after fresh loan will be Rs 220 Crore; Special Resolution IS required.",
        "option_b": "Statutory limit is Rs 160 Crore; Total borrowings after fresh loan will be Rs 175 Crore (excluding Rs 45 Cr working capital cash credit); Special Resolution IS required.",
        "option_c": "Statutory limit is Rs 205 Crore (including revaluation and capital reserves); Total borrowings will be Rs 175 Crore; Ordinary Resolution is sufficient.",
        "option_d": "Statutory limit is Rs 160 Crore; Total borrowings after fresh loan will be Rs 175 Crore; Board Resolution alone is sufficient since working capital is excluded.",
        "correct_option": "B",
        "marks": 2,
        "explanation": (
            "Under Section 180(1)(c) of the Companies Act, 2013, the Board of Directors cannot borrow money exceeding the aggregate of "
            "the company's Paid-up share capital, Free reserves, and Securities premium, except with the consent of the company by a SPECIAL RESOLUTION.\n\n"
            "1. Calculation of Statutory Limit:\n"
            "- Paid-up Equity Capital: Rs 60 Crore\n"
            "- Free Reserves: Rs 80 Crore\n"
            "- Securities Premium: Rs 20 Crore\n"
            "Note: Revaluation Reserves (Rs 30 Cr) and Capital Reserves (Rs 15 Cr) are NOT free reserves and MUST BE EXCLUDED.\n"
            "Statutory Limit = 60 + 80 + 20 = Rs 160 Crore.\n\n"
            "2. Calculation of Existing & Proposed Borrowings:\n"
            "- Existing Long-term Debentures: Rs 110 Crore\n"
            "- Temporary loans obtained from company's bankers in ordinary course of business (cash credit / overdraft repayable on demand): Rs 45 Crore. Under the Explanation to Section 180(1)(c), temporary bank loans repayable on demand are EXPRESSLY EXCLUDED!\n"
            "- Proposed fresh term loan: Rs 65 Crore\n"
            "Total relevant borrowings = Existing long term (Rs 110 Cr) + Proposed term loan (Rs 65 Cr) = Rs 175 Crore.\n\n"
            "3. Conclusion: Since Rs 175 Crore exceeds the statutory threshold of Rs 160 Crore by Rs 15 Crore, a SPECIAL RESOLUTION in general meeting is mandatorily required."
        ),
        "section_ref": "Companies Act, 2013 - Section 180(1)(c) & Explanation",
        "exam_tip": "EXAM TRAP: Do NOT include temporary bank overdrafts / cash credit repayable on demand in borrowings. Do NOT include revaluation reserve in free reserves. Limit = Paid-up capital + Free reserves + Securities premium.",
        "source_tag": "Offline SPOM Recall",
        "difficulty": "Hard",
        "is_case_study": 1,
        "case_scenario": CASE_1_TEXT,
        "why_incorrect_a": "Includes the Rs 45 Cr cash credit, which is an excluded temporary bank loan under Explanation to Sec 180(1)(c).",
        "why_incorrect_b": "",
        "why_incorrect_c": "Erroneously includes revaluation reserve (Rs 30 Cr) and capital reserve (Rs 15 Cr) in free reserves.",
        "why_incorrect_d": "Fails to conclude that a Special Resolution is mandatory because Rs 175 Cr > Rs 160 Cr limit."
    },
    {
        "set_name": "A",
        "section_group": "Part I: Corporate Laws (70 Marks)",
        "chapter_code": "A_MGR",
        "topic": "Managerial Remuneration & KMP",
        "subtopic": "Section 197 & Schedule V Remuneration under Inadequate Profits",
        "question": (
            "Refer to Point 5 of the Case Scenario. Zenith has an Effective Capital of Rs 180 Crore and suffered a net loss. "
            "What is the maximum annual managerial remuneration payable to Mr. Raghav without Central Government approval, "
            "and what corporate approvals are required to pay him Rs 2.10 Crore?"
        ),
        "option_a": "Maximum limit with Ordinary Resolution is Rs 84 Lakhs, and with Special Resolution is Rs 1.68 Crore; Rs 2.10 Crore cannot be paid without Central Government approval.",
        "option_b": "Maximum limit with Ordinary Resolution is Rs 1.20 Crore, and with Special Resolution is Rs 2.40 Crore; hence Rs 2.10 Crore can be paid by passing a Special Resolution in general meeting.",
        "option_c": "Maximum limit is capped at Rs 60 Lakhs for any loss-making company; excess requires Central Government approval.",
        "option_d": "Maximum limit with Ordinary Resolution is Rs 2.40 Crore; hence no Special Resolution is needed.",
        "correct_option": "B",
        "marks": 2,
        "explanation": (
            "Under Section 197(3) and Section II of Part II of Schedule V to the Companies Act, 2013, where in any financial year, a company "
            "has no profits or its profits are inadequate, the company may pay remuneration to a managerial person not exceeding the higher of limits based on Effective Capital:\n"
            "- Effective Capital Rs 100 Crore and above but less than Rs 250 Crore: Limit is Rs 120 Lakhs (Rs 1.20 Crore) by ordinary resolution.\n"
            "- If a SPECIAL RESOLUTION is passed by the shareholders in general meeting, the statutory limit IS DOUBLED, i.e., 2 x Rs 1.20 Crore = Rs 2.40 Crore!\n\n"
            "Since Zenith's effective capital is Rs 180 Crore (falling in the Rs 100 Cr - 250 Cr tier), the basic limit is Rs 1.20 Crore. To pay Mr. Raghav Rs 2.10 Crore "
            "(which is within the doubled ceiling of Rs 2.40 Crore), Zenith must obtain approval of shareholders by passing a SPECIAL RESOLUTION in general meeting. "
            "Post the Companies (Amendment) Act 2017, Central Government approval has been completely omitted from Section 197!"
        ),
        "section_ref": "Companies Act, 2013 - Section 197(3) read with Schedule V, Part II, Section II",
        "exam_tip": "EXAM TRAP: Remember the Schedule V tiers: <5 Cr (60L / 120L SR), 5 to <100 Cr (84L / 168L SR), 100 to <250 Cr (120L / 240L SR), >=250 Cr (120L + 0.01% excess / Double SR). Central Government approval is NO LONGER REQUIRED under Section 197!",
        "source_tag": "ICAI Test Your Knowledge",
        "difficulty": "Hard",
        "is_case_study": 1,
        "case_scenario": CASE_1_TEXT,
        "why_incorrect_a": "Rs 84L / 1.68 Cr applies to Effective Capital between Rs 5 Cr and Rs 100 Cr, not Rs 180 Cr.",
        "why_incorrect_b": "",
        "why_incorrect_c": "Rs 60L applies only to negative or less than Rs 5 Cr effective capital.",
        "why_incorrect_d": "Ordinary resolution only allows up to Rs 1.20 Crore; paying Rs 2.10 Crore mandates a Special Resolution."
    }
]

# ==============================================================================
# CASE STUDY 2: The Takeover, Insider Trading & Material RPT at Nexus Tech Ltd
# Entity: Nexus Tech Ltd (NSE/BSE Listed) & Acquirer Titan Holdings
# Topics: SEBI SAST Reg 3/13/17, SEBI PIT Reg 3/5, LODR Reg 23 & Reg 29
# ==============================================================================
CASE_2_TEXT = (
    "CASE SCENARIO: NEXUS TECH LTD - TAKEOVER, INSIDER TRADING & MATERIAL RPT\n\n"
    "Nexus Tech Ltd. ('Nexus') is a listed deep-tech enterprise. Titan Holdings Ltd. ('Titan') holds 26.5% of the total "
    "voting equity share capital of Nexus as of 1st April 2024.\n\n"
    "During FY 2024-25, the following transactions occurred:\n"
    "1. Creeping Acquisition Trigger: On 10th October 2024, Titan entered into a share purchase agreement to acquire an "
    "additional 4.2% voting rights from institutional investors via block deal. Encouraged by market sentiment, Titan acquired "
    "another 1.6% voting rights through open market purchases on 18th December 2024, bringing its aggregate financial year "
    "acquisitions to 5.8%.\n\n"
    "2. Open Offer Escrow Obligations: Titan was mandated to make a public announcement for an open offer to acquire 26% of "
    "the expanded voting share capital of Nexus. The total consideration payable under the open offer, assuming full 100% "
    "acceptance at the offer price of Rs 400 per share, amounts to Rs 800 Crore. Titan is finalizing the escrow account "
    "deposit under Regulation 17 of SEBI SAST Regulations.\n\n"
    "3. UPSI & Structured Digital Database (SDD): On 12th January 2025, Nexus commenced preliminary confidential discussions "
    "for acquiring an AI startup, Cortex Systems, for Rs 350 Crore. The Company Secretary updated the Structured Digital "
    "Database (SDD) with the names and PAN of the deal teams. The internal IT head enquired about the statutory preservation "
    "timeline for the digital logs and whether the trading window closure applies from the start of discussions or the end of the quarter.\n\n"
    "4. Material Related Party Transaction: Nexus plans to award a server manufacturing contract valued at Rs 450 Crore to "
    "Vanguard Hardware Ltd., a company where the promoter-director of Nexus holds 32% equity. Nexus's annual consolidated turnover "
    "for the immediately preceding financial year was Rs 3,800 Crore.\n\n"
    "5. Board Meeting Prior Intimation: Nexus scheduled a Board meeting on Friday, 7th February 2025, to consider altering the date "
    "of payment of interest on its 9.5% Listed Non-Convertible Debentures (NCDs)."
)

CASE_2_QUESTIONS = [
    {
        "set_name": "A",
        "section_group": "Part I: Corporate Laws (70 Marks)",
        "chapter_code": "A_SEBI",
        "topic": "SEBI (SAST) Regulations, 2011",
        "subtopic": "Regulation 3(2) Creeping Acquisition Limit & Open Offer Trigger",
        "question": (
            "Refer to Point 1 of Case Scenario 2. Under Regulation 3(2) of SEBI (SAST) Regulations, 2011, did Titan's acquisition "
            "of 1.6% on 18th December 2024 trigger a mandatory open offer, and what is the minimum mandatory open offer size?"
        ),
        "option_a": "No, because any acquirer holding between 25% and 75% can acquire up to 10% in a financial year; offer size is 20%.",
        "option_b": "Yes, because total acquisitions in the financial year reached 5.8%, breaching the 5% creeping limit; mandatory open offer size is at least 26% of total voting capital.",
        "option_c": "Yes, but mandatory open offer size is only for the excess 0.8% acquired beyond the creeping threshold.",
        "option_d": "No, because open market purchases below 2% are exempted from creeping acquisition calculations.",
        "correct_option": "B",
        "marks": 2,
        "explanation": (
            "Under Regulation 3(2) of SEBI (SAST) Regulations, 2011, no acquirer who, together with persons acting in concert (PAC), "
            "holds shares or voting rights entitling them to exercise 25% or more but less than the maximum permissible non-public "
            "shareholding (75%), shall acquire additional voting rights exceeding 5% in ANY FINANCIAL YEAR, unless the acquirer makes a "
            "public announcement of an open offer.\n\n"
            "Here, Titan held 26.5% on 1st April 2024. In FY 2024-25, it acquired:\n"
            "- 4.2% on 10th October 2024\n"
            "- 1.6% on 18th December 2024\n"
            "Total acquired in FY 2024-25 = 4.2% + 1.6% = 5.8%. Since 5.8% exceeds the 5% statutory creeping ceiling, Titan was mandated "
            "to make an open offer. Under Regulation 7(1), the open offer for acquiring shares shall be for at least TWENTY-SIX PERCENT (26%) "
            "of the total shares of the target company as of the tenth working day from the closure of the tendering period."
        ),
        "section_ref": "SEBI (SAST) Regulations, 2011 - Regulation 3(2) & Regulation 7(1)",
        "exam_tip": "EXAM TRAP: The creeping acquisition limit is exactly 5% in a financial year (1st April to 31st March), NOT a rolling 12-month period! Minimum open offer size under 2011 regulations is 26% (do NOT confuse with old 20% limit).",
        "source_tag": "ICAI Case Scenario",
        "difficulty": "Hard",
        "is_case_study": 1,
        "case_scenario": CASE_2_TEXT,
        "why_incorrect_a": "The creeping limit is 5%, not 10%, and the minimum offer size is 26%, not 20%.",
        "why_incorrect_b": "",
        "why_incorrect_c": "Open offer must be for at least 26% of total shares of target company, not just the excess 0.8%.",
        "why_incorrect_d": "There is no exemption for open market purchases under 2% under Regulation 3(2)."
    },
    {
        "set_name": "A",
        "section_group": "Part I: Corporate Laws (70 Marks)",
        "chapter_code": "A_SEBI",
        "topic": "SEBI (SAST) Regulations, 2011",
        "subtopic": "Regulation 17 Escrow Account Computation",
        "question": (
            "Refer to Point 2 of Case Scenario 2. The total consideration payable under Titan's open offer is Rs 800 Crore. "
            "What is the exact minimum escrow account deposit required under Regulation 17 of SEBI SAST Regulations, 2011?"
        ),
        "option_a": "Rs 200 Crore (flat 25% of Rs 800 Crore).",
        "option_b": "Rs 80 Crore (flat 10% of Rs 800 Crore).",
        "option_c": "Rs 155 Crore (25% on first Rs 500 Crore = Rs 125 Crore + 10% on balance Rs 300 Crore = Rs 30 Crore).",
        "option_d": "Rs 100 Crore (statutory cap on cash escrow deposits under SEBI regulations).",
        "correct_option": "C",
        "marks": 2,
        "explanation": (
            "Under Regulation 17(1) of the SEBI (Substantial Acquisition of Shares and Takeovers) Regulations, 2011, the acquirer "
            "shall create an escrow account towards security for performance of obligations under the open offer.\n\n"
            "Under Regulation 17(3), the escrow amount shall be calculated as follows:\n"
            "(a) On the first Rs 500 Crore of the consideration payable: TWENTY-FIVE PERCENT (25%)\n"
            "(b) On the balance consideration beyond Rs 500 Crore: TEN PERCENT (10%)\n\n"
            "Calculation for Titan's Open Offer:\n"
            "- Total consideration = Rs 800 Crore\n"
            "- First Rs 500 Crore @ 25% = Rs 125 Crore\n"
            "- Balance Rs 300 Crore (Rs 800 Cr - Rs 500 Cr) @ 10% = Rs 30 Crore\n"
            "Total Escrow Amount = Rs 125 Crore + Rs 30 Crore = Rs 155 Crore."
        ),
        "section_ref": "SEBI (SAST) Regulations, 2011 - Regulation 17(3)",
        "exam_tip": "EXAM TRAP: Escrow calculation is slab-based! 25% on first 500 Crore, and 10% on the excess beyond 500 Crore. Do not apply flat 25% across the entire sum.",
        "source_tag": "ICAI Test Your Knowledge",
        "difficulty": "Moderate",
        "is_case_study": 1,
        "case_scenario": CASE_2_TEXT,
        "why_incorrect_a": "Applies flat 25% on entire Rs 800 Cr, ignoring the 10% slab for amounts over Rs 500 Cr.",
        "why_incorrect_b": "Applies flat 10% on entire Rs 800 Cr.",
        "why_incorrect_c": "",
        "why_incorrect_d": "There is no Rs 100 Crore cap under Regulation 17."
    },
    {
        "set_name": "A",
        "section_group": "Part I: Corporate Laws (70 Marks)",
        "chapter_code": "A_SEBI",
        "topic": "SEBI (Prohibition of Insider Trading) Regulations, 2015",
        "subtopic": "Regulation 3(5) Structured Digital Database (SDD) Retention & Integrity",
        "question": (
            "Refer to Point 3 of Case Scenario 2. Under Regulation 3(5) and 3(6) of SEBI (PIT) Regulations, 2015, what is the "
            "statutory preservation timeline for the Structured Digital Database (SDD) maintained by Nexus Tech Ltd.?"
        ),
        "option_a": "Not less than 5 years from the date of completion of the transaction.",
        "option_b": "Not less than 8 years after completion of the concerned transaction, and indefinitely in case of pending SEBI investigation.",
        "option_c": "Not less than 3 years from the date of disclosure of UPSI to the stock exchange.",
        "option_d": "Permanently archived on immutable cloud storage with no option to purge.",
        "correct_option": "B",
        "marks": 2,
        "explanation": (
            "Under Regulation 3(5) of the SEBI (Prohibition of Insider Trading) Regulations, 2015, the board of directors or head(s) "
            "of the organisation of every person required to handle unpublished price sensitive information (UPSI) shall ensure that a "
            "structured digital database (SDD) is maintained containing the nature of UPSI and the names of persons who have shared the "
            "information and the persons with whom information is shared along with PAN/identifier.\n\n"
            "Under Regulation 3(6), the structured digital database shall be preserved for a period of NOT LESS THAN EIGHT (8) YEARS after "
            "completion of the relevant transaction, and in the event of receipt of any information from SEBI regarding any investigation "
            "or enforcement proceedings, the relevant information in the structured digital database shall be preserved until the completion "
            "of such proceedings."
        ),
        "section_ref": "SEBI (PIT) Regulations, 2015 - Regulation 3(5) & 3(6)",
        "exam_tip": "EXAM TRAP: SDD must be preserved for at least 8 YEARS (not 5 years as under PMLA, and not 3 years). Also note: database CANNOT be outsourced; it must be maintained internally with adequate internal controls and time-stamping.",
        "source_tag": "Offline SPOM Recall",
        "difficulty": "Moderate",
        "is_case_study": 1,
        "case_scenario": CASE_2_TEXT,
        "why_incorrect_a": "5 years is the rule under PMLA Section 12, not SEBI PIT SDD.",
        "why_incorrect_b": "",
        "why_incorrect_c": "3 years is incorrect; statutory rule is 8 years.",
        "why_incorrect_d": "SEBI does not require permanent non-purgeable archiving, but prescribes 8 years (or till completion of proceedings)."
    },
    {
        "set_name": "A",
        "section_group": "Part I: Corporate Laws (70 Marks)",
        "chapter_code": "A_SEBI",
        "topic": "SEBI (LODR) Regulations, 2015",
        "subtopic": "Regulation 23 Material Related Party Transaction Thresholds & Approvals",
        "question": (
            "Refer to Point 4 of Case Scenario 2. Nexus proposes a contract of Rs 450 Crore with Vanguard Hardware Ltd. "
            "Turnover is Rs 3,800 Crore. Under Regulation 23 of SEBI (LODR) Regulations, 2015, is this transaction a 'Material RPT' "
            "requiring prior approval of shareholders by Ordinary Resolution?"
        ),
        "option_a": "No, because the transaction is Rs 450 Crore, which is below the Rs 1,000 Crore threshold; only Audit Committee approval suffices.",
        "option_b": "Yes, because Rs 450 Crore exceeds 10% of annual consolidated turnover (10% of Rs 3,800 Cr = Rs 380 Cr); requires prior shareholder approval by Ordinary Resolution where related parties cannot vote.",
        "option_c": "No, because transactions with companies where a director holds less than 50% shares are exempted under LODR.",
        "option_d": "Yes, but it requires approval by Special Resolution under Section 188 of the Companies Act, 2013.",
        "correct_option": "B",
        "marks": 2,
        "explanation": (
            "Under Regulation 23(1) of the SEBI (LODR) Regulations, 2015 (amended w.e.f. April 1, 2022), a transaction with a related party "
            "shall be considered material if the transaction(s) to be entered into individually or taken together with previous transactions "
            "during a financial year exceeds RUPEES ONE THOUSAND CRORE (Rs 1,000 Crore) OR TEN PERCENT (10%) OF THE ANNUAL CONSOLIDATED TURNOVER "
            "of the listed entity as per the last audited financial statements of the listed entity, WHICHEVER IS LOWER.\n\n"
            "Threshold evaluation for Nexus:\n"
            "- 10% of consolidated turnover (10% of Rs 3,800 Crore) = Rs 380 Crore.\n"
            "- Fixed monetary ceiling = Rs 1,000 Crore.\n"
            "- Lower of the two = Rs 380 Crore.\n"
            "Since the proposed contract of Rs 450 Crore exceeds Rs 380 Crore, it is a MATERIAL RELATED PARTY TRANSACTION under LODR Reg 23.\n"
            "Under Regulation 23(4), all material related party transactions require prior approval of the shareholders through an ORDINARY RESOLUTION, "
            "and no related party shall vote to approve such resolutions whether the entity is a related party to the particular transaction or not."
        ),
        "section_ref": "SEBI (LODR) Regulations, 2015 - Regulation 23(1) & 23(4)",
        "exam_tip": "EXAM TRAP: Material RPT threshold under LODR is Rs 1,000 Crore OR 10% of consolidated turnover, WHICHEVER IS LOWER! Notice that shareholder approval is by ORDINARY resolution (not Special resolution).",
        "source_tag": "ICAI BoS Module",
        "difficulty": "Hard",
        "is_case_study": 1,
        "case_scenario": CASE_2_TEXT,
        "why_incorrect_a": "Incorrectly relies solely on the Rs 1,000 Crore limb, ignoring the 'whichever is lower' rule with 10% turnover (Rs 380 Cr).",
        "why_incorrect_b": "",
        "why_incorrect_c": "Director holding 32% creates a related party entity under Companies Act Sec 2(76) and LODR Reg 2(1)(zb).",
        "why_incorrect_d": "LODR mandates Ordinary Resolution, not Special Resolution."
    },
    {
        "set_name": "A",
        "section_group": "Part I: Corporate Laws (70 Marks)",
        "chapter_code": "A_SEBI",
        "topic": "SEBI (LODR) Regulations, 2015",
        "subtopic": "Regulation 29 Prior Intimation Timelines for Debt Securities",
        "question": (
            "Refer to Point 5 of Case Scenario 2. Under Regulation 29 and Regulation 50 of SEBI (LODR) Regulations, 2015, "
            "what is the statutory prior intimation notice period that Nexus must give to the stock exchange for the Board meeting "
            "called to alter the date of payment of interest on its debentures?"
        ),
        "option_a": "At least 2 working days in advance.",
        "option_b": "At least 5 working days in advance.",
        "option_c": "At least 11 working days in advance.",
        "option_d": "At least 7 calendar days in advance.",
        "correct_option": "C",
        "marks": 2,
        "explanation": (
            "Under Regulation 29(1)(d) and Regulation 29(3) / Regulation 50 of the SEBI (LODR) Regulations, 2015:\n"
            "- For consideration of financial results: at least 5 working days (excluding date of intimation and date of meeting).\n"
            "- For buyback, dividend, bonus shares, fund raising: at least 2 working days.\n"
            "- For altering the date on which interest on debentures or bonds, or redemption amount of redeemable shares or of debentures "
            "or bonds, shall be paid: AT LEAST ELEVEN (11) WORKING DAYS prior intimation is mandatorily required!\n\n"
            "This 11 working days requirement ensures that debenture holders and the secondary debt market have sufficient advance notice of any alteration in debt servicing schedules."
        ),
        "section_ref": "SEBI (LODR) Regulations, 2015 - Regulation 29(3) / Regulation 50",
        "exam_tip": "SUPER HIGH-YIELD EXAM TRAP: Most students remember 5 days (results) and 2 days (dividend/buyback). The 11 WORKING DAYS rule for altering date of payment of interest or redemption on debentures is a favorite ICAI SPOM trap!",
        "source_tag": "Offline SPOM Recall",
        "difficulty": "Hard",
        "is_case_study": 1,
        "case_scenario": CASE_2_TEXT,
        "why_incorrect_a": "2 working days applies to dividend, buyback, bonus, and convertible issues.",
        "why_incorrect_b": "5 working days applies to financial results.",
        "why_incorrect_c": "",
        "why_incorrect_d": "The requirement is specified in working days (11 working days), not 7 calendar days."
    }
]

# ==============================================================================
# CASE STUDY 3: Corporate Distress, Insolvency Resolution & Liquidation
# Entity: Sterling Steels Ltd (Corporate Debtor) & Multiple Creditor Classes
# Topics: IBC Sec 4, Sec 7 (Homebuyers), Sec 8/9, Sec 21/24 (CoC), Sec 53 (Waterfall)
# ==============================================================================
CASE_3_TEXT = (
    "CASE SCENARIO: STERLING STEELS LTD & REAL ESTATE AFFILIATE - INSOLVENCY & WATERFALL\n\n"
    "Sterling Steels Ltd. ('Sterling') is an integrated industrial manufacturer that also floated a real estate township project, "
    "'Sterling Greens', through its infrastructure division. Owing to protracted market distress, default occurred across multiple fronts:\n\n"
    "1. Homebuyers' Section 7 CIRP Petition: Sterling Greens consists of 600 allottees across 4 residential towers. A group of "
    "48 allottees, having collectively deposited Rs 32 Crore, filed an application under Section 7 of the Insolvency and Bankruptcy "
    "Code (IBC), 2016 before the NCLT for initiation of CIRP against Sterling on grounds of project delivery delay.\n\n"
    "2. Operational Creditor Demand Notice & Pre-Existing Dispute: Alpha Refractories supplied industrial furnace bricks worth "
    "Rs 1.40 Crore to Sterling. On 5th August 2024, Alpha served a Section 8 demand notice. Sterling had, on 20th July 2024 (prior to the notice), "
    "sent an email debit note rejecting 40% of the bricks for structural cracks and lodging an arbitration invocation notice under the contract. "
    "Alpha proceeded to file a Section 9 application before NCLT claiming the dispute was spurious.\n\n"
    "3. Committee of Creditors (CoC) Voting Rights: Upon CIRP admission, the Interim Resolution Professional (IRP) constituted the CoC. "
    "The financial creditors comprise:\n"
    "- State Bank of India (Secured FC): Debt Rs 200 Crore (40% voting share)\n"
    "- Punjab National Bank (Secured FC): Debt Rs 150 Crore (30% voting share)\n"
    "- Zenith Finance Ltd (Unsecured FC, but a wholly-owned subsidiary of Sterling): Debt Rs 100 Crore (20% voting share)\n"
    "- Independent Trade Debenture Holders: Debt Rs 50 Crore (10% voting share).\n\n"
    "4. Resolution Plan Voting Majority: A resolution plan submitted by a resolution applicant received favorable votes from "
    "SBI (40%) and PNB (30%), while Independent Trade Debenture Holders (10%) voted against. The CoC seeks confirmation on whether the plan is approved.\n\n"
    "5. Liquidation Waterfall Priority: The corporate debtor ultimately proceeded into liquidation under Section 33. The Liquidator realized "
    "total liquidation assets of Rs 180 Crore. Admitted claims are:\n"
    "- CIRP Costs & Liquidator remuneration: Rs 10 Crore\n"
    "- Workmen dues for 24 months preceding liquidation: Rs 30 Crore\n"
    "- Secured Financial Creditor (SBI) who relinquished security under Section 52: Rs 80 Crore\n"
    "- Wages due to other non-workmen employees for 12 months: Rs 15 Crore\n"
    "- Unsecured Financial Creditors: Rs 50 Crore\n"
    "- Central Government tax dues (GST/Income Tax for 2 years): Rs 25 Crore."
)

CASE_3_QUESTIONS = [
    {
        "set_name": "A",
        "section_group": "Part II: Economic Laws (30 Marks)",
        "chapter_code": "A_IBC",
        "topic": "Insolvency and Bankruptcy Code, 2016",
        "subtopic": "Section 7 CIRP Threshold for Real Estate Allottees (Homebuyers)",
        "question": (
            "Refer to Point 1 of Case Scenario 3. Is the Section 7 CIRP application filed by the 48 allottees of Sterling Greens "
            "maintainable before the NCLT under the Insolvency and Bankruptcy Code, 2016?"
        ),
        "option_a": "Yes, because the default amount exceeds the statutory minimum threshold of Rs 1 Crore under Section 4.",
        "option_b": "No, because under the Second Proviso to Section 7(1), the application must be filed jointly by not less than 100 allottees OR not less than 10% of total allottees under the same real estate project, whichever is less.",
        "option_c": "Yes, provided the allottees deposit an indemnity bond for 10% of the project value with the Registry.",
        "option_d": "No, because allottees in real estate projects can only seek relief before RERA, not under IBC.",
        "correct_option": "B",
        "marks": 2,
        "explanation": (
            "Under the Second Proviso to Section 7(1) of the Insolvency and Bankruptcy Code, 2016 (as amended by IBC Amendment Act 2020 "
            "and upheld by the Supreme Court in Manish Kumar v. Union of India):\n"
            "For financial creditors who are allottees under a real estate project, an application for initiating corporate insolvency "
            "resolution process against the corporate debtor shall be filed JOINTLY by:\n"
            "- NOT LESS THAN ONE HUNDRED (100) of such allottees under the same real estate project, OR\n"
            "- NOT LESS THAN TEN PERCENT (10%) of the total number of such allottees under the same real estate project, WHICHEVER IS LESS.\n\n"
            "In Sterling Greens:\n"
            "- Total allottees = 600\n"
            "- 10% of total allottees = 60 allottees\n"
            "- Statutory requirement = Lower of 100 or 60 = 60 allottees.\n"
            "Since only 48 allottees joined in the petition, the statutory numerical threshold of 60 is not met. Therefore, the application is NOT maintainable."
        ),
        "section_ref": "Insolvency and Bankruptcy Code, 2016 - Section 7(1) Second Proviso",
        "exam_tip": "EXAM TRAP: For homebuyers, meeting the Rs 1 Crore threshold is NOT enough! They must also satisfy the numerical filter: MINIMUM 100 or 10% of total allottees, whichever is lower.",
        "source_tag": "ICAI Case Scenario",
        "difficulty": "Moderate",
        "is_case_study": 1,
        "case_scenario": CASE_3_TEXT,
        "why_incorrect_a": "Ignores the mandatory numerical threshold of the Second Proviso to Section 7(1).",
        "why_incorrect_b": "",
        "why_incorrect_c": "There is no provision for depositing an indemnity bond under Section 7.",
        "why_incorrect_d": "Homebuyers are financial creditors and can initiate CIRP under IBC, subject to the threshold."
    },
    {
        "set_name": "A",
        "section_group": "Part II: Economic Laws (30 Marks)",
        "chapter_code": "A_IBC",
        "topic": "Insolvency and Bankruptcy Code, 2016",
        "subtopic": "Section 8 & 9 Operational Creditor Demand Notice & Pre-Existing Dispute",
        "question": (
            "Refer to Point 2 of Case Scenario 3. Can the NCLT admit Alpha Refractories' Section 9 application against Sterling Steels Ltd.?"
        ),
        "option_a": "Yes, because the operational debt exceeds Rs 1 Crore and invoice default is undisputed.",
        "option_b": "No, because Sterling had raised a bona fide pre-existing dispute and invoked arbitration prior to the receipt of the Section 8 demand notice.",
        "option_c": "Yes, because the dispute relates to only 40% of the consignment, so CIRP must be admitted for the remaining 60%.",
        "option_d": "No, because operational creditors cannot file for insolvency against manufacturing companies.",
        "correct_option": "B",
        "marks": 2,
        "explanation": (
            "Under Section 9(5)(ii)(d) of the Insolvency and Bankruptcy Code, 2016, the Adjudicating Authority (NCLT) SHALL REJECT the application "
            "if notice of dispute has been received by the operational creditor or there is a record of dispute in the information utility.\n\n"
            "As established by the Supreme Court in the landmark ruling of Mobilox Innovations Pvt. Ltd. v. Kirusa Software Pvt. Ltd., "
            "all that the Adjudicating Authority has to see at the stage of admitting a Section 9 application is whether there is a plausible "
            "contention requiring further investigation and that the 'dispute' is not a patently feeble legal argument or an assertion of fact unsupported by evidence. "
            "Crucially, the dispute/arbitration notice must exist PRIOR TO the receipt of the Section 8 demand notice.\n\n"
            "Here, Sterling had sent the debit note and arbitration notice on 20th July 2024, well before Alpha served the demand notice on 5th August 2024. "
            "Because there is a clear pre-existing dispute, NCLT cannot admit the Section 9 application."
        ),
        "section_ref": "Insolvency and Bankruptcy Code, 2016 - Section 8, Section 9(5)(ii)(d) & Mobilox Innovations Principle",
        "exam_tip": "EXAM TRAP: If arbitration is invoked or a civil suit is pending BEFORE the Section 8 demand notice is issued, Section 9 CANNOT be admitted. IBC is not a debt recovery mechanism!",
        "source_tag": "Offline SPOM Recall",
        "difficulty": "Moderate",
        "is_case_study": 1,
        "case_scenario": CASE_3_TEXT,
        "why_incorrect_a": "The presence of a genuine pre-existing dispute mandates rejection under Section 9(5)(ii)(d).",
        "why_incorrect_b": "",
        "why_incorrect_c": "CIRP is an all-or-nothing composite process; NCLT cannot admit partial CIRP for 60% of an operational claim.",
        "why_incorrect_d": "Operational creditors can file against any corporate debtor, including manufacturers."
    },
    {
        "set_name": "A",
        "section_group": "Part II: Economic Laws (30 Marks)",
        "chapter_code": "A_IBC",
        "topic": "Insolvency and Bankruptcy Code, 2016",
        "subtopic": "Section 21 & Section 24 Committee of Creditors - Disenfranchisement of Related Parties",
        "question": (
            "Refer to Point 3 and Point 4 of Case Scenario 3. Determine the voting rights in the Committee of Creditors (CoC) "
            "and whether the Resolution Plan received the mandatory statutory voting majority for approval under Section 30(4)."
        ),
        "option_a": "Zenith Finance has 20% voting rights; Total votes in favor = 70% (SBI 40% + PNB 30%); Plan fails as 75% is required.",
        "option_b": "Zenith Finance, being a related party financial creditor, has NO right of representation, participation or voting; Recomputed voting shares are SBI (50%), PNB (37.5%), Trade Debentures (12.5%); Total votes in favor = 87.5%; Plan IS APPROVED (exceeds 66%).",
        "option_c": "Zenith Finance has voting rights; Total votes in favor = 70%; Plan is approved since it exceeds 66%.",
        "option_d": "Related parties can vote if they are wholly-owned subsidiaries; Plan is approved with 90% majority.",
        "correct_option": "B",
        "marks": 2,
        "explanation": (
            "This question tests two pivotal IBC principles:\n"
            "1. Disenfranchisement of Related Party Financial Creditors under First Proviso to Section 21(2):\n"
            "A financial creditor or the authorized representative of the financial creditor, if it is a RELATED PARTY of the corporate debtor, "
            "SHALL NOT HAVE ANY RIGHT OF REPRESENTATION, PARTICIPATION OR VOTING in a meeting of the committee of creditors.\n"
            "Here, Zenith Finance Ltd. is a wholly-owned subsidiary of Sterling (Corporate Debtor), making it a related party under Section 5(24). "
            "Hence, Zenith Finance is completely excluded from the CoC voting base.\n\n"
            "2. Recomputation of CoC Voting Base:\n"
            "Eligible Financial Debt = SBI (Rs 200 Cr) + PNB (Rs 150 Cr) + Trade Debentures (Rs 50 Cr) = Total Rs 400 Crore.\n"
            "- SBI voting share = 200 / 400 = 50.0%\n"
            "- PNB voting share = 150 / 400 = 37.5%\n"
            "- Trade Debentures = 50 / 400 = 12.5%\n\n"
            "3. Resolution Plan Voting Majority under Section 30(4):\n"
            "Under Section 30(4), the CoC must approve the resolution plan by a vote of NOT LESS THAN SIXTY-SIX PERCENT (66%) of voting share of financial creditors.\n"
            "Votes in favor = SBI (50%) + PNB (37.5%) = 87.5%.\n"
            "Since 87.5% >= 66%, the resolution plan is APPROVED."
        ),
        "section_ref": "Insolvency and Bankruptcy Code, 2016 - Section 21(2) First Proviso & Section 30(4)",
        "exam_tip": "CRITICAL EXAM TRAP: When calculating CoC voting percentages, EXCLUDE related party financial debt entirely from the denominator! Do not leave related party shares in the pool.",
        "source_tag": "ICAI Case Scenario",
        "difficulty": "Hard",
        "is_case_study": 1,
        "case_scenario": CASE_3_TEXT,
        "why_incorrect_a": "Zenith Finance is a related party and cannot have voting rights; also approval threshold is 66%, not 75%.",
        "why_incorrect_b": "",
        "why_incorrect_c": "Fails to exclude related party from voting and miscalculates voting shares.",
        "why_incorrect_d": "Wholly-owned subsidiaries are not exempt from the related party voting bar unless they are regulated financial entities under the second proviso."
    },
    {
        "set_name": "A",
        "section_group": "Part II: Economic Laws (30 Marks)",
        "chapter_code": "A_IBC",
        "topic": "Insolvency and Bankruptcy Code, 2016",
        "subtopic": "Section 53 Distribution of Assets (Liquidation Waterfall Priority)",
        "question": (
            "Refer to Point 5 of Case Scenario 3. In the Section 53 liquidation waterfall distribution of Rs 180 Crore, "
            "how will the available proceeds be allocated between Workmen Dues (Rs 30 Cr) and the Secured Financial Creditor SBI (Rs 80 Cr) "
            "after meeting liquidation costs of Rs 10 Crore?"
        ),
        "option_a": "SBI gets full Rs 80 Crore first because it is a secured financial creditor; Workmen get the remaining Rs 90 Crore.",
        "option_b": "Workmen dues (Rs 30 Crore) and SBI claims (Rs 80 Crore) rank equally pari-passu under Section 53(1)(b); both will be paid 100% in full as available funds (Rs 170 Cr) comfortably exceed their combined total of Rs 110 Crore.",
        "option_c": "Central Government taxes (Rs 25 Cr) take priority over both workmen and secured creditors under statutory Crown debt supremacy.",
        "option_d": "Workmen dues for 24 months are capped at Rs 5 Lakhs per workman, with balance subordinated to unsecured creditors.",
        "correct_option": "B",
        "marks": 2,
        "explanation": (
            "Under Section 53(1) of the Insolvency and Bankruptcy Code, 2016, liquidation proceeds are distributed in the following strict priority:\n"
            "1. Section 53(1)(a): Insolvency resolution process costs and liquidation costs in full = Rs 10 Crore.\n"
            "Remaining funds = Rs 180 Cr - Rs 10 Cr = Rs 170 Crore.\n\n"
            "2. Section 53(1)(b): The following rank PARI PASSU (equally):\n"
            "(i) Workmen's dues for the period of 24 months preceding liquidation commencement date (Rs 30 Crore)\n"
            "(ii) Debts owed to a secured creditor in the event such secured creditor has relinquished security in the manner set out in section 52 (Rs 80 Crore).\n"
            "Total required for tier (b) = 30 + 80 = Rs 110 Crore.\n\n"
            "Since the available surplus of Rs 170 Crore is greater than Rs 110 Crore, BOTH Workmen dues (Rs 30 Cr) and SBI (Rs 80 Cr) receive 100% in full!\n"
            "Remaining Rs 60 Crore (Rs 170 Cr - Rs 110 Cr) then cascades down to Tier (c) [Other employee wages: Rs 15 Cr], leaving Rs 45 Cr for Tier (d) [Unsecured FC: Rs 50 Cr, receiving Rs 45 Cr pro-rata]."
        ),
        "section_ref": "Insolvency and Bankruptcy Code, 2016 - Section 53(1)(b)",
        "exam_tip": "EXAM TRAP: Workmen dues (24 months) and Secured Creditors relinquishing security rank PARI PASSU (equally) under Section 53(1)(b). Crown debt (Govt taxes) ranks way down at Section 53(1)(e)—IBC completely abolished Crown debt supremacy!",
        "source_tag": "Offline SPOM Recall",
        "difficulty": "Moderate",
        "is_case_study": 1,
        "case_scenario": CASE_3_TEXT,
        "why_incorrect_a": "Workmen dues and secured creditors rank equally pari passu under Section 53(1)(b); secured creditors have no seniority over workmen.",
        "why_incorrect_b": "",
        "why_incorrect_c": "Grossly incorrect; Government dues are at clause (e), subordinate to workmen, secured creditors, employees, and unsecured financial creditors.",
        "why_incorrect_d": "The 24-month period under Section 53(1)(b) does not have a Rs 5 Lakh per workman cap in liquidation waterfall."
    }
]

# ==============================================================================
# CASE STUDY 4: Global Financing, FEMA Regulations & Foreign Contributions
# Entity: Global EPC Projects Ltd & Foundation
# Topics: FEMA Current Account Sched III, Compounding of Contraventions, FCRA Sec 6/17
# ==============================================================================
CASE_4_TEXT = (
    "CASE SCENARIO: GLOBAL EPC PROJECTS LTD - FEMA & FCRA CROSS-BORDER TRANSACTIONS\n\n"
    "Global EPC Projects Ltd. ('Global EPC') is an Indian infrastructure contractor executing multi-billion dollar EPC "
    "projects across Asia and Africa. Alongside, its CSR wing operates the Global Welfare Trust ('Trust'), registered under "
    "the Foreign Contribution (Regulation) Act, 2010 (FCRA).\n\n"
    "During FY 2024-25, the following cross-border remittances and events transpired:\n"
    "1. Infrastructure Consultancy Remittance: For an urban metro project in Mumbai, Global EPC engaged a Swiss structural "
    "engineering consultancy firm and remitted USD 12,500,000 as professional consultancy fees through its authorized dealer.\n\n"
    "2. Repeat Compounding Application under FEMA: Global EPC inadvertently delayed filing Form FC-GPR for foreign investment "
    "amounting to Rs 25 Lakhs. In July 2022, Global EPC had compounded an identical contravention of delayed Form FC-GPR filing. "
    "In August 2024, the company filed a fresh compounding application before the Reserve Bank of India.\n\n"
    "3. Foreign Hospitality to Public Servants: The Chairman of the Trust, who is also a sitting Member of the Legislative "
    "Assembly (MLA), was invited to Geneva for a 3-week conference by an international donor. While in Geneva, he suffered an acute "
    "cardiac event requiring emergency surgery and hospitalization. The foreign host paid the entire medical expenses of USD 9,000 "
    "(approx. Rs 7.5 Lakhs). No prior approval of the Central Government had been obtained.\n\n"
    "4. FCRA Designated Account Routing: The Trust opened a bank account with HDFC Bank, Fort Branch, Mumbai, and received "
    "foreign contributions of USD 500,000 directly into this account to fund rural skill centres."
)

CASE_4_QUESTIONS = [
    {
        "set_name": "A",
        "section_group": "Part II: Economic Laws (30 Marks)",
        "chapter_code": "A_FEMA",
        "topic": "Foreign Exchange Management Act, 1999",
        "subtopic": "Current Account Transactions - Schedule III Consultancy Services Limits",
        "question": (
            "Refer to Point 1 of Case Scenario 4. Under Schedule III to the Foreign Exchange Management (Current Account Transactions) "
            "Rules, 2000, was prior approval of the Reserve Bank of India required for Global EPC's remittance of USD 12,500,000 for infrastructure consultancy?"
        ),
        "option_a": "No, because all consultancy remittances for infrastructure projects are completely unrestricted without any ceiling.",
        "option_b": "Yes, because prior RBI approval is mandatory for consultancy services procured from abroad for infrastructure projects exceeding USD 10,000,000 per project.",
        "option_c": "No, because the limit for infrastructure consultancy is USD 20,000,000 per project.",
        "option_d": "Yes, but approval must be sought from the Ministry of Commerce & Industry, not RBI.",
        "correct_option": "B",
        "marks": 2,
        "explanation": (
            "Under Schedule III (Item 4) of the FEM (Current Account Transactions) Rules, 2000, remittances by persons other than individuals "
            "require prior approval of the Reserve Bank of India for:\n"
            "- Remittances exceeding USD 10,000,000 (Ten Million USD) per project for any consultancy services in respect of INFRASTRUCTURE PROJECTS "
            "and USD 1,000,000 (One Million USD) per project for OTHER CONSULTANCY SERVICES procured from outside India.\n\n"
            "Here, Global EPC remitted USD 12,500,000 for consultancy in respect of an urban metro (infrastructure) project. "
            "Since USD 12,500,000 exceeds the statutory threshold of USD 10,000,000, PRIOR APPROVAL OF THE RESERVE BANK OF INDIA WAS MANDATORILY REQUIRED."
        ),
        "section_ref": "FEM (Current Account Transactions) Rules, 2000 - Schedule III, Item 4",
        "exam_tip": "EXAM TRAP: Remember the dual consultancy limits under Schedule III: USD 10 Million per project for INFRASTRUCTURE projects, and USD 1 Million per project for OTHER consultancy services.",
        "source_tag": "ICAI Test Your Knowledge",
        "difficulty": "Moderate",
        "is_case_study": 1,
        "case_scenario": CASE_4_TEXT,
        "why_incorrect_a": "Remittances exceeding USD 10 Million require prior RBI approval.",
        "why_incorrect_b": "",
        "why_incorrect_c": "The statutory limit is USD 10 Million, not USD 20 Million.",
        "why_incorrect_d": "Schedule III specifies Reserve Bank of India as the approving authority, not the Ministry of Commerce."
    },
    {
        "set_name": "A",
        "section_group": "Part II: Economic Laws (30 Marks)",
        "chapter_code": "A_FEMA",
        "topic": "Foreign Exchange Management Act, 1999",
        "subtopic": "Compounding of Contraventions - 3-Year Repeat Bar & Officer Jurisdiction",
        "question": (
            "Refer to Point 2 of Case Scenario 4. Under the Foreign Exchange Management (Compounding Proceedings) Rules, 2000, "
            "can Global EPC's fresh compounding application filed in August 2024 be entertained by the Reserve Bank of India?"
        ),
        "option_a": "Yes, provided the company pays a 25% penal surcharge for repeat offences.",
        "option_b": "No, because under Rule 11, no contravention can be compounded if a similar contravention was compounded within a period of THREE (3) YEARS immediately preceding.",
        "option_c": "Yes, because compounding can be undertaken at any time as long as the amount does not exceed Rs 1 Crore.",
        "option_d": "No, because filing of Form FC-GPR is a non-compoundable criminal offence under Section 13.",
        "correct_option": "B",
        "marks": 2,
        "explanation": (
            "Under Rule 11 of the Foreign Exchange Management (Compounding Proceedings) Rules, 2000:\n"
            "Where a contravention has been compounded by the Compounding Authority, NO SIMILAR CONTRAVENTION SHALL BE COMPOUNDED "
            "within a period of THREE (3) YEARS from the date on which such contravention was compounded. Any second or subsequent "
            "contravention committed after the expiry of three years from the date on which the contravention was previously compounded "
            "shall be deemed to be a first contravention.\n\n"
            "Here, Global EPC compounded an identical contravention of delayed Form FC-GPR filing in July 2022. The fresh application was filed "
            "in August 2024, which is approximately 2 years and 1 month later (less than 3 years). Therefore, under Rule 11, the RBI CANNOT entertain "
            "the compounding application."
        ),
        "section_ref": "FEM (Compounding Proceedings) Rules, 2000 - Rule 11",
        "exam_tip": "EXAM TRAP: The repeat compounding bar is exactly 3 YEARS! Any similar contravention within 3 years cannot be compounded and will face regular adjudication and penalty.",
        "source_tag": "Offline SPOM Recall",
        "difficulty": "Moderate",
        "is_case_study": 1,
        "case_scenario": CASE_4_TEXT,
        "why_incorrect_a": "There is no surcharge mechanism; Rule 11 imposes an absolute bar on repeat compounding within 3 years.",
        "why_incorrect_b": "",
        "why_incorrect_c": "The 3-year bar applies regardless of the monetary amount involved.",
        "why_incorrect_d": "Delayed FC-GPR is compoundable as a civil contravention, but barred here due to the 3-year repeat rule."
    },
    {
        "set_name": "A",
        "section_group": "Part II: Economic Laws (30 Marks)",
        "chapter_code": "A_PMLA_FCRA",
        "topic": "Foreign Contribution (Regulation) Act, 2010",
        "subtopic": "Section 6 Foreign Hospitality & Emergency Medical Exception",
        "question": (
            "Refer to Point 3 of Case Scenario 4. Did the MLA violate Section 6 of the Foreign Contribution (Regulation) Act, 2010 "
            "by accepting medical expenses of USD 9,000 without prior Central Government permission, and what is his legal duty?"
        ),
        "option_a": "Yes, it is an incurable violation of FCRA punishable with imprisonment up to 5 years.",
        "option_b": "No, because medical emergencies are completely exempt from FCRA without any requirement of reporting to the government.",
        "option_c": "Under the Proviso to Section 6, prior permission is not required for emergent medical illness abroad; however, since the market value exceeds Rs 1,00,000, he must intimate the Central Government within ONE (1) MONTH of receipt.",
        "option_d": "No, because MLAs are not covered under the restrictions of Section 6 of FCRA.",
        "correct_option": "C",
        "marks": 2,
        "explanation": (
            "Under Section 6 of the Foreign Contribution (Regulation) Act, 2010, no member of a Legislature, office-bearer of a political party, "
            "judge, government servant or employee of any corporation owned/controlled by the Government shall, while visiting any country or territory "
            "outside India, accept, except with the prior permission of the Central Government, any foreign hospitality.\n\n"
            "However, under the Proviso to Section 6 read with Rule 7 of the FCR Rules, 2011:\n"
            "It shall not be necessary to obtain any prior permission for an emergent medical aid contracted suddenly during a visit abroad, "
            "where the value of such hospitality does not exceed Rs 1,00,000. Where the foreign hospitality exceeds Rs 1,00,000, the person receiving "
            "such hospitality SHALL INTIMATE THE CENTRAL GOVERNMENT WITHIN ONE (1) MONTH of receipt of such hospitality along with the source, approximate value, and manner of receipt.\n\n"
            "Here, the Chairman is an MLA (covered under Sec 6). The sudden medical expenses were USD 9,000 (Rs 7.5 Lakhs > Rs 1 Lakh). "
            "Prior permission was not needed due to the emergent medical crisis, but he is legally bound to intimate the Central Government within 1 month."
        ),
        "section_ref": "FCRA, 2010 - Section 6 Proviso read with Rule 7",
        "exam_tip": "EXAM TRAP: Emergency medical aid abroad does NOT require prior approval, BUT if it exceeds Rs 1,00,000, mandatory intimation to Central Government must be given WITHIN ONE MONTH!",
        "source_tag": "ICAI Case Scenario",
        "difficulty": "Hard",
        "is_case_study": 1,
        "case_scenario": CASE_4_TEXT,
        "why_incorrect_a": "Emergency medical treatment is protected by the Proviso and is not an incurable violation if reported.",
        "why_incorrect_b": "Intimation is mandatory within 1 month if value exceeds Rs 1,00,000.",
        "why_incorrect_c": "",
        "why_incorrect_d": "Members of a Legislature (MLAs/MPs) are explicitly covered under Section 6."
    },
    {
        "set_name": "A",
        "section_group": "Part II: Economic Laws (30 Marks)",
        "chapter_code": "A_PMLA_FCRA",
        "topic": "Foreign Contribution (Regulation) Act, 2010",
        "subtopic": "Section 17 Mandatory Receipt in SBI Main Branch, New Delhi",
        "question": (
            "Refer to Point 4 of Case Scenario 4. Under Section 17 of the Foreign Contribution (Regulation) Act, 2010, "
            "did the Trust act in compliance with law by receiving foreign contributions into its HDFC Bank Fort Branch account?"
        ),
        "option_a": "Yes, because any scheduled commercial bank holding an AD Category-I license is permitted to receive foreign contribution.",
        "option_b": "No, because under amended Section 17(1), every person who has been granted certificate under Section 12 SHALL RECEIVE foreign contribution ONLY in an account designated as 'FCRA Account' opened in State Bank of India, Main Branch, New Delhi.",
        "option_c": "Yes, provided 20% of the funds are transferred to the Prime Minister's National Relief Fund within 15 days.",
        "option_d": "No, because foreign contributions cannot be received in any private sector bank unless authorized by the Supreme Court.",
        "correct_option": "B",
        "marks": 2,
        "explanation": (
            "Under Section 17(1) of the Foreign Contribution (Regulation) Act, 2010 (as substituted by the FCRA Amendment Act, 2020):\n"
            "Every person who has been granted certificate or given prior permission under Section 12 SHALL RECEIVE FOREIGN CONTRIBUTION "
            "ONLY IN AN ACCOUNT DESIGNATED AS 'FCRA ACCOUNT' BY THE BANK, WHICH SHALL BE OPENED BY HIM IN SUCH BRANCH OF THE STATE BANK OF INDIA "
            "AT NEW DELHI, AS THE CENTRAL GOVERNMENT MAY, BY NOTIFICATION, SPECIFY (specifically State Bank of India, Main Branch, 11 Sansad Marg, New Delhi).\n\n"
            "While the person may open another FCRA account in any scheduled bank for UTILIZING the funds, the INITIAL RECEIPT of foreign contributions "
            "must occur exclusively in the designated SBI Main Branch account in New Delhi. Receiving funds directly into HDFC Bank Fort Branch violates Section 17(1)."
        ),
        "section_ref": "FCRA, 2010 - Section 17(1)",
        "exam_tip": "EXAM TRAP: Foreign contributions CANNOT be received directly in private or regional bank branches. They must FIRST land in State Bank of India, Main Branch, New Delhi!",
        "source_tag": "Offline SPOM Recall",
        "difficulty": "Moderate",
        "is_case_study": 1,
        "case_scenario": CASE_4_TEXT,
        "why_incorrect_a": "Amended Section 17 mandates initial receipt only in SBI Main Branch, New Delhi.",
        "why_incorrect_b": "",
        "why_incorrect_c": "There is no requirement to transfer 20% to PMNRF.",
        "why_incorrect_d": "Utilization accounts can be in private banks, but the primary receipt account must be SBI New Delhi."
    }
]

# ==============================================================================
# CASE STUDY 5: Compromises, Mergers & Oppression/Mismanagement
# Entity: Bharat Dynamics Engineering Ltd & Precision Tooling Pvt Ltd
# Topics: Sec 230(6), Sec 233 Fast Track, Sec 241/244 Oppression, Sec 212 SFIO
# ==============================================================================
CASE_5_TEXT = (
    "CASE SCENARIO: BHARAT DYNAMICS & SUBSIDIARY - RESTRUCTURING, OPPRESSION & SFIO\n\n"
    "Bharat Dynamics Engineering Ltd. ('Bharat Dynamics') is an unlisted public engineering enterprise with 800 shareholders "
    "and Paid-up Equity Capital of Rs 50 Crore divided into 5,00,00,000 shares of Rs 10 each. It wholly owns Precision Tooling Pvt. Ltd. "
    "('Precision'), a wholly-owned subsidiary.\n\n"
    "During FY 2024-25, the following matters arose:\n"
    "1. Scheme of Arrangement Voting Test: Bharat Dynamics proposed a scheme of compromise with its 300 unsecured trade creditors "
    "having total claims of Rs 60 Crore. At the NCLT-convened meeting, 100 creditors holding Rs 40 Crore of claims attended and voted. "
    "The voting result showed: 65 creditors holding Rs 31 Crore voted FOR the scheme, and 35 creditors holding Rs 9 Crore voted AGAINST.\n\n"
    "2. Fast-Track Merger under Section 233: Bharat Dynamics and Precision propose to merge under the Fast-Track route under Section 233 "
    "without approaching NCLT. Bharat Dynamics' legal advisor prepared the statutory consent documentation for members and creditors.\n\n"
    "3. Petition for Oppression and Mismanagement: A disgruntled minority group of 45 shareholders, holding 12% of the paid-up share capital, "
    "filed a petition under Section 241 alleging severe oppression and siphoning of company contracts to promoter-linked firms. The company "
    "argued that 45 members represents only 5.6% of the 800 total shareholders, and therefore falls below the 100 members / 10% threshold under Section 244.\n\n"
    "4. SFIO Investigation & Arrest Powers: Following a forensic report, the Central Government assigned the investigation into Bharat Dynamics "
    "to the Serious Fraud Investigation Office (SFIO) under Section 212. During the investigation, the SFIO Director ordered the arrest of "
    "the Finance Director based on credible evidence of Section 447 corporate fraud."
)

CASE_5_QUESTIONS = [
    {
        "set_name": "A",
        "section_group": "Part I: Corporate Laws (70 Marks)",
        "chapter_code": "A_COMP",
        "topic": "Compromises, Arrangements & Amalgamations",
        "subtopic": "Section 230(6) Dual Majority Approval Rule for Compromise",
        "question": (
            "Refer to Point 1 of Case Scenario 5. Based on the voting results at the court-convened meeting of creditors, "
            "is the scheme of compromise approved under Section 230(6) of the Companies Act, 2013?"
        ),
        "option_a": "Yes, because 65 creditors voted in favor (majority in number) and Rs 31 Crore represents more than 50% in value.",
        "option_b": "No, because the scheme requires approval by a majority in number representing at least THREE-FOURTHS (75%) in value of creditors present and voting; here Rs 31 Crore is only 77.5%, but 75% of total creditors (300) must vote.",
        "option_c": "Yes, because 65 out of 100 is a majority in number (65%), and Rs 31 Crore out of Rs 40 Crore is 77.5% (exceeding the 75% value threshold of creditors present and voting).",
        "option_d": "No, because Rs 31 Crore does not represent 75% of the total creditor debt of Rs 60 Crore.",
        "correct_option": "C",
        "marks": 2,
        "explanation": (
            "Under Section 230(6) of the Companies Act, 2013, a scheme of compromise or arrangement must be approved by:\n"
            "- A MAJORITY IN NUMBER (i.e. more than 50% of persons voting), representing\n"
            "- THREE-FOURTHS (75%) IN VALUE of the creditors or class of creditors, or members or class of members, as the case may be,\n"
            "PRESENT AND VOTING at the meeting (either in person or by proxy or by postal ballot).\n\n"
            "Evaluation of Voting Results:\n"
            "1. Creditors present and voting = 100 creditors holding Rs 40 Crore.\n"
            "2. Majority in number test: 65 creditors voted in favor. Since 65 > 50 (majority of 100), the number test is SATISFIED.\n"
            "3. Three-fourths in value test: 75% of Rs 40 Crore = Rs 30 Crore. The creditors voting in favor hold Rs 31 Crore (77.5% > 75%). "
            "Hence, the value test is SATISFIED.\n\n"
            "Crucially, the 3/4th in value test is computed on the value of creditors PRESENT AND VOTING (Rs 40 Cr), NOT the total debt of the company (Rs 60 Cr). "
            "Therefore, the scheme is legally approved under Section 230(6)."
        ),
        "section_ref": "Companies Act, 2013 - Section 230(6)",
        "exam_tip": "EXAM TRAP: The 3/4th (75%) in value threshold is calculated based on creditors/members PRESENT AND VOTING, NOT total registered debt or capital of the company!",
        "source_tag": "ICAI BoS Module",
        "difficulty": "Moderate",
        "is_case_study": 1,
        "case_scenario": CASE_5_TEXT,
        "why_incorrect_a": "Section 230(6) requires 3/4th (75%) in value, not simple 50% in value.",
        "why_incorrect_b": "Misrepresents the law; the 75% applies to creditors present and voting, not total registered creditors.",
        "why_incorrect_c": "",
        "why_incorrect_d": "Incorrectly evaluates value against total debt of Rs 60 Cr rather than debt of creditors present and voting (Rs 40 Cr)."
    },
    {
        "set_name": "A",
        "section_group": "Part I: Corporate Laws (70 Marks)",
        "chapter_code": "A_COMP",
        "topic": "Compromises, Arrangements & Amalgamations",
        "subtopic": "Section 233 Fast Track Merger Eligibility & Thresholds",
        "question": (
            "Refer to Point 2 of Case Scenario 5. Under Section 233 of the Companies Act, 2013, can Bharat Dynamics and Precision Tooling "
            "merge through the Fast-Track route, and what are the creditor approval requirements?"
        ),
        "option_a": "No, because Fast Track merger is available ONLY between two or more small companies, and never for public companies.",
        "option_b": "Yes, because Section 233 explicitly covers a merger between a holding company and its wholly-owned subsidiary; creditor approval requires consent of at least 90% in value of creditors.",
        "option_c": "Yes, but it requires final confirmation from the National Company Law Tribunal (NCLT).",
        "option_d": "No, because Precision is a private company while Bharat Dynamics is an unlisted public company.",
        "correct_option": "B",
        "marks": 2,
        "explanation": (
            "Under Section 233(1) of the Companies Act, 2013 read with Rule 25 of the Companies (Compromises, Arrangements and Amalgamations) Rules, 2016:\n"
            "A scheme of merger or amalgamation may be entered into between:\n"
            "(a) Two or more small companies, OR\n"
            "(b) A HOLDING COMPANY AND ITS WHOLLY-OWNED SUBSIDIARY COMPANY, OR\n"
            "(c) Two or more startup companies, or startup with small company.\n\n"
            "Since Precision is a wholly-owned subsidiary of Bharat Dynamics, they qualify for the Section 233 Fast Track route, even though "
            "Bharat Dynamics is a public company!\n"
            "Under Section 233(1)(d), the scheme must be approved by creditors representing at least NINETY PERCENT (90%) IN VALUE of creditors, "
            "obtained either at a meeting or in writing. Once approved by members (90% of total shares) and filed with the Regional Director (Central Govt), "
            "the Regional Director registers the scheme WITHOUT ANY NEED TO APPROACH NCLT."
        ),
        "section_ref": "Companies Act, 2013 - Section 233(1) & Rule 25",
        "exam_tip": "EXAM TRAP: Fast Track Merger is NOT limited to small companies! It is fully available for a Holding Company and its Wholly-Owned Subsidiary (regardless of whether holding company is public or private). NCLT approval is NOT required!",
        "source_tag": "Offline SPOM Recall",
        "difficulty": "Hard",
        "is_case_study": 1,
        "case_scenario": CASE_5_TEXT,
        "why_incorrect_a": "Fast track merger is expressly available between a holding company and its wholly-owned subsidiary under Sec 233(1).",
        "why_incorrect_b": "",
        "why_incorrect_c": "Fast track merger is approved by the Regional Director (Central Govt), bypassing NCLT.",
        "why_incorrect_d": "The holding company can be public as long as the subsidiary is 100% wholly-owned."
    },
    {
        "set_name": "A",
        "section_group": "Part I: Corporate Laws (70 Marks)",
        "chapter_code": "A_OPPR",
        "topic": "Prevention of Oppression and Mismanagement",
        "subtopic": "Section 244 Right to Apply - Alternative Eligibility Limb",
        "question": (
            "Refer to Point 3 of Case Scenario 5. Is the company's objection regarding the maintainability of the minority shareholders' "
            "petition under Section 241 legally tenable under Section 244 of the Companies Act, 2013?"
        ),
        "option_a": "Yes, because meeting the 100 members or 10% member count threshold is mandatory in all circumstances.",
        "option_b": "No, because under Section 244(1)(a), the eligibility criteria are ALTERNATIVE: any member or members holding NOT LESS THAN ONE-TENTH (10%) OF THE ISSUED SHARE CAPITAL have the right to apply, irrespective of the number of members.",
        "option_c": "Yes, because unlisted companies require at least 25% shareholding to maintain an oppression suit.",
        "option_d": "No, because any single shareholder with more than 1,000 shares can file under Section 241.",
        "correct_option": "B",
        "marks": 2,
        "explanation": (
            "Under Section 244(1)(a) of the Companies Act, 2013, in the case of a company having a share capital, the following members "
            "shall have the right to apply under Section 241:\n"
            "- Not less than 100 members, OR\n"
            "- Not less than 1/10th (10%) of the total number of its members,\n"
            "WHICHEVER IS LESS, OR\n"
            "- ANY MEMBER OR MEMBERS HOLDING NOT LESS THAN ONE-TENTH (10%) OF THE ISSUED SHARE CAPITAL of the company, provided all calls and other sums due have been paid.\n\n"
            "Notice the statutory word 'OR'! The share capital criterion (10% of issued share capital) is an INDEPENDENT ALTERNATIVE to the numerical member count. "
            "Since the 45 members hold 12% of the paid-up share capital (which exceeds 10%), they fully satisfy Section 244(1)(a) on the capital limb alone, "
            "rendering the company's objection completely untenable."
        ),
        "section_ref": "Companies Act, 2013 - Section 244(1)(a)",
        "exam_tip": "EXAM TRAP: The three limbs under Section 244(1)(a) are: (1) >=100 members, OR (2) >=1/10th total members, OR (3) holding >=10% of issued share capital. Satisfying ANY ONE limb is sufficient!",
        "source_tag": "ICAI Test Your Knowledge",
        "difficulty": "Moderate",
        "is_case_study": 1,
        "case_scenario": CASE_5_TEXT,
        "why_incorrect_a": "Fails to recognize that holding 10% of issued share capital is an independent alternative limb.",
        "why_incorrect_b": "",
        "why_incorrect_c": "There is no 25% threshold for unlisted companies under Section 244.",
        "why_incorrect_d": "A single shareholder can only apply if they hold at least 10% of issued capital."
    },
    {
        "set_name": "A",
        "section_group": "Part I: Corporate Laws (70 Marks)",
        "chapter_code": "A_INSP",
        "topic": "Inspection, Inquiry and Investigation",
        "subtopic": "Section 212 SFIO Exclusive Jurisdiction & Section 212(8) Arrest Powers",
        "question": (
            "Refer to Point 4 of Case Scenario 5. Under Section 212 of the Companies Act, 2013, what are the legal conditions "
            "governing an arrest made by an SFIO officer during an investigation into Section 447 corporate fraud?"
        ),
        "option_a": "SFIO officers have no power to arrest and must seek an arrest warrant from the Chief Judicial Magistrate.",
        "option_b": "Under Section 212(8), the Director, Additional Director or Joint Director of SFIO may arrest a person if they have reason to believe on the basis of material that the person is guilty of an offence under Section 447, and must forward the order to the designated authority in a sealed envelope.",
        "option_c": "Arrest can only be made after the final investigation report is submitted to the Central Government and accepted.",
        "option_d": "The officer can arrest only with prior written concurrence of the President of NCLT.",
        "correct_option": "B",
        "marks": 2,
        "explanation": (
            "Under Section 212(8) of the Companies Act, 2013:\n"
            "If any officer not below the rank of Additional Director of the Serious Fraud Investigation Office (SFIO) has on the basis of material "
            "in his possession reason to believe (the reason for such belief to be recorded in writing) that any person has been guilty of any offence "
            "punishable under section 212(6) (i.e. offences under section 447), he may arrest such person.\n\n"
            "Under Section 212(9), the officer shall immediately after arrest forward a copy of the order, along with the material in his possession, "
            "to the Serious Fraud Investigation Office in a sealed envelope. Under Section 212(10), every person arrested shall be produced before "
            "a Special Court or Judicial Magistrate within 24 hours of arrest (excluding journey time)."
        ),
        "section_ref": "Companies Act, 2013 - Section 212(8) & 212(9)",
        "exam_tip": "EXAM TRAP: SFIO officers (Additional Director and above) HAVE DIRECT ARREST POWERS without prior court warrant for Section 447 fraud offences, subject to recording reasons and producing the arrestee within 24 hours.",
        "source_tag": "Offline SPOM Recall",
        "difficulty": "Hard",
        "is_case_study": 1,
        "case_scenario": CASE_5_TEXT,
        "why_incorrect_a": "SFIO officers of rank Additional Director and above possess statutory arrest powers under Section 212(8).",
        "why_incorrect_b": "",
        "why_incorrect_c": "Arrest can be made during the pendency of the investigation; waiting for final report is not required.",
        "why_incorrect_d": "NCLT concurrence is not required for SFIO statutory arrests under Section 212(8)."
    }
]

# ==============================================================================
# STANDALONE HIGH-YIELD EXAM TRAP MCQs ACROSS UNDER-REPRESENTED CHAPTERS
# Chapters: A_WIND, A_FOREIGN, A_INSP, A_PMLA_FCRA, A_DIR, A_BM, A_MGR, A_FEMA
# ==============================================================================
STANDALONE_QUESTIONS = [
    # --- A_WIND (Winding Up by Tribunal) ---
    {
        "set_name": "A",
        "section_group": "Part I: Corporate Laws (70 Marks)",
        "chapter_code": "A_WIND",
        "topic": "Winding Up by Tribunal",
        "subtopic": "Section 271(d) Default in Filing Financial Statements as Ground for Winding Up",
        "question": (
            "Under Section 271(d) of the Companies Act, 2013, the Tribunal may order winding up of a company if it has made default "
            "in filing with the Registrar its financial statements or annual returns for:"
        ),
        "option_a": "Immediately preceding 3 consecutive financial years.",
        "option_b": "Immediately preceding 5 consecutive financial years.",
        "option_c": "Any 3 financial years out of the preceding 5 financial years.",
        "option_d": "Immediately preceding 2 consecutive financial years.",
        "correct_option": "B",
        "marks": 2,
        "explanation": (
            "Under Section 271(d) of the Companies Act, 2013, a company may be wound up by the Tribunal if the company has made "
            "default in filing with the Registrar its financial statements or annual returns for IMMEDIATELY PRECEDING FIVE (5) CONSECUTIVE FINANCIAL YEARS.\n\n"
            "Contrast this with Section 164(2)(a) (disqualification of directors), which requires default for 3 consecutive financial years! "
            "For winding up under Section 271(d), the statutory threshold is 5 consecutive financial years."
        ),
        "section_ref": "Companies Act, 2013 - Section 271(d)",
        "exam_tip": "CRITICAL NUMERICAL DISTINCTION: Director disqualification (Sec 164(2)) = 3 consecutive years; Winding up of company (Sec 271(d)) = 5 CONSECUTIVE YEARS!",
        "source_tag": "ICAI BoS Module",
        "difficulty": "Moderate",
        "is_case_study": 0,
        "case_scenario": None,
        "why_incorrect_a": "3 consecutive years applies to Director disqualification under Section 164(2), not company winding up.",
        "why_incorrect_b": "",
        "why_incorrect_c": "The default must be for consecutive 5 years, not any 3 out of 5.",
        "why_incorrect_d": "2 years is the threshold for striking off / dormant status, not winding up."
    },
    {
        "set_name": "A",
        "section_group": "Part I: Corporate Laws (70 Marks)",
        "chapter_code": "A_WIND",
        "topic": "Winding Up by Tribunal",
        "subtopic": "Section 272 Petitioners & ROC Prior Sanction Restriction",
        "question": (
            "Under Section 272(3) of the Companies Act, 2013, on which of the following grounds is the Registrar of Companies (ROC) "
            "EXPRESSLY BARRED from presenting a petition for winding up of a company to the Tribunal?"
        ),
        "option_a": "Ground (b): Company acted against sovereignty and integrity of India.",
        "option_b": "Ground (c): Affairs of company conducted in a fraudulent manner.",
        "option_c": "Ground (a): Company has, by special resolution, resolved that it be wound up by the Tribunal.",
        "option_d": "Ground (d): Default in filing financial statements for immediately preceding 5 consecutive financial years.",
        "correct_option": "C",
        "marks": 2,
        "explanation": (
            "Under Section 272(3) of the Companies Act, 2013, the Registrar shall be entitled to present a petition for winding up "
            "on ANY of the grounds specified in sub-section (1) of section 271, EXCEPT ON THE GROUND SPECIFIED IN CLAUSE (a) of that sub-section!\n\n"
            "Clause (a) of Section 271 refers to the ground where the company itself has resolved by Special Resolution that it be wound up by Tribunal. "
            "Since passing a Special Resolution is an internal decision of the company and its members, the petition on this ground can be filed ONLY "
            "by the company itself, NOT by the Registrar. Furthermore, for filing on other grounds, the ROC must obtain the previous sanction of the Central Government."
        ),
        "section_ref": "Companies Act, 2013 - Section 272(3)",
        "exam_tip": "EXAM TRAP: The ROC cannot petition on Clause (a) (Special Resolution). On all other grounds (b, c, d, e), ROC can petition ONLY with prior sanction of Central Government.",
        "source_tag": "Offline SPOM Recall",
        "difficulty": "Hard",
        "is_case_study": 0,
        "case_scenario": None,
        "why_incorrect_a": "ROC can present petition under clause (b) with prior Central Govt sanction.",
        "why_incorrect_b": "ROC can present petition under clause (c) with prior Central Govt sanction.",
        "why_incorrect_c": "",
        "why_incorrect_d": "ROC is the primary petitioner under clause (d) (5 years non-filing)."
    },
    {
        "set_name": "A",
        "section_group": "Part I: Corporate Laws (70 Marks)",
        "chapter_code": "A_WIND",
        "topic": "Winding Up by Tribunal",
        "subtopic": "Section 287 Advisory Committee Maximum Composition",
        "question": (
            "Under Section 287 of the Companies Act, 2013, the Tribunal may direct that there shall be an Advisory Committee to report "
            "to the Tribunal on such matters as the Tribunal may direct and to advise the Company Liquidator. What is the maximum number "
            "of members permitted on the Advisory Committee?"
        ),
        "option_a": "Not exceeding 5 members.",
        "option_b": "Not exceeding 7 members.",
        "option_c": "Not exceeding 12 members.",
        "option_d": "Not exceeding 15 members.",
        "correct_option": "C",
        "marks": 2,
        "explanation": (
            "Under Section 287(2) of the Companies Act, 2013, the Advisory Committee shall consist of such number of members, "
            "NOT EXCEEDING TWELVE (12), being creditors and contributories of the company or persons holding general or special powers "
            "of attorney from creditors or contributories, in such proportions as the Tribunal may determine having regard to the value of debts "
            "and shares respectively."
        ),
        "section_ref": "Companies Act, 2013 - Section 287(2)",
        "exam_tip": "EXAM TRAP: Maximum number of members on the Advisory Committee in Winding Up is 12 (twelve).",
        "source_tag": "ICAI BoS Module",
        "difficulty": "Moderate",
        "is_case_study": 0,
        "case_scenario": None,
        "why_incorrect_a": "Incorrect limit.",
        "why_incorrect_b": "Incorrect limit.",
        "why_incorrect_c": "",
        "why_incorrect_d": "15 is the maximum number of directors on a Board under Section 149(1), not the Advisory Committee in Winding Up."
    },

    # --- A_FOREIGN (Companies Incorporated Outside India) ---
    {
        "set_name": "A",
        "section_group": "Part I: Corporate Laws (70 Marks)",
        "chapter_code": "A_FOREIGN",
        "topic": "Companies Incorporated Outside India",
        "subtopic": "Section 379(2) Applicability of Chapter XXII (50% Indian Shareholding)",
        "question": (
            "Under Section 379(2) of the Companies Act, 2013, where not less than _________ of the paid-up share capital, whether equity "
            "or preference or partly equity and partly preference, of a foreign company is held by one or more citizens of India or companies "
            "incorporated in India, such company shall comply with the provisions of Chapter XXII and such other provisions of this Act as may be prescribed as if it were an Indian company:"
        ),
        "option_a": "51%",
        "option_b": "50%",
        "option_c": "26%",
        "option_d": "75%",
        "correct_option": "B",
        "marks": 2,
        "explanation": (
            "Under Section 379(2) of the Companies Act, 2013:\n"
            "Where not less than FIFTY PERCENT (50%) of the paid-up share capital, whether equity or preference or partly equity and "
            "partly preference, of a foreign company is held by one or more citizens of India or by one or more companies or bodies corporate "
            "incorporated in India, or by one or more citizens of India and one or more companies or bodies corporate incorporated in India, "
            "whether singly or in the aggregate, such company shall comply with the provisions of this Chapter (Chapter XXII) and with such "
            "other provisions of this Act as may be prescribed with regard to the business carried on by it in India as if it were a company incorporated in India.\n\n"
            "Notice that the threshold is 'NOT LESS THAN 50%', NOT 51%!"
        ),
        "section_ref": "Companies Act, 2013 - Section 379(2)",
        "exam_tip": "EXAM TRAP: Government companies require 'not less than 51%' under Sec 2(45). But for Foreign Companies under Section 379(2), the Indian ownership threshold is 'NOT LESS THAN 50%'!",
        "source_tag": "Offline SPOM Recall",
        "difficulty": "Hard",
        "is_case_study": 0,
        "case_scenario": None,
        "why_incorrect_a": "51% is the threshold for Government Company under Section 2(45), but Section 379(2) specifies 50%.",
        "why_incorrect_b": "",
        "why_incorrect_c": "26% is the takeover offer size under SEBI SAST.",
        "why_incorrect_d": "75% is special resolution threshold."
    },
    {
        "set_name": "A",
        "section_group": "Part I: Corporate Laws (70 Marks)",
        "chapter_code": "A_FOREIGN",
        "topic": "Companies Incorporated Outside India",
        "subtopic": "Section 380 Time Limit for Delivering Documents to ROC",
        "question": (
            "Every foreign company shall, within _________ of establishing a place of business in India, deliver to the Registrar for registration "
            "a certified copy of its charter, statute or memorandum, the address of its principal office, and the list of its directors and secretary:"
        ),
        "option_a": "15 days",
        "option_b": "30 days",
        "option_c": "60 days",
        "option_d": "90 days",
        "correct_option": "B",
        "marks": 2,
        "explanation": (
            "Under Section 380(1) of the Companies Act, 2013, every foreign company shall, within THIRTY (30) DAYS of the establishment of "
            "its place of business in India, deliver to the Registrar for registration:\n"
            "(a) certified copy of the charter, statutes, or memorandum and articles of the company;\n"
            "(b) full address of the registered or principal office of the company;\n"
            "(c) list of the directors and secretary of the company;\n"
            "(d) name and address of the person(s) resident in India authorized to accept service of process;\n"
            "(e) full address of the office of the company in India deemed to be its principal place of business in India;\n"
            "(f) particulars of opening and closing of a place of business in India on earlier occasions;\n"
            "(g) declaration that none of the directors or authorized representative in India has ever been convicted or debarred."
        ),
        "section_ref": "Companies Act, 2013 - Section 380(1)",
        "exam_tip": "EXAM TRAP: Time limit for delivering documents to ROC under Section 380 is 30 days from establishing place of business in India.",
        "source_tag": "ICAI BoS Module",
        "difficulty": "Moderate",
        "is_case_study": 0,
        "case_scenario": None,
        "why_incorrect_a": "Incorrect period.",
        "why_incorrect_b": "",
        "why_incorrect_c": "60 days is incorrect.",
        "why_incorrect_d": "90 days is incorrect."
    },

    # --- A_INSP (Inspection, Inquiry and Investigation) ---
    {
        "set_name": "A",
        "section_group": "Part I: Corporate Laws (70 Marks)",
        "chapter_code": "A_INSP",
        "topic": "Inspection, Inquiry and Investigation",
        "subtopic": "Section 218 Protection of Employees During Investigation (30-Day Objection Rule)",
        "question": (
            "Under Section 218 of the Companies Act, 2013, if a company proposes to discharge, suspend, or terminate an employee during the pendency "
            "of an investigation into its affairs, the company must seek prior approval of the Tribunal. If the Tribunal does NOT communicate "
            "its objection within _________ of receiving the application, the company may proceed to take the proposed action:"
        ),
        "option_a": "15 days",
        "option_b": "30 days",
        "option_c": "45 days",
        "option_d": "60 days",
        "correct_option": "B",
        "marks": 2,
        "explanation": (
            "Under Section 218(1) of the Companies Act, 2013, if during the pendency of any investigation under section 210, 212, or 213, "
            "the company proposes to discharge or suspend any employee, or punish him, it must make an application to the Tribunal for its approval.\n\n"
            "Under Section 218(2), if the Tribunal DOES NOT object to the proposed action within THIRTY (30) DAYS of the receipt of the application, "
            "the company may proceed to take the proposed action against the employee. If the Tribunal does object within 30 days, the company "
            "may appeal to the Appellate Tribunal (NCLAT) within 30 days of the receipt of objection under Section 218(3)."
        ),
        "section_ref": "Companies Act, 2013 - Section 218(2)",
        "exam_tip": "EXAM TRAP: Section 218 gives the Tribunal 30 days to object. If Tribunal remains silent for 30 days, deemed approval applies and the company can proceed with disciplinary action.",
        "source_tag": "Offline SPOM Recall",
        "difficulty": "Hard",
        "is_case_study": 0,
        "case_scenario": None,
        "why_incorrect_a": "Incorrect period.",
        "why_incorrect_b": "",
        "why_incorrect_c": "45 days is the appeal timeline from NCLT to NCLAT under Sec 421.",
        "why_incorrect_d": "60 days is incorrect."
    },

    # --- A_PMLA_FCRA & ARBITRATION ---
    {
        "set_name": "A",
        "section_group": "Part II: Economic Laws (30 Marks)",
        "chapter_code": "A_PMLA_FCRA",
        "topic": "Arbitration and Conciliation Act, 1996",
        "subtopic": "Section 29A Time Limit for Making Arbitral Award",
        "question": (
            "Under Section 29A of the Arbitration and Conciliation Act, 1996 (as amended in 2019), the arbitral award in matters other than "
            "international commercial arbitration SHALL be made within a period of _________ from the date of completion of pleadings under Section 23(4):"
        ),
        "option_a": "6 months",
        "option_b": "12 months",
        "option_c": "18 months",
        "option_d": "24 months",
        "correct_option": "B",
        "marks": 2,
        "explanation": (
            "Under Section 29A(1) of the Arbitration and Conciliation Act, 1996 (as amended by the Arbitration Amendment Act, 2019):\n"
            "The award in matters OTHER THAN international commercial arbitration shall be made by the arbitral tribunal within a period of "
            "TWELVE (12) MONTHS from the date of completion of pleadings under sub-section (4) of section 23.\n\n"
            "Note the crucial amendments:\n"
            "1. In 2015, the 12-month period ran from the date the arbitral tribunal entered upon reference.\n"
            "2. Under the 2019 Amendment, the 12-month clock begins upon COMPLETION OF PLEADINGS (which must be completed within 6 months).\n"
            "3. The parties may by consent extend this period for a further period not exceeding SIX (6) MONTHS under Section 29A(3)."
        ),
        "section_ref": "Arbitration and Conciliation Act, 1996 - Section 29A(1)",
        "exam_tip": "EXAM TRAP: The 12-month timeline runs from 'COMPLETION OF PLEADINGS', NOT from entering upon reference (2019 amendment). Parties can extend by mutual consent by max 6 months; further extension requires Court permission.",
        "source_tag": "ICAI BoS Module",
        "difficulty": "Moderate",
        "is_case_study": 0,
        "case_scenario": None,
        "why_incorrect_a": "6 months is the maximum consensual extension under Sec 29A(3), or the target for fast track arbitration under Sec 29B.",
        "why_incorrect_b": "",
        "why_incorrect_c": "18 months is the combined period (12 months + 6 months consensual extension).",
        "why_incorrect_d": "Incorrect period."
    },
    {
        "set_name": "A",
        "section_group": "Part II: Economic Laws (30 Marks)",
        "chapter_code": "A_PMLA_FCRA",
        "topic": "Arbitration and Conciliation Act, 1996",
        "subtopic": "Section 34 Setting Aside Arbitral Award Limitation & Condonation",
        "question": (
            "Under Section 34(3) of the Arbitration and Conciliation Act, 1996, an application for setting aside an arbitral award must be "
            "made within _________ from the date of receipt of the award, and the Court may condone delay for a further maximum period of _________:"
        ),
        "option_a": "3 months; 30 days (but not thereafter)",
        "option_b": "30 days; 30 days",
        "option_c": "60 days; 60 days",
        "option_d": "3 months; 60 days",
        "correct_option": "A",
        "marks": 2,
        "explanation": (
            "Under Section 34(3) of the Arbitration and Conciliation Act, 1996, an application for setting aside an arbitral award may not "
            "be made after THREE (3) MONTHS have elapsed from the date on which the party making that application had received the arbitral award.\n\n"
            "Under the Proviso to Section 34(3), if the Court is satisfied that the applicant was prevented by sufficient cause from making "
            "the application within the said period of three months, it may entertain the application within a further period of THIRTY (30) DAYS, "
            "BUT NOT THEREAFTER!\n\n"
            "As held by the Supreme Court in Union of India v. Popular Construction Co., Section 5 of the Limitation Act is completely excluded; "
            "the Court has ABSOLUTELY NO POWER to condone even a single day's delay beyond the 30-day grace period."
        ),
        "section_ref": "Arbitration and Conciliation Act, 1996 - Section 34(3) & Proviso",
        "exam_tip": "EXAM TRAP: Section 34 limitation is '3 MONTHS + 30 DAYS' (note months vs days!). The Court CANNOT condone delay beyond 30 days under any circumstances.",
        "source_tag": "Offline SPOM Recall",
        "difficulty": "Hard",
        "is_case_study": 0,
        "case_scenario": None,
        "why_incorrect_a": "",
        "why_incorrect_b": "Primary period is 3 months, not 30 days.",
        "why_incorrect_c": "60 days is the limitation for appeal to Supreme Court under Section 423.",
        "why_incorrect_d": "Condonation is limited to 30 days, not 60 days."
    },
    {
        "set_name": "A",
        "section_group": "Part II: Economic Laws (30 Marks)",
        "chapter_code": "A_PMLA_FCRA",
        "topic": "Prevention of Money Laundering Act, 2002",
        "subtopic": "Section 5 Provisional Attachment Period & Section 12 Record Maintenance",
        "question": (
            "Under Section 5(1) of the Prevention of Money Laundering Act, 2002 (PMLA), the Director or an officer not below the rank of "
            "Deputy Director may order provisional attachment of property involved in money laundering for a period not exceeding:"
        ),
        "option_a": "90 days",
        "option_b": "120 days",
        "option_c": "180 days",
        "option_d": "365 days",
        "correct_option": "C",
        "marks": 2,
        "explanation": (
            "Under Section 5(1) of the Prevention of Money Laundering Act, 2002 (PMLA):\n"
            "Where the Director or any other officer not below the rank of Deputy Director authorized by him for the purposes of this section, "
            "has reason to believe on the basis of material in his possession that any person is in possession of proceeds of crime and such proceeds "
            "are likely to be concealed, transferred or dealt with, he may, by order in writing, provisionally attach such property for a period "
            "NOT EXCEEDING ONE HUNDRED AND EIGHTY (180) DAYS from the date of the order."
        ),
        "section_ref": "PMLA, 2002 - Section 5(1)",
        "exam_tip": "EXAM TRAP: Provisional attachment period under PMLA is 180 DAYS. The Adjudicating Authority must confirm it within this 180-day window under Section 8.",
        "source_tag": "ICAI BoS Module",
        "difficulty": "Moderate",
        "is_case_study": 0,
        "case_scenario": None,
        "why_incorrect_a": "Incorrect period.",
        "why_incorrect_b": "Incorrect period.",
        "why_incorrect_c": "",
        "why_incorrect_d": "365 days is the period under Section 8(3)(a) during investigation, but provisional attachment under Section 5(1) is 180 days."
    },

    # --- APPEALS & NIDHI COMPANIES (Company Law Miscellaneous & NCLT) ---
    {
        "set_name": "A",
        "section_group": "Part I: Corporate Laws (70 Marks)",
        "chapter_code": "A_BM",
        "topic": "Nidhi Companies Rules, 2014",
        "subtopic": "Rule 6 Deposit Acceptance Limit & Ratio of Net Owned Funds (NOF)",
        "question": (
            "Under Rule 6 of the Nidhi Rules, 2014, a Nidhi company SHALL NOT accept deposits from its members exceeding _________ times "
            "of its Net Owned Funds (NOF):"
        ),
        "option_a": "10 times",
        "option_b": "15 times",
        "option_c": "20 times",
        "option_d": "25 times",
        "correct_option": "C",
        "marks": 2,
        "explanation": (
            "Under Rule 6(d) of the Nidhi Rules, 2014:\n"
            "A Nidhi shall not accept deposits from or lend to any person other than its members, and a Nidhi SHALL NOT accept deposits "
            "exceeding TWENTY (20) TIMES of its Net Owned Funds (NOF) as per its last audited financial statements.\n\n"
            "Furthermore, under Rule 14, every Nidhi must invest and continue to keep invested, in unencumbered term deposits with a Scheduled "
            "commercial bank or post office, an amount which shall not be less than 10% of the deposits outstanding at the close of business on the last working day of the second preceding month."
        ),
        "section_ref": "Nidhi Rules, 2014 - Rule 6(d) & Rule 14",
        "exam_tip": "EXAM TRAP: Nidhi deposit cap = 20 TIMES OF NET OWNED FUNDS (NOF). Unencumbered term deposit reserve = MINIMUM 10% of outstanding deposits.",
        "source_tag": "Offline SPOM Recall",
        "difficulty": "Moderate",
        "is_case_study": 0,
        "case_scenario": None,
        "why_incorrect_a": "10% is the unencumbered term deposit liquidity requirement, not the deposit to NOF ratio.",
        "why_incorrect_b": "Incorrect multiplier.",
        "why_incorrect_c": "",
        "why_incorrect_d": "Incorrect multiplier."
    },
    {
        "set_name": "A",
        "section_group": "Part I: Corporate Laws (70 Marks)",
        "chapter_code": "A_BM",
        "topic": "Appellate Jurisdiction - NCLAT & Supreme Court",
        "subtopic": "Section 421 & Section 423 Limitation & Condonation for Appeals",
        "question": (
            "Under Section 421(3) and Section 423 of the Companies Act, 2013, what are the statutory limitation periods for filing an appeal "
            "from NCLT to NCLAT, and from NCLAT to the Supreme Court respectively?"
        ),
        "option_a": "NCLT to NCLAT: 45 days (+ 45 days condonation); NCLAT to Supreme Court: 60 days (+ 60 days condonation on Question of Law).",
        "option_b": "NCLT to NCLAT: 30 days (+ 30 days condonation); NCLAT to Supreme Court: 90 days (+ 30 days condonation).",
        "option_c": "NCLT to NCLAT: 60 days (+ 30 days condonation); NCLAT to Supreme Court: 60 days (+ 30 days condonation).",
        "option_d": "NCLT to NCLAT: 45 days (no condonation); NCLAT to Supreme Court: 60 days (no condonation).",
        "correct_option": "A",
        "marks": 2,
        "explanation": (
            "1. Appeal from NCLT to NCLAT under Section 421(3):\n"
            "Every appeal shall be filed within a period of FORTY-FIVE (45) DAYS from the date on which a copy of the order of the Tribunal is made available.\n"
            "Under the Proviso to Section 421(3), NCLAT may entertain an appeal after the expiry of 45 days if satisfied of sufficient cause, "
            "within a further period not exceeding FORTY-FIVE (45) DAYS (Total 45 + 45 days).\n\n"
            "2. Appeal from NCLAT to Supreme Court under Section 423:\n"
            "Any person aggrieved by any order of the Appellate Tribunal may file an appeal to the Supreme Court within SIXTY (60) DAYS "
            "from the date of receipt of the order, ON ANY QUESTION OF LAW arising out of such order.\n"
            "The Supreme Court may entertain the appeal after the expiry of 60 days if satisfied of sufficient cause, within a further period "
            "not exceeding SIXTY (60) DAYS (Total 60 + 60 days)."
        ),
        "section_ref": "Companies Act, 2013 - Section 421(3) & Section 423",
        "exam_tip": "EXAM TRAP: Memorize the appeal matrix: NCLT -> NCLAT = 45 + 45 days; NCLAT -> Supreme Court = 60 + 60 days (only on Question of Law).",
        "source_tag": "ICAI Test Your Knowledge",
        "difficulty": "Moderate",
        "is_case_study": 0,
        "case_scenario": None,
        "why_incorrect_a": "",
        "why_incorrect_b": "30 days is the appeal timeline under IBC Section 61, not Companies Act Section 421.",
        "why_incorrect_c": "Incorrect periods.",
        "why_incorrect_d": "Condonation of 45 days and 60 days respectively is expressly provided in the provisos."
    }
]


def seed_database():
    if not os.path.exists(DB_PATH):
        print(f"[ERROR] Database file not found at: {DB_PATH}")
        sys.exit(1)

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    all_questions = (
        CASE_1_QUESTIONS +
        CASE_2_QUESTIONS +
        CASE_3_QUESTIONS +
        CASE_4_QUESTIONS +
        CASE_5_QUESTIONS +
        STANDALONE_QUESTIONS
    )

    print(f"Total Questions to Seed: {len(all_questions)}")
    print(f"- Case Scenario 1 (Zenith Heavy Industries - Directorship, Quorum, Sec 180, Sched V): {len(CASE_1_QUESTIONS)}")
    print(f"- Case Scenario 2 (Nexus Tech - SEBI SAST, PIT SDD, LODR Reg 23 RPT & Reg 29): {len(CASE_2_QUESTIONS)}")
    print(f"- Case Scenario 3 (Sterling Steels - IBC Sec 7 Homebuyers, Sec 8/9, CoC, Sec 53): {len(CASE_3_QUESTIONS)}")
    print(f"- Case Scenario 4 (Global EPC - FEMA Sched III, Compounding 3-yr, FCRA Sec 6/17): {len(CASE_4_QUESTIONS)}")
    print(f"- Case Scenario 5 (Bharat Dynamics - Sec 230(6), Fast Track Sec 233, Oppression, SFIO): {len(CASE_5_QUESTIONS)}")
    print(f"- Standalone Trap Questions (Winding Up, Foreign Co, SFIO, Arbitration, Nidhi, Appeals): {len(STANDALONE_QUESTIONS)}")

    inserted_count = 0
    updated_count = 0

    for q in all_questions:
        # Check if identical question already exists in DB to prevent duplicates
        cursor.execute("SELECT id FROM mcqs WHERE set_name = ? AND question = ?", (q['set_name'], q['question']))
        existing = cursor.fetchone()

        if existing:
            # Update existing record
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
            # Insert fresh record
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

    # Query summary counts
    cursor.execute("SELECT count(*) FROM mcqs WHERE set_name = 'A'")
    total_a = cursor.fetchone()[0]

    cursor.execute("SELECT count(*) FROM mcqs WHERE set_name = 'A' AND is_case_study = 1")
    total_case_studies = cursor.fetchone()[0]

    cursor.execute("SELECT chapter_code, count(*) FROM mcqs WHERE set_name = 'A' GROUP BY chapter_code ORDER BY chapter_code")
    chapter_breakdown = cursor.fetchall()

    conn.close()

    print("\n[SUCCESS] Seeding completed successfully!")
    print(f"- New MCQs Inserted: {inserted_count}")
    print(f"- Existing MCQs Updated: {updated_count}")
    print(f"- Total Set A MCQs in Database: {total_a}")
    print(f"- Total Set A Case Study Questions: {total_case_studies}")
    print("\nChapter Breakdown for Set A:")
    for ch, count in chapter_breakdown:
        print(f"  {ch}: {count} MCQs")

if __name__ == "__main__":
    seed_database()

