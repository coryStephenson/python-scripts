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


def angle_finder(file_path):
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
                    angle = angle_corpus(sentence)
                    print(f"   📌 Suggested Angle: {angle}")

        if text_opinionated:
            print("\n⚠️  Opinionated Language Detected: Consider reframing for neutrality.")
        else:
            print("\n✅ Neutral Tone: The text avoids strong opinions.")


def angle_corpus(sentence):
    """Suggest an angle based on the text's tone (e.g., Human Interest, Conflict)."""
    sentence_lower = sentence.lower()

    keywords = {
        "new development": ["innovation", "breakthrough", "new", "latest"],
        "local": ["community", "local", "neighborhood", "town"],
        "human interest": ["story", "person", "human", "emotional", "heartwarming"],
        "progress": ["growth", "advancement", "improvement", "better"],
        "consequence": ["impact", "result", "aftermath", "change"],
        "eminence": ["leader", "expert", "renowned", "distinguished"],
        "prominence": ["famous", "notable", "celebrity", "well-known"],
        "conflict": ["struggle", "war", "clash", "dispute"],
        "drama": ["mystery", "thriller", "twist", "unexpected"],
        "disaster": ["crisis", "catastrophe", "failure", "accident"],
        "timing and proximity": ["soon", "near", "upcoming", "current"]
    }

    for angle, sub_keywords in keywords.items():
        if any(keyword in sentence_lower for keyword in sub_keywords):
            return angle

    return "Human Interest"
