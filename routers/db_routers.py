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
    
    