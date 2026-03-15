import spacy
from collections import defaultdict
from textblob import TextBlob

def is_opinionated(token, sentence_text, subjectivity_threshold=0.4):
    """
    Determine if a token is opinionated using two checks:
    1. The token's POS tag is opinion-relevant (ADJ, ADV, VERB)
    2. The sentence containing it has a TextBlob subjectivity score above the threshold
    """
    if token.pos_ not in ["ADJ", "ADV", "VERB"]:
        return False

    blob = TextBlob(sentence_text)
    return blob.sentiment.subjectivity > subjectivity_threshold


def angle_detect(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            text = file.read()
        doc = nlp(text)

        # Track opinionated tokens and their sentences
        opinionated_tokens = defaultdict(list)

        for sent in doc.sents:
            sentence_text = sent.text.strip()
            for token in sent:
                if is_opinionated(token, sentence_text):
                    opinionated_tokens[token.text].append(sentence_text)

        # Check for opinionated words in the text
        opinionated_words = [
            "should", "must", "prefer", "dislike", "believe", "argue", "claim",
            "advocate", "oppose", "criticize", "improve", "enhance", "better",
            "worse", "essential", "unnecessary", "necessary", "important"
        ]
        text_opinionated = any(word in text.lower() for word in opinionated_words)

        # --- Opinion Analysis Results ---
        print("\n=== OPINION ANALYSIS RESULTS ===")

        if not opinionated_tokens:
            print("✅ No strong opinionated tokens detected. The text reads objectively.")
        else:
            for token, sentences in opinionated_tokens.items():
                # Deduplicate sentences for this token
                seen = set()
                for sentence in sentences:
                    if sentence in seen:
                        continue
                    seen.add(sentence)

                    print(f"\n🔍 Token: '{token}'")
                    print(f"   → Full sentence: '{sentence}'")

                    # Subjectivity score for context
                    blob = TextBlob(sentence)
                    polarity = blob.sentiment.polarity
                    subjectivity = blob.sentiment.subjectivity
                    print(f"   📊 Sentiment — Polarity: {polarity:.2f} (negative=-1, positive=1) | Subjectivity: {subjectivity:.2f} (objective=0, subjective=1)")

                    # Angle suggestion
                    angle = detect_angle(sentence)
                    print(f"   📌 Suggested Angle: {angle}")

        if text_opinionated:
            print("\n⚠️  Opinionated Language Detected: Consider reframing for neutrality.")
        else:
            print("\n✅ Neutral Tone: The text avoids strong opinions.")

def content_edit(file_path):
    # Docstring
    """
        Analyzes a given text for:

          Intent (what the article is focused on)
          Topic (overlap in content)
          Angle (underlying opinion)
            Returns weak/strong recommendations based on detected patterns.
    """

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()

        # Load spaCy model for basic NLP analysis
        nlp = spacy.load("en_core_web_sm")

        # Process the text
        doc = nlp(text)

        # --- Weak Recommendations (General Checks)
        print("=== WEAK RECOMMENDATIONS (General Checks) ===")

        # 1. **Entity Detection (5W2H Analysis)**
        entities = [(ent.text, ent.label_) for ent in doc.ents]
        print("\n**Key Entities (Intent Indicators):**")
        for ent, label in entities:
            print(f"- {ent} ({label})")

        # 2. **Topic Overlap (Frequent Thematic Words)**
        topic_words = defaultdict(int)
        for token in doc:
            if token.is_alpha and not token.is_stop:
                topic_words[token.text.lower()] += 1
        sorted_words = sorted(topic_words.items(), key=lambda x: x[1], reverse=True)
        print("\n**Top Thematic Words (Topic Overlap):**")
        for word, freq in sorted_words[:5]:
            print(f"- {word} ({freq})")

        # --- Strong Recommendations (Conditional Checks)
        print("\n=== STRONG RECOMMENDATIONS (Conditional Checks) ===")

        # 3. **Angle Detection (Underlying Opinion)**
        angle_detect(file_path)


        # --- Suggested Edits Based on Sample Text (Conditional Logic)
        if text:
            print("\n=== SUGGESTED STRUCTURE EDIT (Conditional Checks) ===")

        # --- Weak: Check for Missing Transitions (Coherence)
        transitions = ["however", "therefore", "consequently", "in contrast"]
        missing_transitions = [t for t in transitions if t in [token.text.lower() for token in doc]]
        if not missing_transitions:
            print("⚠ Weak: Missing transitions (e.g., 'however', 'therefore'). Consider adding for clarity.")

        # --- Strong: Check for Complex Sentences (Sentence Length)
        long_sentences = [sent for sent in doc.sents if len(sent) > 20]
        if long_sentences:
            print("✅ Strong: Long sentences detected. Suggest splitting for clarity.")
            for sent in long_sentences:
                print(f"- Example: '{sent.text}' → Consider breaking into shorter sentences.")

        # --- Strong: Check for Overlapping Topic (Sample Text Alignment)
        text_words = set(text.lower().split())
        doc_words = set(token.text.lower() for token in doc if token.is_alpha and not token.is_stop)
        overlap = text_words & doc_words

        if not overlap:
            print("⚠ Weak: Topic overlap missing. Ensure sample_text aligns with content.")
        else:
            print("✅ Strong: Topic overlap confirmed. Proceed with confidence.")

        # --- Strong: Check for Opinionated Language (Sample Text Alignment)
        text_opinion_indicators = [
            "should", "must", "prefer", "dislike", "believe", "argue"
        ]
        text_opinionated = any(
            word in text.lower() for word in text_opinion_indicators
        )

        if sample_opinionated:
            print("✅ Strong: Sample text contains opinionated language. Ensure consistency.")
        else:
            print("⚠ Weak: Sample text lacks explicit opinion. Clarify stance.")

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except PermissionError:
        print(f"Error: Permission denied when trying to read '{file_path}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

# Example usage with the provided text file
if __name__ == "__main__":
    # Replace with your actual file path
    text_file = "text.txt"
    content_edit(text_file)
