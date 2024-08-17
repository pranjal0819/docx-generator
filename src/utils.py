import os
import pandas as pd
from docxtpl import DocxTemplate


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
    Generate a Word document based on the template and context.
    """
    try:
        doc = DocxTemplate(template_path)
        doc.render(context)
        doc.save(output_path)
    except Exception as e:
        raise Exception(f"Error generating document: {e}")


def create_output_directory(path: str):
    """
    Create the output directory if it doesn't exist.
    """
    os.makedirs(path, exist_ok=True)
