"""If you remember back to your Stage 3 interview, we asked you to write some code to capitalise a name. For this task, we're going to 
recreate that function, but following a TDD process.

Write three tests to test that:

A name with one name is being correctly capitalised, e.g. "chRis" to "Chris"
A name with four names is being correctly capitalised, e.g. "maya alice Jane johnson" to    
No name returns None, e.g. "".
After completing the tests, write a function that ensures your tests pass."""


def capitalize_name(name: str):
    if name == "":
        return None
    return name.title()
