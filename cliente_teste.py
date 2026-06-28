"""Prints the JSON envelope the autograder reads."""

import json

# Simula a execução do autograder — imprime um envelope JSON
envelope = {
    "exercise": "4.2",
    "status": "ready",
    "tools": ["consultar_saldo", "transferir"],
}

if __name__ == "__main__":
    print(json.dumps(envelope, indent=2))
