# Personal File Crypto-Vault (AES-256 Symmetric Encryption)

A lightweight, local command-line security tool built in Python that allows users to securely encrypt and decrypt files using industry-standard Advanced Encryption Standard (AES) with a 256-bit key.

---

## 🔒 Project Overview & Use Case Diagram
The goal of this project is to demonstrate the practical application of **Symmetric Cryptography**. This tool provides a hands-on environment to understand how cryptographic keys protect data-at-rest.

The diagram below shows the core workflow of the application and how the security professional interacts with the system to manage file security.

```mermaid
%%{init: {'theme': 'base', 'themeVariables': { 'primaryColor': '#ffffff', 'primaryBorderColor': '#2ea44f', 'actorBkg': '#f6f8fa', 'actorBorder': '#2ea44f' }}}%%
graph TD
    %% Define User
    subgraph Userspace ["Local Security Admin"]
        User[("🔒 Security<br/>Operator")]
    end

    %% Define System Boundaries
    subgraph VaultSystem ["Python Crypto Vault (Local System)"]
        
        %% Main Menu (Decision Point)
        CLI_Menu{"Command-Line<br/>Menu Prompt"}

        %% Action Case 1: Key Management
        subgraph KeyUse ["Case 1: Key Generation"]
            GenerateKey(["🔐 Generate unique<br/>random key"])
        end

        %% Action Case 2: Protection
        subgraph EncryptUse ["Case 2: File Protection"]
            EncryptFile(["🔒 Scramble plain text<br/>into ciphertext"])
        end

        %% Action Case 3: Restoration
        subgraph DecryptUse ["Case 3: Data Restoration"]
            DecryptFile(["🔓 Reverse algorithm<br/>back to plain text"])
        end

    end

    %% Define External Resources
    subgraph Storage ["Local Storage (.gitignore)"]
        KeyFile[("🔑 secret.key<br/>(Hidden/Private)")]
        SecureFiles[("📁 encrypted_file.txt<br/>(Scrambled ciphertext)")]
    end

    %% Define Connections
    User ==>|Runs Script| CLI_Menu
    
    %% Option 1 Workflow
    CLI_Menu -.->|Choice '1'| GenerateKey
    GenerateKey ==>|Saves new file| KeyFile

    %% Option 2 Workflow
    CLI_Menu -.->|Choice '2'| EncryptFile
    EncryptFile ---|Reads unique key| KeyFile
    EncryptFile ==>|Overwrites data| SecureFiles

    %% Option 3 Workflow
    CLI_Menu -.->|Choice '3'| DecryptFile
    DecryptFile ---|Validates against| KeyFile
    DecryptFile ==>|Restores original| SecureFiles

    %% Styling for clarity
    classDef mainCase fill:#2ea44f,stroke:#fff,stroke-width:1px,color:white,font-weight:bold;
    classDef menu fill:#e1f5fe,stroke:#01579b,stroke-width:2px,rx:5px,ry:5px;
    classDef storage fill:#fff3e0,stroke:#e65100,stroke-width:2px,rx:5px,ry:5px;

    class GenerateKey,EncryptFile,DecryptFile mainCase;
    class CLI_Menu menu;
    class KeyFile,SecureFiles storage;
