import ply.yacc as yacc
import sys
import logging
from lexer import tokens
import os

def p_compilation_unit(p):
    'compilation_unit :  import_declarations_extras classes_objects_list'

def p_import_declarations_extras(p):
  '''import_declarations_extras : import_declarations
                                          | empty'''

def p_import_declarations(p):
    '''import_declarations :  import_declaration
                                    | import_declarations import_declaration'''

def p_import_declaration(p):
    '''import_declaration :  K_IMPORT ambiguous_name'''


def p_classes_objects_list(p):
    '''classes_objects_list : classes_objects_list  class_and_objects_declaration
                              | class_and_objects_declaration '''

def p_class_and_objects_declaration(p):
  '''class_and_objects_declaration : object_declaration
                                                | class_declaration'''

def p_object_declaration(p):
    'object_declaration : ObjectDeclare block'


def p_object_declare(p):
    '''ObjectDeclare : K_OBJECT IDENTIFIER super '''

def p_class_type(p):
  '''class_type : IDENTIFIER
                    | K_WITH class_type'''

def p_super(p):
  '''super : K_EXTENDS class_type
              | empty'''

def p_class_declaration(p):
        '''class_declaration : class_header class_body'''

def p_class_header(p):
        '''class_header : K_CLASS IDENTIFIER LPAREN class_arguement_header RPAREN super'''

def p_class_body(p):
        '''class_body : BLOCK_BEGIN class_body_declarations_extras BLOCK_END '''

def p_class_body_declarations_extras(p):
      '''class_body_declarations_extras : class_body_declarations
                                                    | empty'''

def p_class_body_declarations(p):
    '''class_body_declarations : class_body_declaration
                                          | class_body_declarations class_body_declaration'''

def p_class_body_declaration(p):
    '''class_body_declaration : field_declaration
                                          | method_declaration'''

def p_field_declaration(p):
    'field_declaration :   declaration_keyword variable_declaration_body  semi'

def p_semi(p):
    '''semi : SEMI_COLON
              | NEWLINE'''

def p_class_arguement_header(p):
  '''class_arguement_header : class_arguement_list
                                        | empty '''

def p_class_arguement_list(p):
  '''class_arguement_list : IDENTIFIER COLON type
                                    | IDENTIFIER COLON type COMMA class_arguement_list'''

def p_func_arguement_list_extras(p):
  '''func_arguement_list_extras : variable_declarators
                                        | empty '''

def p_method_declaration(p):
        '''method_declaration : K_DEF IDENTIFIER LPAREN func_arguement_list_extras RPAREN method_return_type_extras '''

def p_method_return_type_extras(p):
  '''method_return_type_extras : COLON method_return_type ASSIGN method_body
                                          | ASSIGN method_body
                                          | empty method_body'''

def p_method_return_type(p):
        '''method_return_type : type
                                | K_UNIT'''

def p_method_body(p):
        '''method_body : block'''

def p_type(p):
        '''type : basic_type
                 | other_type '''

def p_basic_type(p):
    '''basic_type : K_CHAR
                             | K_FLOAT
                             | K_STRING
                             | K_BOOLEAN
                             | K_INT'''


def p_other_type(p):
      '''other_type : nonarray_datatype
                        | array_datatype'''

def p_array_datatype(p):
      '''array_datatype : K_ARRAY square_block
                                | K_LIST square_block'''

def p_square_block(p):
    ''' square_block : SQUARE_BEGIN type SQUARE_END'''

def p_nonarray_datatype(p):
      '''nonarray_datatype : IDENTIFIER'''


def p_expression(p):
    '''expression : assignment
                        | or_expression'''

def p_assignment(p):
    '''assignment : left_hand_side ASSIGN or_expression'''


def p_or_expression(p):
    '''or_expression : and_expression
                            | or_expression OR and_expression'''

def p_and_expression(p):
    '''and_expression : xor_expression
                            | and_expression AND xor_expression'''

def p_xor_expression(p):
    '''xor_expression : equality_expression
                            | xor_expression XOR equality_expression'''


