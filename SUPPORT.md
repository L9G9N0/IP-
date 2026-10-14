# Academic Support & Community Channels

> **Document:** `SUPPORT.md`  
> **Platform:** Evidence-Based CCU Research & Data Engine  
> **Status:** Canonical Support Guide  
> **Last Updated:** October 2026  

---

## 1. Getting Help & Support Channels

If you encounter technical issues running the build scripts, have questions regarding specific chemical reactions or thermodynamic calculations, or wish to explore academic collaboration, please use the appropriate channel below:

| Inquery Type | Recommended Channel | Response SLA |
|---|---|---|
| **Script Execution / Python Bugs** | [GitHub Issues](https://github.com/L9G9N0/IP-/issues) | 2–4 business days |
| **Scientific / Data Questions** | [GitHub Discussions](https://github.com/L9G9N0/IP-/discussions) or Direct Email | 3–5 business days |
| **Data Correction / Discrepancy** | [Security & Integrity Protocol](SECURITY.md) | 48 hours |
| **Academic Collaboration / Co-Authorship** | Direct Email to Institutional Leads | 5 business days |

---

## 2. Institutional Contacts & Authors

This project is hosted at the **Indraprastha Institute of Information Technology Delhi (IIIT-Delhi)**, New Delhi, India.

### Research Leads
- **Anusha Rana**  
  *Lead Author & Research Lead*  
  Email: `anusharana510@gmail.com`  
  Affiliation: Department of Computer Science & Engineering, IIIT-Delhi

- **Rishab Raghuvanshi**  
  *Computational Chemistry & Pathway Modeling*  
  Affiliation: IIIT-Delhi

- **Amit Beniwal**  
  *Techno-Economic & Life-Cycle Systems Analysis*  
  Affiliation: IIIT-Delhi

- **Durlubh Kumar Sharma**  
  *Catalytic Reaction Engineering & Kinetics*  
  Affiliation: IIIT-Delhi

### Institutional Postal Address
```text
Indraprastha Institute of Information Technology Delhi (IIIT-Delhi)
Okhla Industrial Estate, Phase III
Near Govind Puri Metro Station
New Delhi, Delhi 110020, India
Official Portal: https://www.iiitd.ac.in
```

---

## 3. Frequently Asked Questions (FAQ)

### Q1: Can I reuse the CSV databases for my own meta-analysis or modeling study?
**Yes.** All datasets in `research/**/*.csv` are licensed under the **Creative Commons Attribution 4.0 International (CC BY 4.0)** license. You are free to share and adapt the data, provided you cite the repository and original authors (see [Citation in README.md](README.md#18-license--citation)).

### Q2: How do I resolve `SyntaxWarning: invalid escape sequence` in Python 3.12+?
Ensure you are using the latest version of the repository scripts. In Python 3.12 and 3.14, escape sequences inside multiline strings must use raw string literals (`r'''...'''`). All scripts in `scripts/` have been updated to use raw string formatting for LaTeX equations.

### Q3: Why is my preferred research paper not in the Master Literature Matrix?
The `MASTER_LITERATURE_MATRIX.csv` currently focuses on 22 landmark primary research benchmarks from 2020–2025 selected via our PRISMA protocol. If a paper represents an exceptional technological leap (e.g., >1,000 h operational stability, record Faradaic efficiency at industrial current density >300 mA/cm²), please submit a Pull Request following the guidelines in [CONTRIBUTING.md](CONTRIBUTING.md).

### Q4: Where can I find the unrevised original manuscript?
The exact original 26-page PDF is preserved in `manuscript/original/original_manuscript.pdf` and in the repository root as `CO2_UTILIZATION_ResearchPaper_2026 (1).pdf`. The extracted raw text is available in `original_manuscript_text.txt`.
