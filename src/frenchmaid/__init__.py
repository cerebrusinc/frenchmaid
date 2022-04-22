
__app_name__ = "French Maid"
__version__ = "0.1.0"


(
    SUCCESS,
    DIR_ERROR,
    DEL_ERROR,
) = range(3)

ERRORS = {
    DIR_ERROR: "Failed to find directory",
    DEL_ERROR: "Failed to delete directory"
}