def p_equality_expression(p):
    '''equality_expression : relational_expression
                                    | equality_expression EQUAL relational_expression
                                    | equality_expression NEQUAL relational_expression'''


def p_relational_expression(p):
    '''relational_expression : add_expression
                                        | relational_expression GREATER_THAN add_expression
                                        | relational_expression GREATER_THAN_EQUAL add_expression
                                        | relational_expression LESS_THAN add_expression
                                        | relational_expression LESS_THAN_EQUAL add_expression'''


def p_add_expression(p):
    '''add_expression : mult_expression
                                    | add_expression PLUS mult_expression
                                    | add_expression MINUS mult_expression'''

def p_mult_expression(p):
    '''mult_expression : unary_expression
                                             | mult_expression DIVIDE unary_expression
                                             | mult_expression MULT unary_expression
                                             | mult_expression MOD unary_expression'''


def p_unary_expression(p):
    '''unary_expression : PLUS unary_expression
                                | MINUS unary_expression
                                | unary_expression_not_plus_minus'''

def p_unary_expression_not_plus_minus(p):
    '''unary_expression_not_plus_minus : postfix_expression
                                                       | NOT unary_expression'''

def p_postfix_expression(p):
    '''  postfix_expression : primary_no_new_array
                                    | ambiguous_name'''

def p_primary_no_new_array(p):
    '''  primary_no_new_array : literal
                                            | method_invocation
                                            | LPAREN expression RPAREN
                                            | array_invocation'''

def p_array_invocation(p):
    '''array_invocation : ambiguous_name SQUARE_BEGIN expression SQUARE_END '''


def p_literal(p):
  '''literal : STRING
            | CHAR
            | K_FALSE
            | K_TRUE
            | K_NULL
            | FLOAT
            | INT'''

def p_method_invocation(p):
    '''method_invocation : ambiguous_name LPAREN argument_list_extras RPAREN '''

def p_argument_list_extras(p):
    '''argument_list_extras : argument_list
                                | empty'''


def p_argument_list(p):
    '''argument_list : expression
                            | argument_list COMMA expression'''

def p_ambiguous_name(p):
    '''ambiguous_name : IDENTIFIER
                                | ambiguous_name DOT IDENTIFIER'''

def p_left_hand_side(p):
    '''left_hand_side : ambiguous_name
                            | array_invocation'''

# BLOCK STATEMENTS


def p_block(p):
      '''block : BLOCK_BEGIN block_body BLOCK_END '''


def p_block_body(p):
      '''block_body : block_statements
                        | empty'''

def p_block_statements(p):
      '''block_statements : block_statement
                                    | block_statements block_statement'''

def p_block_statement(p):
      '''block_statement : local_variable_declaration_statement
                                    | statement
                                    | method_declaration'''
                           

def p_declaration_keyword(p):
  '''declaration_keyword : K_VAR
                                    | K_VAL '''


def p_local_variable_declaration_statement(p):
      '''local_variable_declaration_statement : local_variable_declaration  semi '''

def p_local_variable_declaration(p):
      '''local_variable_declaration : declaration_keyword variable_declaration_body''' 


def p_variable_declaration_initializer(p):
  '''variable_declaration_initializer : expression
                                                  | array_initializer
                                                  | class_instance_creation_expression'''

def p_array_initializer(p):
  ''' array_initializer : K_NEW K_ARRAY SQUARE_BEGIN type SQUARE_END LPAREN INT RPAREN
                            | K_ARRAY LPAREN argument_list_extras RPAREN '''



def p_class_instance_creation_expression(p):
  ''' class_instance_creation_expression : K_NEW nonarray_datatype LPAREN argument_list_extras RPAREN '''


def p_variable_declaration_body(p):
      '''variable_declaration_body : variable_declarator_extra_rule  ASSIGN  variable_declaration_initializer '''

def p_variable_declarators(p):
      '''variable_declarators : variable_declarator
                                        | variable_declarator COMMA variable_declarators'''

def p_variable_declarator(p):
      '''variable_declarator : IDENTIFIER COLON type'''


