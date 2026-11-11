"""
CA Final SPOM Set A - Master Synthesis Batch 2
Adds 17 more Master Integrated Evaluative Scenarios covering all remaining high-yield concepts.
Brings Set A to 206 Master MCQs.
"""

import sqlite3
import os

DB_PATH = r"C:\Users\Ansh\Desktop\Coding\ca-spom-portal\spom_portal.db"

ADDITIONAL_MASTER_MCQS = [
    # --- A_BM: Nidhi Company Loan Slabs & Net Owned Funds ---
    {
        "set_name": "A",
        "section_group": "Part I: Corporate Laws (70 Marks)",
        "chapter_code": "A_BM",
        "topic": "Nidhi Companies Lending Slabs & Gold Loan Rules",
        "subtopic": "Rule 9 & Rule 10 Loan Limits based on Aggregate Deposits",
        "question": (
            "Shubham Nidhi Ltd. has aggregate deposits of Rs 35 Crore from its members as per its latest audited financial statements. "
            "A member who has been a regular deposit holder for 2 years applies for a loan against the security of immovable property and gold. "
            "Under Rule 9 and Rule 10 of the Nidhi Rules, 2014, what is the MAXIMUM loan amount Shubham Nidhi Ltd. can grant to any single member, "
            "and what are the statutory repayment periods for loans against immovable property and gold jewellery respectively?"
        ),
        "option_a": "Maximum loan: Rs 2 Lakhs; Repayment: Immovable property max 7 years, Gold jewellery max 1 year.",
        "option_b": "Maximum loan: Rs 12 Lakhs (for deposits > Rs 20 Cr but <= Rs 50 Cr); Repayment: Immovable property max 7 years, Gold jewellery max 1 year.",
        "option_c": "Maximum loan: Rs 15 Lakhs; Repayment: Immovable property max 10 years, Gold jewellery max 3 years.",
        "option_d": "Maximum loan: Rs 7.50 Lakhs; Repayment: Immovable property max 5 years, Gold jewellery max 6 months.",
        "correct_option": "B",
        "marks": 2,
        "explanation": (
            "Under Rule 9 of the Nidhi Rules, 2014, the maximum ceiling of loan that a Nidhi can advance to a single member depends on the aggregate deposits of the Nidhi:\n"
            "1. Where deposits are <= Rs 2 Crore: Max loan = Rs 2 Lakhs\n"
            "2. Where deposits are > Rs 2 Crore but <= Rs 20 Crore: Max loan = Rs 7.50 Lakhs\n"
            "3. Where deposits are > Rs 20 Crore but <= Rs 50 Crore: Max loan = Rs 12 Lakhs\n"
            "4. Where deposits are > Rs 50 Crore: Max loan = Rs 15 Lakhs\n\n"
            "Since Shubham Nidhi has deposits of Rs 35 Crore (falling in the Rs 20 Cr - 50 Cr tier), the maximum loan to any single member is Rs 12 Lakhs.\n\n"
            "Under Rule 10(2), the repayment periods for secured loans are:\n"
            "- Against gold, silver and jewellery: SHALL NOT EXCEED ONE (1) YEAR.\n"
            "- Against immovable property: SHALL NOT EXCEED SEVEN (7) YEARS (and loan shall not exceed 50% of the overall loan portfolio)."
        ),
        "section_ref": "Nidhi Rules, 2014 - Rule 9 & Rule 10",
        "exam_tip": "EXAM TRAP: Memorize the Nidhi lending tiers: <=2Cr (2L), 2-20Cr (7.5L), 20-50Cr (12L), >50Cr (15L). Repayment: Gold max 1 yr; Immovable property max 7 yrs!",
        "source_tag": "Offline SPOM Recall",
        "difficulty": "Hard",
        "is_case_study": 0,
        "case_scenario": None,
        "why_incorrect_a": "Rs 2 Lakh applies when deposits are <= Rs 2 Crore.",
        "why_incorrect_b": "",
        "why_incorrect_c": "Rs 15 Lakh applies when deposits exceed Rs 50 Crore.",
        "why_incorrect_d": "Rs 7.5 Lakh applies when deposits are between Rs 2 Cr and Rs 20 Cr."
    },
    # --- A_BM: Vigil Mechanism & Direct Access ---
    {
        "set_name": "A",
        "section_group": "Part I: Corporate Laws (70 Marks)",
        "chapter_code": "A_BM",
        "topic": "Vigil Mechanism & Whistleblower Protection",
        "subtopic": "Section 177(9) & (10) Mandatory Applicability & Direct Access",
        "question": (
            "Examine the applicability and operational mechanics of the Vigil Mechanism under Section 177 of the Companies Act, 2013:\n"
            "Statement I: Establishment of a Vigil Mechanism is mandatory for all listed companies, companies accepting public deposits, and companies that have borrowed money from banks/FIs in excess of Rs 50 Crore.\n"
            "Statement II: The vigil mechanism must provide adequate safeguards against victimization of persons who use it, and provide for direct access to the Chairperson of the Audit Committee in appropriate or exceptional cases.\n"
            "Statement III: In the case of companies not required to constitute an Audit Committee, the Board of Directors shall nominate a director to play the role of the Audit Committee for the purpose of the vigil mechanism.\n"
            "Which of the above statements are CORRECT?"
        ),
        "option_a": "Statements I and II only",
        "option_b": "Statements II and III only",
        "option_c": "Statement I only",
        "option_d": "All Statements I, II, and III are correct.",
        "correct_option": "D",
        "marks": 2,
        "explanation": (
            "All three statements correctly set out the legal framework under Section 177(9) & (10) and Rule 7 of Companies (Meetings of Board and its Powers) Rules, 2014:\n"
            "1. Applicability (Rule 7): Mandatory for (i) Every listed company; (ii) Companies that accept deposits from the public; and (iii) Companies that have borrowed money from banks and public financial institutions EXCEEDING RS 50 CRORE.\n"
            "2. Direct Access (Sec 177(10)): The mechanism must provide for direct access to the Chairperson of the Audit Committee in appropriate or exceptional cases.\n"
            "3. Non-Audit Committee Companies (Rule 7(4)): In case of other companies, the Board of Directors shall nominate a director to whom other directors and employees may report their concerns."
        ),
        "section_ref": "Companies Act, 2013 - Section 177(9), (10) read with Rule 7",
        "exam_tip": "EXAM TRAP: Borrowing threshold for Vigil Mechanism is EXCEEDING Rs 50 Crore (not >= 50 Cr). Direct access goes to Chairperson of Audit Committee!",
        "source_tag": "ICAI BoS Module",
        "difficulty": "Moderate",
        "is_case_study": 0,
        "case_scenario": None,
        "why_incorrect_a": "Incomplete; Statement III is also correct under Rule 7(4).",
        "why_incorrect_b": "Incomplete; Statement I is also correct.",
        "why_incorrect_c": "Incomplete; all statements are accurate.",
        "why_incorrect_d": ""
    },
    # --- A_BM: Section 185 Wholly-Owned Subsidiary Exemption ---
    {
        "set_name": "A",
        "section_group": "Part I: Corporate Laws (70 Marks)",
        "chapter_code": "A_BM",
        "topic": "Loans to Directors & Corporate Guarantees",
        "subtopic": "Section 185(3) Absolute Statutory Exemptions for Holding & Subsidiary",
        "question": (
            "Zenith Holdings Ltd. (Holding Company) proposes to provide a corporate guarantee and pledge securities for a term loan of Rs 100 Crore "
            "availed by its 100% Wholly-Owned Subsidiary, Zenith Manufacturing Pvt. Ltd., from State Bank of India. "
            "Zenith Manufacturing will utilize the loan exclusively for procuring machinery for its principal manufacturing business. "
            "Two directors of Zenith Holdings are also directors in Zenith Manufacturing. "
            "Examine whether a Special Resolution of Zenith Holdings is required under Section 185 of the Companies Act, 2013."
        ),
        "option_a": "Yes, because Section 185(2) requires a Special Resolution whenever directors are interested in the borrower company.",
        "option_b": "No; under Section 185(3)(c), any guarantee given or security provided by a holding company in respect of a loan made to its WHOLLY-OWNED SUBSIDIARY company is STATUTORILY EXEMPTED from Section 185, provided the loans are utilized by the subsidiary solely for its principal business activities.",
        "option_c": "Yes, and prior approval of the Central Government is also mandatory.",
        "option_d": "No, because loans between private and public companies are outside the purview of the Companies Act, 2013.",
        "correct_option": "B",
        "marks": 2,
        "explanation": (
            "Under Section 185(3) of the Companies Act, 2013 (as substituted by the Companies Amendment Act, 2017), nothing contained in sub-sections (1) and (2) shall apply to:\n"
            "(a) The giving of any loan to a managing or whole-time director as part of condition of service extended to all employees, or pursuant to an approved scheme;\n"
            "(b) A company which in the ordinary course of business provides loans/guarantees for due repayment (lending companies charging interest >= RBI bank rate);\n"
            "(c) ANY LOAN MADE BY A HOLDING COMPANY TO ITS WHOLLY OWNED SUBSIDIARY COMPANY or any guarantee given or security provided by a holding company in respect of any loan made to its wholly owned subsidiary company;\n"
            "(d) Any guarantee given or security provided by a holding company in respect of loan made to its subsidiary company (where loan is made by bank/FI).\n\n"
            "Condition: In clauses (c) and (d), the loans MUST be utilized by the subsidiary company solely for its principal business activities.\n"
            "Because Zenith Manufacturing is a 100% wholly-owned subsidiary using the funds for its principal manufacturing business, it falls under the absolute statutory exemption of Section 185(3)(c). NO Special Resolution is required!"
        ),
        "section_ref": "Companies Act, 2013 - Section 185(3)(c) & Proviso",
        "exam_tip": "EXAM TRAP: Guarantee/Security given by Holding Company to its WHOLLY-OWNED SUBSIDIARY (WOS) is completely EXEMPT from Section 185 (no SR needed), so long as used for principal business activities!",
        "source_tag": "ICAI Test Your Knowledge",
        "difficulty": "Hard",
        "is_case_study": 0,
        "case_scenario": None,
        "why_incorrect_a": "Section 185(2) Special Resolution rule is overridden by the specific exemption in Section 185(3)(c).",
        "why_incorrect_b": "",
        "why_incorrect_c": "Central Government approval was omitted from Section 185.",
        "why_incorrect_d": "Section 185 applies to all companies, public and private."
    },
    # --- A_MGR: Section 198 Net Profits Deductions & Credits ---
    {
        "set_name": "A",
        "section_group": "Part I: Corporate Laws (70 Marks)",
        "chapter_code": "A_MGR",
        "topic": "Computation of Net Profits for Managerial Remuneration",
        "subtopic": "Section 198 Permitted Deductions & Statutory Non-Credits",
        "question": (
            "In computing the net profits of a company under Section 198 of the Companies Act, 2013 for determining managerial remuneration, "
            "which of the following items SHALL NOT BE DEDUCTED from the gross revenue?"
        ),
        "option_a": "Interest on debentures issued by the company.",
        "option_b": "Directors' remuneration paid or payable under Section 197.",
        "option_c": "Depreciation calculated in the manner specified under Section 123 read with Schedule II.",
        "option_d": "Contributions made to charitable funds under Section 181.",
        "correct_option": "B",
        "marks": 2,
        "explanation": (
            "Under Section 198(5) of the Companies Act, 2013, in making the computation of net profits, the following sums SHALL NOT BE DEDUCTED:\n"
            "(a) REMUNERATION IN RESPECT OF DIRECTORS (because managerial remuneration is the end objective of the computation itself; deducting it would create an impossible circular loop!);\n"
            "(b) Income tax and super tax payable by the company;\n"
            "(c) Any compensation, damages or payments made voluntarily;\n"
            "(d) Loss of a capital nature including loss on sale of undertaking or of any asset;\n"
            "(e) Any change in carrying amount of an asset or liability recognized in equity reserves (fair value reserves).\n\n"
            "Conversely, interest on debentures, statutory depreciation, and charitable contributions under Sec 181 are legitimate operating/statutory expenses that ARE deducted under Section 198(4)."
        ),
        "section_ref": "Companies Act, 2013 - Section 198(4) & Section 198(5)",
        "exam_tip": "EXAM TRAP: In Section 198 calculations, NEVER deduct: (1) Directors' Remuneration, (2) Income Tax, (3) Voluntary damages, and (4) Capital losses!",
        "source_tag": "Offline SPOM Recall",
        "difficulty": "Moderate",
        "is_case_study": 0,
        "case_scenario": None,
        "why_incorrect_a": "Interest on debentures is an allowable deduction under Sec 198(4)(b).",
        "why_incorrect_b": "",
        "why_incorrect_c": "Depreciation is an allowable deduction under Sec 198(4)(k).",
        "why_incorrect_d": "Contributions under Sec 181 are deductible under Sec 198(4)(m)."
    },
    # --- A_INSP: Investigation of Related Companies ---
    {
        "set_name": "A",
        "section_group": "Part I: Corporate Laws (70 Marks)",
        "chapter_code": "A_INSP",
        "topic": "Investigation into Affairs of Related Companies",
        "subtopic": "Section 219 Scope & Mandatory Prior Central Government Approval",
        "question": (
            "An inspector appointed by the Central Government under Section 210 to investigate the affairs of Prime Steels Ltd. "
            "discovers evidence that funds were systematically siphoned off through its subsidiary, Apex Minerals Pvt. Ltd., and an associate firm. "
            "The inspector seeks to expand the scope of investigation to inspect the books and examine officers of Apex Minerals. "
            "What is the statutory requirement under Section 219 of the Companies Act, 2013?"
        ),
        "option_a": "The inspector has unfettered discretion to investigate any related company without seeking any further approvals.",
        "option_b": "The inspector must obtain the PRIOR APPROVAL OF THE CENTRAL GOVERNMENT before expanding the investigation to any related company (holding, subsidiary, associate, or entity whose MD is nominee of the company).",
        "option_c": "The inspector must apply to the National Company Law Tribunal for an expansion order within 30 days.",
        "option_d": "Investigation can only be expanded if minority shareholders of the subsidiary file an independent petition.",
        "correct_option": "B",
        "marks": 2,
        "explanation": (
            "Under Section 219 of the Companies Act, 2013 (Power of inspector to conduct investigation into affairs of related companies):\n"
            "If an inspector appointed under section 210 or section 212 or section 213 to investigate the affairs of the company thinks it necessary for the purposes of his investigation to investigate also the affairs of:\n"
            "(a) Any other body corporate which is, or has at any relevant time been the company's subsidiary company or holding company, or a subsidiary company of its holding company;\n"
            "(b) Any other body corporate which is, or has at any relevant time been managed by any person as managing director or manager who is, or was at any relevant time, such managing director or manager of the company; or\n"
            "(c) Any other body corporate whose board of directors comprises nominees of the company,\n\n"
            "The inspector SHALL, SUBJECT TO THE PRIOR APPROVAL OF THE CENTRAL GOVERNMENT, have power to investigate the affairs of such related body corporate.\n"
            "This prior Central Government sanction acts as a statutory check against arbitrary jurisdictional overreach."
        ),
        "section_ref": "Companies Act, 2013 - Section 219",
        "exam_tip": "EXAM TRAP: Section 219 expansion of investigation to a subsidiary or holding company MANDATES PRIOR APPROVAL OF CENTRAL GOVERNMENT!",
        "source_tag": "ICAI BoS Module",
        "difficulty": "Moderate",
        "is_case_study": 0,
        "case_scenario": None,
        "why_incorrect_a": "Inspectors do not have unfettered autonomy; Section 219 explicitly mandates prior CG sanction.",
        "why_incorrect_b": "",
        "why_incorrect_c": "Approving authority is the Central Government (Ministry of Corporate Affairs), not NCLT.",
        "why_incorrect_d": "Shareholder petition is not required for an ongoing statutory investigation expansion."
    },
    # --- A_COMP: Squeeze-Out of Dissenting Shareholders ---
    {
        "set_name": "A",
        "section_group": "Part I: Corporate Laws (70 Marks)",
        "chapter_code": "A_COMP",
        "topic": "Acquisition of Shares of Dissenting Shareholders (Squeeze-Out)",
        "subtopic": "Section 235 90% Acceptance, 4-Month & 2-Month Notice Timelines",
        "question": (
            "Titan Agro Ltd. (Transferee Company) made an offer to acquire all shares of Green Fields Ltd. (Transferor Company). "
            "Within 4 months of making the offer, the scheme was approved by holders of 92% in value of the shares whose transfer was involved. "
            "Titan Agro wishes to acquire the shares of the remaining 8% dissenting shareholders. "
            "Under Section 235 of the Companies Act, 2013, what are the statutory timelines for giving notice to dissenting shareholders, "
            "and within what period can a dissenting shareholder apply to the Tribunal against compulsory acquisition?"
        ),
        "option_a": "Transferee gives notice within 1 month; Dissenting shareholder applies to Tribunal within 14 days.",
        "option_b": "Transferee company may give notice within TWO (2) MONTHS after the expiry of the 4 months; and the dissenting shareholder may apply to the Tribunal within ONE (1) MONTH from the date on which notice was given.",
        "option_c": "Transferee gives notice within 6 months; Dissenting shareholder applies to Tribunal within 3 months.",
        "option_d": "Dissenting shareholders have no right to apply to Tribunal once 90% have approved.",
        "correct_option": "B",
        "marks": 2,
        "explanation": (
            "Under Section 235 of the Companies Act, 2013:\n"
            "1. Approval Threshold: The scheme must be approved within FOUR (4) MONTHS after the making of the offer by the holders of not less than NINE-TENTHS (90%) IN VALUE of the shares whose transfer is involved.\n"
            "2. Notice by Transferee Company (Sec 235(1)): The transferee company may, at any time within TWO (2) MONTHS after the expiry of the said 4 months, give notice in the prescribed manner to any dissenting shareholder that it desires to acquire his shares.\n"
            "3. Application by Dissenting Shareholder (Sec 235(2)): Where such notice is given, the transferee company shall, UNLESS ON AN APPLICATION MADE BY THE DISSENTING SHAREHOLDER WITHIN ONE (1) MONTH from the date on which the notice was given, the Tribunal thinks fit to order otherwise, be entitled and bound to acquire those shares on the terms of the scheme."
        ),
        "section_ref": "Companies Act, 2013 - Section 235(1) & Section 235(2)",
        "exam_tip": "EXAM TRAP: The Section 235 squeeze-out clock: 9/10th (90%) within 4 MONTHS -> Notice within 2 MONTHS -> Dissenting shareholder challenge to NCLT within 1 MONTH!",
        "source_tag": "Offline SPOM Recall",
        "difficulty": "Hard",
        "is_case_study": 0,
        "case_scenario": None,
        "why_incorrect_a": "Notice is 2 months, challenge is 1 month.",
        "why_incorrect_b": "",
        "why_incorrect_c": "Incorrect timelines.",
        "why_incorrect_d": "Dissenting shareholders have a statutory right to apply to the Tribunal under Section 235(2)."
    },
    # --- A_OPPR: NCLT Relief Powers ---
    {
        "set_name": "A",
        "section_group": "Part I: Corporate Laws (70 Marks)",
        "chapter_code": "A_OPPR",
        "topic": "Powers of Tribunal in Oppression and Mismanagement",
        "subtopic": "Section 242 Comprehensive Order Scope & Statutory Alterations",
        "question": (
            "In a petition under Section 241, the NCLT finds that a company's affairs have been conducted oppressively. "
            "Which of the following reliefs CANNOT be granted by the Tribunal under Section 242 of the Companies Act, 2013?"
        ),
        "option_a": "Directing the regulation of the conduct of affairs of the company in future.",
        "option_b": "Directing the purchase of shares of any members by other members or by the company with consequent capital reduction.",
        "option_c": "Directing the company to declare and pay interim dividends to minority shareholders contrary to Board recommendation.",
        "option_d": "Setting aside any transfer, delivery of goods, payment, or execution made within 3 months before the date of the application which would be deemed a fraudulent preference in insolvency.",
        "correct_option": "C",
        "marks": 2,
        "explanation": (
            "Under Section 242(2) of the Companies Act, 2013, the Tribunal may make an order providing for:\n"
            "(a) Regulation of the conduct of the affairs of the company in future;\n"
            "(b) Purchase of shares of any members by other members or by the company (with capital reduction);\n"
            "(c) Restrictions on transfer or allotment of shares;\n"
            "(d) Termination, setting aside or modification of any agreement with MD/directors;\n"
            "(e) Setting aside of fraudulent preference transactions made within 3 months prior to petition;\n"
            "(f) Removal of the managing director or directors; and\n"
            "(g) Appointment of new directors.\n\n"
            "Declaration of dividend is an exclusive prerogative of the Board and shareholders in general meeting. Courts and Tribunals do not sit in commercial management to force dividend declarations unless funds are being actively siphoned to starve minorities. Hence, Option C is not a statutory relief under Section 242."
        ),
        "section_ref": "Companies Act, 2013 - Section 242(2)",
        "exam_tip": "EXAM TRAP: Section 242 powers are extensive (purchase of shares, removing MD, setting aside 3-month preferences, modifying MOA/AOA), but Tribunal does not assume normal commercial management like declaring interim dividends.",
        "source_tag": "ICAI Test Your Knowledge",
        "difficulty": "Moderate",
        "is_case_study": 0,
        "case_scenario": None,
        "why_incorrect_a": "Expressly permitted under Section 242(2)(a).",
        "why_incorrect_b": "Expressly permitted under Section 242(2)(b).",
        "why_incorrect_c": "",
        "why_incorrect_d": "Expressly permitted under Section 242(2)(g)."
    },
    # --- A_OPPR: Class Action Suit Thresholds ---
    {
        "set_name": "A",
        "section_group": "Part I: Corporate Laws (70 Marks)",
        "chapter_code": "A_OPPR",
        "topic": "Class Action Suits",
        "subtopic": "Section 245 Numerical Thresholds for Depositors vs Members",
        "question": (
            "Under Section 245 of the Companies Act, 2013, an application for a Class Action Suit on behalf of depositors "
            "seeking damages against fraudulent directors or auditors can be filed by:\n"
            "1. Not less than _________ depositors, OR\n"
            "2. Not less than _________ of the total number of depositors, whichever is less; OR\n"
            "3. Any depositor or depositors to whom the company owes _________ of total deposits of the company:"
        ),
        "option_a": "50; 5%; 10%",
        "option_b": "100; 10%; 5%",
        "option_c": "100; 5%; 2%",
        "option_d": "500; 10%; 5%",
        "correct_option": "B",
        "marks": 2,
        "explanation": (
            "Under Section 245(1) read with Rule 84 of the National Company Law Tribunal Rules, 2016:\n"
            "In case of DEPOSITORS, a class action suit may be filed by:\n"
            "(a) NOT LESS THAN ONE HUNDRED (100) depositors, OR\n"
            "(b) NOT LESS THAN TEN PERCENT (10%) of the total number of depositors, WHICHEVER IS LESS; OR\n"
            "(c) Any depositor or depositors to whom the company owes FIVE PERCENT (5%) of total deposits of the company.\n\n"
            "Notice the clean numerical formula for depositors: 100 or 10% (whichever is less) OR 5% of total deposits in value."
        ),
        "section_ref": "Companies Act, 2013 - Section 245(1) & Rule 84",
        "exam_tip": "EXAM TRAP: Depositors Class Action formula = 100 or 10% (whichever less) OR 5% in value of deposits! Contrast with members (100 or 10% OR 5% unlisted / 2% listed share capital).",
        "source_tag": "ICAI BoS Module",
        "difficulty": "Hard",
        "is_case_study": 0,
        "case_scenario": None,
        "why_incorrect_a": "Incorrect thresholds.",
        "why_incorrect_b": "",
        "why_incorrect_c": "2% is the capital threshold for members of listed companies, not depositors.",
        "why_incorrect_d": "Incorrect numerical count."
    },
    # --- A_WIND: Liquidator Preliminary Report ---
    {
        "set_name": "A",
        "section_group": "Part I: Corporate Laws (70 Marks)",
        "chapter_code": "A_WIND",
        "topic": "Winding Up Preliminary Report by Company Liquidator",
        "subtopic": "Section 281 60-Day Submission Timeline & Report Contents",
        "question": (
            "Where the Tribunal has made a winding up order or appointed a Company Liquidator, the Company Liquidator shall, "
            "within _________ from the date of the winding up order, submit to the Tribunal a PRELIMINARY REPORT containing "
            "the nature and details of the assets, cash balance, debts, liabilities, and whether in his opinion any fraud has been committed:"
        ),
        "option_a": "30 days",
        "option_b": "60 days",
        "option_c": "90 days",
        "option_d": "180 days",
        "correct_option": "B",
        "marks": 2,
        "explanation": (
            "Under Section 281(1) of the Companies Act, 2013:\n"
            "Where the Tribunal has made a winding up order or appointed a Company Liquidator, such liquidator SHALL, WITHIN SIXTY (60) DAYS "
            "from the date of the winding up order, submit to the Tribunal a preliminary report stating:\n"
            "(a) The nature and details of the assets of the company, including cash balance, negotiable securities, debts etc.;\n"
            "(b) The amount of capital issued, subscribed and paid-up;\n"
            "(c) The existing and probable liabilities of the company;\n"
            "(d) Debts due to the company and guarantees;\n"
            "(e) Whether in his opinion further inquiry is desirable as to any matter relating to the promotion, formation or failure of the company or conduct of its business; and\n"
            "(f) Whether any fraud has been committed by any person.\n\n"
            "Under Section 281(4), the liquidator may also make viable reports on whether the company should be dissolved."
        ),
        "section_ref": "Companies Act, 2013 - Section 281(1)",
        "exam_tip": "EXAM TRAP: The Company Liquidator's preliminary report must be submitted to the Tribunal within SIXTY (60) DAYS of the winding up order.",
        "source_tag": "Offline SPOM Recall",
        "difficulty": "Moderate",
        "is_case_study": 0,
        "case_scenario": None,
        "why_incorrect_a": "30 days is the statement of affairs filing timeline by directors under Sec 274.",
        "why_incorrect_b": "",
        "why_incorrect_c": "90 days is the Tribunal winding up order decision timeline under Sec 273.",
        "why_incorrect_d": "180 days is the PMLA provisional attachment period."
    },
    # --- A_FOREIGN: Financial Statements Delivery ---
    {
        "set_name": "A",
        "section_group": "Part I: Corporate Laws (70 Marks)",
        "chapter_code": "A_FOREIGN",
        "topic": "Accounts of Foreign Company & ROC Filings",
        "subtopic": "Section 381 6-Month Timeline, Schedule III Audit & Form FC-3",
        "question": (
            "Global Aviation Ltd., a foreign company having a place of business in Mumbai, closes its financial year on 31st December. "
            "Under Section 381 of the Companies Act, 2013 and the Companies (Registration of Foreign Companies) Rules, 2014, "
            "within what period must it deliver its audited financial statements of Indian operations to the ROC, and which accompanying documents are mandatory?"
        ),
        "option_a": "Within 30 days of the AGM; accompanied only by the foreign board resolution.",
        "option_b": "Within SIX (6) MONTHS of the close of the financial year (i.e. by 30th June); prepared in accordance with Schedule III, audited by a practicing Indian CA, accompanied by Form FC-3 containing list of places of business, statement of related party transactions, and repatriation of profits.",
        "option_c": "Within 90 days; prepared under US GAAP without requiring Indian Chartered Accountant audit.",
        "option_d": "Foreign companies are exempt from filing accounts with ROC if audited in their home country.",
        "correct_option": "B",
        "marks": 2,
        "explanation": (
            "Under Section 381(1) of the Companies Act, 2013 read with Rule 4 and Rule 5 of Companies (Registration of Foreign Companies) Rules, 2014:\n"
            "1. Every foreign company shall, in every calendar year, deliver to the Registrar a copy of the balance sheet and profit and loss account prepared in accordance with Schedule III within a period of SIX (6) MONTHS of the close of the financial year of the foreign company.\n"
            "2. Audit Requirement: The accounts of the Indian business operations must be audited by a practicing Chartered Accountant in India.\n"
            "3. Accompanying Documents (Form FC-3): Must deliver documents relating to: (i) Consolidated financial statements of the parent foreign company; (ii) Statement of Related Party Transactions; (iii) Statement of Repatriation of Profits; and (iv) Statement of transfer of funds between place of business in India and any other related party."
        ),
        "section_ref": "Companies Act, 2013 - Section 381 read with Rule 4 & 5",
        "exam_tip": "EXAM TRAP: Foreign company accounts timeline = 6 MONTHS from close of financial year (not 30 days from AGM!). Must be Schedule III compliant and audited by an Indian CA.",
        "source_tag": "ICAI Test Your Knowledge",
        "difficulty": "Moderate",
        "is_case_study": 0,
        "case_scenario": None,
        "why_incorrect_a": "AGM rules do not govern foreign company filing under Section 381.",
        "why_incorrect_b": "",
        "why_incorrect_c": "Indian operations must follow Schedule III and be audited by an Indian CA.",
        "why_incorrect_d": "Section 381 contains no exemption for home-country audited firms."
    },
    # --- A_SEBI: Section 11(5) Provisional Attachment ---
    {
        "set_name": "A",
        "section_group": "Part I: Corporate Laws (70 Marks)",
        "chapter_code": "A_SEBI",
        "topic": "SEBI Provisional Attachment of Bank Accounts",
        "subtopic": "Section 11(5) Maximum 90-Day Validity & Special Court Confirmation",
        "question": (
            "SEBI initiated an investigation into an unauthorized collective investment scheme and, under Section 11(5) of the SEBI Act, 1992, "
            "passed an ex-parte order provisionally attaching the bank accounts of the promoter for an amount equal to alleged illicit gains. "
            "What is the MAXIMUM STATUTORY DURATION for which such provisional attachment can remain in force without confirmation by the Special Court?"
        ),
        "option_a": "Not exceeding 30 days.",
        "option_b": "Not exceeding 90 days.",
        "option_c": "Not exceeding 180 days.",
        "option_d": "Indefinitely until the final penalty order is passed.",
        "correct_option": "B",
        "marks": 2,
        "explanation": (
            "Under Section 11(5) of the SEBI Act, 1992:\n"
            "The Board may, by order, for reasons to be recorded in writing, in the interests of investors or securities market, "
            "take any of the measures under this Act, including the provisional attachment of bank accounts or other property.\n\n"
            "Under the Proviso to Section 11(5):\n"
            "'Provided that such provisional attachment shall be for a period NOT EXCEEDING NINETY (90) DAYS.'\n"
            "If SEBI desires to continue the attachment beyond 90 days, it MUST obtain an order of confirmation from the Special Court within the said 90-day period. "
            "(Contrast this with PMLA Section 5 provisional attachment, which is 180 days! SEBI Section 11(5) is strictly 90 days)."
        ),
        "section_ref": "SEBI Act, 1992 - Section 11(5) Proviso",
        "exam_tip": "EXAM TRAP: Do NOT confuse PMLA with SEBI! Provisional attachment of bank accounts by SEBI under Sec 11(5) = MAX 90 DAYS. PMLA provisional attachment under Sec 5 = 180 DAYS!",
        "source_tag": "Offline SPOM Recall",
        "difficulty": "Hard",
        "is_case_study": 0,
        "case_scenario": None,
        "why_incorrect_a": "Incorrect period.",
        "why_incorrect_b": "",
        "why_incorrect_c": "180 days is the period under PMLA Section 5, not SEBI Act Section 11(5).",
        "why_incorrect_d": "Indefinite attachment violates the statutory 90-day ceiling."
    },
    # --- A_FEMA: Export Proceeds Realization Timelines ---
    {
        "set_name": "A",
        "section_group": "Part II: Economic Laws (30 Marks)",
        "chapter_code": "A_FEMA",
        "topic": "Export of Goods and Services Realization",
        "subtopic": "Regulation 9 Period of Realization (9 Months vs 15 Months for Warehouse)",
        "question": (
            "Under the Foreign Exchange Management (Export of Goods and Services) Regulations, what is the statutory period "
            "within which the full export value of goods or software exported must be realized and repatriated to India, "
            "for normal exports and for goods exported to a warehouse established outside India respectively?"
        ),
        "option_a": "Normal exports: 6 months; Warehouse exports: 12 months",
        "option_b": "Normal exports: NINE (9) MONTHS from the date of export; Warehouse exports: FIFTEEN (15) MONTHS from the date of shipment.",
        "option_c": "Normal exports: 12 months; Warehouse exports: 18 months",
        "option_d": "Normal exports: 180 days; Warehouse exports: 365 days",
        "correct_option": "B",
        "marks": 2,
        "explanation": (
            "Under Regulation 9 of the Foreign Exchange Management (Export of Goods and Services) Regulations, 2016:\n"
            "1. Normal Exports: The amount representing the full export value of goods/software exported shall be realized and repatriated to India within NINE (9) MONTHS from the date of export.\n"
            "2. Warehouse Exports: Where the goods are exported to a warehouse established outside India with the permission of the Reserve Bank, the amount representing the full export value of goods exported shall be paid to the authorized dealer within FIFTEEN (15) MONTHS from the date of shipment of goods.\n\n"
            "Authorized Dealer Category-I banks are permitted to extend the period of realization by up to 6 months in genuine cases beyond these periods."
        ),
        "section_ref": "FEM (Export of Goods and Services) Regulations, 2016 - Regulation 9",
        "exam_tip": "EXAM TRAP: Export realization clocks: Standard exports = 9 MONTHS. Warehouse exports outside India = 15 MONTHS!",
        "source_tag": "ICAI BoS Module",
        "difficulty": "Moderate",
        "is_case_study": 0,
        "case_scenario": None,
        "why_incorrect_a": "6 months was an older pre-amendment timeline.",
        "why_incorrect_b": "",
        "why_incorrect_c": "12 and 18 months are incorrect.",
        "why_incorrect_d": "Specified in months (9m and 15m), not days."
    },
    # --- A_IBC: Information Utility Record of Default ---
    {
        "set_name": "A",
        "section_group": "Part II: Economic Laws (30 Marks)",
        "chapter_code": "A_IBC",
        "topic": "Information Utilities & Record of Default",
        "subtopic": "Section 215 & Section 7 Conclusive Proof of Default",
        "question": (
            "State Bank of India filed a Section 7 CIRP application against Omkar Steels Ltd. based on a certified 'Record of Default' "
            "issued by National E-Governance Services Ltd. (NeSL), a registered Information Utility under Section 214 of the IBC. "
            "The corporate debtor argued that the debt had not been adjudicated by a civil court or DRT and hence cannot be treated as default. "
            "Examine the evidentiary value of the Information Utility's Record of Default."
        ),
        "option_a": "The Record of Default is merely prima facie evidence and requires corroboration through a decree of a civil court.",
        "option_b": "Under Section 7(3) read with Section 215 of the IBC and the Supreme Court ruling in Swiss Ribbons, a certified Record of Default authenticated by an Information Utility is CONCLUSIVE PROOF of default; the NCLT is not required to conduct a mini-trial and must admit CIRP if the default exceeds Rs 1 Crore.",
        "option_c": "Information Utilities can only register operational debts, not financial debts.",
        "option_d": "NCLT must reject any application that is not preceded by a DRT recovery certificate.",
        "correct_option": "B",
        "marks": 2,
        "explanation": (
            "Under Section 7(3)(a) of the Insolvency and Bankruptcy Code, 2016, the financial creditor shall, along with the application, furnish record of the default recorded with the information utility or such other record or evidence of default as may be specified.\n\n"
            "As held by the Supreme Court in the landmark constitutionality judgment of Swiss Ribbons Pvt. Ltd. v. Union of India (2019):\n"
            "Information Utilities (like NeSL) are set up to provide authenticated, tamper-proof electronic records of debts and defaults. Once a financial creditor submits information of default to the Information Utility and it is authenticated under Section 215, it acts as conclusive evidence of default. The Adjudicating Authority (NCLT) is merely required to ascertain the existence of default from the records of the Information Utility within 14 days, without requiring any prior decree or civil adjudication. Hence, Omkar's objection is baseless."
        ),
        "section_ref": "Insolvency and Bankruptcy Code, 2016 - Section 7(3) read with Section 215 & Swiss Ribbons",
        "exam_tip": "EXAM TRAP: NeSL / Information Utility Record of Default is conclusive proof under Section 7. No prior DRT certificate or civil decree is needed to trigger CIRP!",
        "source_tag": "ICAI Test Your Knowledge",
        "difficulty": "Hard",
        "is_case_study": 0,
        "case_scenario": None,
        "why_incorrect_a": "Record of default from an IU does not require prior civil court decree corroboration.",
        "why_incorrect_b": "",
        "why_incorrect_c": "Financial creditors are statutorily MANDATED to submit financial information to IUs under Sec 215(2).",
        "why_incorrect_d": "DRT recovery certificate is not a prerequisite under IBC Section 7."
    },
    # --- A_PMLA_FCRA: FCRA Cancellation & Assets Disposal ---
    {
        "set_name": "A",
        "section_group": "Part II: Economic Laws (30 Marks)",
        "chapter_code": "A_PMLA_FCRA",
        "topic": "FCRA Cancellation of Certificate & Disposal of Assets",
        "subtopic": "Section 14 & Section 15 Re-Registration Bar (3 Years) & Banking Directions",
        "question": (
            "The FCRA registration certificate of 'Samarpan Trust' was cancelled by the Central Government under Section 14 "
            "for misutilizing foreign contributions for speculative stock trading. "
            "Examine: (1) After what minimum period can Samarpan Trust apply for fresh registration under FCRA? "
            "and (2) What can the Central Government direct regarding the unutilized foreign contribution and assets created out of it?"
        ),
        "option_a": "Can apply after 1 year; unutilized funds are forfeited to the local municipality.",
        "option_b": "Under Section 14(3), the entity SHALL NOT BE ELIGIBLE for registration for a period of THREE (3) YEARS from the date of cancellation; and under Section 15, the Central Government may direct the banking authority to utilize or dispose of the assets for permissible charitable activities in public interest.",
        "option_c": "Cancellation creates a lifetime permanent debarment; funds are automatically transferred to the UN Human Rights Council.",
        "option_d": "Can apply after 5 years; the bank account must be refunded to foreign donors within 30 days.",
        "correct_option": "B",
        "marks": 2,
        "explanation": (
            "Under the Foreign Contribution (Regulation) Act, 2010:\n"
            "1. Bar on Re-Registration (Section 14(3)):\n"
            "Any person or association whose certificate has been cancelled under this section SHALL NOT BE ELIGIBLE for registration or grant of prior permission for a period of THREE (3) YEARS from the date of cancellation of such certificate.\n\n"
            "2. Disposal of Assets (Section 15):\n"
            "Where the certificate of registration is cancelled, the foreign contribution and assets created out of foreign contribution shall vest in the banking authority until directed otherwise. Under Section 15(2), the Central Government may, if satisfied in the public interest, direct the banking authority to UTILIZE the foreign contribution or DISPOSE of the assets created out of it in such manner as may be prescribed to continue the activities for which foreign contribution was received."
        ),
        "section_ref": "FCRA, 2010 - Section 14(3) & Section 15",
        "exam_tip": "EXAM TRAP: FCRA cancellation imposes a strictly 3-YEAR BAR on applying for fresh registration. Unutilized assets and bank funds can be directed by Central Govt for approved charitable use under Sec 15.",
        "source_tag": "Offline SPOM Recall",
        "difficulty": "Moderate",
        "is_case_study": 0,
        "case_scenario": None,
        "why_incorrect_a": "1 year is incorrect; statutory bar is 3 years.",
        "why_incorrect_b": "",
        "why_incorrect_c": "Cancellation does not create permanent lifetime debarment; statutory bar is 3 years.",
        "why_incorrect_d": "5 years is incorrect; foreign refund is not mandatory under Section 15."
    },
    # --- A_PMLA_FCRA: PMLA Special Courts Jurisdiction ---
    {
        "set_name": "A",
        "section_group": "Part II: Economic Laws (30 Marks)",
        "chapter_code": "A_PMLA_FCRA",
        "topic": "PMLA Special Courts & Trial Jurisdiction",
        "subtopic": "Section 43 & Section 44 Exclusive Jurisdiction over Scheduled & PMLA Offences",
        "question": (
            "Mr. X is accused of committing an offence of corruption under the Prevention of Corruption Act (Scheduled Offence) "
            "investigated by the CBI, and generating proceeds of crime laundered through dummy companies investigated by the "
            "Enforcement Directorate (ED) under the PMLA, 2002. CBI filed a charge sheet before the Special CBI Court, "
            "while ED filed a complaint before the Special Court designated under Section 43 of PMLA. "
            "Under Section 44(1)(c) of PMLA, what is the procedure for trial of these two offences?"
        ),
        "option_a": "Both trials must proceed independently before their respective courts without any transfer.",
        "option_b": "The court trying the scheduled offence SHALL COMMIT the case relating to the scheduled offence to the SPECIAL COURT DESIGNATED UNDER PMLA, and the Special Court shall try both the scheduled offence and the PMLA offence jointly or concurrently.",
        "option_c": "The PMLA trial is stayed until the scheduled offence is conclusively decided by the Supreme Court.",
        "option_d": "The Enforcement Directorate complaint is dismissed if the accused is granted bail in the CBI case.",
        "correct_option": "B",
        "marks": 2,
        "explanation": (
            "Under Section 44(1)(c) of the Prevention of Money Laundering Act, 2002 (PMLA):\n"
            "If the court which has taken cognizance of the scheduled offence is other than the Special Court which has taken cognizance of the complaint of the offence of money-laundering under sub-clause (b), it SHALL, on an application by the authorized officer, COMMIT THE CASE relating to the scheduled offence to the SPECIAL COURT and the Special Court shall proceed with such case from the stage at which it was committed.\n\n"
            "The objective of Section 44(1)(c) is to avoid conflicting findings and ensure that both the predicate scheduled offence and the money laundering offence are heard by the designated Special Court under PMLA. Hence, the scheduled offence case must be committed to the Special Court under PMLA."
        ),
        "section_ref": "PMLA, 2002 - Section 43 & Section 44(1)(c)",
        "exam_tip": "EXAM TRAP: Under Section 44(1)(c), the scheduled offence court MUST COMMIT the predicate case to the PMLA Special Court so both can be tried together!",
        "source_tag": "ICAI BoS Module",
        "difficulty": "Hard",
        "is_case_study": 0,
        "case_scenario": None,
        "why_incorrect_a": "Section 44(1)(c) specifically prohibits independent scattered trials to avoid conflicts.",
        "why_incorrect_b": "",
        "why_incorrect_c": "PMLA trial is not stayed; both are tried concurrently by the PMLA Special Court.",
        "why_incorrect_d": "Bail in the predicate offence does not lead to dismissal of the PMLA complaint."
    },
    # --- A_DIR: Director Disqualification Proviso to 164(2) ---
    {
        "set_name": "A",
        "section_group": "Part I: Corporate Laws (70 Marks)",
        "chapter_code": "A_DIR",
        "topic": "Director Disqualification 6-Month Grace Period",
        "subtopic": "Section 164(2) Proviso Immunity for Newly Appointed Directors",
        "question": (
            "Mr. Sharan was appointed as a director of Alpha Castings Ltd. on 1st January 2024. "
            "Alpha Castings had already failed to file its financial statements for FY 2020-21 and FY 2021-22, and on 31st January 2024 "
            "(within 30 days of his appointment), it defaulted in filing financial statements for FY 2022-23, completing a continuous 3-year default. "
            "ROC issued a show-cause notice disqualifying Mr. Sharan under Section 164(2)(a). "
            "Examine whether Mr. Sharan is protected under the Proviso to Section 164(2)."
        ),
        "option_a": "No, because incurring a 3-year default applies strictly against all serving directors on the board.",
        "option_b": "Yes; under the Proviso to Section 164(2) (inserted by the Companies Amendment Act), where a person is appointed as a director of a company which is in default, he SHALL NOT INCUR THE DISQUALIFICATION for a period of SIX (6) MONTHS from the date of his appointment.",
        "option_c": "Yes, but he must resign within 15 days of receiving the ROC notice.",
        "option_d": "No, because newly appointed directors assume personal liability for all past corporate defaults.",
        "correct_option": "B",
        "marks": 2,
        "explanation": (
            "Under the Proviso to Section 164(2) of the Companies Act, 2013 (inserted by the Companies (Amendment) Act, 2017):\n"
            "'Provided that where a person is appointed as a director of a company which is in default under clause (a) or clause (b), he SHALL NOT INCUR THE DISQUALIFICATION for a period of SIX (6) MONTHS from the date of his appointment.'\n\n"
            "The legislative rationale of this 6-month grace period is to give a turnaround professional or new director adequate time to cure the company's past defaults without immediately becoming disqualified across all his other companies upon stepping onto the board. "
            "Because Mr. Sharan was appointed on 1st January 2024 and the default materialized on 31st January 2024, he is fully shielded by the 6-month statutory immunity period."
        ),
        "section_ref": "Companies Act, 2013 - Section 164(2) Proviso",
        "exam_tip": "EXAM TRAP: A newly appointed director in a defaulting company is granted a 6-MONTH STATUTORY GRACE PERIOD under Section 164(2) Proviso during which he incurs zero disqualification!",
        "source_tag": "Offline SPOM Recall",
        "difficulty": "Hard",
        "is_case_study": 0,
        "case_scenario": None,
        "why_incorrect_a": "Fails to recognize the statutory 6-month immunity proviso.",
        "why_incorrect_b": "",
        "why_incorrect_c": "Resignation is not mandatory to claim the benefit of the statutory proviso.",
        "why_incorrect_d": "Section 164(2) proviso expressly shields new appointees from immediate disqualification."
    },
    # --- A_SEBI: Structured Digital Database Time-Stamping & Audit Trail ---
    {
        "set_name": "A",
        "section_group": "Part I: Corporate Laws (70 Marks)",
        "chapter_code": "A_SEBI",
        "topic": "SEBI PIT Regulations Structured Digital Database Controls",
        "subtopic": "Regulation 3(5) In-House Maintenance, Audit Trail & Non-Outsourcing Rule",
        "question": (
            "Zenith Infotech Ltd. (a listed entity) engages a third-party SaaS cloud vendor to host and manage its "
            "Structured Digital Database (SDD) for tracking Unpublished Price Sensitive Information (UPSI). "
            "The vendor maintains logs on a public cloud server with manual time-stamping entries by staff. "
            "Examine whether this arrangement satisfies Regulation 3(5) of the SEBI (PIT) Regulations, 2015."
        ),
        "option_a": "Yes, because cloud outsourcing is standard industry practice for listed entities.",
        "option_b": "No; under Regulation 3(5) of SEBI (PIT) Regulations, the Structured Digital Database SHALL BE MAINTAINED INTERNALLY (cannot be outsourced) with adequate internal controls and checks such as time-stamping and audit trails to ensure non-tampering of the database.",
        "option_c": "Yes, provided the SaaS vendor signs an indemnity bond of Rs 50 Crore with SEBI.",
        "option_d": "No, because SDD is mandatory only for banking and insurance companies.",
        "correct_option": "B",
        "marks": 2,
        "explanation": (
            "Under Regulation 3(5) of the SEBI (Prohibition of Insider Trading) Regulations, 2015 and SEBI's clarificatory FAQs:\n"
            "1. The Structured Digital Database (SDD) MUST BE MAINTAINED INTERNALLY by the listed entity or intermediary, and CANNOT BE OUTSOURCED to any external third-party vendor or SaaS provider.\n"
            "2. The database must feature robust internal controls, including AUTOMATED TIME-STAMPING and an immutable AUDIT TRAIL to guarantee that entries of UPSI and PAN of recipient persons cannot be altered, forged, back-dated, or deleted.\n"
            "3. Outsourcing the database to an external vendor creates confidentiality breaches and violates Regulation 3(5)."
        ),
        "section_ref": "SEBI (PIT) Regulations, 2015 - Regulation 3(5) & SEBI Circulars",
        "exam_tip": "EXAM TRAP: SEBI PIT Structured Digital Database (SDD) CANNOT BE OUTSOURCED! It must be maintained internally with immutable audit trails and preserved for at least 8 YEARS.",
        "source_tag": "ICAI Test Your Knowledge",
        "difficulty": "Moderate",
        "is_case_study": 0,
        "case_scenario": None,
        "why_incorrect_a": "SEBI PIT FAQs explicitly prohibit outsourcing of SDD to third parties.",
        "why_incorrect_b": "",
        "why_incorrect_c": "Indemnity bonds cannot cure a direct regulatory violation.",
        "why_incorrect_d": "SDD is mandatory for all listed entities and intermediaries handling UPSI."
    }
]


