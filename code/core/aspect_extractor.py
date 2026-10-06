"""
Aspect Extractor Module for AspectSense AI
Extracts fine-grained aspect targets from customer reviews using
syntactic heuristics, compound noun phrases, and domain ontology mappings.
"""

import os
import json
import re
from typing import List, Dict, Any, Optional, Set
from .preprocessor import TextPreprocessor


DEFAULT_ASPECT_CATEGORIES = {
    "battery": ["battery", "battery life", "battery longevity", "charging", "charger", "fast charging", "mah"],
    "screen_display": ["screen", "display", "oled", "amoled", "refresh rate", "brightness", "resolution", "panel"],
    "camera": ["camera", "photo", "lens", "low-light", "zoom", "sensors", "video recording", "night mode", "webcam"],
    "performance": ["performance", "speed", "processor", "chipset", "lag", "snappy", "multitasking", "stutter", "cpu", "gpu", "ram"],
    "build_durability": ["build quality", "chassis", "durability", "casing", "materials", "hinge", "frame", "headband"],
    "pricing_value": ["price", "pricing", "expensive", "dollar", "cost", "value", "overpriced", "cheap", "subscription fee", "quota"],
    "customer_service": ["customer service", "support", "warranty", "replacement", "repair", "service center", "support ticket", "concierge"],
    "audio_sound": ["audio clarity", "sound", "soundstage", "treble", "mids", "bass", "noise cancellation", "anc", "speakers", "microphone"],
    "comfort_ergonomics": ["comfort", "ear pads", "cushions", "headband", "keyboard", "trackpad", "clamping pressure", "bed"],
    "software_reliability": ["software", "bloatware", "fingerprint sensor", "app", "ui", "sync", "uptime", "downtime", "firmware", "bug", "crash"],
    "connectivity": ["bluetooth", "wi-fi", "wifi", "wireless", "usb-c", "ports", "hdmi", "connection"],
    "cleanliness_hospitality": ["cleanliness", "dirty", "smell", "odor", "towels", "housekeeping", "room", "decor", "pool", "buffet"]
}


class AspectExtractor:
    """
    Extracts multi-aspect targets from customer feedback texts.
    Combines domain ontology matching with compound noun collocation detection.
    """

    def __init__(self, lexicon_path: Optional[str] = None):
        self.preprocessor = TextPreprocessor()
        self.ontology = self._load_ontology(lexicon_path)
        self.aspect_index = self._build_aspect_index()

    def _load_ontology(self, lexicon_path: Optional[str]) -> Dict[str, Dict[str, List[str]]]:
        if lexicon_path and os.path.exists(lexicon_path):
            try:
                with open(lexicon_path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    return data.get("domains", {})
            except Exception:
                pass
        return DEFAULT_ASPECT_CATEGORIES

    def _build_aspect_index(self) -> Dict[str, str]:
        """Flattens ontology into term -> canonical aspect category mapping."""
        mapping: Dict[str, str] = {}
        # Load from DEFAULT_ASPECT_CATEGORIES
        for category, terms in DEFAULT_ASPECT_CATEGORIES.items():
            for term in terms:
                mapping[term.lower()] = category

        # Also add any domain-specific terms from ontology
        if isinstance(self.ontology, dict):
            for domain_or_cat, val in self.ontology.items():
                if isinstance(val, dict):
                    for aspect, terms in val.items():
                        for term in terms:
                            mapping[term.lower()] = aspect
                elif isinstance(val, list):
                    for term in val:
                        mapping[term.lower()] = domain_or_cat
        return mapping

    def extract_compound_nouns(self, text: str) -> List[str]:
        """
        Extracts multi-word noun candidates (e.g. 'battery life', 'customer support',
        'noise cancellation', 'screen resolution') via regex n-gram collocations.
        """
        cleaned = self.preprocessor.clean_text(text).lower()
        candidates: Set[str] = set()

        # Check existing known multi-word aspect keys
        for term in self.aspect_index.keys():
            if " " in term and re.search(r'\b' + re.escape(term) + r'\b', cleaned):
                candidates.add(term)

        # Common 2-word noun patterns in reviews
        common_second_words = r"(life|quality|service|support|cancellation|resolution|sensor|motor|speed|noise|feel|longevity|fee|tier|department|app|response)"
        pattern = r"\b([a-z0-9\-]+)\s+" + common_second_words + r"\b"
        for match in re.finditer(pattern, cleaned):
            candidates.add(match.group(0).strip())

        return list(candidates)

    def extract_aspects_from_clause(self, clause: str) -> List[Dict[str, Any]]:
        """Identifies aspect mentions within a specific clause."""
        clause_clean = self.preprocessor.clean_text(clause).lower()
        found_aspects: List[Dict[str, Any]] = []
        found_spans: Set[str] = set()

        # Match compound phrases first (longer terms first)
        sorted_terms = sorted(self.aspect_index.keys(), key=len, reverse=True)
        for term in sorted_terms:
            pattern = r'\b' + re.escape(term) + r'\b'
            for match in re.finditer(pattern, clause_clean):
                span = (match.start(), match.end())
                # Avoid overlapping substrings
                overlap = any(s[0] <= span[0] and span[1] <= s[1] for s in [m["span"] for m in found_aspects])
                if not overlap and term not in found_spans:
                    found_aspects.append({
                        "term": term,
                        "canonical_aspect": self.aspect_index[term],
                        "span": span,
                        "clause": clause.strip()
                    })
                    found_spans.add(term)

        return found_aspects

    def extract_aspects(self, text: str) -> Dict[str, Any]:
        """
        Extracts all aspects from a full review text with clause context
        and canonical aspect categorization.
        """
        clauses = self.preprocessor.segment_into_clauses(text)
        all_aspect_mentions: List[Dict[str, Any]] = []
        seen_terms = set()

        for clause_idx, clause in enumerate(clauses):
            clause_aspects = self.extract_aspects_from_clause(clause)
            for item in clause_aspects:
                item["clause_index"] = clause_idx
                all_aspect_mentions.append(item)
                seen_terms.add(item["canonical_aspect"])

        # Fallback if no specific aspect detected: extract general topic
        if not all_aspect_mentions:
            all_aspect_mentions.append({
                "term": "overall_product",
                "canonical_aspect": "general_experience",
                "span": (0, len(text)),
                "clause": text.strip(),
                "clause_index": 0
            })
            seen_terms.add("general_experience")

        return {
            "text": text,
            "aspect_count": len(all_aspect_mentions),
            "aspect_mentions": all_aspect_mentions,
            "unique_categories": sorted(list(seen_terms))
        }
