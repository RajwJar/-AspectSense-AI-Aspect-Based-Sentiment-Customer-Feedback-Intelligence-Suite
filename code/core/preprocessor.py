"""
Text Preprocessor Module for AspectSense AI
Handles text normalization, contraction expansion, clause segmentation,
tokenization, stopword filtering, and negation handling.
"""

import re
from typing import List, Dict, Any, Tuple


CONTRACTIONS_DICT: Dict[str, str] = {
    "ain't": "am not", "aren't": "are not", "can't": "cannot", "can't've": "cannot have",
    "'cause": "because", "could've": "could have", "couldn't": "could not",
    "didn't": "did not", "doesn't": "does not", "don't": "do not", "hadn't": "had not",
    "hasn't": "has not", "haven't": "have not", "he'd": "he would", "he'll": "he will",
    "he's": "he is", "how'd": "how did", "how'll": "how will", "how's": "how is",
    "i'd": "i would", "i'll": "i will", "i'm": "i am", "i've": "i have",
    "isn't": "is not", "it'd": "it would", "it'll": "it will", "it's": "it is",
    "let's": "let us", "might've": "might have", "mightn't": "might not",
    "must've": "must have", "mustn't": "must not", "shan't": "shall not",
    "she'd": "she would", "she'll": "she will", "she's": "she is",
    "should've": "should have", "shouldn't": "should not", "that's": "that is",
    "there's": "there is", "they'd": "they would", "they'll": "they will",
    "they're": "they are", "they've": "they have", "wasn't": "was not",
    "we'd": "we would", "we'll": "we will", "we're": "we are", "we've": "we have",
    "weren't": "were not", "what'll": "what will", "what're": "what are",
    "what's": "what is", "what've": "what have", "where'd": "where did",
    "where's": "where is", "where've": "where have", "who'll": "who will",
    "who's": "who is", "who've": "who have", "won't": "will not",
    "would've": "would have", "wouldn't": "would not", "you'd": "you would",
    "you'll": "you will", "you're": "you are", "you've": "you have"
}

NEGATION_TOKENS = {
    "not", "no", "never", "neither", "nor", "barely", "hardly", "scarcely",
    "seldom", "cannot", "without", "lack", "lacks", "lacking"
}

CLAUSE_DELIMITERS = [
    r",\s*but\s+", r",\s*however\s+", r",\s*although\s+", r",\s*though\s+",
    r",\s*yet\s+", r",\s*nevertheless\s+", r";\s*", r"\.\s+"
]


class TextPreprocessor:
    """
    NLP Preprocessing Engine for AspectSense AI.
    Provides robust multi-phase text normalization, sentence segmentation,
    and syntactic token manipulation tailored for Aspect-Based Sentiment Analysis.
    """

    def __init__(self, preserve_case_for_ner: bool = False):
        self.preserve_case = preserve_case_for_ner
        self.contractions_pattern = re.compile(
            r'\b(' + '|'.join(re.escape(key) for key in CONTRACTIONS_DICT.keys()) + r')\b',
            flags=re.IGNORECASE
        )

    def expand_contractions(self, text: str) -> str:
        """Expands common English contractions into standard form."""
        def replace(match):
            contraction = match.group(0).lower()
            replacement = CONTRACTIONS_DICT.get(contraction, contraction)
            if match.group(0)[0].isupper():
                return replacement.capitalize()
            return replacement

        return self.contractions_pattern.sub(replace, text)

    def clean_text(self, text: str) -> str:
        """Removes HTML artifacts, weird formatting, and normalizes whitespaces."""
        if not text or not isinstance(text, str):
            return ""

        # Remove HTML tags
        text = re.sub(r'<[^>]+>', ' ', text)
        # Remove URLs
        text = re.sub(r'https?://\S+|www\.\S+', ' ', text)
        # Expand contractions
        text = self.expand_contractions(text)
        # Normalize redundant punctuation (e.g. !!!! -> !)
        text = re.sub(r'([!?.]){2,}', r'\1', text)
        # Normalize whitespace
        text = re.sub(r'\s+', ' ', text).strip()
        return text

    def segment_into_clauses(self, text: str) -> List[str]:
        """
        Splits a compound review text into discrete clauses based on contrastive
        conjunctions and sentence boundaries. Crucial for separating opposing
        aspect sentiments (e.g., 'Great screen, but terrible battery').
        """
        cleaned = self.clean_text(text)
        pattern = '|'.join(CLAUSE_DELIMITERS)
        raw_clauses = re.split(pattern, cleaned, flags=re.IGNORECASE)
        clauses = [c.strip() for c in raw_clauses if c and len(c.strip()) > 2]
        return clauses if clauses else [cleaned]

    def tokenize(self, text: str, lower: bool = True) -> List[str]:
        """Extracts word tokens while preserving hyphens and apostrophes."""
        if lower:
            text = text.lower()
        tokens = re.findall(r"\b[a-zA-Z0-9_\-]+(?:\'[a-z]+)?\b", text)
        return tokens

    def tag_negations(self, tokens: List[str], window: int = 3) -> List[Tuple[str, bool]]:
        """
        Applies grammatical negation tagging to token sequence.
        Returns pairs of (token, is_negated).
        """
        tagged: List[Tuple[str, bool]] = []
        neg_counter = 0

        for tok in tokens:
            lower_tok = tok.lower()
            if lower_tok in NEGATION_TOKENS:
                neg_counter = window
                tagged.append((tok, False))
                continue

            if neg_counter > 0:
                tagged.append((tok, True))
                neg_counter -= 1
            else:
                tagged.append((tok, False))

        return tagged

    def preprocess_pipeline(self, text: str) -> Dict[str, Any]:
        """Runs complete pre-processing workflow and returns rich metadata."""
        cleaned = self.clean_text(text)
        clauses = self.segment_into_clauses(text)
        tokens = self.tokenize(cleaned)
        negation_tagged = self.tag_negations(tokens)

        return {
            "original_text": text,
            "cleaned_text": cleaned,
            "clause_count": len(clauses),
            "clauses": clauses,
            "tokens": tokens,
            "token_count": len(tokens),
            "negation_tagged": negation_tagged,
        }
