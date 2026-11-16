# Expected scanner behaviour

## Valid input

`valid_rules.tr` must produce tokens for each keyword, identifier, relational operator, IPv4 address, integer, string, and punctuation mark. Its summary must state `0 lexical error(s)`.

## Invalid input and recovery

`invalid_rules.tr` must report all three faults without stopping at the first one:

| Input fault | Required diagnostic | Recovery |
| --- | --- | --- |
| `999.10.1.1` | IPv4 octet must be 0..255 | Skip the invalid IP lexeme and continue |
| `@` | unsupported character | Skip one character and continue |
| unfinished quote | unterminated string | Skip to the end of the line and continue |

The program must return a non-zero exit code after invalid input. This makes automated tests distinguish a clean scan from a scan that recovered from errors.
