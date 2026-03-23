# PGN Tokenizer

![PGN Tokenizer Visualization](https://github.com/DVDAGames/pgn-tokenizer/raw/main/docs/assets/pgn-tokenizer.png)

This is a Byte Pair Encoding (BPE) tokenizer for Chess Portable Game Notation (PGN).

## Supported Languages

- [Python](#python)
- [TypeScript](#typescript)

**Note**: This is part of a work-in-progress project to investigate how language models might understand chess without an engine or any chess-specific knowledge.

## Installation

You can install it with your package manager of choice:

### Python Package

#### uv

```bash
uv add pgn-tokenizer
```

#### pip

```bash
pip install pgn-tokenizer
```

### TypeScript Package

#### npm

```bash
npm install @dvdagames/pgn-tokenizer
```

#### bun

```bash
bun add @dvdagames/pgn-tokenizer
```

## Getting Started

Here's a brief overview of getting started with the Python and TypeScript versions of the PGN Tokenizer.

### Python

The Python package uses the
[`tokenizers`](https://huggingface.co/docs/tokenizers/) library for training the tokenizer and the [`transformers`](https://huggingface.co/docs/transformers/) library to create a `PreTrainedTokenizerFast` interface from the PGN Tokenizer configuration, and provides minimal interface with `.encode()` and `.decode()` methods, and a `.vocab_size` property, but you can also access the underlying tokenizer class via the `.tokenizer` property.

```py
from pgn_tokenizer import PGNTokenizer

# Initialize the tokenizer
tokenizer = PGNTokenizer()

# Tokenize a PGN string into a List of Token IDs
tokens = tokenizer.encode("1.e4 e5 2.Nf6 Nc3 3.Bc4")

# Decode a List of Token IDs into a String
decoded = tokenizer.decode(tokens)

# print the vocab size
print(f"Tokenizer vocabulary: {tokenzier.vocabSize}")
```

### TypeScript

The TypeScript package uses the same underlying PGN Tokenizer configuration as the Python package, which is the output of the [`tokenizers`](https://huggingface.co/docs/tokenizers/) training, but the [`@huggingface/transformers`](https://huggingface.co/docs/transformers.js/en/index) package does not fully support all of the same tokenizer options that the PGN Tokenizer relies on, so the encoding and decoding logic has been implemented manually following the same [Byte Pair Encoding](https://en.wikipedia.org/wiki/Byte_pair_encoding) (BPE) algorithm.

The most basic use case is to import the `encode` or `decode` methods and use them directly:

```ts
import { encode, decode } from "@dvdagames/pgn-tokenizer";

// convert a string into an Array of token IDs
tokens = encode("1.e4 e5 2.Nf6 Nc3 3.Bc4");

// decode an encoded Array of token IDs into a String
decoded = decode(tokens);
```

But you can also import the underlying pgnTokenizer class to have access to the `vocab_size` property, too:

```ts
import pgnTokenizer from "@dvdagames/pgn-tokenizer";

// convert a string into an Array of token IDs
tokens = pgnTokenizer.encode("1.e4 e5 2.Nf6 Nc3 3.Bc4");

// decode an encoded Array of token IDs into a String
decoded = pgnTokenizer.decode(tokens);

// print the vocab size
console.log(`Tokenizer vocabulary: ${pgnTokenizer.vocab_size}`);
```

## Tokenizer Comparison

More traditional, language-focused BPE tokenizer implementations are not suited for PGN strings because they are more likely to break the actual moves apart.

For example `1.e4 e5` would likely be tokenized as `1`, `.e`, `4`, ` e`, `5` (or `1`, `.`, `e`, `4`, ` e`, `5` depending on the tokenizer), but using this specialized PGN Tokenizer it will be tokenized as `1.`, `e4`, ` e5`. This allows models to be trained with more accurate connections between tokens in PGN strings and more accurate inference when completing PGN strings.

### Visualization

Here is a visualization of the vocabulary of this specialized PGN tokenizer compared to the BPE tokenizer vocabularies of the `cl100k_base` (the vocabulary for the `gpt-3.5-turbo` and `gpt-4` models' tokenizer) and the `o200k_base` (the vocabulary for the `gpt-4o` model's tokenizer):

#### PGN Tokenizer

![PGN Tokenizer Visualization](https://github.com/DVDAGames/pgn-tokenizer/raw/main/docs/assets/pgn-tokenizer.png)

**Note**: The tokenizer was trained with ~2.8 Million chess games in PGN notation with a target vocabulary size of `4096`.

#### GPT-3.5-turbo and GPT-4 Tokenizers

![GPT-4 Tokenizer Visualization](https://github.com/DVDAGames/pgn-tokenizer/raw/main/docs/assets/gpt-4-tokenizer.png)

#### GPT-4o Tokenizer

![GPT-4o Tokenizer Visualization](https://github.com/DVDAGames/pgn-tokenizer/raw/main/docs/assets/gpt-4o-tokenizer.png)

**Note**: These visualizations were generated with a function adapted from an [educational Jupyter Notebook in the `tiktoken` repository](https://github.com/openai/tiktoken/blob/main/tiktoken/_educational.py#L186).

## Acknowledgements

- [@karpathy](https://github.com/karpathy) for the [Let's build the GPT Tokenizer tutorial](https://youtu.be/zduSFxRajkE)
- [Hugging Face](https://huggingface.co/) for the [`tokenizers`](https://huggingface.co/docs/tokenizers/) and [`transformers`](https://huggingface.co/docs/transformers/) libraries.
- Kaggle user [MilesH14](https://www.kaggle.com/milesh14), whoever you are, for the (now-unpublished) dataset of 3.5 million chess games cleaned from [the Chess Research Project](https://chess-research-project.readthedocs.io/en/latest/)
