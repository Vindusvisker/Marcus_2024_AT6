from user_input_validator import UserInputValidator

validator1 = UserInputValidator()
validator2 = UserInputValidator()

test_list1 = ["5", "10", "-3", "hello", "20"]
test_list2 = ["1", "abc", "0", "15", "7"]

result1 = validator1.validate_positive_integers(test_list1)
result2 = validator2.validate_positive_integers(test_list2)

print("Validator 1 result:", result1)
print("Validator 2 result:", result2)

validator1.display_validation_message()
validator2.display_validation_message()
