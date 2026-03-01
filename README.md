# Statistical Analysis Project — Mobile Sales Data

This project fulfills the Udacity Data and Statistical Reasoning capstone. It includes descriptive statistics, visualizations, and a hypothesis test on the Mobile Sales dataset from Kaggle.

## Contents

- **analysis.ipynb** — Jupyter notebook: load data, descriptive statistics, ≥3 visualizations, one hypothesis test, and a short summary.
- **Statistical_Analysis_Report.md** — Written report (Overview, Dataset, Methods, Results, Non-technical interpretation, Limitations/Bias, References) with in-text citations.
- **requirements.txt** — Python dependencies. Install with: `pip install -r requirements.txt`

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. (Optional) Configure Kaggle API so the notebook can download the dataset:
   - Place `kaggle.json` in `~/.kaggle/` or set environment variables.
   - Or download the dataset from [Kaggle – Mobile Sales Data](https://www.kaggle.com/datasets/syedaeman2212/mobile-sales-data) and place the CSV in this folder; the notebook will use it if the Kaggle download is skipped.

## Running the notebook

Open and run `analysis.ipynb` from top to bottom (e.g. in Jupyter Notebook, JupyterLab, or VS Code with the Jupyter extension). The notebook downloads the dataset via `kagglehub` (or uses a local CSV if present).

## Generating the PDF report

The project expects **Statistical_Analysis_Report.pdf**.

- **Option A:** Run the script (requires `fpdf2`):
  ```bash
  pip install fpdf2
  python generate_report_pdf.py
  ```
- **Option B:** Open `Statistical_Analysis_Report.md` in VS Code (or any editor), then use **File → Print → Save as PDF** (or “Print to PDF”).
- **Option C:** If you have `pandoc`: `pandoc Statistical_Analysis_Report.md -o Statistical_Analysis_Report.pdf`

## Submission checklist

- [ ] **analysis.ipynb** runs top to bottom without errors  
- [ ] **Statistical_Analysis_Report.pdf** is included (generate from `.md` as above)  
- [ ] **requirements.txt** is included (for submission you may run `pip freeze > requirements.txt` to capture your exact environment)  
- [ ] Dataset: the notebook downloads it via kagglehub; optionally include the CSV in the submission folder if required

## Citation requirements

The report cites:

1. Lusa et al. (2024), *Initial data analysis for longitudinal studies to build a solid foundation for reproducible analysis*, PLOS One — for IDA and reproducibility.
2. McDonald, *Handbook of Biological Statistics* — for hypothesis test choice and interpretation.

Both appear in-text and in the References section of the report.