def p_variable_declarator_extra_rule(p):
      '''variable_declarator_extra_rule : IDENTIFIER COLON type
                                                    | IDENTIFIER'''


def p_statement(p):
    '''  statement : statement_without_trailing_substatement
                            | while_statement
                            | if_then_else_statement
                            | if_then_statement
                            | for_loop'''

def p_if_then_statement(p):
    'if_then_statement : K_IF LPAREN expression RPAREN statement'

def p_if_then_else_statement(p):
    'if_then_else_statement : K_IF LPAREN expression RPAREN statement_no_short_if K_ELSE statement'

def p_if_then_else_statement_no_short_if(p):
    'if_then_else_statement_no_short_if : K_IF LPAREN expression RPAREN statement_no_short_if K_ELSE statement_no_short_if'

def p_statement_no_short_if(p):
    '''  statement_no_short_if : statement_without_trailing_substatement
                                            | if_then_else_statement_no_short_if'''


def p_statement_without_trailing_substatement(p):
    '''  statement_without_trailing_substatement : block
                                                                        | switch
                                                                        | expression_statement
                                                                        | blank_statement
                                                                        | return_statement'''

def p_blank_statement(p):
    'blank_statement : semi'

def p_empty(p):
    'empty :'

def p_expression_statement(p):
    'expression_statement : statement_expression semi'

def p_statement_expression(p):
    '''  statement_expression : assignment
                                            | method_invocation
                                            | class_instance_creation_expression'''


def p_switch(p):
    'switch : switch_header switch_body'

def p_switch_header(p):
    '''switch_header : expression K_MATCH'''

def p_switch_body(p):
    'switch_body : BLOCK_BEGIN multiple_inner_switch_statement  BLOCK_END'


def p_multiple_inner_switch_statement(p):
    '''  multiple_inner_switch_statement : single_inner_switch_statement
                                                        | multiple_inner_switch_statement single_inner_switch_statement'''

def p_single_inner_switch_statement(p):
    '''single_inner_switch_statement : single_switch_statement_header single_switch_statement_body '''

def p_single_switch_statement_body(p):
    '''single_switch_statement_body : expression
                                                    | block_statements'''


def p_single_switch_statement_header(p):
    'single_switch_statement_header : K_CASE expression IMPLIES'

def p_while_statement(p):
    'while_statement : K_WHILE LPAREN expression RPAREN statement'

def p_for_loop(p):
    'for_loop : K_FOR LPAREN for_exprs  RPAREN statement'


def p_for_exprs(p):
    '''for_exprs :  for_variables SEMI_COLON for_exprs
                        | for_variables'''

def p_for_variables(p):
    'for_variables : declaration_keyword_extras IDENTIFIER IN expression for_untilTo expression '

def p_declaration_keyword_extras(p):
    '''declaration_keyword_extras : declaration_keyword 
                                    | empty'''
def p_for_untilTo(p):
    '''  for_untilTo : K_UNTIL
                        | K_TO'''

def p_return_statement(p):
    '''return_statement : K_RETURN expression semi
                                    | K_RETURN semi'''


logging.basicConfig(
    level = logging.DEBUG,
    filename = "parselog.txt",
    filemode = "w"
)

log = logging.getLogger()
parser = yacc.yacc()


if __name__ == "__main__" :

    s = open(sys.argv[1],'r')
    data = s.read()
    data+= "\n"
    s.close()
    result = parser.parse(data,debug=log)


    import re
    
    #obtain the lines with the productions used
    outfile = open("rules_used.txt",'w')
    with open("parselog.txt") as f:
        for line in f:
            if re.match("INFO:root:Action(.*)", line):
                outfile.write(line)


    #clean the productions to give the required information
    infile = "rules_used.txt"
    outfile = "reverse_actions.txt"

    delete_list2 = ["rule [","] with"]

    fin = open(infile)
    fout = open(outfile, "w+")
    for line in fin:
       matches = re.findall('rule \[(.*)\] with', line)
       fout.write(matches[0])
       fout.write("\n")
    fin.close()
    fout.close()
    os.remove("rules_used.txt")

    