# AI Lead Qualification & Sales Assistant

## Project Overview

This project was developed as part of the **SafeX Solutions AI & ML Internship – Week 3**.

The system automatically evaluates inbound sales leads by analyzing lead information and assigning a qualification score along with a recommended next action.

The prototype demonstrates how AI-assisted lead qualification can help sales teams prioritize high-value leads and improve response times.

---

## Features

- Lead qualification scoring (0–100)
- 7 predefined qualification criteria
- Automatic next-action recommendation
- Testing with 10 sample leads
- Results exported to CSV
- Integration-ready through `integration_wrapper.py`

---

## Qualification Criteria

| Criterion | Maximum Score |
|-----------|--------------:|
| Budget | 20 |
| Urgency | 15 |
| Industry Fit | 15 |
| Company Size | 15 |
| Purchase Intent | 15 |
| Decision Maker | 10 |
| Message Quality | 10 |

**Maximum Score: 100**

---

## Project Structure

```text
AI_Lead_Qualification_Assistant/
│
├── app.py
├── lead_scorer.py
├── rubric.py
├── sample_leads.json
├── results.csv
├── integration_wrapper.py
├── requirements.txt
├── README.md
├── templates/
└── screenshots/
```

---

## Input

- Lead Name
- Company Name
- Customer Message

---

## Output

- Qualification Score (0–100)
- Recommended Next Action

Possible actions include:
- Contact Immediately
- Schedule Product Demo
- Follow Up by Email
- Keep in Nurture Campaign

---

## Technologies Used

- Python
- Pandas
- JSON
- FastAPI (Integration Layer)

---

## How to Run

Install the required packages:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app.py
```

---

## Sample Output

```text
Lead Name : Ali Ahmed
Company   : ABC Electronics

Score     : 100/100

Next Step : Contact immediately
```

---

## Internship Information

**Organization:** SafeX Solutions

**Department:** AI & ML

**Project:** AI Lead Qualification & Sales Assistant

---

## Developer

**Safya Ali**

BS Mathematics

Data Science & AI Enthusiast