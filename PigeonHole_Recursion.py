def pigeonhole_sort(array, min, max):
  """Sorts the given array using the pigeonhole sort algorithm.

  Args:
    array: The array to be sorted.
    min: The minimum value in the array.
    max: The maximum value in the array.

  Returns:
    The sorted array.
  """

  # If the array is empty or has only one element, then it is already sorted.
  if len(array) <= 1:
    return array

  # Create a list of pigeonholes, where each pigeonhole can hold up to `max - min + 1` elements.
  pigeonholes = [[] for _ in range(max - min + 1)]

  # For each element in the array, put it in the pigeonhole corresponding to its value.
  for i in range(len(array)):
    pigeonholes[array[i] - min].append(array[i])

  # For each pigeonhole, sort the elements in it.
  for i in range(len(pigeonholes)):
    pigeonholes[i].sort()

  # Put the elements back into the array in order.
  sorted_array = []
  for i in range(len(pigeonholes)):
    for j in range(len(pigeonholes[i])):
      sorted_array.append(pigeonholes[i][j])

  return sorted_array
