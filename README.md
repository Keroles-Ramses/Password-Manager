# Password Manager

This Password Manager is a Python-based application designed to securely store and manage your account credentials. It uses encryption to protect your data, ensuring that your passwords remain safe.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [Encryption](#encryption)
- [File Structure](#file-structure)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Project Overview

The Password Manager allows users to securely store and retrieve account information, including usernames, passwords, and associated categories. The application uses the `cryptography` library to encrypt and decrypt the stored data, ensuring that only the user with the correct master password can access the information.

## Features

- **User Authentication**: Set and verify a master password to access stored credentials.
- **Secure Encryption**: Protects stored passwords using strong encryption (Fernet symmetric encryption).
- **Add Credentials**: Easily add new account credentials to the password manager.
- **View Credentials**: Retrieve and decrypt stored account information.
- **Data Persistence**: Stores user data in local files for persistence across sessions.

## Technologies Used

- **Python**: Core programming language used for the project.
- **Cryptography**: Python library used for encrypting and decrypting data.
- **OS Module**: Used for file handling and checking file existence.

## Setup and Installation

### Prerequisites

- Python 3.x installed on your system.
- `pip` (Python package installer).

### Installation Steps

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/Keroles-Ramses/Password-Manager.git
    cd Password-Manager
    ```

2. **Install Required Python Packages**:
    - Ensure that you have the necessary dependencies installed by running:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Application**:
    - Execute the main script to start the Password Manager:
    ```bash
    python password_manager.py
    ```

## Usage

1. **Set or Enter Master Password**:
   - When you run the application for the first time, you'll be prompted to set a master password. This password will be used to encrypt and decrypt your stored data.
   - For subsequent runs, you'll be required to enter the master password to access your credentials.

2. **Add a New Account**:
   - Choose the "Add" option to store new credentials. You'll be prompted to enter the account name, password, and category (e.g., Email, Social Media).

3. **View Stored Credentials**:
   - Choose the "View" option to display all stored credentials. The passwords will be decrypted and shown in plain text.

4. **Exit the Application**:
   - Type `q` or `quit` to exit the Password Manager.

## Encryption

This Password Manager uses the `cryptography` library's Fernet symmetric encryption to securely encrypt and decrypt your data. The encryption key is generated and stored in a local file, and it is used to encrypt both the master password and the account credentials.

## File Structure

- **`username.txt`**: Stores the username of the person using the Password Manager.
- **`key.key`**: Contains the encryption key used for encrypting and decrypting data.
- **`PassManger.txt`**: Stores encrypted account credentials.
- **`encrypted_master.txt`**: Stores the encrypted master password.

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

If you have any questions, feel free to reach out:

- **Email**: keroles.ramses612@gmail.com
- **LinkedIn**: [Keroles Ramses](https://www.linkedin.com/in/keroles-ramses/)

---

Thank you for using the Password Manager! If you have any suggestions or issues, please don't hesitate to contribute or contact me.
