import json
from bert_score import score as bert_scorer
from rouge_score import rouge_scorer
import pandas as pd

class Evaluator:
    def __init__(self, results_path):
        with open(results_path, 'r') as f:
            self.results = json.load(f)

    def _qualitative_heuristic(self, original, generated, ground_truth):
        """
        A simple heuristic for personalization.
        1 - Not Personalized: Generated is same as original.
        2 - Partially Personalized: Generated is different, but doesn't match ground truth well.
        3 - Highly Personalized: Generated is very similar to ground truth.
        """
        if generated.strip() == original.strip():
            return 1
        
        # Simple similarity check for "Highly Personalized"
        gt_words = set(ground_truth.split())
        gen_words = set(generated.split())
        if len(gt_words.intersection(gen_words)) / len(gt_words.union(gen_words)) > 0.5:
            return 3
        
        return 2

    def evaluate(self):
        """
        Runs both automatic and qualitative evaluations.
        """
        candidates = [item['generated'] for item in self.results]
        references = [item['ground_truth'] for item in self.results]

        # 1. Automatic Evaluation: BERTScore
        # The model will be downloaded on first run.
        P, R, F1 = bert_scorer(candidates, references, lang="en", verbose=True)
        
        # 2. Qualitative & Other Metrics
        eval_results = []
        rouge = rouge_scorer.RougeScorer(['rougeL'], use_stemmer=True)

        for i, item in enumerate(self.results):
            original = item['original']
            generated = item['generated']
            ground_truth = item['ground_truth']
            
            # ROUGE-L Score
            rouge_l_score = rouge.score(ground_truth, generated)['rougeL'].fmeasure
            
            # Qualitative Score
            qual_score = self._qualitative_heuristic(original, generated, ground_truth)

            eval_results.append({
                "original_query": original,
                "generated_rewrite": generated,
                "ground_truth": ground_truth,
                "bert_f1": F1[i].item(),
                "rouge_l": rouge_l_score,
                "qualitative_score": qual_score
            })
            
        return pd.DataFrame(eval_results)

if __name__ == '__main__':
    evaluator = Evaluator('data/rewrite_results.json')
    df_results = evaluator.evaluate()
    
    # Save to CSV for easy viewing
    df_results.to_csv('data/evaluation_report.csv', index=False)
    
    print("Evaluation Complete!")
    print(df_results)
    
    # Print average scores
    print("\n--- Average Scores ---")
    print(f"Average BERT F1 Score: {df_results['bert_f1'].mean():.4f}")
    print(f"Average ROUGE-L Score: {df_results['rouge_l'].mean():.4f}")
    print(f"Average Qualitative Score: {df_results['qualitative_score'].mean():.4f}")