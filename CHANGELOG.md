# CHANGELOG


## v0.1.6 (2025-03-27)

### Bug Fixes

- Properly split test and validation data; update packages
  ([`769f2a5`](https://github.com/DVDAGames/pgn-tokenizer/commit/769f2a5f24eb33eb9333ad6f1f4448412376cc3e))


## v0.1.5 (2025-02-11)

### Bug Fixes

- Go back to original tokenizer config
  ([`7371553`](https://github.com/DVDAGames/pgn-tokenizer/commit/73715532ec1907979d15e08489629d8d65be865d))

Adding a comment to trigger a new deployment because chore types don't publish, but fix types do.

### Chores

- Remove normalizer from training pipeline
  ([`75e25fd`](https://github.com/DVDAGames/pgn-tokenizer/commit/75e25fd5617b1e74a1e0e39a9124b59c8edb2b62))

- Revert to NFD normalizer because otherwise tokens are janky
  ([`fa2b851`](https://github.com/DVDAGames/pgn-tokenizer/commit/fa2b8512af59b6dd64974d4b53d9c37eb0555b43))

- Temporarily remove HF pubish script
  ([`5e267d0`](https://github.com/DVDAGames/pgn-tokenizer/commit/5e267d001cf79342f58f19d9724c4b3569f3ed54))


## v0.1.4 (2025-02-11)

### Bug Fixes

- Convert NFD normalizer to NFC normalizer
  ([`33df3c5`](https://github.com/DVDAGames/pgn-tokenizer/commit/33df3c521e7370e18686daf2201a75129cb298fd))

Transformers.js doensn't support NFD tokenizers.

### Chores

- Add model card template
  ([`35e3c77`](https://github.com/DVDAGames/pgn-tokenizer/commit/35e3c77e726f3e7879b9782e9cdd968c466a79ed))


## v0.1.3 (2025-01-25)

### Bug Fixes

- Get correct version in pyproject
  ([`b48786d`](https://github.com/DVDAGames/pgn-tokenizer/commit/b48786dc8be6534f43f2b5930c8aa1e317c4803d))


## v0.1.2 (2025-01-25)

### Bug Fixes

- Try to sync version numbers across the CI/CD pipeline
  ([`de5f449`](https://github.com/DVDAGames/pgn-tokenizer/commit/de5f4497dad0c1d80453dad0c3e37a48ba4feef7))


## v0.1.1 (2025-01-25)

### Bug Fixes

- Add MIT LICENSE file and pyproject.toml config
  ([`07be1da`](https://github.com/DVDAGames/pgn-tokenizer/commit/07be1da09b2fa9e02f83a7a2b5ed433f76a39fe6))

### Chores

- Try to publish package from actions
  ([`ec26771`](https://github.com/DVDAGames/pgn-tokenizer/commit/ec267710eecb9a0e4edc2d0d6b0f31559e45c865))

- Update workflow again
  ([`afcf28f`](https://github.com/DVDAGames/pgn-tokenizer/commit/afcf28fca6645c06e7f8f8a0b0bd1dbbb254bf26))


## v0.1.0 (2025-01-24)

### Chores

- Add pre-commit hooks
  ([`acf3c2c`](https://github.com/DVDAGames/pgn-tokenizer/commit/acf3c2c870e5095956d13c21c425ffe7390ab00f))

- Try to configure publishing workflow
  ([`a87f305`](https://github.com/DVDAGames/pgn-tokenizer/commit/a87f3051e938fef8f85020b89bd991351875b275))

- Try to fix release workflow
  ([`acccdc4`](https://github.com/DVDAGames/pgn-tokenizer/commit/acccdc4f14eb243659772f50f3d9d82437a3e020))

- Try to reset workflows for tagging
  ([`6fea9b3`](https://github.com/DVDAGames/pgn-tokenizer/commit/6fea9b3790a4473eafb8d001de8219c222864c2e))

- Tweak workflows again
  ([`9d83f5b`](https://github.com/DVDAGames/pgn-tokenizer/commit/9d83f5b0e9510b614612d27edf6d911fa326df1a))

### Features

- Get tokenizer test, build, and export working
  ([`94d2be1`](https://github.com/DVDAGames/pgn-tokenizer/commit/94d2be1fa1acae8166792f56f86bdefdce612783))

- Intial commit of train PGN tokenizer
  ([`ab9742e`](https://github.com/DVDAGames/pgn-tokenizer/commit/ab9742e63437067977ad55d71f183b8963293b66))
