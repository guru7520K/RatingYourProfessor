## RatingYourProfessor
 Allows anyone to rate their professors anonymously.



Mulitple users can register,log-in create their professors and give their ratings to a professor and their rating for each professors would be truly anonymous.
## How?
We are making the rating anonymous by generating a unique UUID (Universal Unique Identifier) for each user's rating and storing it in the Rating model's user_id field. This UUID is generated using Python's built-in uuid module, and it ensures that each rating is associated with a unique and random identifier that cannot be traced back to any specific user.

Use Django's built-in functionality to prevent duplicate ratings from the same user. In particular, we can use the unique_together attribute in the Meta class to ensure that each combination of professor and user is unique. This means that each user can only rate each professor once.

Since we are using Django's built-in User model for authentication and management, we don't need to store the user's username or any other identifiable information in the Rating model. Instead, we can use the UUID to ensure that each user can only submit one rating for each professor, regardless of whether they log in or out, and without exposing their identity.

## what happens when a new user logs in ?
By using a UUID-based identifier instead of a foreign key to the User model, we can ensure that each rating is still anonymous, while still preventing duplicate ratings from the same user. The unique_together attribute in the Meta class ensures that each combination of professor and user_id is unique.


So each user will be assigned a unique UUID when they submit a rating, and this UUID will be used to check for duplicate ratings. So if a new user logs in and submits a rating, their UUID will be saved along with the rating, and if they log out and another user logs in and tries to submit a rating, a new UUID will be generated for the second user and saved with their rating. This ensures that each user can only submit one rating for each professor.
