# Sieve of Eratosthenes

This project implements the **Sieve of Eratosthenes**, an efficient algorithm to find all prime numbers up to a given number `n`.

## How It Works

The algorithm follows these steps:

1. Take an integer input `n` (upper limit for finding prime numbers).
2. Create a list of numbers from `2` to `n`.
3. Iterate through the list, starting with the smallest number (2), and remove all of its multiples.
4. Move to the next available number and repeat step 3 until reaching `sqrt(n)`.
5. The remaining numbers in the list are prime.

## Installation

To use this program, follow these steps: 
 
1. Clone the repository:  

	git clone https://github.com/AllEyesOnMyPon/sieve-of-eratosthenes.git


2. Navigate to the project directory:

	cd sieve-of-eratosthenes


3. Run the script:

	python sieve.py


## Example Usage

	Enter a number: 30
Output:

	[2, 3, 5]  # Numbers used to sieve (sieve basis)
	[2, 3, 5, 7, 11, 13, 17, 19, 23, 29]  # Final list of prime numbers


## Contributing

	Feel free to contribute by submitting pull requests. Any improvements or optimizations are welcome!


## License

	This project is open-source and licensed under the MIT License.

