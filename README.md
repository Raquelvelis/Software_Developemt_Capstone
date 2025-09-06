# Software Development Capstone

This repository organizes work by lab. 
Each lab lives in its own folder and contains ALL scripts and the lab-specific instructions or requirements in that lab’s README file.

## Project Structure

- One folder per lab at the repository root (e.g., `Lab1`, `Lab2`, ...).
- Each lab folder includes:
  - All Python scripts for that lab.
  - A `README.md` describing the lab’s instructions, requirements, how to run the scripts, and any notes.

Example layout:
Software_Developemt_Capstone/ 
    ├─ Lab1/ 
    │ 
    ├─ README.md # Lab 1 instructions/requirements and run steps 
    │ 
    ├─ script1.py 
    │ 
    ├─ script2.py 
    │ 
    └─ ... 
    ├─ Lab2/ 
    │ 
    ├─ README.md 
    │ 
    ├─ ... 
    │ 
    └─ ... 
    └─ README.md # This file

## Conventions

- Python version: 3.10 or newer.
- Use `virtualenv` for isolated dependencies, if needed.
- Keep each lab self-contained: do not rely on files outside the lab’s folder.

## Adding a New Lab

1. Create a new folder at the root: `LabX/` (replace X with the lab number or name).
2. Place all scripts for the lab inside this folder.
3. Add `LabX/README.md` with:
    - A short description.
    - Requirements/instructions.
    - How to run and test.
    - Any references or notes.

## Running a Lab

- Navigate into the desired lab folder (e.g., `cd Lab1`).
- Follow the steps in that lab’s `README.md` to run the scripts.