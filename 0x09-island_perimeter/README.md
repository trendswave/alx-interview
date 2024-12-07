# Island Perimeter

This project contains a function `def island_perimeter(grid):` that calculates the perimeter of an island described in a grid.

## Function Description

The function `island_perimeter(grid)` takes a single argument:
- `grid`: A list of lists of integers where:
    - `0` represents water
    - `1` represents land

Each cell in the grid is a square with a side length of 1. Cells are connected horizontally or vertically (not diagonally). The grid is rectangular, with its width and height not exceeding 100. The grid is completely surrounded by water, and there is only one island (or none). The island does not have any lakes (water inside that isn't connected to the water surrounding the island).

## Example

```python
def island_perimeter(grid):
        # Your implementation here
```

## Usage

To use the `island_perimeter` function, simply pass a grid as described above to the function and it will return the perimeter of the island.

```python
grid = [
        [0, 1, 0, 0],
        [1, 1, 1, 0],
        [0, 1, 0, 0],
        [1, 1, 0, 0]
]

print(island_perimeter(grid))  # Output: 16
```

## Constraints

- The width and height of the grid do not exceed 100.
- The grid is completely surrounded by water.
- There is only one island (or none).
- The island does not have lakes.

## License

This project is licensed under the MIT License.
