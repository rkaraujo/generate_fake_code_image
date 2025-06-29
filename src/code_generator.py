import random
from src.config import *
from src.syntax_highlighting import get_text_color

def generate_random_number_content():
    num_type = random.choice(["int", "float", "hex", "bin"])
    if num_type == "int":
        return str(random.randint(0, 999))
    elif num_type == "float":
        return f"{random.uniform(0.0, 999.99):.2f}"
    elif num_type == "hex":
        return hex(random.randint(0, 255))
    elif num_type == "bin":
        return bin(random.randint(0, 255))

def generate_random_string_content():
    char_pool = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=[]{}|;:,.<>/?`~"
    length = random.randint(5, 20) # Varying lengths
    return ''.join(random.choice(char_pool) for i in range(length))

def generate_comment():
    comment_type = random.choice(["single_line", "multi_line"])
    comment_text = random.choice(["This is a comment.", "TODO: Implement this.", "Fix bug #123.", "Important logic here."])
    if comment_type == "single_line":
        return [("//", COLOR_COMMENT), (comment_text, COLOR_COMMENT)]
    else:
        lines = [
            ("/*", COLOR_COMMENT),
            (" " * 4 + comment_text, COLOR_COMMENT),
            (" " * 4 + "More details...", COLOR_COMMENT),
            ("*/", COLOR_COMMENT)
        ]
        return lines

def generate_inner_statements(min_statements=2, max_statements=7):
    inner_code_parts = []
    num_inner = random.randint(min_statements, max_statements)
    for _ in range(num_inner):
        inner_statement_type = random.choice(["declaration", "assignment", "function_call", "return_statement"])
        if inner_statement_type == "declaration":
            var_type = random.choice(DATA_TYPES)
            var_name = random.choice(VARIABLES) + str(random.randint(0,9))
            value = ""
            if var_type == "int":
                value = generate_random_number_content()
            elif var_type == "string":
                value = f'"{generate_random_string_content()}"'
            elif var_type == "bool":
                value = random.choice(["true", "false"])
            elif var_type == "float":
                value = generate_random_number_content()
            inner_code_parts.append((var_type, COLOR_DATATYPE))
            inner_code_parts.append((var_name, COLOR_VARIABLE))
            inner_code_parts.append(("=", COLOR_OPERATOR))
            inner_code_parts.append((value, get_text_color(value)))
            inner_code_parts.append((";", COLOR_VARIABLE))
        elif inner_statement_type == "assignment":
            var_name = random.choice(VARIABLES) + str(random.randint(0,9))
            value = random.choice([generate_random_number_content(), f'"{generate_random_string_content()}"', "true", "false", "null"])
            inner_code_parts.append((var_name, COLOR_VARIABLE))
            inner_code_parts.append(("=", COLOR_OPERATOR))
            inner_code_parts.append((value, get_text_color(value)))
            inner_code_parts.append((";", COLOR_VARIABLE))
        elif inner_statement_type == "function_call":
            func_name = random.choice(FUNCTIONS)
            arg1 = random.choice(VARIABLES + [str(random.randint(0, 10))])
            arg2 = random.choice(VARIABLES + [str(random.randint(0, 10))])
            inner_code_parts.append((func_name, COLOR_FUNCTION))
            inner_code_parts.append(("(", COLOR_VARIABLE))
            inner_code_parts.append((arg1, COLOR_VARIABLE))
            inner_code_parts.append((",", COLOR_VARIABLE))
            inner_code_parts.append((arg2, COLOR_VARIABLE))
            inner_code_parts.append((")", COLOR_VARIABLE))
            inner_code_parts.append((";", COLOR_VARIABLE))
        elif inner_statement_type == "return_statement":
            return_val = random.choice(VARIABLES + [str(random.randint(0, 100)), f'"{random.choice(["success", "failure"])}"', "true", "false", "null"])
            inner_code_parts.append(("return", COLOR_KEYWORD))
            inner_code_parts.append((return_val, get_text_color(return_val)))
            inner_code_parts.append((";", COLOR_VARIABLE))
    return inner_code_parts

def generate_code_statements(num_statements):
    all_code_parts = []
    for _ in range(num_statements):
        statement_type = random.choice(["declaration", "assignment", "function_call", "method_definition", "class_definition", "conditional", "loop", "comment"])
        
        current_statement_parts = []
        if statement_type == "declaration":
            var_type = random.choice(DATA_TYPES)
            var_name = random.choice(VARIABLES) + str(random.randint(0,9))
            value = ""
            if var_type == "int":
                value = generate_random_number_content()
            elif var_type == "string":
                value = f'"{generate_random_string_content()}"'
            elif var_type == "bool":
                value = random.choice(["true", "false"])
            elif var_type == "float":
                value = generate_random_number_content()
            current_statement_parts.append((var_type, COLOR_DATATYPE))
            current_statement_parts.append((var_name, COLOR_VARIABLE))
            current_statement_parts.append(("=", COLOR_OPERATOR))
            current_statement_parts.append((value, get_text_color(value)))
            current_statement_parts.append((";", COLOR_VARIABLE))
        elif statement_type == "assignment":
            var_name = random.choice(VARIABLES) + str(random.randint(0,9))
            value = random.choice([str(random.randint(0, 100)), f'"{random.choice(["hello", "world", "test"])}"', "true", "false", "null"])
            current_statement_parts.append((var_name, COLOR_VARIABLE))
            current_statement_parts.append(("=", COLOR_OPERATOR))
            current_statement_parts.append((value, get_text_color(value)))
            current_statement_parts.append((";", COLOR_VARIABLE))
        elif statement_type == "function_call":
            func_name = random.choice(FUNCTIONS)
            arg1 = random.choice(VARIABLES + [str(random.randint(0, 10))])
            arg2 = random.choice(VARIABLES + [str(random.randint(0, 10))])
            current_statement_parts.append((func_name, COLOR_FUNCTION))
            current_statement_parts.append(("(", COLOR_VARIABLE))
            current_statement_parts.append((arg1, COLOR_VARIABLE))
            current_statement_parts.append((",", COLOR_VARIABLE))
            current_statement_parts.append((arg2, COLOR_VARIABLE))
            current_statement_parts.append((")", COLOR_VARIABLE))
            current_statement_parts.append((";", COLOR_VARIABLE))
        elif statement_type == "method_definition":
            return_type = random.choice(["void", "int", "string", "bool"])
            func_name = random.choice(FUNCTIONS) + "".join(random.sample("abcdefghijklmnopqrstuvwxyz", random.randint(3, 6)))
            param1_type = random.choice(DATA_TYPES)
            param1_name = random.choice(VARIABLES)
            param2_type = random.choice(DATA_TYPES)
            param2_name = random.choice(VARIABLES)
            current_statement_parts.append((return_type, COLOR_DATATYPE))
            current_statement_parts.append((func_name, COLOR_FUNCTION))
            current_statement_parts.append(("(", COLOR_VARIABLE))
            current_statement_parts.append((param1_type, COLOR_DATATYPE))
            current_statement_parts.append((param1_name, COLOR_VARIABLE))
            current_statement_parts.append((",", COLOR_VARIABLE))
            current_statement_parts.append((param2_type, COLOR_DATATYPE))
            current_statement_parts.append((param2_name, COLOR_VARIABLE))
            current_statement_parts.append((")", COLOR_VARIABLE))
            current_statement_parts.append(("{", COLOR_VARIABLE))
            current_statement_parts.extend(generate_inner_statements(3, 8))
            current_statement_parts.append(("}", COLOR_VARIABLE))
            current_statement_parts.append((";", COLOR_VARIABLE))
        elif statement_type == "class_definition":
            class_name = "".join(random.sample("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 1)) + "".join(random.sample("abcdefghijklmnopqrstuvwxyz", random.randint(4, 8)))
            current_statement_parts.append(("class", COLOR_KEYWORD))
            current_statement_parts.append((class_name, COLOR_DATATYPE))
            current_statement_parts.append(("{", COLOR_VARIABLE))
            current_statement_parts.extend(generate_inner_statements(5, 10))
            current_statement_parts.append(("}", COLOR_VARIABLE))
            current_statement_parts.append((";", COLOR_VARIABLE))
        elif statement_type == "conditional":
            var_name = random.choice(VARIABLES) + str(random.randint(0,9))
            op = random.choice(OPERATORS)
            val = random.randint(0, 100)
            current_statement_parts.append(("if", COLOR_KEYWORD))
            current_statement_parts.append(("(", COLOR_VARIABLE))
            current_statement_parts.append((var_name, COLOR_VARIABLE))
            current_statement_parts.append((op, COLOR_OPERATOR))
            current_statement_parts.append((str(val), COLOR_NUMBER))
            current_statement_parts.append((")", COLOR_VARIABLE))
            current_statement_parts.append(("{", COLOR_VARIABLE))
            current_statement_parts.extend(generate_inner_statements(2, 6))
            current_statement_parts.append(("}", COLOR_VARIABLE))
            current_statement_parts.append((";", COLOR_VARIABLE))
        elif statement_type == "loop":
            var_name = random.choice(VARIABLES) + str(random.randint(0,9))
            list_name = random.choice(VARIABLES) + "List"
            current_statement_parts.append(("for", COLOR_KEYWORD))
            current_statement_parts.append(("(", COLOR_PUNCTUATION))
            current_statement_parts.append(("int", COLOR_DATATYPE))
            current_statement_parts.append(("i", COLOR_VARIABLE))
            current_statement_parts.append(("=", COLOR_OPERATOR))
            current_statement_parts.append(("0", COLOR_NUMBER))
            current_statement_parts.append((";", COLOR_PUNCTUATION))
            current_statement_parts.append(("i", COLOR_VARIABLE))
            current_statement_parts.append(("<", COLOR_OPERATOR))
            current_statement_parts.append((list_name, COLOR_VARIABLE))
            current_statement_parts.append((".length", COLOR_VARIABLE))
            current_statement_parts.append((";", COLOR_PUNCTUATION))
            current_statement_parts.append(("i++", COLOR_OPERATOR))
            current_statement_parts.append((")", COLOR_PUNCTUATION))
            current_statement_parts.append(("{", COLOR_BRACKET))
            current_statement_parts.extend(generate_inner_statements(2, 6))
            current_statement_parts.append(("}", COLOR_BRACKET))
            current_statement_parts.append((";", COLOR_PUNCTUATION))
        elif statement_type == "comment":
            current_statement_parts.extend(generate_comment())
        
        all_code_parts.append(current_statement_parts)
    return all_code_parts
