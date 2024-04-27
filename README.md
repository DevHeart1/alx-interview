mkdir 0x00-pascal_triangle

This repository contains a Python function `pascal_triangle(n)` that efficiently generates Pascal's Triangle up to a specified row index `n`. The code adheres to best practices for readability, maintainability, and correctness.

**Features:**

- **Clear and concise implementation:** The code utilizes a nested loop approach to construct the triangle, with comments explaining each step.
- **Handles empty input:** The function gracefully returns an empty list if `n` is less than or equal to zero.
- **Optimized calculation:** Values in each row are calculated by summing adjacent elements in the previous row, reducing redundant calculations.
- **Docstring:** A detailed docstring provides a clear explanation of the function's purpose, parameters, and return value.

**Usage:**

1. **Clone the repository:**

   ```bash
   git clone https://github.com/DevHeart1/alx-interview.git
   ```

2. **Import the function:**

   ```python
   from pascal_triangle import pascal_triangle
   ```

3. **Call the function with desired row index:**

   ```python
   triangle = pascal_triangle(5)
   print(triangle)
   ```

   This will output:

   ```
   [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
   ```