### Python Coding Style Guide

#### 1. Naming Conventions
- **Variables and Function Names**: Use `snake_case`.
  ```python
  total_price = 0
  def calculate_total_price(item_list):
      pass
  ```
- **Class Names**: Use `CamelCase`.
  ```python
  class ShoppingCart:
      pass
  ```
- **Constants**: Use `UPPER_CASE_WITH_UNDERSCORES`.
  ```python
  MAX_ITEMS = 100
  ```

#### 2. Indentation
- Use 4 spaces per indentation level. Avoid using tabs.
  ```python
  def example_function():
      for i in range(10):
          print(i)
  ```

#### 3. Line Length
- Limit lines to 79 characters.
  ```python
  def long_function_name(variable_one, variable_two, variable_three, variable_four):
      pass
  ```

#### 4. Imports
- Import standard libraries first, then third-party libraries, and local modules last.
- Use absolute imports whenever possible.
  ```python
  import os
  import sys

  import requests

  from my_project import my_module
  ```

#### 5. Docstrings
- Use triple double quotes for docstrings.
- Include a summary, parameters, return values, and exceptions.
  ```python
  def example_function(param1, param2):
      """
      Summary of the function.

      Parameters:
      param1 (int): Description of param1.
      param2 (str): Description of param2.

      Returns:
      bool: Description of the return value.
      """
      # Function implementation
      pass
  ```

#### 6. Code Layout
- Separate top-level function and class definitions with two blank lines.
- Separate method definitions inside a class with one blank line.
- Use spaces around operators and after commas, but not directly inside brackets.
  ```python
  # Example of a top-level function
  def example_function(param1, param2):
      """
      Summary of the function.

      Parameters:
      param1 (int): Description of param1.
      param2 (str): Description of param2.

      Returns:
      bool: Description of the return value.
      """
      result = param1 + param2  # Spaces around operators
      return result


  class ExampleClass:
      
      def __init__(self, value):
          self.value = value

      def example_method(self):
          """
          Summary of the method.

          Returns:
          str: Description of the return value.
          """
          return f"The value is {self.value}"


  MAX_ITEMS = 100

  def another_function(param):
      """
      Summary of another function.

      Parameters:
      param (list): Description of param.

      Returns:
      list: Description of the return value.
      """
      processed_items = [item for item in param if item < MAX_ITEMS]
      return processed_items
  ```
