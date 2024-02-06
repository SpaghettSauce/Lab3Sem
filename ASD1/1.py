def is_higher_precedence(op1, op2):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    return precedence[op1] >= precedence[op2]

def evaluate_expression(expression):
    def apply_operator(operators, values):
        operator = operators.pop()
        right = values.pop()
        left = values.pop()
        if operator == '+':
            values.append(left + right)
        elif operator == '-':
            values.append(left - right)
        elif operator == '*':
            values.append(left * right)
        elif operator == '/':
            if right == 0:
                raise ValueError("Division by zero is not allowed")
            values.append(left / right)

    def evaluate_subexpression(subexpression):
        operators = []
        values = []
        i = 0
        while i < len(subexpression):
            if subexpression[i] == ' ':
                i += 1
                continue
            if subexpression[i] in '0123456789':
                j = i
                while j < len(subexpression) and subexpression[j] in '0123456789':
                    j += 1
                values.append(int(subexpression[i:j]))
                i = j
            elif subexpression[i] in '+-*/':
                while (operators and operators[-1] in '+-*/' and
                       is_higher_precedence(operators[-1], subexpression[i])):
                    apply_operator(operators, values)
                operators.append(subexpression[i])
                i += 1
            elif subexpression[i] == '(':
                operators.append(subexpression[i])
                i += 1
            elif subexpression[i] == ')':
                while operators[-1] != '(':
                    apply_operator(operators, values)
                operators.pop()
                i += 1
        while operators:
            apply_operator(operators, values)
        return values[0]

    expression = expression.replace(" ", "")
    if '=' not in expression:
        raise ValueError("Expression must end with '='")
    if expression.count('(') != expression.count(')'):
        raise ValueError("Mismatched parentheses in the expression")

    result = evaluate_subexpression(expression)
    return result

# Example usage:
input_expression = "2+7*(3/9)-5="
try:
    result = evaluate_expression(input_expression)
    print(f"Result: {result}")
except Exception as e:
    print(f"Error: {str(e)}")