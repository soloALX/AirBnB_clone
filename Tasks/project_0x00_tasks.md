# Task 0. README, AUTHORS 

**Incomplete**

Write a `README.md`:
    -description of the project
    -description of the command interpreter:
        -how to start it
        -how to use it
        -examples
-You should have an `AUTHORS` file at the root of your repository, listing all individuals having contributed content to the repository. For format, reference Docker’s `[AUTHORS page](https://github.com/moby/moby/blob/master/AUTHORS)`
-You should use branches and pull requests on GitHub - it will help you as team to organize your work

# Task 2. Unittests 

All your files, classes, functions must be tested with unit tests

**Incomplete**

```sh
python3 -m unittest discover tests
```

Unit tests must also pass in non-interactive mode:

```sh
echo "python3 -m unittest discover tests" | bash
```
# Task 3. BaseModel 

Write a class `BaseModel` that defines all common attributes/methods for other classes:
    -`models/base_model.py`
    -Public instance attributes:
        -`id`: string - assign with an `uuid` when an instance is created:
            -you can use `uuid.uuid4()` to generate unique `id` but don’t forget to convert to a string
            -the goal is to have unique `id` for each `BaseModel`
    -`created_at`: datetime - assign with the current datetime when an instance is created
    -`updated_at`: datetime - assign with the current datetime when an instance is created and it will be updated every time you change your object
    -`__str__`: should print: `[<class name>] (<self.id>) <self.__dict__>`
    -Public instance methods:
        -`save(self)`: updates the public instance attribute `updated_at` with the current datetime
        -`to_dict(self)`: returns a dictionary containing all keys/values of `__dict__` of the instance:
            -by using `self.__dict__`, only instance attributes set will be returned
            -a key `__class__` must be added to this dictionary with the class name of the object
            -`created_at` and `updated_at` must be converted to string object in ISO format:
                -format: `%Y-%m-%dT%H:%M:%S.%f` (ex: `2017-06-14T22:31:03.285259`)
                -you can use `isoformat()` of `datetime` object
        -This method will be the first piece of the serialization/deserialization process: create a dictionary representation with “simple object type” of our `BaseModel`
