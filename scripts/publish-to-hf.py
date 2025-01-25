from pgn_tokenizer import PGNTokenizer

__version__ = "0.1.3"

tokenizer = PGNTokenizer().tokenizer

tokenizer.push_to_hub(
    repo_id="InterwebAlchemy/PGNTokenizer",
    revision=__version__,
    token=True,
)
