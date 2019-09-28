"""
Library time module.
"""
import datetime


def as_git_timestamp(date_str: str) -> datetime.date:
    """
    Convert string matching "YYYY-MM-DD" into GitTimestamp string.

    The output format is the datetime formatted string required by Github's
    GraphQL.
    """
    return datetime.datetime.strptime(date_str, '%Y-%m-%d').isoformat()


def as_date(datetime_str: str) -> datetime.date:
    """
    Convert string which starts with "YYYY-MM-DD" to a date object.
    """
    date_str = datetime_str[:10]

    return datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
