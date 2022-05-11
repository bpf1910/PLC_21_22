import ply.yacc as yacc
import sys

from plclex import tokens


def p_prog(p):
    "Prog : Decls Main"
    print(p[1]+p[2])


########################## GIC para as declaraçoes
def p_decls(p):
    "Decls : Decls Decl"
    p[0] = p[1] + p[2]

def p_decls_empty(p):
    "Decls : "
    p[0] = ''


def p_decl_int(p):
    "Decl : INT SETA DeclList PV NL"
    p[0] = p[3]

def p_decl_array(p):
    "Decl : ARR SETA ArrayList PV NL"
    p[0] = p[3]

def p_decl_nl(p):
    "Decl : NL"
    p[0] = ''


def p_decllist(p):
    "DeclList : UniDecl VIR DeclList"
    p[0] = p[1] + p[3]

def p_decllist_uni(p):
    "DeclList : UniDecl"
    p[0] = p[1]

def p_arraylist(p):
    "ArrayList : Array VIR ArrayList"
    p[0] = p[1] + p[3]

def p_arraylist_uni(p):
    "ArrayList : Array"
    p[0] = p[1]


def p_unidecl_id(p): 
    "UniDecl : ID"
    if p[1] in parser.tabID:
        string = "Erro semântico: Var " + p[1] + " já está definida!"
        p[0] = r'ERR "' + string + '"' + '\n' + 'STOP' + '\n'
    
    else:
        parser.tabID.update({p[1] : (parser.proxE,0,"Int")})
        parser.proxE += 1
        p[0] = r'PUSHI 0' + '\n'


def p_unidecl_atr(p):
    "UniDecl : ID DP NUMI"
    if p[1] in parser.tabID:
        string = "Erro semântico: Var " + p[1] + " já está definida!"
        p[0] = r'ERR "' + string + '"' + '\n' + 'STOP' + '\n'
    
    else:
        parser.tabID.update({p[1] : (parser.proxE,p[3],"Int")})
        parser.proxE += 1
        p[0] = r'PUSHI '+ str(p[3]) + '\n'


def p_unidecl_atrn(p):
    "UniDecl : ID DP MENOS NUMI"
    if p[1] in parser.tabID:
        string = "Erro semântico: Var " + p[1] + " já está definida!"
        p[0] = r'ERR "' + string + '"' + '\n' + 'STOP' + '\n'
    
    else:
        parser.tabID.update({p[1] : (parser.proxE,-p[4],"Int")})
        parser.proxE += 1
        p[0] = r'PUSHI '+ str(-p[4]) + '\n'


def p_arrayAtr(p):
    "Array : ID DP NUMI"
    if p[1] in parser.tabID:
        string = "Erro semântico: Var " + p[1] + " já está definida!"
        p[0] = r'ERR "' + string + '"' + '\n' + 'STOP' + '\n'
    
    else:
        parser.tabID.update({p[1] : (parser.proxE,p[3],"Array")})    #(end do inicio do array,tamanho,tipo da var Array)
        parser.proxE += p[3]
        p[0] = r'PUSHN ' + str(p[3]) + '\n'


def p_arrayAtrlist(p):
    "Array : ID DP List"
    if p[1] in parser.tabID:
        string = "Erro semântico: Var " + p[1] + " já está definida!"
        p[0] = r'ERR "' + string + '"' + '\n' + 'STOP' + '\n'
    
    else:
        p[0] = p[3]
        parser.tabID.update({p[1] : (parser.proxE-parser.conta,parser.conta,"Array")})
        parser.conta = 0

def p_arrayAtrlist2(p):
    "List : LPARENR Nums RPARENR"
    p[0] = p[2]

def p_elems(p):
    "Nums : Nums VIR Num"
    parser.conta += 1
    p[0] = p[1] + p[3]

def p_elems2(p):
    "Nums : Num"
    parser.conta = 1
    p[0] = p[1]

def p_elems3(p):
    "Num : NUMI"
    p[0] = r'PUSHI ' + str(p[1]) + '\n'
    parser.proxE += 1

def p_elems4(p):
    "Num : MENOS NUMI"
    p[0] = r'PUSHI ' + str(-p[2]) + '\n'
    parser.proxE += 1


########################## GIC para a main function
def p_main(p):
    "Main : MAIN SETA NL Instrs PV"
    p[0] = r'START' + '\n' + p[4] + r'STOP'


########################## GIC para instructions
def p_instrs(p):
    "Instrs : Instrs Instr"
    p[0] = p[1] + p[2]

def p_instrs_empty(p):
    "Instrs : "
    p[0] = ''


