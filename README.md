# Personalized Query Rewriter - Take-Home Assignment

## Project Overview

This project is a simple, backend-focused system that rewrites user queries to be more personalized based on their simulated preferences. The goal is to demonstrate a problem-solving approach, backend skills, and a solid evaluation methodology.

## Dataset

The dataset used is synthetically generated and can be found in `data/synthetic_data.json`.

**Assumptions:**

- A user's profile and history can be abstracted into a list of keywords representing their interests (e.g., `["python", "api"]`).
- Personalization can be effectively achieved by appending relevant keywords from the user's profile to their original query.

The data is structured with two main keys:

- `users`: A dictionary of user profiles.
- `queries`: A list of query objects, each containing a `user_id`, an `original_query`, and a `ground_truth_rewrite` for evaluation purposes.

## Setup

1. Clone the repository:
   ```bash
   git clone <your-repo-link>
   cd query-rewriter-assignment
   ```
2. Create and activate a Python virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```
3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Execution

The entire process can be run in sequence:

1. **Generate Synthetic Data:**

   ```bash
   python -m src.data_generator
   ```

2. **Run the Query Rewriter:** This will process all queries in the dataset and save the results.

   ```bash
   python main.py
   ```

3. **Run the Evaluation:** This will compare the generated rewrites against the ground truth and produce a report.

   ```bash
   python -m src.evaluation
   ```

   The detailed results will be saved in `data/evaluation_report.csv`.

## Evaluation Methodology

Two types of metrics were used for evaluation:

1. **Automatic Metric: BERTScore**

   - **Justification:** BERTScore was chosen because it evaluates semantic similarity, not just word-for-word overlap. This is crucial as a good personalization might use synonyms or related concepts. It is more robust than metrics like BLEU or ROUGE for this task. The F1-score from BERTScore is reported as the primary automatic metric.

2. **Qualitative Metric: Heuristic Score**

   - **Justification:** A simple 1-3 qualitative score was implemented to capture the _degree_ of personalization, which is difficult for automated metrics to assess.
   - **Scale:**
     - `1 - Not Personalized`: The query was not changed.
     - `2 - Partially Personalized`: The query was changed but is not semantically close to the ideal rewrite.
     - `3 - Highly Personalized`: The query was changed and is semantically very similar to the ideal rewrite.

## Summary of Results

The system was evaluated against the ground-truth rewrites in the synthetic dataset.

The system achieved the following average scores:

- **Average BERT F1 Score:** 0.9110
- **Average ROUGE-L Score:** 0.6161
- **Average Qualitative Score:** 2.7500

These results indicate that the simple, rule-based rewriting logic is effective at incorporating user preferences and aligns well with the semantic meaning of the ideal rewrites. The high qualitative score suggests the personalization was consistently applied.
