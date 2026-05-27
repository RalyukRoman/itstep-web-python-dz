from enum import Enum

class GenderType(Enum):
    """Enumeration for targeting specific gender categories."""

    MALE = "male"
    FEMALE = "female"
    UNISEX = "unisex"

class ShoeKind(Enum):
    """Enumeration for defining the category or style of the footwear."""
    
    SNEAKERS = "sneakers"
    BOOTS = "boots"
    SANDALS = "sandals"
    SHOES = "shoes"