def p_instr_atr(p):
    "Instr : Atr NL"
    p[0] = p[1]

def p_instr_cond(p):
    "Instr : Cond NL"
    p[0] = p[1]

def p_instr_ciclo(p):
    "Instr : Ciclo NL"
    p[0] = p[1]

def p_instr_write(p):
    "Instr : Write NL"
    p[0] = p[1]

def p_instr_nl(p):
    "Instr : NL"
    p[0] = ''


########################## GIC para atribuiçoes
def p_atrib(p):
    "Atr : ID DP Expr PV"
    if p[1] not in parser.tabID:
        string = "Erro semântico: Var " + str(p[1]) + " não está definida!"
        p[0] = r'ERR "' + string + '"' + '\n' + 'STOP' + '\n'

    elif parser.tabID[p[1]][2]!="Int":
        string = "Erro semântico: Var " + str(p[1]) + " não é do tipo inteiro!"
        p[0] = r'ERR "' + string + '"' + '\n' + 'STOP' + '\n'     
    
    else:
        p[0] = p[3] + r'STOREG ' + str(parser.tabID[p[1]][0]) + '\n'
    

def p_atrib_read(p):
    "Atr : ID DP Read"
    if p[1] not in parser.tabID:
        string = "Erro semântico: Var " + str(p[1]) + " não está definida!"
        p[0] = r'ERR "' + string + '"' + '\n' + 'STOP' + '\n'

    elif parser.tabID[p[1]][2]!="Int":
        string = "Erro semântico: Var " + str(p[1]) + " não é do tipo inteiro!"
        p[0] = r'ERR "' + string + '"' + '\n' + 'STOP' + '\n'

    else:
        p[0] = p[3] + r'STOREG ' + str(parser.tabID[p[1]][0]) + '\n'


def p_atribarray_numi(p):
    "Atr : ID LPARENR NUMI RPARENR DP Expr PV"
    if p[1] not in parser.tabID:
        string = "Erro semântico: Var " + str(p[1]) + " não está definida!"
        p[0] = r'ERR "' + string + '"' + '\n' + 'STOP' + '\n'

    elif parser.tabID[p[1]][2]!="Array":
        string = "Erro semântico: Var " + str(p[1]) + " não é do tipo array!"
        p[0] = r'ERR "' + string + '"' + '\n' + 'STOP' + '\n'

    elif p[3]>=parser.tabID[p[1]][1]:
        string = "Erro semântico: " + p[3] + " encontra-se fora do limite do tamanho do array!"
        p[0] = r'ERR "' + string + '"' + '\n' + 'STOP' + '\n'

    else:
        p[0] = p[6] + r'STOREG ' + str(parser.tabID[p[1]][0]+p[3]) + '\n'


def p_atribarray_numi_read(p):
    "Atr : ID LPARENR NUMI RPARENR DP Read"
    if p[1] not in parser.tabID:
        string = "Erro semântico: Var " + str(p[1]) + " não está definida!"
        p[0] = r'ERR "' + string + '"' + '\n' + 'STOP' + '\n'

    elif parser.tabID[p[1]][2]!="Array":
        string = "Erro semântico: Var " + str(p[1]) + " não é do tipo array!"
        p[0] = r'ERR "' + string + '"' + '\n' + 'STOP' + '\n'

    else:
        p[0] = p[6] + r'STOREG ' + str(parser.tabID[p[1]][0]+p[3]) + '\n'


def p_atribarray_id(p):
    "Atr : ID LPARENR ID RPARENR DP Expr PV"
    if p[1] not in parser.tabID:
        string = "Erro semântico: Var " + str(p[1]) + " não está definida!"
        p[0] = r'ERR "' + string + '"' + '\n' + 'STOP' + '\n'

    elif parser.tabID[p[1]][2]!="Array":
        string = "Erro semântico: Var " + str(p[1]) + " não é do tipo array!"
        p[0] = r'ERR "' + string + '"' + '\n' + 'STOP' + '\n'

    elif p[3] not in parser.tabID:
        string = "Erro semântico: Var " + str(p[3]) + " não está definida!"
        p[0] = r'ERR "' + string + '"' + '\n' + 'STOP' + '\n'

    elif parser.tabID[p[3]][2]!="Int":
        string = "Erro semântico: Var " + str(p[1]) + " não é do tipo inteiro!"
        p[0] = r'ERR "' + string + '"' + '\n' + 'STOP' + '\n'

    else:
        p[0] = r'PUSHGP' + '\n' + \
               r'PUSHI ' + str(parser.tabID[p[1]][0]) + '\n' + \
               r'PADD' + '\n' + \
               r'PUSHG ' + str(parser.tabID[p[3]][0]) + '\n' + \
               r'CHECK ' + '0 ' + str(parser.tabID[p[1]][1]-1) + '\n' + \
               p[6] + \
               r'STOREN' + '\n'


