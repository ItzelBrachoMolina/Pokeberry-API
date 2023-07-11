This is a Pokeberries statistics API created in Flask.

Please follow the instructions below to run the code:

1. Make sure you have Python installed. If not, please follow the instructions to install Python.
2. Clone this repository.

3. Create a virtual environment and activate it:
   ```
   BASH:
   python -m venv venv
   source venv/bin/activate

   WINDOWS:
   venv\Scripts\activate
   ```

4. Install all dependencies using the following command:

```pip install -r requirements.txt```

Once you have completed these steps, you can run the project:
5. Make sure you are in the root directory of the project.
6. Run the following command in the console:

```python app.py```


To run the tests, follow these steps:
7. Open the console.
8. Type and run the command:

```pytest```

9. Route to display statistics in HTML format:

URL: /allBerryStats

Method: GET

Description: This route displays the growth statistics of all berries in HTML format.
Route to display statistics in JSON format:

10. URL: /allBerryStats/headers

Method: GET

Description: This route displays the growth statistics of all berries in JSON format.
Route to display the list of berries in HTML format:

11. URL: /berries

Method: GET

Description: This route displays the list of names of all berries in HTML format.



12. Folder structure:
```
├── .env/
├── app.py
├── README.md
├── requirements.txt
├── test_app.py
├── venv/
└── templates/
    └── index.html
└── .pytest_cache
```
Contact:
If you have any questions or comments, feel free to contact me at itzelbrachomolina@gmail.com
