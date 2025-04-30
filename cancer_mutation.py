#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 29 19:36:30 2025

@author: fennypatel
"""
import pandas as pd

# Load MAF file, skip comment lines and problematic rows
df = pd.read_csv("data_mutations.txt", sep="\t", comment='#', on_bad_lines='skip', low_memory=False)

# Preview the data
df.head()

print(df.columns.tolist())

# Count how often each gene is mutated
mutation_counts = df['Hugo_Symbol'].value_counts()

# Show the top 10 mutated genes
print("Top 10 most mutated genes:")
print(mutation_counts.head(10))

mutation_types = df['Variant_Classification'].value_counts()

print("Most common mutation types:")
print(mutation_types)

import matplotlib.pyplot as plt


# Plot top 10 most mutated genes
mutation_counts.head(10).plot(kind='bar', title='Top 10 Mutated Genes')
plt.xlabel('Gene')
plt.ylabel('Mutation Count')
plt.tight_layout()
plt.show()

# Count mutations per patient/sample
mutations_per_sample = df['Tumor_Sample_Barcode'].value_counts()

# Show top 10 most mutated samples
print("Top 10 samples with the most mutations:")
print(mutations_per_sample.head(10))

# Find top 5 most frequently mutated genes
top_genes = df['Hugo_Symbol'].value_counts().head(5).index.tolist()
# Subset the dataframe to include only those top genes
df_top_genes = df[df['Hugo_Symbol'].isin(top_genes)]
# Create pivot table: gene on rows, mutation types as columns
gene_mutation_pivot = df_top_genes.pivot_table(
    index='Hugo_Symbol',
    columns='Variant_Classification',
    aggfunc='size',
    fill_value=0
)

# Show the table
print(gene_mutation_pivot)

# Plot stacked bar chart
gene_mutation_pivot.plot(kind='bar', stacked=True, figsize=(10,6), title='Mutation Types in Top 5 Genes')
plt.xlabel('Gene')
plt.ylabel('Mutation Count')
plt.tight_layout()
plt.show()

mutation_counts.to_csv("top_mutated_genes.csv")
mutations_per_sample.to_csv("mutations_per_sample.csv")
gene_mutation_pivot.to_csv("gene_mutation_breakdown.csv")
