import pandas as pd
from collections import Counter
import math

# Play Golf dataset
data = {
    'Outlook': ['Rainy','Rainy','Overcast','Sunny','Sunny','Sunny','Overcast','Rainy',
                'Rainy','Sunny','Rainy','Overcast','Overcast','Sunny'],
    'Temperature': ['Hot','Hot','Hot','Mild','Cool','Cool','Cool','Mild',
                    'Cool','Mild','Mild','Mild','Hot','Mild'],
    'Humidity': ['High','High','High','High','Normal','Normal','Normal','High',
                 'Normal','Normal','Normal','High','Normal','High'],
    'Windy': ['False','True','False','False','False','True','True','False',
              'False','False','True','True','False','True'],
    'PlayGolf': ['No','No','Yes','Yes','Yes','No','Yes','No',
                 'Yes','Yes','Yes','Yes','Yes','No']
}

df = pd.DataFrame(data)

def prior_probabilities(df, target):
    total = len(df)
    counts = Counter(df[target])
    priors = {k: v / total for k, v in counts.items()}
    return priors


def conditional_probability(df, feature, feature_value, target, target_value):
    subset = df[df[target] == target_value]
    count_feature = len(subset[subset[feature] == feature_value])
    return count_feature / len(subset)


def naive_bayes_predict(df, X, target):
    priors = prior_probabilities(df, target)
    results = {}

    for class_value in priors:
        prob = priors[class_value]
        
        for feature, feature_value in X.items():
            cond_prob = conditional_probability(
                df, feature, feature_value, target, class_value
            )
            prob *= cond_prob
        
        results[class_value] = prob

    return results

X_test = {
    'Outlook': 'Rainy',
    'Temperature': 'Cool',
    'Humidity': 'High',
    'Windy': 'True'
}

result = naive_bayes_predict(df, X_test, 'PlayGolf')

print("Posterior Probabilities:")
for k, v in result.items():
    print(f"P(PlayGolf={k}) = {v}")

print("\nPrediction:", max(result, key=result.get))
