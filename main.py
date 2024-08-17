from config import CHOICE_MAPPING, CSV_PATH, OPTIONS, TEMPLATE_PATH
from src.document_generator import generate_documents_from_csv


def generate_documents(doc_type):
    if doc_type not in CSV_PATH or doc_type not in TEMPLATE_PATH:
        print(f"Unknown document type: {doc_type}")
        return

    csv_path = CSV_PATH[doc_type]
    template_path = TEMPLATE_PATH[doc_type]
    output_prefix = doc_type

    generate_documents_from_csv(csv_path, template_path, output_prefix)


def main():
    while True:
        print("\nChoose an option:")
        for key, description in OPTIONS.items():
            print(f"\t{key.ljust(20)}: {description}")
        print(f"\t{'exit or (q)'.ljust(20)}: Exit the program")

        choice = input("\nEnter your choice: ").strip().lower()

        if choice in OPTIONS:
            print(f"\nRunning {OPTIONS[choice]}...\n")
            generate_documents(CHOICE_MAPPING[choice])
        elif choice == "exit" or choice == "q":
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")
            break


if __name__ == "__main__":
    main()
