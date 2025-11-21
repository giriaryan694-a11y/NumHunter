# NumHunter

**Phone Number Intelligence Generator & Guesser**


---

## Overview

NumHunter is a **powerful and flexible tool** for generating realistic phone numbers and exploring number patterns. It can be used to:

* Generate large sets of realistic sample phone numbers for testing and research.
* Guess all possibilities for a given number pattern (e.g., `+9199xxxx`).
* Experiment with number patterns, repetitions, and telecom prefixes.

NumHunter supports:

* **Multiple generation modes**:

  1. National format pattern
  2. Telecom operator prefix
  3. Human-style pattern clustering
  4. Weighted digit distribution
* **Pattern detection** from sample numbers to guide generation.
* **Unique numbers** and optional **maximum consecutive repeated digits**.
* **Progress bars** for generation and guessing using `tqdm`.
* Beautiful **terminal banner** with `pyfiglet`, colored output with `termcolor` and `colorama`.

---

## Installation

```bash
git clone https://github.com/giriaryan694-a11y/NumHunter
cd NumHunter
pip install -r requirements.txt
```

**Dependencies**:

* Python 3.8+
* `pyfiglet`
* `termcolor`
* `colorama`
* `tqdm`

---

## Usage

### 1️⃣ Generate realistic numbers

```bash
python numhunter.py -q 100 -c +91 -r 10 -o samples.txt
```

* `-q` / `--quantity` → number of numbers to generate
* `-c` / `--country` → country code, default `+91`
* `-r` / `--range` → number of digits after country code
* `-o` / `--output` → file to save results
* `-s` / `--sample` → optional number to detect patterns

---

### 2️⃣ Guess all numbers from a pattern

```bash
python numhunter.py -g +9199xxxx -o guess.txt
```

* `-g` / `--guess` → pattern to guess, use `x` as placeholder

---

## Examples

* Generate 50 realistic Indian numbers:

```bash
python numhunter.py -q 50 -c +91 -r 10 -o samples.txt
```

* Guess all combinations for `+9199xxxx`:

```bash
python numhunter.py -g +9199xxxx -o num.txt
```

---

## Ethical Use Notice

**NumHunter is strictly intended for educational, research, and ethical purposes.**

* Do **not** use this tool to:

  * Spam or harass individuals
  * Attempt illegal access or fraud
  * Violate privacy or telecom regulations

* Use this tool to:

  * Keep your curiosity alive safely
  * Learn about number patterns and telecom structures
  * Test apps, databases, or systems in controlled environments

> “Explore knowledge, but never harm others.” — Aryan Giri

---

## Credits

* **Made by Aryan Giri**
* Uses open-source Python libraries: `pyfiglet`, `termcolor`, `colorama`, `tqdm`

---

This project is released for **educational and ethical research use only**.