def p_atribarray_read(p):
    "Atr : ID LPARENR ID RPARENR DP Read"
    if p[1] not in parser.tabID:
        string = "Erro semântico: Var " + str(p[1]) + " não está definida!"
        p[0] = r'ERR "' + string + '"' + '\n' + 'STOP' + '\n'

    elif parser.tabID[p[1]][2]!="Array":
        string = "Erro semântico: Var " + str(p[1]) + " não é do tipo array!"
        p[0] = r'ERR "' + string + '"' + '\n' + 'STOP' + '\n'

    elif p[3] not in parser.tabID:
        string = "Erro semântico: Var " + str(p[3]) + " não está definida!"
        p[0] = r'ERR "' + string + '"' + '\n' + 'STOP' + '\n'

    elif parser.tabID[p[3]][2]!="Int":
        string = "Erro semântico: Var " + str(p[1]) + " não é do tipo inteiro!"
        p[0] = r'ERR "' + string + '"' + '\n' + 'STOP' + '\n'

    else:
        p[0] = r'PUSHGP' + '\n' + \
               r'PUSHI ' + str(parser.tabID[p[1]][0]) + '\n' + \
               r'PADD' + '\n' + \
               r'PUSHG ' + str(parser.tabID[p[3]][0]) + '\n' + \
               r'CHECK ' + '0 ' + str(parser.tabID[p[1]][1]) + '\n' + \
               p[6] + \
               r'STOREN' + '\n'


########################## GIC para a function read
def p_read(p):
    "Read : READ LPAREN RPAREN PV"
    p[0] = r'READ' + '\n' + r'ATOI' + '\n'

def p_read_String(p):
    "Read : READ LPAREN String RPAREN PV"
    p[0] = r'PUSHS ' + p[3] + '\n' + r'WRITES' + '\n' + \
           r'PUSHS ' + r'"\n"' + '\n' + r'WRITES' + '\n' + \
           r'READ' + '\n' + r'ATOI' + '\n'


########################## GIC para condiçoes
def p_cond_if(p):
    "Cond : IF LPAREN Expr RPAREN SETA NL Instrs PV"
    p[0] = r'E' + str(parser.nivelC) + r': nop' + '\n' + p[3] + \
           r'JZ E' + str(parser.nivelC + 1) + '\n' + p[7] + \
           r'E' + str(parser.nivelC + 1) + r': nop' + '\n'
    parser.nivelC += 2


def p_cond_ifelse(p):
    "Cond : IF LPAREN Expr RPAREN SETA NL Instrs PV ELSE NL Instrs PV"
    p[0] = r'E' + str(parser.nivelC) + r': nop' + '\n' + p[3] + \
           r'JZ E' + str(parser.nivelC + 1) + '\n' + p[7] + 'JUMP E' + str(parser.nivelC + 2) + '\n' + \
           r'E' + str(parser.nivelC + 1) + r': nop' + '\n' + p[11] + \
           r'E' + str(parser.nivelC + 2) + r': nop' + '\n'
    parser.nivelC += 3


########################## GIC para ciclos
def p_ciclo(p):
    "Ciclo : WHILE LPAREN Expr RPAREN SETA NL Instrs PV"
    p[0] = r'E' + str(parser.nivelC) + r': nop' + '\n' + p[3] + \
           r'JZ E' + str(parser.nivelC + 1) + '\n' + p[7] + 'JUMP E' + str(parser.nivelC) + '\n' + \
           r'E' + str(parser.nivelC + 1) + r': nop' + '\n'
    parser.nivelC += 2


########################## GIC para a function write
def p_write_string(p):
    "Write : WRITE LPAREN String RPAREN PV"   
    p[0] = r'PUSHS ' + p[3] + '\n' + r'WRITES' + '\n' + r'PUSHS ' + r'"\n"' + '\n' + r'WRITES' + '\n'

def p_write_args(p):
    "Write : WRITE LPAREN String VIR ListArgs RPAREN PV"
    p[0] = r'PUSHS ' + p[3] + '\n' + r'WRITES' + '\n' + r'PUSHS ' + r'"\n"' + '\n' + r'WRITES' + '\n' + p[5]

