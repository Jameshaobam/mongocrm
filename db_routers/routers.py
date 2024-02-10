class MyDBRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'contact':
            return 'test_db'
        return 'default'

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'contact':
            return 'test_db'
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'contact' or obj2._meta.app_label == 'contact':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'contact':
            return db == 'test_db'
        return db == 'default'


# class AuthRouter:
#     # route_app_labels = {'auth', 'contenttypes', 'sessions', 'admin'}

#     # def db_for_read(self, model, **hints):
#     #     if model._meta.app_label in self.route_app_labels:
#     #         return 'test_db'
#     #     return None
#     def db_for_read(self, model, **hints):
#         """Point model-specific read operations to the corresponding database."""
#         if model._meta.model_name == 'Article':
#             return 'crmdb'
#         elif model._meta.model_name == 'Tag':
#             return 'test_db'
#         # Add more model-specific conditions as needed
#         return None

#     def db_for_write(self, model, **hints):
#         """Point model-specific write operations to the corresponding database."""
#         if model._meta.model_name == 'Article':
#             return 'crmdb'
#         elif model._meta.model_name == 'Tag':
#             return 'test_db'
#         # Add more model-specific conditions as needed
#         return None

#     def allow_relation(self, obj1, obj2, **hints):
#        """Allow relations if both objects are in the same database."""
#        if(
#             obj1._state.db in ['Article', 'Tag'] and
#             obj2._state.db in ['Article', 'Tag'] and
#             obj1._state.db == obj2._state.db
#         ):
#             return True
#        return None

#     def allow_migrate(self, db, app_label, model_name=None, **hints):
#         """Allow migrations for models in the corresponding databases."""
#         if db == 'crmdb' and model_name == 'Article':
#             return True
#         elif db == 'test_db' and model_name == 'Tag':
#             return True
#         # Add more model-specific conditions as needed
#         return None