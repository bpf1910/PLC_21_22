import ply.lex as lex
import sys


tokens = ('MAIN',
          'SETA',
          'LPAREN',
          'RPAREN',
          'WHILE',
          'IF',
          'ELSE',
          'DP',
          'INT',
          'ARR',
          'NUMI',
          'ID',
          'VIR',
          'AND',
          'OR',
          'NOT',
          'EQ',
          'NEQ',
          'LE',
          'GE',
          'MENOR',
          'MAIOR',
          'MAIS',
          'MENOS',
          'MUL',
          'DIV',
          'RESDI',
          'PV',
          'READ',
          'WRITE',
          'STRING',
          'NL',
          'LPARENR',
          'RPARENR'
        )


t_EQ = r'\='
t_MAIOR = r'\>'
t_MENOR = r'\<'
t_MENOS = r'\-'
t_MAIS = r'\+'
t_MUL = r'\*'
t_DIV = r'\/'
t_RESDI = r'\%'
t_PV = r';'
t_VIR = r','
t_DP = r':'
t_IF = r'\?'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LPARENR = r'\['
t_RPARENR = r'\]'
t_SETA = r'\->'
t_ID = r'[a-z][a-zA-Z]*'


def t_NEQ(t):
    r'\!\='
    return t

def t_ELSE(t):
    r'\->>'
    return t

def t_MAIN(t):
    r'Main'
    return t

def t_WHILE(t):
    r'W\?'
    return t

def t_INT(t):
    r'Int'
    return t

def t_ARR(t):
    r'Array'
    return t

def t_WRITE(t):
    r'write'
    return t

def t_READ(t):
    r'read'
    return t

def t_STRING(t):
    r'\"[^\"]*\"'
    return t

def t_NUMI(t):
    r'[0-9]+'
    t.value = int(t.value)
    return t

def t_AND(t):
    r'and'
    return t

def t_OR(t):
    r'or'
    return t

def t_NOT(t):
    r'\!'
    return t

def t_LE(t):
    r'\<\='
    return t

def t_GE(t):
    r'\>\='
    return t

def t_NL(t):
    r'\n'
    t.lexer.lineno += len(t.value)
    return t

t_ignore = ' \t'

def t_error(t):
    print("Illegal character {} at line {}".format(t.value[0], t.lineno,))
    t.lexer.skip(1)

lexer = lex.lex()