import pandas as pd
import language_tool_python

tool = language_tool_python.LanguageTool('en-US')
df = pd.read_csv("clean_data.csv")

word_counts = []
# sentence_counts = []
avg_word_lengths = []
unique_words_ratio = []
Sentence_complexity_scores = []
strong_verbs_counts=[]
gramer_eror = []

conjunctions = [
    'and', 'but', 'or', 'so',
    'because', 'though', 'while', 'when',
    'if', 'until', 'since', 'after', 'before',
    'which', 'that', 'who'
]

strong_verbs = [
     # Tier 1 - Ratio 10+
    "started", "learned", "changed", "improved", "practiced",
    "worked", "realized", "stopped", "received", "invested",
    # Tier 2 - Ratio 5-9
    "failed", "recognized", "helped", "created", "developed",
    "used", "treated", "turned", "saved", "stayed",
    "expected", "reviewed", "noticed", "asked", "respected",
    # Tier 3 - Ratio 2-5
    "identified", "designed", "decided", "completed", "accepted",
    "volunteered", "pushed", "reduced", "discovered", "trusted",
    "focused", "prepared", "followed", "disagreed", "accelerated",
    "restructured", "shaped", "mattered", "dropped"
]

for text in df["answer"]:
    
    # 🔥 handle NaN / empty
    if pd.isna(text):
        text = ""
    
    # word count
    words = text.lower().split()
    word_count = len(words)

    # avg word length
    total_length = 0
    for word in words:
        total_length += len(word.strip('.,!?;:"\'-'))
    
    avg_word_length = total_length / word_count if word_count > 0 else 0
    
    # unique words
    clean_words = []
    for word in words:
        clean_word = word.strip('.,!?;:"\'-')
        clean_words.append(clean_word)

    unique_words = set(clean_words)
    unique_counts = len(unique_words)
    ratio = unique_counts / word_count if word_count > 0 else 0
    

    # sentence complexity
    count = 0
    for word in clean_words:
        if word in conjunctions:
            count += 1

    # 🔥 STRONG VERB COUNT (FIXED)
    negations = ['no', 'not', 'never', 'without']

    strong_verbs_count = 0

    for i in range(len(clean_words)):
        word = clean_words[i]

        if word in strong_verbs:

            prev1 = clean_words[i - 1] if i >= 1 else ""
            prev2 = clean_words[i - 2] if i >= 2 else ""

            if prev1 not in negations and prev2 not in negations:
                strong_verbs_count += 1
    

    #gramer_count
    if text.strip() == "":
       error_count = 0
    else:
       matches = tool.check(text)
       error_count = len(matches)

    
    # store
    word_counts.append(word_count)
    avg_word_lengths.append(round(avg_word_length, 6))#round
    unique_words_ratio.append(ratio)
    Sentence_complexity_scores.append(count)
    strong_verbs_counts.append(strong_verbs_count)
    gramer_eror.append(error_count)


    

# add columns
df["word_count"] = word_counts
df["avg_word_length"] = avg_word_lengths
df["unique_word_ratio"] = unique_words_ratio
df["sentence_complexity_score"] = Sentence_complexity_scores
df["strong_verbs_count"] = strong_verbs_counts
df["grammar_error_count"]=gramer_eror

print(df.head())

df.to_csv("featured_data_v9.csv", index=False)
print(df.shape)