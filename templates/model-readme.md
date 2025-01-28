---
license: mit
library_name: transformers
tags:
  - chess
  - pgn
datasets:
  - InterwebAlchemy/pgn-dataset-including-special-tokens
---

# Model Card for InterwebAlchemy/kn1ght

**Note**: This is a work-in-progress.

This is an experimental model for chess move prediction via Portable Game Notation (PGN). It is trained on the [PGN Dataset](https://huggingface.co/InterwebAlchemy/pgn-dataset-including-special-tokens) and uses the [PGNTokenizer](https://huggingface.co/InterwebAlchemy/PGNTokenizer) for tokenization of PGN strings.

## Model Details

### Model Description

- **Developed by:** [InterwebAlchemy](https://huggingface.co/InterwebAlchemy)
- **License:** MIT

### Model Sources

- **Repository:** [DVDAGames/kn1ght](https://github.com/DVDAGames/kn1ght)
- **Tokenizer:** [InterwebAlchemy/PGNTokenizer](https://huggingface.co/InterwebAlchemy/PGNTokenizer)
- **Dataset:**
  - **w/ special tokens:**[InterwebAlchemy/pgn-dataset-including-special-tokens](https://huggingface.co/InterwebAlchemy/pgn-dataset-including-special-tokens)
  - **w/o special tokens:**[InterwebAlchemy/pgn-dataset](https://huggingface.co/InterwebAlchemy/pgn-dataset)
