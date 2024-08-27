import logging
import os

from src.utils import create_output_directory, generate_document, load_data, sanitize_filename

OUTPUT_DIR = "output"


def generate_documents_from_csv(csv_path: str, template_path: str, output_prefix: str, logger: logging.Logger):
    """
    Generate multiple Word documents based on data from a CSV file and a Word template.
    """
    # Load data from CSV
    try:
        data = load_data(csv_path)
    except Exception as e:
        logger.error(f"Error loading CSV file: {e}")
        return

    # Create output directory
    create_output_directory(OUTPUT_DIR)

    # Iterate over each row in the DataFrame
    for index, row in data.iterrows():
        context = {key: row.get(key, "") for key in data.columns}
        logger.debug(f"Context: {context}")

        # Generate a unique filename
        sanitized_name = sanitize_filename(context[data.columns[0]].replace(" ", "_").upper())
        filename = f"{output_prefix}_{sanitized_name}_{index + 1}.docx"
        output_path = os.path.join(OUTPUT_DIR, filename)

        # Generate the document
        try:
            generate_document(template_path, context, output_path)
            logger.info(f"Generated: {output_path}")
        except Exception as e:
            logger.error(f"Failed to generate document for row {index + 1}: {e}")
