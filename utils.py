def normalize_text(value):
    """
    Normalize text for machine comparison.

    Steps:
    1. Handle None
    2. Convert to string
    3. Remove leading/trailing spaces
    4. Convert to lowercase
    """

    if value is None:
        return ""

    return str(value).strip().lower()