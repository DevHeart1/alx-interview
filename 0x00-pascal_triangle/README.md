## 0x00. Pascal's Triangle
- Implementation of ALX Pascals Triangle given `def pascal_triangle(n):` prototype

## Tasks :page_with_curl:

* **0. Pascal's Triangle**
  * [0-pascal_triangle.py](0-pascal_triangle.py): Create a function def pascal_triangle(n): that returns a list of lists of integers representing the Pascal’s triangle of n:

	* Returns an empty list if n <= 0
	* You can assume n will be always an integer

## Usage:

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