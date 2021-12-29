from django.apps import AppConfig


class BookInventoryConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'book_inventory'
    def ready(self):
        import book_inventory.models