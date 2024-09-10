def calculate_average(numbers):
  """
  Calculates the average of a list of numbers.

  Args:
      numbers: A list of numerical values.

  Returns:
      The average of the numbers, or None if the list is empty.
  """

  if not numbers:  # Check if the list is empty
      return None

  total = 0
  for num in numbers:  # Iterate through the list
      total += num

  average = total / len(numbers)
  return average