def p_write_id(p):
    "Write : WRITE LPAREN ID RPAREN PV"
    if p[3] not in parser.tabID:
        string = "Erro semântico: Var " + p[3] + " não está definida!" + '\n'
        p[0] = r'ERR "' + string + '"' + '\n' + 'STOP' + '\n'

    elif parser.tabID[p[3]][2]=="Int":
        p[0] = r'PUSHG ' + str(parser.tabID[p[3]][0]) + '\n' + r'WRITEI' + '\n' + r'PUSHS ' + r'"\n"' + '\n' + r'WRITES' + '\n'

    elif parser.tabID[p[3]][2]=="Array":
        aux = 0
        s = ''
        while aux<parser.tabID[p[3]][1]:
            s += r'PUSHG ' + str(parser.tabID[p[3]][0]+aux) + '\n' + r'WRITEI' + '\n' + r'PUSHS ' + r'"\n"' + '\n' + r'WRITES' + '\n'
            aux += 1
        p[0] = s


def p_string(p):
    "String : STRING"
    p[0] = str(p[1])

def p_listargs(p):
    "ListArgs : ListArgs VIR Elem"
    p[0] = p[1] + p[3]

def p_listargs_uno(p):
    "ListArgs : Elem"
    p[0] = p[1]


def p_elem_id(p):
    "Elem : ID"
    if p[1] not in parser.tabID:
        string = "Erro semântico: Var " + str(p[1]) + " não está definida!"
        p[0] = r'ERR "' + string + '"' + '\n' + 'STOP' + '\n'

    elif parser.tabID[p[1]][2]!="Int":
        string = "Erro semântico: Var " + str(p[1]) + " não é do tipo inteiro!"
        p[0] = r'ERR "' + string + '"' + '\n' + 'STOP' + '\n'

    else:
        p[0] = r'PUSHG ' + str(parser.tabID[p[1]][0]) + '\n' + r'WRITEI' + '\n' + r'PUSHS ' + r'"\n"' + '\n' + r'WRITES' + '\n'


########################## GIC para Expressoes
def p_expr_and(p):
    "Expr : Expr AND LExpr"
    p[0] = p[1] + p[3] + r'MUL' + '\n' + \
           r'PUSHI 0' + '\n' + r'EQUAL' + '\n' + r'NOT' + '\n'

def p_expr_or(p):
    "Expr : Expr OR LExpr"
    p[0] = p[1] + p[3] + r'ADD' + '\n' + \
           r'PUSHI 0' + '\n' + r'EQUAL' + '\n' + r'NOT' + '\n' 

def p_expr_not(p):
    "Expr : NOT LExpr"
    p[0] = p[2] + r'NOT' + '\n'

def p_expr(p):
    "Expr : LExpr"
    p[0] = p[1]


########################## GIC para Expressoes Logicas
def p_lexpr_eq(p):
    "LExpr : LExpr EQ AritE"
    p[0] = p[1] + p[3] + r'EQUAL' + '\n'

def p_lexpr_neq(p):
    "LExpr : LExpr NEQ AritE"
    p[0] = p[1] + p[3] + r'EQUAL' + '\n' + r'NOT'+ '\n'

def p_lexpr_ge(p):
    "LExpr : LExpr GE AritE"
    p[0] = p[1] + p[3] + r'SUPEQ' + '\n'

def p_lexpr_LE(p):
    "LExpr : LExpr LE AritE"
    p[0] = p[1] + p[3] + r'INFEQ' + '\n'

def p_lexpr_maior(p):
    "LExpr : LExpr MAIOR AritE"
    p[0] = p[1] + p[3] + r'SUP' + '\n'

def p_lexpr_menor(p):
    "LExpr : LExpr MENOR AritE"
    p[0] = p[1] + p[3] + r'INF' + '\n'

def p_lexpr(p):
    "LExpr : AritE"
    p[0] = p[1]


########################## GIC para Espressoes Aritmeticas
def p_arite_mais(p):
    "AritE : AritE MAIS Termo"
    p[0] = p[1] + p[3] + r'ADD' + '\n'

def p_arite_menos(p):
    "AritE : AritE MENOS Termo"
    p[0] = p[1] + p[3] + r'SUB' + '\n'

def p_arite(p):
    "AritE : Termo"
    p[0] = p[1]


def p_termo_mul(p):
    "Termo : Termo MUL Parc"
    p[0] = p[1] + p[3] + r'MUL' + '\n'

def p_termo_div(p):
    "Termo : Termo DIV Parc"
    p[0] = p[1] + p[3] + r'DIV' + '\n'

def p_termo_divi(p):
    "Termo : Termo RESDI Parc"
    p[0] = p[1] + p[3] + r'MOD' + '\n'

def p_termo(p):
    "Termo : Parc"
    p[0] = p[1]


def p_parc_exp(p):
    "Parc : LPAREN Expr RPAREN"
    p[0] = p[2]

