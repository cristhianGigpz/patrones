from pipeline.pipeline import Pipeline

from filters.normalize_name import normalize_name
from filters.normalize_email import normalize_email
from filters.validate_age import validate_age


pipeline = Pipeline()

pipeline.add_filter(normalize_name)
pipeline.add_filter(normalize_email)
pipeline.add_filter(validate_age)

user = {"name": "  cristian acevedo ", "email": " USER@GMAIL.COM ", "age": 25}
result = pipeline.execute(user)

print(result)
