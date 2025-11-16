# NumPy Array Creator (Console Application)

This project is a simple **console-based NumPy array generator** written
in Python. It allows users to interactively create different types of
arrays through a text-based menu. The program supports:

-   One-dimensional arrays created from user input
-   Two-dimensional arrays
-   Zero-filled arrays
-   One-filled arrays
-   Range-based arrays (`np.arange`)
-   Evenly spaced arrays (`np.linspace`)

After creating an array, the program automatically displays its
**dimensions**, **shape**, **size**, and **data type**.

The main purpose of this script is to provide an intuitive and
educational tool for users learning NumPy or experimenting with array
creation. Its modular structure makes the code easy to read, maintain,
and expand.

------------------------------------------------------------------------

## Features

-   Choose between two NumPy data types:
    -   `int32`
    -   `float64`
-   Create multiple types of arrays interactively
-   Automatically prints array information
-   No dependencies beyond NumPy
-   Fully console-based and lightweight

------------------------------------------------------------------------

## Tech Stack

**Python 3** -- Core programming language used for the entire
application.

**NumPy** -- Used to create and manipulate arrays of different
structures and data types.

**Command-Line Interface (CLI)** -- Provides an interactive text menu
for user interaction.

------------------------------------------------------------------------

## Deployment

### 1. Clone this repository

``` bash
git clone https://github.com/oscarpizrodriguez/Numpy/tree/main/Array%20Creator
cd array-creator
```

### 2. Ensure Python is installed

``` bash
python --version
```

### 3. Install NumPy if necessary

``` bash
pip install numpy
```

### 4. Run the application

``` bash
python main.py
```

------------------------------------------------------------------------

## Using the Program

Once the script starts, you will be asked to:

1.  Select the **data type** (`int32` or `float64`)
2.  Choose the kind of array you want to create:

-   Create list array
-   Create 2D array
-   Create zeros array
-   Create ones array
-   Create range array
-   Create space array

The program will then request the required inputs (numbers, rows,
columns, etc.) and display:

-   **Dimensions**
-   **Shape**
-   **Size**
-   **Data type**

No additional configuration is required. Everything runs interactively
through the console.

------------------------------------------------------------------------

## File Structure

    main.py        # Main script containing the NumPy array generator menu

------------------------------------------------------------------------

## Example Output

    Enter data type:
    1) int32
    2) float64

    Select an option:
    1) Create list array
    2) Create 2D array
    3) Create zeros array
    ...

------------------------------------------------------------------------

## License

This project is open source and available for personal or educational
use.
