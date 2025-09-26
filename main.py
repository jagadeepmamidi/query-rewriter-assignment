import json
from src.rewriter import SimpleQueryRewriter

def run_rewriting_for_all():
    """
    Loads all queries from the dataset, rewrites them, and stores the results.
    """
    rewriter = SimpleQueryRewriter('data/synthetic_data.json')
    queries_data = rewriter.data['queries']
    
    results = []

    for item in queries_data:
        user_id = item['user_id']
        original_query = item['original_query']
        ground_truth = item['ground_truth_rewrite']
        
        generated_rewrite = rewriter.rewrite_query(user_id, original_query)
        
        results.append({
            "user_id": user_id,
            "original": original_query,
            "ground_truth": ground_truth,
            "generated": generated_rewrite
        })
        
    # Save results to a file for evaluation
    with open('data/rewrite_results.json', 'w') as f:
        json.dump(results, f, indent=4)
        
    print("Rewriting complete. Results saved to data/rewrite_results.json")

if __name__ == '__main__':
    run_rewriting_for_all()