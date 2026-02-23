"""Simple character-level language model to detect likely words vs gibberish.

Usage:
  python lm_gibberish_detector.py hello qzxptx asdfg "machine learning"
"""

from __future__ import annotations

import math
import re
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


ALPHABET = "abcdefghijklmnopqrstuvwxyz'"
TOKEN_RE = re.compile(r"[a-z']+")


SEED_WORDS = [
    "hello",
    "world",
    "apple",
    "banana",
    "computer",
    "science",
    "search",
    "model",
    "language",
    "learning",
    "python",
    "terminal",
    "project",
    "function",
    "variable",
    "system",
    "analysis",
    "question",
    "answer",
    "example",
    "people",
    "korea",
    "simple",
    "gibberish",
    "actual",
    "word",
]


@dataclass
class Prediction:
    text: str
    label: str
    confidence: float
    score: float


class CharBigramLM:
    """A tiny character bigram language model with add-one smoothing."""

    def __init__(self) -> None:
        self.bigram_counts: dict[str, Counter[str]] = defaultdict(Counter)
        self.unigram_counts: Counter[str] = Counter()
        self.vocab: set[str] = set()

    def train(self, words: Iterable[str]) -> None:
        for raw in words:
            word = normalize(raw)
            if not word:
                continue
            self.vocab.add(word)
            padded = f"^{word}$"
            for i in range(len(padded) - 1):
                prev_ch, next_ch = padded[i], padded[i + 1]
                self.bigram_counts[prev_ch][next_ch] += 1
                self.unigram_counts[prev_ch] += 1

    def log_probability(self, text: str) -> float:
        padded = f"^{text}$"
        total = 0.0
        vocab_size = len(ALPHABET) + 2  # start and end marker
        for i in range(len(padded) - 1):
            prev_ch, next_ch = padded[i], padded[i + 1]
            next_count = self.bigram_counts[prev_ch][next_ch]
            prev_total = self.unigram_counts[prev_ch]
            prob = (next_count + 1) / (prev_total + vocab_size)
            total += math.log(prob)
        return total

    def normalized_score(self, text: str) -> float:
        # Less negative (higher) means more likely under the model.
        lp = self.log_probability(text)
        return lp / max(1, len(text))


def normalize(text: str) -> str:
    return "".join(ch for ch in text.lower() if ch in ALPHABET)


def load_training_words() -> list[str]:
    words = list(SEED_WORDS)
    dict_paths = [Path("/usr/share/dict/words"), Path("/usr/dict/words")]
    for path in dict_paths:
        if path.exists():
            with path.open("r", encoding="utf-8", errors="ignore") as f:
                for line in f:
                    token = normalize(line.strip())
                    if token and 2 <= len(token) <= 20:
                        words.append(token)
            break
    return words


def vowel_ratio(word: str) -> float:
    vowels = sum(ch in "aeiou" for ch in word)
    return vowels / len(word) if word else 0.0


def max_consonant_cluster(word: str) -> int:
    longest = 0
    current = 0
    for ch in word:
        if ch in "aeiou":
            current = 0
        else:
            current += 1
            longest = max(longest, current)
    return longest


def repeated_char_ratio(word: str) -> float:
    if not word:
        return 0.0
    repeats = sum(1 for i in range(1, len(word)) if word[i] == word[i - 1])
    return repeats / max(1, len(word) - 1)


def predict_word_or_gibberish(model: CharBigramLM, raw_text: str) -> Prediction:
    word = normalize(raw_text)
    if not word:
        return Prediction(raw_text, "gibberish", 1.0, -999.0)

    # Strong signal: seen in training vocabulary.
    if word in model.vocab:
        return Prediction(raw_text, "word", 0.98, 0.0)

    score = model.normalized_score(word)
    ratio = vowel_ratio(word)
    cluster = max_consonant_cluster(word)
    repeat_ratio = repeated_char_ratio(word)

    # Lightweight heuristics over LM score.
    likely_word = (
        score > -4.2
        and 0.15 <= ratio <= 0.8
        and len(word) >= 2
        and cluster <= 4
        and repeat_ratio <= 0.35
    )

    if likely_word:
        confidence = min(0.95, max(0.55, (score + 5.0) / 2.0))
        return Prediction(raw_text, "word", confidence, score)

    confidence = min(0.99, max(0.55, (-score - 3.2) / 2.0))
    return Prediction(raw_text, "gibberish", confidence, score)


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print("Provide one or more words to classify.")
        print('Example: python lm_gibberish_detector.py hello qzxptx "machien"')
        return 1

    lm = CharBigramLM()
    lm.train(load_training_words())

    for item in argv[1:]:
        parts = TOKEN_RE.findall(item.lower()) or [item]
        for part in parts:
            pred = predict_word_or_gibberish(lm, part)
            print(
                f"{pred.text:15} -> {pred.label:9} "
                f"(confidence={pred.confidence:.2f}, score={pred.score:.3f})"
            )
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
