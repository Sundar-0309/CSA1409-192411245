# LEX scanner build guide

The scanner is defined in `../src/threatrule.l`.

```powershell
New-Item -ItemType Directory -Force build
flex -o build/lex.yy.c src/threatrule.l
gcc -std=c11 -Wall -Wextra -O2 build/lex.yy.c -o build/threatrule.exe
./build/threatrule.exe Input_Files/valid_rules.tr
```

Flex generates `lex.yy.c` from the specification. GCC then produces the executable. A successful valid-input scan exits with code 0; an invalid scan prints diagnostics and exits with code 1.
