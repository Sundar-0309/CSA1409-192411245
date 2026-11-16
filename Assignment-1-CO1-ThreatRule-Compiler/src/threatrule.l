%option noyywrap yylineno nounput noinput case-insensitive

%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#define MAX_SYMBOLS 256
#define MAX_LEXEME 512

static char *symbols[MAX_SYMBOLS];
static int symbol_count = 0;
static int token_count = 0;
static int error_count = 0;

static void emit(const char *kind, const char *lexeme) {
    printf("line %-3d %-14s %s\n", yylineno, kind, lexeme);
    token_count++;
}

static void lexical_error(const char *message, const char *lexeme) {
    fprintf(stderr, "line %d: lexical error: %s [%s]\n", yylineno, message, lexeme);
    error_count++;
}

static void install_identifier(const char *lexeme) {
    int i;
    for (i = 0; i < symbol_count; i++) {
        if (strcmp(symbols[i], lexeme) == 0) return;
    }
    if (symbol_count >= MAX_SYMBOLS) {
        lexical_error("symbol table is full", lexeme);
        return;
    }
    symbols[symbol_count] = malloc(strlen(lexeme) + 1);
    if (!symbols[symbol_count]) {
        fprintf(stderr, "out of memory\n");
        exit(EXIT_FAILURE);
    }
    strcpy(symbols[symbol_count++], lexeme);
}

static int valid_ipv4(const char *text) {
    unsigned int a, b, c, d;
    char tail;
    return sscanf(text, "%u.%u.%u.%u%c", &a, &b, &c, &d, &tail) == 4 &&
           a <= 255 && b <= 255 && c <= 255 && d <= 255;
}

static void print_summary(void) {
    int i;
    printf("\nSummary: %d token(s), %d lexical error(s), %d identifier(s)\n",
           token_count, error_count, symbol_count);
    if (symbol_count) {
        printf("Symbol table:\n");
        for (i = 0; i < symbol_count; i++) printf("  %s\n", symbols[i]);
    }
}
%}

WS          [ \t\r]+
ID          [A-Za-z_][A-Za-z0-9_]*
INT         [0-9]+
IP          [0-9]{1,3}(\.[0-9]{1,3}){3}
HASH        [A-Fa-f0-9]{64}
CVE         CVE-[0-9]{4}-[0-9]{4,7}
URL         https?://[A-Za-z0-9._~:/?#\[\]@!$&'()*+,;=%-]+
STRING      \"([^\\\n\"]|\\[\\\"nrt])*\"

%%
{WS}                ;
"//"[^\n]*         ;
"#"[^\n]*          ;
\n                  ;

"RULE"              { emit("KEYWORD_RULE", yytext); }
"IF"                { emit("KEYWORD_IF", yytext); }
"THEN"              { emit("KEYWORD_THEN", yytext); }
"ALERT"             { emit("KEYWORD_ALERT", yytext); }
"AND"               { emit("LOGICAL_AND", yytext); }
"OR"                { emit("LOGICAL_OR", yytext); }
"NOT"               { emit("LOGICAL_NOT", yytext); }

"=="|"!="|">="|"<="|">"|"<" { emit("RELATIONAL_OP", yytext); }
"="                 { emit("ASSIGN_OP", yytext); }
"("|")"|","|";"  { emit("PUNCTUATION", yytext); }

{HASH}               { emit("SHA256_HASH", yytext); }
{CVE}                { emit("CVE_ID", yytext); }
{URL}                { emit("URL", yytext); }
{IP}                 { if (valid_ipv4(yytext)) emit("IPV4_ADDRESS", yytext); else lexical_error("IPv4 octet must be 0..255", yytext); }
{STRING}             { emit("STRING", yytext); }
{INT}                { emit("INTEGER", yytext); }
{ID}                 { install_identifier(yytext); emit("IDENTIFIER", yytext); }

\"[^\n]*           { lexical_error("unterminated string", yytext); }
.                   { lexical_error("unsupported character", yytext); }
%%

int main(int argc, char **argv) {
    FILE *input = stdin;
    int i;
    if (argc > 2) {
        fprintf(stderr, "usage: %s [rule-file]\n", argv[0]);
        return EXIT_FAILURE;
    }
    if (argc == 2) {
        input = fopen(argv[1], "r");
        if (!input) {
            perror(argv[1]);
            return EXIT_FAILURE;
        }
    }
    yyin = input;
    yylex();
    if (input != stdin) fclose(input);
    print_summary();
    for (i = 0; i < symbol_count; i++) free(symbols[i]);
    return error_count ? EXIT_FAILURE : EXIT_SUCCESS;
}
