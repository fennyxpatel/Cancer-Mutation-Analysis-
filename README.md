# 🧬 TCGA Breast Cancer Mutation Analysis

This project analyzes somatic mutation data from The Cancer Genome Atlas (TCGA) Breast Invasive Carcinoma cohort. The goal is to identify the most frequently mutated genes and explore mutation patterns across patients and mutation types using Python.

---

## 📌 Objectives

- Load and parse MAF (Mutation Annotation Format) files
- Identify the most frequently mutated genes in the dataset
- Find samples (patients) with the highest mutation burdens
- Explore mutation classifications by gene (e.g., missense, nonsense)
- Visualize results using bar plots and stacked charts

---

## 🧪 Dataset

- **Source**: [TCGA via cBioPortal](https://www.cbioportal.org/study/summary?id=brca_tcga)
- **File Used**: `data_mutations.txt` (Mutation data in MAF format)

---

## 🛠️ Tools & Libraries

- Python 3
- `pandas` for data manipulation
- `matplotlib` for plotting
- Jupyter Notebook 

---

## 📊 Key Analyses

- 🔬 Top 10 mutated genes (e.g., TP53, PIK3CA)
- 👤 Top 10 mutated samples (patients)
- 🔁 Breakdown of mutation types (missense, nonsense, frameshift) for top 5 genes
- 📈 Visualizations of mutation counts and classifications

---

## 📂 Repository Structure
---

## 📌 Example Visualizations

![image](https://github.com/user-attachments/assets/dcea3323-7af6-471a-982d-43cc5855cb71)

![image](https://github.com/user-attachments/assets/5fb6bdab-3842-4d14-8683-97c6d14d1077)


---

## 🧠 Summary

- TP53 and PIK3CA are among the most commonly mutated genes in breast cancer
- Mutation types vary by gene, with some showing high proportions of missense mutations
- This workflow demonstrates mutation profiling using real-world cancer genomics data

---

## 🔜 Future Work

- Extend analysis to additional TCGA cancer types
- Build an interactive Streamlit dashboard
- Integrate clinical metadata (e.g., survival, subtype)

---

## 👤 Author

**Fenny Patel**  
*Aspiring Bioinformatics Data Analyst*  
