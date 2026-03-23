import { plugin } from "typescript-eslint";
import love from "eslint-config-love";

export default [
  {
    ...love,
    files: ["**/*.js", "**/*.ts", "**/*.jsx", "**/*.tsx"],
    ignores: [
      "**/node_modules/**",
      "**/dist/**",
      "**/build/**",
      ".storybook/**",
      "stories/**",
      "commitlint.config.js",
      "rollup.config.mjs",
      "eslint.config.js",
    ],
  },
  {
    plugins: {
      "@typescript-eslint": plugin,
    },
    rules: {
      "@typescript-eslint/no-magic-numbers": [
        "error",
        {
          ignore: [-1, 0, 1],
        },
      ],
      "@typescript-eslint/prefer-destructuring": [
        "warn",
        {
          VariableDeclarator: {
            array: false,
            object: true,
          },
          AssignmentExpression: {
            array: false,
            object: true,
          },
        },
        {
          // We disable this for renamed properties, since code like the following should be valid:
          // `const someSpecificMyEnum = MyEnum.Value1;`
          enforceForRenamedProperties: false,
        },
      ],
    },
  },
];
