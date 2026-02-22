def analyze_error(error):
    """
    Analyzes automation failure and explains cause + fix.
    This simulates AI reasoning safely.
    """

    explanations = {
        "API_TIMEOUT": "The external API did not respond in time. Retrying the request usually fixes this.",
        "AUTH_EXPIRED": "Authentication token has expired. Refreshing credentials is required.",
        "INVALID_SCHEMA": "API response format changed. Switching to a fallback version fixes the issue."
    }

    return explanations.get(
        error,
        "Unknown error occurred. Manual review required."
    )
