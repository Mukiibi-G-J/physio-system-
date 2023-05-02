class ClincMasterRouter:
        # <--------------These are the allowed apps for the router---------------->
    router_app_labels = {
        "patients"
    }
    # <--------------the router provdies 4 methods to be implemented---------------->
    def db_for_read(self, model, **hints):
        # if model._meta.app_label == 'users':
        if model._meta.app_label in self.router_app_labels:
            return "patients_db"

        return None
    # determine if a write operation should be allowed on a model
    def db_for_write(self, model, **hints):
        # if model._meta.app_label == 'users':
        if model._meta.app_label in self.router_app_labels:
            return "patients_db"

        return None
    
    
    # determine if a migration operation should be run on a database
    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.router_app_labels:
            return db == "patients_db"
        return None
    
    
class MainRouter:
    # <--------------These are the allowed apps for the router---------------->
    router_app_labels = {
        "sessions",
        "auth",
        "contenttypes",
        "admin",
        "main",
    }
    # <--------------the router provdies 4 methods to be implemented---------------->
    def db_for_read(self, model, **hints):
        # if model._meta.app_label == 'users':
        if model._meta.app_label in self.router_app_labels:
            return "main_db"

        return None
    # determine if a write operation should be allowed on a model
    def db_for_write(self, model, **hints):
        # if model._meta.app_label == 'users':
        if model._meta.app_label in self.router_app_labels:
            return "main_db"

        return None
    # determine if a relation should be allowed to be created between two models
    def allow_relation(self, obj1, obj2, **hints):
        if (
            obj1._meta.app_label in self.router_app_labels
            or obj2._meta.app_label in self.router_app_labels
        ):
            return True

        return None
    # determine if a migration operation should be run on a database
    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.router_app_labels:
            return db == "main_db"
        return None
    