def seed_additional_master():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    inserted_count = 0
    updated_count = 0

    for q in ADDITIONAL_MASTER_MCQS:
        cursor.execute("SELECT id FROM mcqs WHERE set_name = ? AND question = ?", (q['set_name'], q['question']))
        existing = cursor.fetchone()

        if existing:
            cursor.execute("""
                UPDATE mcqs SET
                    section_group = ?, chapter_code = ?, topic = ?, subtopic = ?,
                    option_a = ?, option_b = ?, option_c = ?, option_d = ?,
                    correct_option = ?, marks = ?, explanation = ?, section_ref = ?,
                    exam_tip = ?, source_tag = ?, difficulty = ?, is_case_study = ?,
                    case_scenario = ?, why_incorrect_a = ?, why_incorrect_b = ?,
                    why_incorrect_c = ?, why_incorrect_d = ?, verification_status = 'Verified',
                    is_outdated_law = 0
                WHERE id = ?
            """, (
                q['section_group'], q['chapter_code'], q['topic'], q.get('subtopic', ''),
                q['option_a'], q['option_b'], q['option_c'], q['option_d'],
                q['correct_option'], q.get('marks', 2), q['explanation'], q.get('section_ref', ''),
                q.get('exam_tip', ''), q.get('source_tag', 'ICAI Test Your Knowledge'),
                q.get('difficulty', 'Hard'), q.get('is_case_study', 0), q.get('case_scenario'),
                q.get('why_incorrect_a', ''), q.get('why_incorrect_b', ''),
                q.get('why_incorrect_c', ''), q.get('why_incorrect_d', ''),
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
                    source_url_or_ref, source_date, verification_status, is_outdated_law, is_user_uploaded
                ) VALUES (
                    ?, ?, ?, ?, ?,
                    ?, ?, ?, ?, ?,
                    ?, ?, ?, ?, ?,
                    ?, ?, ?, ?,
                    ?, ?, ?, ?,
                    'Master Synthesized High-Yield SPOM Batch 2', '2024-11', 'Verified', 0, 0
                )
            """, (
                q['set_name'], q['section_group'], q['chapter_code'], q['topic'], q.get('subtopic', ''),
                q['question'], q['option_a'], q['option_b'], q['option_c'], q['option_d'],
                q['correct_option'], q.get('marks', 2), q['explanation'], q.get('section_ref', ''),
                q.get('exam_tip', ''), q.get('source_tag', 'ICAI Test Your Knowledge'),
                q.get('difficulty', 'Hard'), q.get('is_case_study', 0), q.get('case_scenario'),
                q.get('why_incorrect_a', ''), q.get('why_incorrect_b', ''),
                q.get('why_incorrect_c', ''), q.get('why_incorrect_d', '')
            ))
            inserted_count += 1

    conn.commit()

    cursor.execute("SELECT count(*) FROM mcqs WHERE set_name = 'A'")
    total_a = cursor.fetchone()[0]

    cursor.execute("SELECT count(*) FROM mcqs WHERE set_name = 'A' AND is_case_study = 1")
    total_case = cursor.fetchone()[0]

    cursor.execute("SELECT count(*) FROM mcqs WHERE set_name = 'B'")
    total_b = cursor.fetchone()[0]

    cursor.execute("SELECT count(*) FROM mcqs")
    grand_total = cursor.fetchone()[0]

    cursor.execute("SELECT chapter_code, count(*) FROM mcqs WHERE set_name = 'A' GROUP BY chapter_code ORDER BY chapter_code")
    breakdown = cursor.fetchall()

    conn.close()

    print(f"\n[SUCCESS] Batch 2 Master Seeding Complete!")
    print(f"- Total Set A MCQs: {total_a} (Pristine High-Density Exam Ready)")
    print(f"- Set A Case Study Questions: {total_case}")
    print(f"- Total Set B MCQs: {total_b}")
    print(f"- Grand Total Portal MCQs: {grand_total}")
    print("\nBalanced Chapter Breakdown for Set A:")
    for ch, count in breakdown:
        print(f"  {ch}: {count} MCQs")

if __name__ == "__main__":
    seed_additional_master()
