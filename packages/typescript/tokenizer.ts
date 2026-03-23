import tokizerConfig from "./config/pgn-tokenizer.json" with { type: "json" };

import type { PGNTokenizerConfig } from "./types";

export interface PGNTokenizerInterface {
  vocabSize: number;
  encode: (pgn: string) => number[];
  decode: (tokens: number[]) => string;
}

const MIN_TOKEN_PAIRS = 2;

const getTokenPairs = (tokenIds: number[]): Record<string, number> => {
  const tokenPairs: Record<string, number> = {};

  for (let i = 0; i < tokenIds.length - 1; i++) {
    const tokenId = tokenIds[i];
    const nextTokenId = tokenIds[i + 1];

    if (
      Object.prototype.hasOwnProperty.call(
        tokenPairs,
        `${tokenId},${nextTokenId}`
      )
    ) {
      tokenPairs[`${tokenId},${nextTokenId}`] =
        tokenPairs[`${tokenId},${nextTokenId}`] + 1;
    } else {
      tokenPairs[`${tokenId},${nextTokenId}`] = 1;
    }
  }

  return tokenPairs;
};

export default class PGNTokenizer implements PGNTokenizerInterface {
  private readonly config: PGNTokenizerConfig;
  private readonly mergedVocabulary: Record<string, number>;
  vocabSize: number;

  constructor() {
    this.config = tokizerConfig;
    this.vocabSize = Object.keys(this.config.model.vocab).length;

    this.mergedVocabulary = this.createMergedVocabulary();
  }

  private createMergedVocabulary(): Record<string, number> {
    const mergedVocabulary: Record<string, number> = {};

    for (const merge of this.config.model.merges) {
      const [token1, token2] = merge;

      const mergedToken = `${token1}${token2}`;

      const token1Id = this.lookupToken(token1);
      const token2Id = this.lookupToken(token2);

      const mergedTokenId = this.lookupToken(mergedToken);

      mergedVocabulary[`${token1Id},${token2Id}`] = mergedTokenId;
    }

    return mergedVocabulary;
  }

  private lookupToken(token: string): number {
    return this.config.model.vocab[token];
  }

  private mergePair(tokenIds: number[], pair: string): number[] {
    const mergedTokenIds: number[] = [];
    const pairTokens = pair.split(",").map((token) => parseInt(token, 10));

    let index = 0;

    while (index < tokenIds.length) {
      if (
        index < tokenIds.length - 1 &&
        tokenIds[index] === pairTokens[0] &&
        tokenIds[index + 1] === pairTokens[1]
      ) {
        mergedTokenIds.push(this.mergedVocabulary[pair]);

        index += MIN_TOKEN_PAIRS;
      } else {
        mergedTokenIds.push(tokenIds[index]);

        index += 1;
      }
    }

    return mergedTokenIds;
  }

  encode(pgn: string): number[] {
    const tokens = pgn.split("");

    let tokenIds = tokens.map((token) => this.lookupToken(token));

    while (tokenIds.length >= MIN_TOKEN_PAIRS) {
      const tokenIdPairs = getTokenPairs(tokenIds);

      const mergeablePairs = Object.keys(tokenIdPairs).filter((pair) =>
        Object.prototype.hasOwnProperty.call(this.mergedVocabulary, pair)
      );

      if (mergeablePairs.length === 0) {
        break;
      }

      const sortedMergeablePairs = mergeablePairs.sort((a, b) => {
        const aId = this.mergedVocabulary[a];
        const bId = this.mergedVocabulary[b];

        return aId - bId;
      });

      const pairToMerge = sortedMergeablePairs[0];

      tokenIds = this.mergePair(tokenIds, pairToMerge);
    }

    return tokenIds;
  }

  decode(tokens: number[]): string {
    const decodedTokens = tokens.map((tokenId) => {
      const token = Object.keys(this.config.model.vocab).find(
        (key) => this.config.model.vocab[key] === tokenId
      );

      return token;
    });

    return decodedTokens.join("");
  }
}
