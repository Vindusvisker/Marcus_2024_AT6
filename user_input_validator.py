class UserInputValidator:
    """A class for validating user input."""

    def validate_positive_integers(self, string_list):
        """
        Takes a list of strings and returns a list of valid positive integers.

        Args:
            string_list: A list of strings to validate

        Returns:
            A list containing only the valid positive integers
        """
        valid_integers = []

        for item in string_list:
            try:
                number = int(item)
                if number > 0:
                    valid_integers.append(number)
            except ValueError:
                pass

        return valid_integers

    def display_validation_message(self):
        print("List has been validated successfully.")
