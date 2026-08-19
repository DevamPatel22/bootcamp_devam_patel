# Loan Default Risk Prediction

**Stage:** Problem Framing & Scoping (Stage 01)

## Problem Statement

Many people struggle to get loans because they have insufficient or nonexistent credit histories. This can make them vulnerable to unfair or untrustworthy lenders. Home Credit aims to broaden financial inclusion by using alternative data to better predict whether applicants can repay a loan.

This project focuses on predicting loan default risk. The goal is to estimate whether an applicant is likely to have repayment difficulty so that qualified borrowers are not rejected unnecessarily and higher-risk borrowers can receive safer loan terms.

## Stakeholder & User

The primary stakeholder is a lending or credit-risk team. The end user is a credit analyst or loan officer who reviews applicant risk before making or recommending a loan decision.

The model output would support the loan review workflow by giving a repayment-risk probability for each applicant.

## Useful Answer & Decision

This is a predictive machine learning problem. The useful answer is a probability that an applicant will have repayment difficulty.

The main evaluation metric is ROC AUC because the original Home Credit Default Risk competition evaluates predicted probabilities using area under the ROC curve.

The decision supported by this model is whether an applicant should be approved, denied, or reviewed with adjusted loan terms.

## Assumptions & Constraints

- The historical dataset is representative of future applicants.
- The target variable correctly identifies repayment difficulty.
- Missing values and alternative data fields need careful handling.
- The model should be explainable because lending decisions affect real people.
- Raw dataset files should not be committed to GitHub because they are large.

## Known Unknowns / Risks

- The dataset may contain missing or noisy values.
- Some features may create fairness or compliance concerns.
- A high ROC AUC does not automatically mean the model is fair or useful.
- The model may need additional explainability tools before it could support real lending decisions.

## Lifecycle Mapping

Goal → Stage → Deliverable

- Define the lending-risk problem → Problem Framing & Scoping (Stage 01) → Scoping README
- Organize the repository → Tooling Setup (Stage 02) → Folder structure and environment files
- Explore the dataset → Python Fundamentals (Stage 03) → Pandas notebook and summary statistics
- Load raw data reproducibly → Data Acquisition & Ingestion (Stage 04) → Raw data ingestion workflow
- Store processed outputs → Data Storage (Stage 05) → CSV/Parquet storage layer
- Clean and prepare features → Data Preprocessing (Stage 06) → Cleaning functions and processed dataset

## Repo Plan

The homework work will be organized inside the `homework/` folder by stage:

- `homework/homework01/` for problem framing and scoping
- `homework/homework02/` for tooling setup
- `homework/homework03/` for Python fundamentals
- `homework/homework04/` for data acquisition and ingestion
- `homework/homework05/` for data storage
- `homework/homework06/` for data preprocessing

For the loan default risk dataset, raw files will be kept in a `data/raw/` folder and excluded from GitHub when the files are too large.

