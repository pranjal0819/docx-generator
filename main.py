import time

from config import CHOICE_MAPPING, CSV_PATH, OPTIONS, TEMPLATE_PATH
from src.document_generator import generate_documents_from_csv
from src.logger import setup_logger, set_log_level

# Setup logger
logger = setup_logger(__name__)


def generate_documents(doc_type):
    if doc_type not in CSV_PATH or doc_type not in TEMPLATE_PATH:
        logger.error(f"Unknown document type: {doc_type}")
        return

    csv_path = CSV_PATH[doc_type]
    template_path = TEMPLATE_PATH[doc_type]
    output_prefix = doc_type

    generate_documents_from_csv(csv_path, template_path, output_prefix, logger)


def main():
    logger.debug("Setup logging")

    while True:
        logger.info("\nChoose an option:\n")
        for key, description in OPTIONS.items():
            logger.info(f"\t{key.ljust(20)}: {description}")
        logger.info(f"\t{'loglevel'.ljust(20)}: Change logging level")
        logger.info(f"\t{'exit or (q)'.ljust(20)}: Exit the program")

        time.sleep(1)  # Delay for 1 second before user input
        choice = input("\nEnter your choice: ").strip().lower()

        if choice in OPTIONS:
            logger.info(f"Running {OPTIONS[choice]}...")
            generate_documents(CHOICE_MAPPING[choice])
        elif choice == "loglevel":
            level_name = input("\nEnter log level (debug, info, warning, error): ").strip().lower()
            set_log_level(logger, level_name)
        elif choice == "exit" or choice == "q":
            logger.info("Exiting...")
            break
        else:
            logger.warning("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
