def infix_to_postfix(expression):
  """Converts an infix expression to postfix notation."""
  stack = []  # Stack to store operators
  postfix = []  # List to store postfix expression
  for token in expression.split():
    if token.isdigit():  # If token is a number, add it directly to the postfix expression
      postfix.append(token)
    elif token == "(":  # If token is an opening parenthesis, push it to the stack
      stack.append(token)
    elif token == ")":  # If token is a closing parenthesis
      while stack[-1] != "(":  # Pop operators from the stack and append them to the postfix expression until an opening parenthesis is found
        postfix.append(stack.pop())
      stack.pop()  # Remove the opening parenthesis from the stack
    else:  # If token is an operator
      while stack and stack[-1] != "(" and precedence(token) <= precedence(stack[-1]):
        # Pop operators from the stack and append them to the postfix expression while the stack is not empty, the top operator is not an opening parenthesis, and the precedence of the current token is less than or equal to the precedence of the top operator
        postfix.append(stack.pop())
      stack.append(token)  # Push the current token to the stack
  while stack:  # Append any remaining operators from the stack to the postfix expression
    postfix.append(stack.pop())
  return postfix


def evaluate_postfix(expression):
  """Evaluates a postfix expression."""
  stack = []  # Stack to store operands
  for token in expression:
    if token.isdigit():  # If token is a number, push it to the stack
      stack.append(int(token))
    else:  # If token is an operator
      operand2 = stack.pop()  # Pop the top two operands from the stack
      operand1 = stack.pop()
      result = eval(f"{operand1} {token} {operand2}")  # Evaluate the operation and push the result back to the stack
      stack.append(result)
  return stack.pop()  # The final result is the only element remaining in the stack


def precedence(operator):
  """Returns the precedence of an operator."""
  precedences = {
      "+": 1,
      "-": 1,
      "*": 2,
      "/": 2,
      "(": 0,
  }
  return precedences[operator]


def main():
  # Testcase 1: Evaluating "10 * 2 - 15" = 5
  expression = "10 * 2 - 15"
  postfix = infix_to_postfix(expression)
  print(f"The Expression:  {expression}")
  result = evaluate_postfix(postfix)
  print(f"The Result : {result}")

  # Testcase 2: Evaluating "10 + 2 * 3" = 16
  expression = "10 + 2 * 3"
  postfix = infix_to_postfix(expression)
  print(f"The Expression:  {expression}")
  result = evaluate_postfix(postfix)
  print(f"The Result : {result}")
 
  # Testcase 3: Evaluating "10 + 6 / 2" = 13.0
  expression = "10 + 6 / 2"
  postfix = infix_to_postfix(expression)
  print(f"The Expression:  {expression}")
  result = evaluate_postfix(postfix)
  print(f"The Result : {result}")

  # Testcase 4: Evaluating "10 / 2 + 3" = 8.0
  expression = "10 / 2 + 3"
  postfix = infix_to_postfix(expression)
  print(f"The Expression:  {expression}")
  result = evaluate_postfix(postfix)
  print(f"The Result : {result}")

  # Testcase 5: Evaluating "10 * 2 + 15" = 35
  expression = "10 * 2 + 15"
  postfix = infix_to_postfix(expression)
  print(f"The Expression:  {expression}")
  result = evaluate_postfix(postfix)
  print(f"The Result : {result}")

  # Testcase 6: Evaluating "10 * 2 + 3" = 23
  expression = "10 * 2 + 3"
  postfix = infix_to_postfix(expression)
  print(f"The Expression:  {expression}")
  result = evaluate_postfix(postfix)
  print(f"The Result : {result}")


if __name__ == "__main__":
  main()
