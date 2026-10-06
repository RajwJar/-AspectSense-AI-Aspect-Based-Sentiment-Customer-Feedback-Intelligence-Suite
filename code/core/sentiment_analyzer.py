"""
Sentiment Analyzer Module for AspectSense AI
Provides clause-level and aspect-level polarity calculation,
subjectivity estimation, emotion classification, and customer urgency triage.
"""

import math
import re
from typing import List, Dict, Any, Tuple
from .preprocessor import TextPreprocessor


# Sentiment polarity lexicon with domain weights
POLARITY_LEXICON: Dict[str, float] = {
    # Strong positive (+2.5 to +3.5)
    "stunning": 3.2, "gorgeous": 3.0, "exceptional": 3.4, "unmatched": 3.5,
    "flawless": 3.5, "spectacular": 3.4, "incredible": 3.2, "fastest": 3.0,
    "unbeatable": 3.3, "sumptuous": 3.0, "audiophile": 2.8, "perfect": 3.2,
    "masterpiece": 3.5, "breathtaking": 3.3,
    # Standard positive (+1.0 to +2.4)
    "great": 2.0, "good": 1.5, "snappy": 1.8, "crisp": 1.6, "solid": 1.5,
    "bright": 1.4, "reliable": 2.2, "intuitive": 1.9, "punchy": 1.7,
    "comfortable": 2.0, "smooth": 1.8, "fast": 1.8, "cheap": 1.0, "worth": 1.7,
    "clean": 1.8, "powerful": 2.1, "pleasure": 2.0, "delight": 2.5,
    "saved": 1.5, "whisper-quiet": 2.2, "tactile": 1.6, "adequate": 0.8,
    # Mild/Neutral (-0.5 to +0.5)
    "standard": 0.1, "basic": -0.2, "decent": 1.1, "average": 0.0,
    # Negative (-1.0 to -2.4)
    "barely": -1.2, "struggles": -1.5, "cheap": -1.1, "cracked": -2.0,
    "grainy": -1.6, "potato": -1.8, "insufficient": -1.8, "rattles": -1.5,
    "sweat": -1.2, "muffled": -1.7, "cluttered": -1.4, "confusing": -1.6,
    "rigid": -1.5, "steep": -1.2, "bulky": -1.3, "tight": -1.1,
    "outdated": -1.8, "warmer": -1.0, "mushy": -1.4, "slow": -1.6,
    "overheating": -2.3, "overheats": -2.3, "annoying": -2.0, "fails": -2.2,
    # Strong Negative (-2.5 to -3.8)
    "overpriced": -2.5, "junk": -3.2, "refused": -2.8, "terrible": -3.0,
    "disastrous": -3.5, "fried": -3.0, "lost": -2.4, "avoid": -3.2,
    "snapped": -2.8, "bug": -2.0, "unacceptable": -3.4, "corrupted": -3.2,
    "painful": -2.8, "freezing": -2.5, "paperweight": -3.0, "sewer": -3.2,
    "odor": -2.4, "excruciatingly": -3.2, "nightmare": -3.5, "broken": -2.8,
    "dismissive": -2.9, "laughed": -2.7, "outage": -3.0, "rage": -3.5,
    "fury": -3.5, "disaster": -3.5, "worst": -3.6, "hate": -3.0
}

INTENSIFIERS: Dict[str, float] = {
    "absolutely": 1.4, "super": 1.3, "extremely": 1.4, "very": 1.25,
    "completely": 1.35, "totally": 1.3, "utterly": 1.4, "terribly": 1.3,
    "insanely": 1.35, "barely": 0.6, "slightly": 0.7, "somewhat": 0.8
}

EMOTION_KEYWORDS = {
    "joy": ["flawless", "delight", "spectacular", "incredible", "superb", "unmatched", "worth", "stunning"],
    "anger": ["fury", "rage", "laughed", "unacceptable", "nightmare", "dismissive", "scam", "corrupted"],
    "disappointment": ["disaster", "struggles", "failed", "broken", "cracked", "muffled", "annoying", "overpriced"],
    "frustration": ["excruciatingly", "confusing", "outage", "freezing", "refused", "lost", "delay"]
}

