# Drug Prescription Decision Tree

This Python script uses a Decision Tree Classifier to predict drug prescriptions based on patient data. It reads patient data from a CSV file, preprocesses it, trains a decision tree model, and provides drug prescription recommendations for new patients.

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Code Explanation](#code-explanation)
- [Contributing](#contributing)
- [License](#license)

## Features

- Predicts drug prescriptions based on patient data.
- Uses a Decision Tree Classifier for classification.
- Reads patient data from a CSV file.
- Provides an easy-to-use interface for entering patient information and getting prescription recommendations.

## Getting Started

### Prerequisites

To run this code, you will need:

- Python 3.x installed on your computer.
- The following Python libraries: `pandas`, `scikit-learn`, `pydotplus`, `matplotlib`.

### Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/your-username/drug-prescription-decision-tree.git
   ```

2. Change into the project directory:

   ```bash
   cd drug-prescription-decision-tree
   ```

3. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment:

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS and Linux:

     ```bash
     source venv/bin/activate
     ```

5. Install the required libraries:

   ```bash
   pip install pandas scikit-learn pydotplus matplotlib
   ```

## Usage

1. Make sure you've followed the installation steps above.

2. Ensure that you have the patient data file (`drug.csv`) in the same directory as the script.

3. Run the script:

   ```bash
   python drug_prescription_decision_tree.py
   ```

4. The script will guide you through entering patient information, and it will provide a drug prescription recommendation based on the decision tree model.

## Code Explanation

The code is organized into sections for data preprocessing, model training, visualization, and prediction. Detailed explanations and comments are provided within the code to help you understand each step.

## Contributing

Contributions are welcome! If you have any suggestions or improvements, please create an issue or pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
