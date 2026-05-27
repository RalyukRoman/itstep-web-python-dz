from enum import Enum

class NameOfCuisine(Enum):
    """Enumeration for targeting specific names of cuisines."""

    ITALIAN = "italian"
    FRENCH = "french"
    UKRAINIAN = "ukrainian"

class RecipeType(Enum):
    """Enumeration for targeting specific types of recipes."""

    FIRST = "first courses"
    SECOND = "second courses"