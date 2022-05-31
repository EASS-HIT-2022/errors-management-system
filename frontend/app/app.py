from src.utils.MultiPage import MultiPage
from src.apps import add_new_error, delete_error, fetch_error, update_error

app = MultiPage()
app.add_app('Add new error',add_new_error.app)
app.add_app('Delete error',delete_error.app)
app.add_app('Fetch error',fetch_error.app)
app.add_app('Update error',update_error.app)
app.run()