CRITICAL_URGENCY_KEYWORDS = [
    "refused refund", "legal", "lawsuit", "unacceptable", "nightmare",
    "fried", "corrupted", "fire", "danger", "outage", "fury", "disaster",
    "worst experience", "scam"
]

HIGH_URGENCY_KEYWORDS = [
    "overheating", "overheats", "cracked", "broken", "snapped",
    "failed", "lost shipment", "odor", "freezing", "bug", "terrible"
]


class SentimentAnalyzer:
    """
    Computes fine-grained aspect polarity and sentence-level sentiment metrics.
    """

    def __init__(self):
        self.preprocessor = TextPreprocessor()

    def score_text_fragment(self, fragment: str) -> Tuple[float, float]:
        """
        Calculates polarity (-1.0 to 1.0) and subjectivity (0.0 to 1.0) for a text fragment.
        """
        cleaned = self.preprocessor.clean_text(fragment)
        tokens = self.preprocessor.tokenize(cleaned)
        tagged_negations = self.preprocessor.tag_negations(tokens)

        total_score = 0.0
        sentiment_words_count = 0
        subjective_weight = 0.0

        for i, (token, is_negated) in enumerate(tagged_negations):
            word = token.lower()
            if word in POLARITY_LEXICON:
                base_score = POLARITY_LEXICON[word]
                # Check intensifier before this word
                multiplier = 1.0
                if i > 0:
                    prev_word = tagged_negations[i - 1][0].lower()
                    if prev_word in INTENSIFIERS:
                        multiplier = INTENSIFIERS[prev_word]

                score = base_score * multiplier
                # Flip sign if negated
                if is_negated:
                    score = -score * 0.85

                total_score += score
                sentiment_words_count += 1
                subjective_weight += abs(base_score)

        if sentiment_words_count == 0:
            return 0.0, 0.0

        # Normalization using hyperbolic tangent for smooth [-1.0, 1.0] scaling
        normalized_polarity = math.tanh(total_score / 3.0)
        subjectivity = min(1.0, (subjective_weight / max(len(tokens), 1)) * 1.5)

        return round(normalized_polarity, 3), round(subjectivity, 3)

    def classify_polarity_label(self, score: float) -> str:
        """Maps continuous polarity to discrete sentiment label."""
        if score >= 0.15:
            return "positive"
        elif score <= -0.15:
            return "negative"
        else:
            return "neutral"

    def detect_emotion(self, text: str, polarity: float) -> str:
        """Determines dominant emotional tone."""
        text_lower = text.lower()
        matched_emotions = []

        for emotion, terms in EMOTION_KEYWORDS.items():
            for term in terms:
                if re.search(r'\b' + re.escape(term) + r'\b', text_lower):
                    matched_emotions.append(emotion)

        if matched_emotions:
            return matched_emotions[0]

        if polarity > 0.4:
            return "joy"
        elif polarity < -0.4:
            return "frustration"
        return "neutral"

    def determine_urgency(self, text: str, polarity: float) -> str:
        """Categorizes customer issue urgency level."""
        text_lower = text.lower()

        if any(keyword in text_lower for keyword in CRITICAL_URGENCY_KEYWORDS) or polarity <= -0.75:
            return "Critical"
        elif any(keyword in text_lower for keyword in HIGH_URGENCY_KEYWORDS) or polarity <= -0.45:
            return "High"
        elif polarity < -0.1:
            return "Medium"
        else:
            return "Low"

    def analyze_aspect_sentiments(self, text: str, aspect_data: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Scores sentiment for each detected aspect based on its local clause context.
        """
        aspect_results = []
        aspect_mentions = aspect_data.get("aspect_mentions", [])

        for mention in aspect_mentions:
            clause = mention.get("clause", text)
            clause_polarity, clause_subjectivity = self.score_text_fragment(clause)
            aspect_sentiment = self.classify_polarity_label(clause_polarity)

            aspect_results.append({
                "aspect_term": mention["term"],
                "canonical_aspect": mention["canonical_aspect"],
                "clause_context": clause,
                "clause_index": mention.get("clause_index", 0),
                "polarity_score": clause_polarity,
                "subjectivity_score": clause_subjectivity,
                "sentiment": aspect_sentiment
            })

        return aspect_results
