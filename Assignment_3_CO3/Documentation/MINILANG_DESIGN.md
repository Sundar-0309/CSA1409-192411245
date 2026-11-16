# MiniLang design record

## Grammar fragment

```text
Program -> Statement* 
Statement -> Type IdList ; | id = Expr ;
Type -> int | float
IdList -> id | IdList , id
Expr -> Expr + Term | Expr - Term | Term
Term -> Term * Factor | Term / Factor | Factor
Factor -> id | number | ( Expr )
```

`Type.type` is synthesized. `IdList.in` is inherited from the enclosing declaration. Expression nodes synthesize an AST node, value when all operands are constants, address, and generated code. The translator checks declaration consistency before accepting an assignment target.
