import os

import pandas as pd
from docxtpl import DocxTemplate


def create_output_directory(path: str):
    """
    Create the output directory if it doesn't exist.
    """
    os.makedirs(path, exist_ok=True)


def load_data(csv_path: str) -> pd.DataFrame:
    """
    Load data from a CSV file into a pandas DataFrame.
    """
    try:
        data = pd.read_csv(csv_path, dtype=str)
        return data.fillna("NaN")  # Replace NaN with empty strings
    except Exception as e:
        raise Exception(f"Error loading CSV file: {e}")


def generate_document(template_path: str, context: dict, output_path: str):
    """
    Generate a Word document based on the template and sanitized context.
    """
    try:
        # Sanitize the context before rendering
        sanitized_context = sanitize_context(context)

        doc = DocxTemplate(template_path)
        doc.render(sanitized_context)
        doc.save(output_path)
    except Exception as e:
        raise Exception(f"Error generating document: {e}")


def sanitize_context(context: dict) -> dict:
    """
    Sanitize context dictionary by cleaning up string values.
    """
    sanitized_context = {}

    for key, value in context.items():
        if isinstance(value, str):
            # Remove extra whitespace
            value = value.strip()
            # Replace any dangerous characters (example: <, >, &, etc.)
            value = value.replace("<", "&lt;").replace(">", "&gt;").replace("&", "&amp;")
        sanitized_context[key] = value
    return sanitized_context


def sanitize_filename(name: str) -> str:
    """
    Sanitize the filename to remove or replace invalid characters.
    """
    invalid_chars = ["<", ">", ":", '"', "/", "\\", "|", "?", "*"]
    for char in invalid_chars:
        name = name.replace(char, "")
    return name
