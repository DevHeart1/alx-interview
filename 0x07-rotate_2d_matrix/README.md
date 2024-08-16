```markdown
# Rotate 2D Matrix

This project contains a Python function that rotates a 2D matrix (list of lists) 90 degrees clockwise.

## Table of Contents

- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [Example](#example)
- [Contributing](#contributing)
- [License](#license)

## Description

The `rotate_2d_matrix` function takes a square 2D matrix as input and rotates it 90 degrees clockwise in place. This is achieved by iteratively swapping the elements of the matrix in a circular fashion.

## Installation

No installation is required for this project. The function is contained in a single Python script, and you can use it directly in your own projects.

## Usage

To use the `rotate_2d_matrix` function, simply import it into your Python script and pass your 2D matrix as an argument:

```python
from rotate_matrix import rotate_2d_matrix

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rotate_2d_matrix(matrix)
print(matrix)
```

This will modify the original matrix, rotating it 90 degrees clockwise.

## Example

Here is an example of how the matrix is rotated:

### Input:
```python
[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```

### Output:
```python
[
    [7, 4, 1],
    [8, 5, 2],
    [9, 6, 3]
]
```

## Contributing

If you'd like to contribute to this project, feel free to fork the repository and submit a pull request. Please make sure your code follows PEP 8 guidelines.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
```

### Explanation:
- **Description**: Explains what the function does.
- **Installation**: Notes that no special installation is required.
- **Usage**: Shows how to use the function with an example.
- **Example**: Provides a visual example of matrix rotation.
- **Contributing**: Invites others to contribute.
- **License**: Specifies the license for the project. 

Feel free to modify it to fit the specific needs of your project!