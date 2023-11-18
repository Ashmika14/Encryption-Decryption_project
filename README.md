# Encryption-Decryption_project
The project consists of two main scripts, one for encryption and another for decryption, both
of which rely on a module called utils for various utility functions. The encryption script starts by checking for the existence of a 'secret.txt' file, which is
intended to store the encryption key. If 'secret.txt' does not exist, it generates a new key and
saves it in the file. Subsequently, it loads this key, creates a Fernet cipher suite, and uses it to
encrypt the contents of 'input.txt,' overwriting the file with the encrypted data. Finally, it
confirms the successful encryption. The decryption script, on the other hand, assumes that 'secret.txt' already contains the
encryption key, which was generated during the encryption phase. It loads this key, creates a
Fernet cipher suite, and decrypts the contents of 'input.txt,' overwriting the file with the
original plaintext. After successful decryption, the script removes 'secret.txt' for security
reasons. In essence, your project provides a basic file encryption and decryption workflow, offering a
way to secure sensitive data using symmetric encryption. This documentation outlines the
encryption and decryption processes and highlights the importance of protecting the
encryption key ('secret.txt'). Further details regarding the project's use cases, potential
improvements, and security considerations should be included in the complete project
documentation
