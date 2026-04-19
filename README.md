# CPF Validator

## Description
This project is a CPF (Cadastro de Pessoas Físicas) validator, designed to check the validity of Brazilian CPF numbers. 
The CPF is an identification number assigned to citizens in Brazil and is often required for various administrative processes.

## How to Use
1. Clone the repository:
   ```bash
   git clone https://github.com/Sonver20/validador-cpf.git
   cd validador-cpf
   ```
2. Install the necessary dependencies (if applicable):
   ```bash
   npm install  # or other package manager commands depending on the project
   ```
3. Run the validator with a CPF number:
   ```bash
   node validator.js 123.456.789-09  # Replace with the CPF number you want to validate
   ```

## How It Works
The validator uses an algorithm that checks the digits of the CPF number according to the rules established by the Brazilian Federal Revenue. 
It performs the following steps:
1. **Input Validation:** Ensures the input CPF is in the correct format.
2. **Digit Verification:** Calculates the verification digits and compares them with the provided CPF digits.
3. **Return Result:** Outputs whether the CPF number is valid or not.

## Examples
- Valid CPF: `123.456.789-09`
- Invalid CPF: `123.456.789-00`

## License
This project is licensed under the MIT License.