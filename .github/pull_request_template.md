## Summary & Scientific Context

Provide a brief explanation of the proposed changes, the motivations behind them, and how they relate to existing literature or code in this repository.

Fixes / Closes #(issue)

---

## Type of Change

- [ ] `fix`: Correction of a chemical reaction, thermodynamic parameter, DOI, or script bug.
- [ ] `feat`: Addition of a new literature benchmark, reaction pathway, or CLI feature.
- [ ] `docs`: Clarification or expansion of documentation, dossiers, or revision plans.
- [ ] `test`: New test cases or enhancements to CI verification.
- [ ] `refactor`: Code reorganization without functional changes.
- [ ] `chore`: Packaging, dependencies, or repository governance maintenance.

---

## Scientific Rigor & Evidence Checklist

- [ ] All new quantitative metrics are backed by verified primary DOIs.
- [ ] Chemical reactions balance for atoms and formal charges.
- [ ] Enthalpy ($\Delta H^\circ$) and Gibbs energy ($\Delta G^\circ$) are consistent with NIST WebBook data.
- [ ] Faradaic efficiency is reported alongside cell voltage, current density, and single-pass conversion where applicable.

---

## Code Quality & Verification Checklist

- [ ] Code modifications were made in `scripts/`, NOT by hand-editing generated CSV files.
- [ ] Regeneated all affected datasets via `make build` or specific Python scripts.
- [ ] Ran automated tests and verified 100% pass: `make test` (`pytest`).
- [ ] Ran static code analysis and linting: `make lint` (`ruff`).
- [ ] Checked CSV files conform to RFC 4180 without mismatched column counts.
