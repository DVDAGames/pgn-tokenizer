import { describe, test, expect } from "bun:test";

import PGNTokenizer from "./tokenizer";

const tokenizer = new PGNTokenizer();

const pgn = "1.d4 d5 2.Nf3 Bf5";
/* eslint-disable-next-line @typescript-eslint/no-magic-numbers -- hardcoded token ids for testing */
const pgnIds = [49, 70, 172, 108, 98, 298];

describe("PGNTokenizer encoding", () => {
  test("should encode pgn to pgn ids", () => {
    const encoded = tokenizer.encode(pgn);

    expect(encoded).toEqual(pgnIds);
  });

  test("should decode pgn ids to pgn", () => {
    const decoded = tokenizer.decode(pgnIds);

    expect(decoded).toEqual(pgn);
  });

  test("should encode and decode pgn", () => {
    const encoded = tokenizer.encode(pgn);
    const decoded = tokenizer.decode(encoded);

    expect(decoded).toEqual(pgn);
  });
});
