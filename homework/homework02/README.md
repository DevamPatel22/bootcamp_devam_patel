# Homework 02 - Tooling Setup

**Stage:** Tooling Setup (Stage 02)

## Overview

This homework sets up a reproducible Python project scaffold for future data science work. The goal is to practice organizing folders, managing environment variables, verifying Python packages, and preparing the repository for repeatable notebook work.

## Folder Structure

This homework uses the following structure:

- `data/raw/` for original input data
- `data/processed/` for cleaned or transformed data
- `notebooks/` for Jupyter notebooks
- `src/` for reusable Python code
- `docs/` for documentation
- `reports/` for outputs and summaries
- `model/` for saved model artifacts

## Environment Setup

The environment should include Python and the packages needed for the setup check:

- `python-dotenv`
- `numpy`
- `jupyter`

## Secrets Management

A `.env` file will be used locally for environment variables such as:

- `API_KEY`
- `DATA_DIR`

The `.env` file should not be committed to GitHub. A safe `.env.example` file will be committed instead.

## Stage Connection

In Stage 02, we learned how to create isolated environments, manage secrets with `.env`, scaffold project folders, verify Jupyter, and use Git for version control.

This homework applies those skills to a clean folder structure that can support later work with the loan default risk dataset.