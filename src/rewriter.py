import json

class SimpleQueryRewriter:
    def __init__(self, data_path):
        with open(data_path, 'r') as f:
            self.data = json.load(f)
        self.users = self.data['users']

    def rewrite_query(self, user_id, query):
        """
        Rewrites a query based on the user's preferences.
        """
        if user_id not in self.users:
            return query # Return original query if user is not found

        user_prefs = self.users[user_id].get("preferences", [])
        
        # Simple logic: find preferences mentioned in the query and append others
        # that are not mentioned.
        
        rewritten_query = query
        appended_prefs = []

        for pref in user_prefs:
            if pref.lower() not in query.lower():
                appended_prefs.append(pref)
        
        if appended_prefs:
            rewritten_query += " " + " ".join(appended_prefs)
            
        return rewritten_query

if __name__ == '__main__':
    # Demo of the rewriter
    rewriter = SimpleQueryRewriter('data/synthetic_data.json')
    
    # Example 1: Python Developer
    user1_query = "how to build a web service"
    rewritten1 = rewriter.rewrite_query("user_101", user1_query)
    print(f"User: user_101 (Python Developer)")
    print(f"Original:  {user1_query}")
    print(f"Rewritten: {rewritten1}")
    print("-" * 20)

    # Example 2: Data Analyst
    user2_query = "clean up my dataset"
    rewritten2 = rewriter.rewrite_query("user_102", user2_query)
    print(f"User: user_102 (Data Analyst)")
    print(f"Original:  {user2_query}")
    print(f"Rewritten: {rewritten2}")