def p_parc(p):
    "Parc : Fator"
    p[0] = p[1]


def p_fator_numi(p):
    "Fator : NUMI"
    p[0] = r'PUSHI ' + str(p[1]) + '\n'

def p_fator_numin(p):
    "Fator : MENOS NUMI"
    p[0] = r'PUSHI ' + str(-p[2]) + '\n'


def p_fator_id(p):
    "Fator : ID"
    if p[1] not in parser.tabID:
        string = "Erro semântico: Var " + str(p[1]) + " não está definida!"
        p[0] = r'Err "' + string + '"' + '\n' + 'STOP'  + '\n'

    elif parser.tabID[p[1]][2]!="Int":
        string = "Erro semântico: Var " + str(p[1]) + " não é do tipo inteiro!"
        p[0] = r'Err "' + string + '"' + '\n' + 'STOP'  + '\n'

    else:
        p[0] = r'PUSHG ' + str(parser.tabID[p[1]][0]) + '\n'

def p_fator_idn(p):
    "Fator : MENOS ID"
    if p[2] not in parser.tabID:
        string = "Erro semântico: Var " + str(p[2]) + " não está definida!"
        p[0] = r'Err "' + string + '"' + '\n' + 'STOP'  + '\n'

    elif parser.tabID[p[2]][2]!="Int":
        string = "Erro semântico: Var " + str(p[2]) + " não é do tipo inteiro!"
        p[0] = r'Err "' + string + '"' + '\n' + 'STOP'  + '\n'
    
    else:
        p[0] = r'PUSHG ' + str(parser.tabID[p[2]][0]) + '\n' + r'PUSHI -1' + '\n' + r'MUL' + '\n'
    

def p_fator_array(p):
    "Fator : ID LPARENR NUMI RPARENR" 
    if p[1] not in parser.tabID:
        string = "Erro semântico: Var " + str(p[1]) + " não está definida!"
        p[0] = r'Err "' + string + '"' + '\n' + 'STOP'  + '\n'

    elif parser.tabID[p[1]][2]!="Array":
        string = "Erro semântico: Var " + str(p[1]) + " não é do tipo array!"
        p[0] = r'Err "' + string + '"' + '\n' + 'STOP'  + '\n'

    else:
        p[0] = r'PUSHGP' + '\n' + \
               r'PUSHI ' + str(parser.tabID[p[1]][0]) + '\n' + \
               r'PADD' + '\n' + \
               r'PUSHI ' + str(p[3]) + '\n' + \
               r'CHECK ' + '0 ' + str(parser.tabID[p[1]][1]-1) + '\n' \
               r'LOADN' + '\n'
        

def p_fator_array2(p):
    "Fator : ID LPARENR ID RPARENR"
    if p[1] not in parser.tabID:
        string = "Erro semântico: Var " + str(p[1]) + " não está definida!"
        p[0] = r'Err "' + string + '"' + '\n' + 'STOP'  + '\n'

    elif parser.tabID[p[1]][2]!="Array":
        string = "Erro semântico: Var " + str(p[1]) + " não é do tipo array!"
        p[0] = r'Err "' + string + '"' + '\n' + 'STOP'  + '\n'

    elif p[3] not in parser.tabID:
        string = "Erro semântico: Var " + str(p[3]) + " não está definida!"
        p[0] = r'Err "' + string + '"' + '\n' + 'STOP'  + '\n'

    elif parser.tabID[p[3]][2]!="Int":
        string = "Erro semântico: Var " + str(p[3]) + " não é do tipo inteiro!"
        p[0] = r'Err "' + string + '"' + '\n' + 'STOP'  + '\n'

    else:
        p[0] = r'PUSHGP' + '\n' + \
               r'PUSHI ' + str(parser.tabID[p[1]][0]) + '\n' + \
               r'PADD' + '\n' + \
               r'PUSHG ' + str(parser.tabID[p[3]][0]) + '\n' + \
               r'CHECK ' + '0 ' + str(parser.tabID[p[1]][1]-1) + '\n' \
               r'LOADN' + '\n'


########################## ERRO
def p_error(p):
    print("Syntax error: ", p)
    parser.exito = False

parser = yacc.yacc()
parser.tabID = {}   
parser.proxE = 0
parser.nivelC = 0
parser.conta = 0

parser.exito = True

fonte = ""

name = input()
name += '.txt'

with open(name,'r') as f:
    for line in f:
        fonte+=line

'''
for linha in sys.stdin:
    fonte += linha
'''

parser.parse(fonte)

#if parser.exito:
#    print ("Parsing teminou com sucesso!")