# AI-Assisted Resume Screening System

## Overview
Recruiters in campus hiring receive thousands of resumes per role, making manual screening slow, inconsistent, and biased.

This product uses AI to rank and highlight high-potential candidates, allowing hiring managers to focus their judgment where it adds the most value.

**Goal:** Reduce resume screening effort by **70–90%** without sacrificing candidate quality or fairness.

---

## Problem Statement

Campus hiring roles often attract **more than 2000 applicants**.

Current screening relies on:
- Keyword filters
- Manual skimming
- Subjective judgment

This leads to:
- Missed high-potential candidates
- High recruiter burnout
- Bias toward well-known colleges and keywords

The core challenge is **search and prioritization**, not final decision-making.

---

## Users & Use Cases

### Primary User
- Recruiters / Talent Acquisition teams

### Secondary User
- Hiring managers

### Key Use Case
1. Recruiter uploads resumes
2. System ranks candidates by relevance
3. Recruiter reviews top-ranked candidates
4. Hiring manager makes final decision

---

## Why AI

- Manual and rule-based screening does not scale beyond thousands of resumes.
- Keyword filters fail to capture semantic skill matches.
- AI enables consistent, role-specific ranking across large candidate volumes.
- The system prioritizes **high recall** to avoid missing strong candidates.
- Final decisions remain **human-driven** to reduce risk and bias.

---

## Goals & Success Metrics

### Business Metrics
- Screening time per role ↓
- Recruiter throughput ↑
- Cost per hire ↓

### ML Metrics
- Recall prioritized over precision
- Ranking relevance (Top-N quality)

---

## Scope Definition

### In Scope (v1)
- Resume parsing
- Skill extraction
- Candidate relevance ranking
- Recruiter dashboard

### Out of Scope (v1)
- Automated rejection
- Interview scheduling
- Final hiring decision

---

## Model & Data Design

### Inputs
- Resume text
- Job description
- Skill taxonomy

### Outputs
- Ranked candidate list
- Confidence score
- Highlighted skill matches

---

## Open Questions
- What is the optimal Top-N threshold?
- How frequently should the model be retrained?
- What level of explainability is required for compliance?